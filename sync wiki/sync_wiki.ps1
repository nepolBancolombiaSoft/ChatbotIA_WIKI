# 📌 Configuración de la Wiki en Git
$WIKI_DIR = "$env:USERPROFILE\wiki_git"
$REPO_URL = "https://npolo@dev.azure.com/npolo/BancolombiaTEST/_git/BancolombiaTEST.wiki"

# 📌 Verificar si Git está instalado
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git no está instalado. Instálalo y vuelve a intentarlo." -ForegroundColor Red
    exit
}

# 📌 Clonar o actualizar la Wiki
if (!(Test-Path -Path $WIKI_DIR)) {
    Write-Host "🚀 Clonando la Wiki desde Git..."
    git clone $REPO_URL $WIKI_DIR
} else {
    Write-Host "🔄 Actualizando la Wiki desde Git..."
    Set-Location -Path $WIKI_DIR
    git pull origin main
}

Write-Host "✅ Wiki actualizada correctamente." -ForegroundColor Green
