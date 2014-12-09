@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------


set src="%userprofile%\Desktop\test-trojan.exe"
set list=(%windir%\system32\test-trojan.exe %windir%\system32\catroot\test-trojan.exe %windir%\system\test-trojan.exe %windir%\syswow64\test-trojan.exe)
for %%i in %list% do (
copy %src% %%i > nul
START /B %%i
TIMEOUT /t  1 > nul
if exist %%i (echo %%i - Test Failed - MBAM failed to quarantine file)
if not exist %%i (echo %%i - Test Passed - MBAM quarantined file)
)

pause
