"""Render a 1080x1920 recommendation video from repository facts and local narration.

Run voice.ps1 first, then this file with the bundled Python. --preview creates
the storyboard, cover, subtitles, and mixed audio without encoding the video.
"""
from pathlib import Path
from functools import lru_cache
import argparse
import json
import math
import subprocess
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
W, H, FPS, SR = 1080, 1920, 30, 44100
CREAM = '#f4f1e9'
DARK = '#12322f'
GREEN = '#1c6b54'
MINT = '#bee5c6'
MUTED = '#62766c'
REGULAR = 'C:/Windows/Fonts/msyh.ttc'
BOLD = 'C:/Windows/Fonts/msyhbd.ttc'
LATIN = 'C:/Windows/Fonts/seguisb.ttf'
MONO = 'C:/Windows/Fonts/consola.ttf'
FFMPEG = 'D:/Programs/ffmpeg/bin/ffmpeg.exe'
SCRIPT = json.loads((BASE / 'script.json').read_text(encoding='utf-8'))
SOURCES = json.loads((ROOT / 'research/sources.json').read_text(encoding='utf-8'))
SELECTION = json.loads((ROOT / 'research/selection.json').read_text(encoding='utf-8'))
RUN = json.loads((ROOT / 'promotion/assets/run-evidence.json').read_text(encoding='utf-8'))
assert len(SOURCES['sources']) == 200
assert RUN['exitCode'] == 0 and RUN['stdout'].strip() == 'ERROR database unavailable'


@lru_cache(maxsize=100)
def font(size, family='regular'):
    return ImageFont.truetype({'regular': REGULAR, 'bold': BOLD, 'latin': LATIN, 'mono': MONO}[family], size)


def text(draw, xy, value, size=50, color=DARK, family='regular', center=False, maxwidth=920):
    x, y = xy
    while draw.textlength(value, font=font(size, family)) > maxwidth and size > 26:
        size -= 1
    if center:
        x -= draw.textlength(value, font=font(size, family)) / 2
    draw.text((x, y), value, font=font(size, family), fill=color, stroke_width=0)


def title(draw, lines, color, y=330, size=88):
    for index, line in enumerate(lines):
        text(draw, (84, y + index * (size + 30)), line, size, color, 'bold')


def layer():
    return Image.new('RGBA', (W, H), (0, 0, 0, 0))


def line(draw, xy, color, width=2):
    draw.line(xy, fill=color, width=width)


def wav_read(path):
    with wave.open(str(path), 'rb') as handle:
        assert handle.getsampwidth() == 2
        rate, channels = handle.getframerate(), handle.getnchannels()
        audio = np.frombuffer(handle.readframes(handle.getnframes()), dtype='<i2').astype(np.float32) / 32768
    if channels > 1:
        audio = audio.reshape(-1, channels).mean(axis=1)
    positions = np.arange(round(len(audio) * SR / rate)) * rate / SR
    return np.interp(positions, np.arange(len(audio)), audio).astype(np.float32)


voices, starts, durations = [], [], []
cursor = 0.0
for scene in SCRIPT:
    audio = wav_read(BASE / 'voices' / (scene['id'] + '.wav'))
    duration = math.ceil(max(scene['min_seconds'], len(audio)/SR + .95) * FPS) / FPS
    starts.append(cursor)
    durations.append(duration)
    voices.append(audio)
    cursor += duration
TOTAL = cursor


def write_wav(path, audio):
    with wave.open(str(path), 'wb') as handle:
        handle.setnchannels(audio.shape[1] if audio.ndim == 2 else 1)
        handle.setsampwidth(2)
        handle.setframerate(SR)
        handle.writeframes((np.clip(audio, -.99, .99) * 32767).astype('<i2').tobytes())


def soundtrack():
    count = round(TOTAL * SR)
    voice = np.zeros(count, np.float32)
    for start, audio in zip(starts, voices):
        audio = audio * (.76 / max(np.max(np.abs(audio)), .01))
        offset = round((start + .38) * SR)
        voice[offset:offset+len(audio)] += audio[:count-offset]
    # An original quiet instrumental bed: soft synthesized chords and sparse plucks.
    t = np.arange(count, dtype=np.float32) / SR
    music = np.zeros(count, np.float32)
    chords = [[130.81,164.81,196.0,246.94], [110,130.81,164.81,196],
              [87.31,130.81,174.61,220], [98,146.83,196,246.94]]
    chord_len = 5.0
    for number in range(math.ceil(TOTAL/chord_len)):
        begin = round(number*chord_len*SR)
        end = min(count, begin+round(chord_len*SR))
        local = t[begin:end]-number*chord_len
        envelope = np.minimum(local/.65, 1) * np.minimum((chord_len-local)/.7, 1)
        for frequency in chords[number % 4]:
            music[begin:end] += (.007 * np.sin(2*np.pi*frequency*local)
                                + .0017*np.sin(2*np.pi*frequency*2*local)) * envelope
    for beat in np.arange(0, TOTAL, .625):
        begin = round(beat*SR)
        end = min(count, begin+round(.38*SR))
        local = t[begin:end]-beat
        frequency = [523.25,659.25,783.99,659.25][int(round(beat/.625))%4]
        music[begin:end] += .009*np.sin(2*np.pi*frequency*local)*np.exp(-local*13)*np.minimum(local/.012,1)
    fade = np.minimum(t/1.2,1)*np.minimum((TOTAL-t)/1.8,1)
    music *= fade
    duck = np.where(np.abs(voice) > .025, .6, 1)
    mixed = np.column_stack((voice+music*duck, voice+np.roll(music, 350)*duck))
    write_wav(BASE/'soundtrack.wav', mixed)


def srt_time(seconds):
    value = round(seconds*1000)
    h, value = divmod(value, 3600000)
    m, value = divmod(value, 60000)
    s, ms = divmod(value, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'


def subtitles():
    blocks = []
    storyboard = ['# README Atlas 宣传短视频', '',
                  f'- 竖屏 1080 × 1920，30 fps，时长 {TOTAL:.1f} 秒。',
                  '- 项目推荐与功能讲解；中文合成旁白、烧录字幕、原创合成轻音乐。',
                  '- 配音：本机 Microsoft Huihui Desktop。',
                  '- 内容以当前本地仓库为依据；日志画面根据真实运行记录制作。',
                  '- 项目地址：https://github.com/chromoany/readme-atlas', '', '| 时间 | 旁白 |', '| --- | --- |']
    for index, (scene, start, duration) in enumerate(zip(SCRIPT, starts, durations)):
        blocks.append(f'{index+1}\n{srt_time(start+.25)} --> {srt_time(start+duration-.15)}\n'+ '\n'.join(scene['subtitles']))
        storyboard.append(f'| {start:.1f}–{start+duration:.1f}s | {scene["narration"]} |')
    (BASE/'subtitles.srt').write_text('\n\n'.join(blocks)+'\n', encoding='utf-8-sig')
    (BASE/'storyboard.md').write_text('\n'.join(storyboard)+'\n', encoding='utf-8')
    (BASE/'timing.json').write_text(json.dumps({'duration':TOTAL,'resolution':[W,H],'fps':FPS,'starts':starts,'durations':durations,'source_date':SELECTION['observed_date']},indent=2)+'\n',encoding='utf-8')


def design(index):
    dark = index in [0, 2, 7]
    fg, accent = (CREAM, MINT) if dark else (DARK, GREEN)
    background = Image.new('RGB', (W,H), DARK if dark else CREAM)
    d = ImageDraw.Draw(background)
    text(d,(84,100),'README Atlas',44,fg,'latin')
    text(d,(890,110),f'{index+1:02} / 08',28,accent,'latin',maxwidth=120)
    line(d,(84,184,996,184), '#44645a' if dark else '#c9d3c9')
    text(d,(84,1798),'github.com/chromoany/readme-atlas',30,accent,'mono')
    main = layer()
    m = ImageDraw.Draw(main)
    extras = []
    if index == 0:
        text(m,(84,315),'开源项目推荐',42,accent,'bold')
        title(m,['写 README','也可以省点心'],fg,y=500,size=98)
        line(m,(84,850,260,850),accent,6)
        text(m,(84,955),'README',126,accent,'latin')
        text(m,(84,1110),'Atlas',154,fg,'latin')
        text(m,(84,1370),'写作 · 审查 · 翻译 · 排版',43,accent)
    elif index == 1:
        title(m,['一份 README，','这些都能帮忙。'],fg,y=310,size=82)
        rows = [('新建','从仓库内容开始写'),('改写','补全首次使用路线'),('审查','找出问题，给出依据'),('翻译','保持命令和功能一致')]
        for n,(a,b) in enumerate(rows):
            item=layer(); p=ImageDraw.Draw(item); y=690+n*188
            line(p,(84,y+145,996,y+145),'#cad5c9')
            text(p,(84,y),f'0{n+1}',38,accent,'latin')
            text(p,(190,y-10),a,64,fg,'bold')
            text(p,(190,y+75),b,39,MUTED)
            extras.append((item,.3+n*.23))
    elif index == 2:
        title(m,['参考不同项目，','找到合适写法。'],fg,y=300,size=80)
        text(m,(84,880),'项 README 研究',52,accent,'bold')
        text(m,(84,1000),'14 个领域 · 按需读取参考资料',42,fg)
        for n,value in enumerate(['FastAPI  /  uv  /  fzf','Linux  /  Godot  /  Zephyr','科技爱好者周刊 · 更多项目']):
            text(m,(84,1110+n*76),value,41,accent,'latin' if n<2 else 'regular')
        text(m,(84,1400),'32 个详细案例 + 168 个结构研究',36,fg)
        text(m,(84,1460),'来源：当前仓库研究清单',29,accent)
    elif index == 3:
        title(m,['先看仓库，','再写 README。'],fg,y=310,size=86)
        m.rounded_rectangle((84,690,996,925),radius=20,fill='#e3eadd')
        text(m,(125,735),'配置 · 入口 · 示例',49,fg,'bold')
        text(m,(125,825),'测试 · 文档 · 许可证',49,fg,'bold')
        line(m,(540,950,540,1030),accent,6)
        m.polygon([(516,1010),(564,1010),(540,1042)],fill=accent)
        m.rounded_rectangle((84,1080,996,1375),radius=20,fill=DARK)
        text(m,(125,1135),'README',65,CREAM,'latin')
        text(m,(125,1238),'功能介绍 · 命令 · 使用示例',44,MINT)
    elif index == 4:
        title(m,['把第一次使用','写清楚。'],fg,y=310,size=90)
        text(m,(84,600),'仓库内日志脚本 · 手工改写示例',36,MUTED)
        m.rounded_rectangle((64,710,1016,1225),radius=20,fill=DARK)
        text(m,(108,754),'COMMAND',32,MINT,'mono')
        text(m,(108,980),'OUTPUT',32,MINT,'mono')
        text(m,(84,1325),'命令 → 输出 → 使用边界',48,accent,'bold')
        text(m,(84,1420),'画面根据仓库示例与实际运行记录制作',31,MUTED)
    elif index == 5:
        title(m,['内容清楚，','页面也好看。'],fg,y=300,size=84)
        m.rounded_rectangle((140,630,940,1350),radius=18,fill='white',outline='#c9d4c9',width=2)
        text(m,(540,680),'项目名称',58,fg,'bold',center=True)
        text(m,(540,780),'一句话说清用途',37,MUTED,center=True)
        m.rounded_rectangle((286,865,794,930),radius=9,fill='#e1eddf')
        text(m,(540,879),'版本 · 许可证 · 状态',32,accent,center=True)
        line(m,(200,980,880,980),'#d5ddd1')
        text(m,(200,1020),'安装 → 首次使用',42,fg,'bold')
        m.rectangle((200,1125,880,1275),fill='#edf2e8')
        text(m,(540,1170),'真实预览 / 示例',40,MUTED,center=True)
        text(m,(140,1375),'排版示意',30,MUTED)
        text(m,(84,1460),'13 个视觉研究案例',39,accent,'bold')
    elif index == 6:
        title(m,['适合这些项目'],fg,y=340,size=88)
        rows=['准备开源的新项目','想补齐文档的小工具','需要改写的旧 README']
        for n,value in enumerate(rows):
            item=layer(); p=ImageDraw.Draw(item); y=650+n*240
            text(p,(84,y),f'0{n+1}',42,accent,'latin')
            text(p,(84,y+78),value,61,fg,'bold')
            line(p,(84,y+178,996,y+178),'#cbd5ca')
            extras.append((item,.3+n*.3))
        text(m,(84,1450),'已提供 Codex 安装与调用说明',36,MUTED)
    else:
        text(m,(84,320),'README',138,accent,'latin')
        text(m,(84,490),'Atlas',162,fg,'latin')
        text(m,(84,780),'让项目更容易看懂和用起来',55,fg,'bold')
        text(m,(84,915),'MIT 开源',45,accent,'bold')
        line(m,(84,1040,996,1040),'#547467')
        text(m,(84,1095),'项目地址',42,accent)
        text(m,(84,1190),'https://github.com/',49,fg,'mono')
        text(m,(84,1270),'chromoany/readme-atlas',61,fg,'mono')
        text(m,(84,1430),'去仓库看看 →',60,accent,'bold')
    return background, main, extras


DESIGNS=[design(index) for index in range(8)]


def ease(value):
    return 1-(1-max(0,min(1,value)))**3


def composite(canvas, foreground, progress):
    p=ease(progress)
    if p<=0:
        return
    offset=round((1-p)*45)
    if p>=.999:
        canvas.paste(foreground,(0,offset),foreground)
    else:
        mask=foreground.getchannel('A').point(lambda a:round(a*p))
        canvas.paste(foreground,(0,offset),mask)


@lru_cache(maxsize=210)
def counter_layer(value):
    overlay=layer(); d=ImageDraw.Draw(overlay)
    text(d,(74,560),str(value),258,MINT,'latin')
    return overlay


@lru_cache(maxsize=100)
def terminal_layer(length):
    overlay=layer(); d=ImageDraw.Draw(overlay)
    command='python logslice.py sample.log --level ERROR'
    text(d,(108,825),'cd examples/fixtures/log-slice',35,CREAM,'mono')
    text(d,(108,885),command[:length],34,CREAM,'mono')
    if length>=len(command):
        text(d,(108,1060),RUN['stdout'].strip(),44,MINT,'mono')
    return overlay


def frame(index, local, global_time):
    background, main, extras=DESIGNS[index]
    image=background.copy()
    composite(image,main,local/.65)
    for item,delay in extras:
        composite(image,item,(local-delay)/.55)
    if index==2:
        value=round(200*ease((local-.4)/1.6))
        overlay=counter_layer(value)
        image.paste(overlay,(0,0),overlay)
    elif index==4:
        length=max(0,min(len('python logslice.py sample.log --level ERROR'),int((local-.7)*22)))
        overlay=terminal_layer(length)
        image.paste(overlay,(0,0),overlay)
    d=ImageDraw.Draw(image)
    dark=index in [0,2,7]
    caption_color=CREAM if dark else DARK
    for n,subtitle in enumerate(SCRIPT[index]['subtitles']):
        text(d,(540,1580+n*67),subtitle,44,caption_color,center=True,maxwidth=930)
    line(d,(84,1870,996,1870),'#466256' if dark else '#d1d9ce',5)
    line(d,(84,1870,84+round(912*global_time/TOTAL),1870),MINT if dark else GREEN,5)
    return image


def review_images():
    sheet=Image.new('RGB',(1080,1100),'#dadfd4')
    for index in range(8):
        shot=frame(index,min(3.5,durations[index]-.5),starts[index]+3.5)
        shot.resize((260,462),Image.Resampling.LANCZOS).save(BASE/f'scene-{index+1:02}.jpg',quality=90)
        sheet.paste(shot.resize((260,462),Image.Resampling.LANCZOS),(10+(index%4)*270,10+(index//4)*550))
    sheet.save(BASE/'storyboard.jpg',quality=92)
    cover=frame(0,2,2)
    cover.save(BASE/'poster.jpg',quality=94)


def encode():
    destination=BASE/'readme-atlas-promo-9x16.mp4'
    cmd=[FFMPEG,'-hide_banner','-loglevel','warning','-y','-f','rawvideo','-pix_fmt','rgb24',
         '-s',f'{W}x{H}','-r',str(FPS),'-i','pipe:0','-i',str(BASE/'soundtrack.wav'),
         '-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','veryfast','-crf','20',
         '-pix_fmt','yuv420p','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-ar','48000','-c:a','aac','-b:a','192k','-movflags','+faststart',
         '-t',str(TOTAL),'-metadata','title=README Atlas | Open-source Skill',str(destination)]
    process=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=open(BASE/'encode.log','w',encoding='utf-8'))
    frames=round(TOTAL*FPS)
    index=0
    previous=None
    for number in range(frames):
        now=number/FPS
        while index<7 and now>=starts[index+1]:
            previous=frame(index,durations[index]-.01,starts[index]+durations[index]-.01)
            index+=1
        local=now-starts[index]
        image=frame(index,local,now)
        if previous is not None and local<.32:
            image=Image.blend(previous,image,ease(local/.32))
        process.stdin.write(image.tobytes())
        if number%(FPS*5)==0:
            print(f'Render {now:.0f}/{TOTAL:.1f}s',flush=True)
    process.stdin.close()
    code=process.wait()
    if code:
        raise RuntimeError((BASE/'encode.log').read_text(encoding='utf-8'))
    print(f'Created {destination}',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--preview',action='store_true')
    options=parser.parse_args()
    soundtrack()
    subtitles()
    review_images()
    print(f'Timeline: {TOTAL:.2f}s / {W}x{H} / {FPS} fps',flush=True)
    if not options.preview:
        encode()
