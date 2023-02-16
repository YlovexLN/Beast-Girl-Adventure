@echo off
chcp 65001
REM 设置mod ID列表
set MOD_ID_LIST=1 2 3 4
REM 设置CurseForge API URL
set API_URL=https://addons-ecs.forgesvc.net/api/v2/addon/%s

REM 创建一个空数组来存储mod信息
set MOD_INFO_LIST=
set "JSON_START=["
set "JSON_END=]"
set "JSON_SEPARATOR=,"
set "JSON_OBJECT_START={"
set "JSON_OBJECT_END=}"
set "JSON_PROPERTY_NAME_START=\""
set "JSON_PROPERTY_NAME_END=\":"
set "JSON_PROPERTY_VALUE_START=\""
set "JSON_PROPERTY_VALUE_END=\""

REM 遍历mod ID列表，发送HTTP请求获取mod信息
for %%i in (%MOD_ID_LIST%) do (
  set API_URL_CUR=!API_URL:%s=%%i!
  echo 正在获取mod %%i 的信息...
  set /p JSON_CUR=< <(powershell -Command "Invoke-WebRequest -Uri !API_URL_CUR! -UseBasicParsing | Select-Object -Expand Content")
  REM 提取名称、版本号、下载地址等信息，存入一个对象数组中
  for /f "tokens=1,2 delims=:" %%a in ('echo !JSON_CUR! ^| findstr /i "name^|filedetails"') do (
    if "%%a"=="      \"name\"" (
      set MOD_NAME=%%b
      set MOD_NAME=!MOD_NAME:"=! 
    ) else if "%%a"=="            \"downloadUrl\"" (
      set MOD_URL=%%b
      set MOD_URL=!MOD_URL:"=!
      REM 这里的%%~ni是将文件名作为mod版本号
      set MOD_INFO_LIST=!MOD_INFO_LIST!!JSON_SEPARATOR!!JSON_OBJECT_START!!JSON_PROPERTY_NAME_START!name!JSON_PROPERTY_NAME_END!!JSON_PROPERTY_VALUE_START!!MOD_NAME!JSON_PROPERTY_VALUE_END!!JSON_SEPARATOR!!JSON_PROPERTY_NAME_START!version!JSON_PROPERTY_NAME_END!!JSON_PROPERTY_VALUE_START!%%~ni!JSON_PROPERTY_VALUE_END!!JSON_SEPARATOR!!JSON_PROPERTY_NAME_START!url!JSON_PROPERTY_NAME_END!!JSON_PROPERTY_VALUE_START!!MOD_URL!JSON_PROPERTY_VALUE_END!!JSON_OBJECT_END!
    )
  )
)

REM 将对象数组转换为json字符串，写入mod-list.json文件中
set MOD_INFO_LIST=!MOD_INFO_LIST:~1!
set JSON_STRING=%JSON_START%%MOD_INFO_LIST%%JSON_END%
echo %JSON_STRING% > ./temp/mod-list.json

REM 上传mod-list.json文件到github仓库
echo 正在上传mod-list.json文件到github仓库...
set COMMIT_TIME=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
git add ./temp/mod-list.json
git commit -m "更新mod列表到 %COMMIT_TIME%"
git push

echo mod-list.json已生成,且已上传到github仓库。
