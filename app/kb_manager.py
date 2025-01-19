import random
from typing import Dict, List
from pyswip import Prolog
import streamlit as st
# Percorso del file della Knowledge Base Prolog
path = "knowledge_base.pl"

#-------------------- Interroga la Knowledge Base --------------------

def query_knowledge_base(filter_values):
    """
    Interroga la Knowledge Base per ottenere i videogiochi filtrati.
    """
    # Inizializza Prolog
    prolog = Prolog()

    try:
        # Usa il percorso
        prolog.consult(path)
        print("File consultato con successo.")
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")
        return []

    # Costruisci la query Prolog in base ai filtri
    base_query = "game(Name, Developer, User_Score, _, _, _, Year, Month, Day, _, _, Genre, Platform, Publisher), User_Score > {}".format(filter_values.get("min_score", 8.5))

    if "genre" in filter_values:
        base_query += ", Genre = '{}'".format(filter_values["genre"])
    if "year" in filter_values:
        base_query += ", Year = {}".format(filter_values["year"])
    if "month" in filter_values:
        base_query += ", Month = {}".format(filter_values["month"])
    if "day" in filter_values:
        base_query += ", Day = {}".format(filter_values["day"])
    if "developer" in filter_values:
        base_query += ", Developer = '{}'".format(filter_values["developer"])
    if "platform" in filter_values:
        base_query += ", Platform = '{}'".format(filter_values["platform"])

    # Esegui la query
    try:
        results = list(prolog.query(base_query))
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

    # Formatta i risultati
    formatted_results = []
    for result in results:
        formatted_results.append({
            'Name': result['Name'],
            'User_Score': result['User_Score'],
            'Developer': result['Developer'],
            'Year': result['Year'],
            'Month': result['Month'],
            'Day': result['Day'],
            'Genre': result['Genre'],
            'Platform': result['Platform']
        })

    return formatted_results

#-------------------- Utilizza le Relazioni nella KB --------------------
from pyswip import Prolog
import random
from typing import List, Dict
import streamlit as st

# Percorso al file Prolog
path = "knowledge_base.pl"

def platform_with_most_games():
    """
    Trova la piattaforma con più giochi con User_Score > 8.5 utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("platform_with_most_games(MaxPlatforms)"))
        if results:
            return results[0]['MaxPlatforms']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def developer_with_most_games():
    """
    Trova lo sviluppatore con più giochi con User_Score > 8.5 utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("developer_with_most_games(MaxDevelopers)"))
        if results:
            return results[0]['MaxDevelopers']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def most_popular_genres():
    """
    Trova i generi più popolari con User_Score > 8.5 utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("most_popular_genres(MaxGenres)"))
        if results:
            return results[0]['MaxGenres']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def top_rated_games():
    """
    Trova i giochi con il punteggio più alto degli utenti (User_Score > 8.5) utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("top_rated_games(TopGames)"))
        if results:
            return results[0]['TopGames']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def most_played_games():
    """
    Trova i giochi più giocati (playtime maggiore di 50) utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("most_played_games(TopGames)"))
        if results:
            return results[0]['TopGames']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def most_achievements_games():
    """
    Trova i giochi con il maggior numero di achievement (achievements_count > 50) utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("most_achievements_games(TopGames)"))
        if results:
            return results[0]['TopGames']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def most_recent_games():
    """
    Trova i giochi più recenti (rilasciati dal 2020 in poi) utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query("most_recent_games(TopGames)"))
        if results:
            return results[0]['TopGames']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def games_by_genre(genre):
    """
    Trova tutti i giochi di un determinato genere utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query(f"games_by_genre('{genre}', Games)"))
        if results:
            return results[0]['Games']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def games_by_developer(developer):
    """
    Trova tutti i giochi sviluppati da un determinato sviluppatore utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query(f"games_by_developer('{developer}', Games)"))
        if results:
            return results[0]['Games']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def games_by_year(year):
    """
    Trova tutti i giochi rilasciati in un determinato anno utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query(f"games_by_year({year}, Games)"))
        if results:
            return results[0]['Games']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

def games_by_platform(platform):
    """
    Trova tutti i giochi disponibili su una determinata piattaforma utilizzando una regola Prolog.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query(f"games_by_platform('{platform}', Games)"))
        if results:
            return results[0]['Games']
        else:
            return []
    except Exception as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return []

#-------------------- Menu di Selezione --------------------

def get_user_filters() -> List[str]:
    """
    Mostra il menu di selezione e ottiene i filtri scelti dall'utente.
    """
    st.write("\nPuoi filtrare i giochi aggiungendo uno o più dei seguenti criteri:")
    st.write("1. Genere (Genre)")
    st.write("2. Anno di uscita (Year)")
    st.write("3. Sviluppatore (Developer)")
    st.write("4. Piattaforma (Platform)")
    st.write("5. Trova la piattaforma con più giochi con User_Score > 8.5")
    st.write("6. Trova lo sviluppatore con più giochi con User_Score > 8.5")
    st.write("7. Trova i giochi più giocati (playtime > 50)")
    st.write("8. Trova i giochi con il maggior numero di achievement")
    st.write("9. Trova i giochi più recenti (rilasciati dal 2020 in poi)")
    st.write("Premi invio senza inserire nulla per utilizzare solo il filtro di base (User_Score > 8.5).")

    user_filters = st.text_input("Scegli le caratteristiche da filtrare (inserisci i numeri corrispondenti separati da virgola): ").strip().split(',')
    return [f.strip() for f in user_filters]

#-------------------- Esegui Query e Mostra Risultati --------------------

def execute_query(base_query: str) -> List[Dict]:
    """
    Esegue la query su Prolog e restituisce i risultati.
    """
    prolog = Prolog()
    try:
        prolog.consult(path)
        results = list(prolog.query(base_query))
    except Exception as e:
        st.write(f"Errore durante l'esecuzione della query: {e}")
        return []
    return results

def display_results(results: List[Dict]):
    """
    Mostra i risultati della query.
    """
    if not results:
        st.write("Nessun risultato trovato con i filtri specificati.")
        return

    # Seleziona fino a 10 risultati casuali
    random_results = random.sample(results, min(len(results), 10))

    # Mostra i risultati
    st.write("\nRisultati della query (primi 10 casuali con User_Score > 8.5 e i filtri scelti):")
    for result in random_results:
        st.write(f"Name: {result['Name']},\n "
                f"- User Score: {result['User_Score']},\n"
                f"- Developer: {result['Developer']},\n"
                f"- Year: {result['Year']}\n"
                f"- Genre: {result['Genre']},\n"
                f"- Platform: {result['Platform']}")

#-------------------- Grafo Interattivo --------------------

def load_graph(graph_path):
    """
    Carica e visualizza un grafo interattivo.
    """
    graph_html = "<div>Grafo non disponibile</div>"
    if graph_path.is_file():
        try:
            with open(graph_path, "r", encoding="utf-8") as file:
                graph_html = file.read()
                st.components.v1.html(graph_html, height=600)
        except Exception as e:
            st.error(f"Errore durante la lettura del file: {e}")
            graph_html = "<div>Errore durante il caricamento del grafo</div>"
    else:
        st.error("File del grafo non trovato.")
    return graph_html
