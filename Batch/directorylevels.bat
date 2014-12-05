@echo off

set trojan="%userprofile%\Desktop\test-trojan.exe"

if not exist %trojan% (
echo test-trojan could not be found
goto End
)

set origin=%CD%

set levels=10
set dirname=folder

cd %userprofile%\Desktop
for /L %%G in (1,1,%levels%) DO (
mkdir %dirname%
cd %dirname%
copy %userprofile%\Desktop\test-trojan.exe test-trojan.exe
)

cd %origin%


:End

pause