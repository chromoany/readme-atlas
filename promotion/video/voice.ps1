$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$videoRoot = $PSScriptRoot
$voiceRoot = Join-Path $videoRoot 'voices'
New-Item -ItemType Directory -Force -Path $voiceRoot | Out-Null
$scenes = Get-Content -LiteralPath (Join-Path $videoRoot 'script.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SelectVoice('Microsoft Huihui Desktop')
$synth.Rate = 2
$synth.Volume = 100
try {
    foreach ($scene in $scenes) {
        $destination = Join-Path $voiceRoot ($scene.id + '.wav')
        $synth.SetOutputToWaveFile($destination)
        $synth.Speak($scene.narration)
        $synth.SetOutputToNull()
        Write-Output ('Narration: ' + $scene.id)
    }
} finally {
    $synth.Dispose()
}
