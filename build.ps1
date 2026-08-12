param(
    [string]$TeXRoot = 'D:\Software\CodexTools\runtimes\miktex'
)

$ErrorActionPreference = 'Stop'
$texBin = Join-Path $TeXRoot 'texmfs\install\miktex\bin\x64'
$xelatex = Join-Path $texBin 'xelatex.exe'

if (-not (Test-Path -LiteralPath $xelatex)) {
    throw "XeLaTeX was not found at: $xelatex"
}

Push-Location $PSScriptRoot
try {
    for ($pass = 1; $pass -le 2; $pass++) {
        Write-Host "XeLaTeX pass $pass/2"
        & $xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
        if ($LASTEXITCODE -ne 0) {
            throw "XeLaTeX failed on pass $pass. See main.log for details."
        }
    }

    $pdf = Join-Path $PSScriptRoot 'main.pdf'
    if (-not (Test-Path -LiteralPath $pdf)) {
        throw 'Compilation completed without producing main.pdf.'
    }

    Write-Host "PDF created: $pdf"
}
finally {
    Pop-Location
}
