@echo off
REM Imposta il numero di core da utilizzare
set LOKY_MAX_CPU_COUNT=8

REM Verifica se Python è installato
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python non è installato sul sistema.
    echo Verrà avviata l'installazione di Python...
    REM Scarica l'installer di Python
    echo Scaricando l'installer di Python...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe' -OutFile 'python_installer.exe'"
    
    REM Esegui l'installer di Python
    echo Installando Python...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe

    echo Python è stato installato. Riavvia il file .bat per continuare.
    pause
    exit /b
)

REM Verifica se pip è installato
where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip non è installato. Installazione di pip...
    python -m ensurepip --upgrade
)

REM Controlla se l'ambiente virtuale esiste già
if exist venv (
    echo Ambiente virtuale già presente.
) else (
    echo Creazione dell'ambiente virtuale...
    python -m venv venv
)

REM Attiva l'ambiente virtuale
echo Attivazione dell'ambiente virtuale...
call venv\Scripts\activate.bat

REM Installa le dipendenze
echo Installazione delle dipendenze da requirements.txt...
pip install -r requirements.txt

REM Passa l'email come argomento allo script Streamlit
set EMAIL="progetto.con.videogamesuccess@gmail.com"
echo Avvio dell'applicazione con l'email: %EMAIL%
streamlit run app/main.py -- %EMAIL%

pause