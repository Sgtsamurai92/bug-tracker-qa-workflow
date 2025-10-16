# Test Runner Script
# This script helps you run tests with the browser visible

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Bug Tracker Test Runner" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Flask app is running
Write-Host "Checking if Flask app is running on port 5000..." -ForegroundColor Yellow
$flaskRunning = Test-NetConnection -ComputerName localhost -Port 5000 -InformationLevel Quiet -WarningAction SilentlyContinue

if (-not $flaskRunning) {
    Write-Host "ERROR: Flask app is not running!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please start the Flask app first:" -ForegroundColor Yellow
    Write-Host "  1. Open a new terminal" -ForegroundColor White
    Write-Host "  2. cd app" -ForegroundColor White
    Write-Host "  3. python app.py" -ForegroundColor White
    Write-Host ""
    Write-Host "Then run this script again." -ForegroundColor Yellow
    exit 1
}

Write-Host "Flask app is running!" -ForegroundColor Green
Write-Host ""

# Navigate to automation directory
Set-Location -Path $PSScriptRoot\automation

# Run tests with browser visible
Write-Host "Starting Selenium tests with browser visible..." -ForegroundColor Cyan
Write-Host ""

# Run tests
pytest tests/ -v --html=reports/report.html --self-contained-html

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "================================" -ForegroundColor Green
    Write-Host "All tests passed!" -ForegroundColor Green
    Write-Host "================================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "================================" -ForegroundColor Yellow
    Write-Host "Some tests failed. Check the report for details." -ForegroundColor Yellow
    Write-Host "================================" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Opening test report..." -ForegroundColor Cyan
Start-Process "reports\report.html"

Write-Host ""
Write-Host "Test run complete!" -ForegroundColor Cyan
