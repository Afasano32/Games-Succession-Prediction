# Videogame Success Predictor

## Descrizione del Progetto
Il progetto **Videogame Success Predictor** è un'applicazione che utilizza tecniche di machine learning per prevedere il successo dei videogiochi. Il sistema è progettato per analizzare diversi parametri e caratteristiche dei videogiochi per fornire previsioni accurate.

## Struttura del Progetto

### Cartelle Principali

- **documentazione**: Contiene la documentazione del progetto, e una presentazioni.
- **app**: Include il codice sorgente dell'applicazione, con script Python per la gestione della knowledge base, il preprocessamento dei dati e il file principale dell'applicazione.
- **data**: Contiene i dati utilizzati nel progetto, suddivisi in cartelle per dati grezzi, intermedi e processati.
- **kb**: Include file relativi alla knowledge base, come grafi interattivi e la base di conoscenza in formato Prolog.
- **models**: Contiene i modelli di machine learning salvati e i parametri utilizzati per l'addestramento.
- **myenv**: Ambiente virtuale per il progetto.
- **notebooks**: Include notebook Jupyter per l'analisi dei dati, il preprocessamento e la creazione di modelli di stacking.

### File Principali

- **README.md**: Questo file, contenente la documentazione del progetto.
- **requirements.txt**: Elenco delle dipendenze necessarie per eseguire il progetto.
- **videogamesuccess.bat**: Script batch per l'avvio del progetto.

## Guida all'Installazione

Questa guida ti aiuterà a configurare e avviare **VideoGameSuccess**.

### Prerequisiti

Assicurati di avere i seguenti strumenti installati sul tuo sistema:
- **Python 3.8 o superiore**: [Scarica Python](https://www.python.org/downloads/)
- **pip** (gestore di pacchetti Python): Di solito è incluso con l'installazione di Python.
- **Git** (opzionale): [Scarica Git](https://git-scm.com/downloads)

### Installazione

1. **Clona il repository** (se il progetto è su GitHub):
   ```bash
   git clone https://github.com/Afasano32/Games-Succession-Prediction.git
   ```

2. **OPZIONE: Avvio rapido**:
   Esegui il file `VideoGameSuccess.bat` (**NON eseguire come amministratore**).
   - Il file contiene uno script che verificherà la presenza di Python nel sistema e in caso di mancanza lo installerà.
   - Creerà un ambiente virtuale e installerà tutte le dipendenze.
   - Avvierà l'interfaccia web di Streamlit per accedere al prototipo.

3. **OPZIONE: Configurazione manuale**:
   1. **Crea un ambiente virtuale** (consigliato):
      - Creare un ambiente virtuale ti permette di isolare le dipendenze del progetto.
      - Comando Python:
        ```bash
        python -m venv venv
        ```
      - Attivazione ambiente virtuale:
        - **Windows**:
          ```bash
          venv\Scripts\activate
          ```
        - **Linux/macOS**:
          ```bash
          source venv/bin/activate
          ```

   2. **Installa le dipendenze**:
      - Usa `pip` per installare le dipendenze necessarie elencate nel file `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```

   3. **Esegui il progetto**:
      - Una volta configurato tutto, puoi avviare il progetto con il comando:
        ```bash
        streamlit run app/main.py
        ```

## Contributi

Se desideri contribuire al progetto, segui questi passaggi:

1. Fork del repository.
2. Crea un nuovo branch:
   ```bash
   git checkout -b feature/nuova-funzionalità
   ```
3. Fai commit delle tue modifiche:
   ```bash
   git commit -m "Aggiunta nuova funzionalità"
   ```
4. Push del branch:
   ```bash
   git push origin feature/nuova-funzionalità
   ```
5. Apri una pull request.

## Licenza

Questo progetto è licenziato sotto la Licenza MIT. Vedi il file `LICENSE` per ulteriori dettagli.

---
