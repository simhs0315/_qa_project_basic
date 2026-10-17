# 경로 설정: Collection과 리포트 저장 위치를 지정
# 테스트 실행: Newman으로 API 테스트 실행 및 HTML 리포트 생성
# 결과 전달: 성공하면 exit 0, 실패하면 exit 1

$projectRoot = Split-Path -Parent $PSScriptRoot
$collectionPath = Join-Path $projectRoot "api_tests/JSONPlaceholder API Test.postman_collection.json"
$reportPath = Join-Path $projectRoot "reports/newman-report.html"

newman run $collectionPath -r "cli,html" --reporter-html-export $reportPath

if ($LASTEXITCODE -eq 0) {
    Write-Host "API Test PASSED"
    exit 0
}
else {
    Write-Host "API Test FAILED"
    exit 1
}