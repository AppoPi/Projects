@color 48
@echo off
cd /d %~dp0

FOR /L %%G IN (1,1,200) DO (
md "%windir%\ADS Test %%G"
copy "%cd%\Files\File.exe" "%windir%\ADS Test %%G"
copy "%cd%\Files\ADS Test 2.exe" "%windir%"
echo Test.ADS.1>"%windir%:ADS Test %%G"
echo "%windir%\ADS Test 2.exe">"%windir%\ADS Test %%G\File.exe:ADS Test %%G.exe"
)
pause
exit