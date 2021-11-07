@echo off
setlocal
ECHO You are about to update the NLP Suite pulling the newest release from GitHub.
ECHO For this to happen, though, you need to be connected to the internet.
ECHO You will also need the freeware Git installed on your machine. Download Git at https://git-scm.com/downloads, if it has not been installed already.

@echo off
echo(
SET /P AREYOUSURE=Do you wish to continue? [y/n]
IF /I "%AREYOUSURE%" NEQ "y" GOTO END
@echo off
cd "%~dp0\..\" || git add -A . || git stash || git pull -f origin
:PROMPT
echo(
ECHO You have updated the NLP Suite to the latest release available on GitHub.
SET /P ENDPROMPT=Press Return to close this window.
EXIT 0

:END
:PROMPT
SET /P ENDPROMPT=Installation Aborted. Press Return to close this window now.
EXIT 0
