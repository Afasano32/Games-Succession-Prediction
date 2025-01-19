
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

## Installazione

1. Clona il repository:
   ```bash
   git clone https://github.com/Afasano32/Games-Succession-Prediction.git
   ```
2. Crea e attiva un ambiente virtuale:
   ```bash
   python -m venv myenv
   source myenv/bin/activate 
   ```
   Ambiente Windows
   ```bash
   python -m venv myenv
   source myenv\Scripts\activate
   ```
3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

## Esecuzione

Per avviare l'applicazione, esegui lo script batch:
```bash
./videogamesuccess.bat
```
oppure eseguire il comando:
```bach
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
