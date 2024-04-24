@echo off
for /f "tokens=1,* delims==" %%a in ('type .env') do (
    set "%%a=%%b"
)
