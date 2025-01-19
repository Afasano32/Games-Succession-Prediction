
import streamlit as st
import pandas as pd
import pickle
import random
from pathlib import Path

# Import delle funzioni di preprocessing
from preprocess import preprocess_input, get_columns

# Import delle funzioni per la Knowledge Base
from kb_manager import (
    query_knowledge_base,
    platform_with_most_games,
    developer_with_most_games,
    most_popular_genres,
    top_rated_games,
    most_played_games,
    most_achievements_games,
    most_recent_games,
    load_graph,
)


# Messaggio di errore predefinito
error_message = "Nessun risultato trovato."

@st.cache_resource(ttl=1)  # Ricarica il modello ogni 1 secondo
def load_model():
    with open('models/save_dir/Stacking_meta_modello_Linear_Regressor.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Titolo dell'app
st.title("Video Game Success Predictor")

# Selezione della modalità
mode = st.radio(
    "Seleziona la modalità:", 
    ["Prevedi il successo!", "Video Game Knowledge Base"],
    key="mode_radio"  # Aggiungi un key univoco
)

if mode == "Prevedi il successo!":
    st.header("Previsione del Successo dei Videogiochi")

    genere_columns, platform_columns_unique, publisher_columns, developer_columns = get_columns()
    
    # Valori predefiniti basati sulle immagini
    default_values = {
        "name": "LittleBigPlanet",
        "genery": "Action",
        "platform": "PSP",
        "publisher": "Sony Interactive Entertainment",
        "developer": "Sony Computer Entertainment",
        "critics": 85.00,
        "users": 5533,
        "playtime": 5,
        "achievements_count": 66,
        "suggestions_count": 502,
        "game_series_count": 4,
        "reviews_count": 455,
        "added_status_yet": 27,
        "added_status_owned": 1436,
        "added_status_beaten": 363,
        "added_status_toplay": 26,
        "added_status_dropped": 165,
        "added_status_playing": 11,
        "released_year": 2008,
        "released_month": 10,
        "released_day": 27,
        "updated_year": 2020,
        "updated_month": 1,
        "updated_day": 7,
        "is_in_top_100_publisher": True,
        "is_in_top_100_developer": False
    }

    # Input dell'utente con valori predefiniti
    name = st.text_input("Nome del Gioco", value=default_values["name"], key="name_input")
    genre = st.selectbox("Genere", genere_columns, index=genere_columns.index(default_values["genery"]), key="genre_select")
    platform = st.selectbox("Piattaforma", platform_columns_unique, index=platform_columns_unique.index(default_values["platform"]), key="platform_select")
    publisher = st.selectbox("Editore", publisher_columns, index=publisher_columns.index(default_values["publisher"]), key="publisher_select")
    developer = st.selectbox("Sviluppatore", developer_columns, index=developer_columns.index(default_values["developer"]), key="developer_select")
    
    critics = st.number_input("Numero di Critici", min_value=0.0, max_value=100.0, value=default_values["critics"], key="critics_input")
    users = st.number_input("Numero di Utenti", min_value=0, value=default_values["users"], key="users_input")
    playtime = st.number_input("Tempo di Gioco", min_value=0, value=default_values["playtime"], key="playtime_input")
    achievements_count = st.number_input("Numero di Achievements", min_value=0, value=default_values["achievements_count"], key="achievements_input")
    suggestions_count = st.number_input("Numero di Suggerimenti del videogioco", min_value=0, value=default_values["suggestions_count"], key="suggestions_count_input")
    game_series_count = st.number_input("Numero di Giochi della Serie", min_value=0, value=default_values["game_series_count"], key="game_series_count_input")
    reviews_count = st.number_input("Numero di Recensioni", min_value=0, value=default_values["reviews_count"], key="reviews_count_input")
    
    added_status_yet = st.number_input("Aggiunto: Non Giocato", min_value=0, max_value=99999, value=default_values["added_status_yet"], key="added_status_yet")
    added_status_owned = st.number_input("Aggiunto: Posseduto", min_value=0, max_value=99999, value=default_values["added_status_owned"], key="added_status_owned")
    added_status_beaten = st.number_input("Aggiunto: Completato", min_value=0, max_value=99999, value=default_values["added_status_beaten"], key="added_status_beaten")
    added_status_toplay = st.number_input("Aggiunto: Da Giocare", min_value=0, max_value=99999, value=default_values["added_status_toplay"], key="added_status_toplay")
    added_status_dropped = st.number_input("Aggiunto: Abbandonato", min_value=0, max_value=99999, value=default_values["added_status_dropped"], key="added_status_dropped")
    added_status_playing = st.number_input("Aggiunto: In Corso", min_value=0, max_value=99999, value=default_values["added_status_playing"], key="added_status_playing")
        
    released_year = st.number_input("Anno di Uscita", min_value=1998, max_value=2130, value=default_values["released_year"], key="released_year_input")
    released_month = st.number_input("Mese di Uscita", min_value=1, max_value=12, value=default_values["released_month"], key="released_month_input")
    released_day = st.number_input("Giorno di Uscita", min_value=1, max_value=31, value=default_values["released_day"], key="released_day_input")
    
    updated_year = st.number_input("Anno di Aggiornamento", min_value=1980, max_value=2030, value=default_values["updated_year"], key="updated_year_input")
    updated_month = st.number_input("Mese di Aggiornamento", min_value=1, max_value=12, value=default_values["updated_month"], key="updated_month_input")
    updated_day = st.number_input("Giorno di Aggiornamento", min_value=1, max_value=31, value=default_values["updated_day"], key="updated_day_input")
    
    is_in_top_100_publisher = st.checkbox("Editore nei Top 100", value=default_values["is_in_top_100_publisher"], key="is_in_top_100_publisher")
    is_in_top_100_developer = st.checkbox("Sviluppatore nei Top 100", value=default_values["is_in_top_100_developer"], key="is_in_top_100_developer")

    # Preprocessing dei dati
    input_data = pd.DataFrame({
        'name': [name],
        'genery': [genre],
        'platform': [platform],
        'publisher': [publisher],
        'developer': [developer],
        'critics': [critics],
        'users': [users],
        'playtime': [playtime],
        'achievements_count': [achievements_count],
        'suggestions_count': [suggestions_count],
        'game_series_count': [game_series_count],
        'reviews_count': [reviews_count],
        'added_status_yet': [added_status_yet],
        'added_status_owned': [added_status_owned],
        'added_status_beaten': [added_status_beaten],
        'added_status_toplay': [added_status_toplay],
        'added_status_dropped': [added_status_dropped],
        'added_status_playing': [added_status_playing],
        'released_year': [released_year],
        'released_month': [released_month],
        'released_day': [released_day],
        'updated_year': [updated_year],
        'updated_month': [updated_month],
        'updated_day': [updated_day],
        'is_in_top_100_publisher': [is_in_top_100_publisher],
        'is_in_top_100_developer': [is_in_top_100_developer]
    })

    # Predizione
    if st.button("Prevedi Successo", key="predict_button"):
        model = load_model()
        processed_data = preprocess_input(input_data)
        prediction = model.predict(processed_data)
        
    # Se il modello restituisce un valore fuori range, applica un clipping
        prediction = max(0, min(prediction[0], 10))  # Assicura che il valore sia tra 0 e 10
    
        st.write(f"**Punteggio previsto:** {prediction:.2f}")

elif mode == "Video Game Knowledge Base":
    st.title("Video Game: Knowledge Base")

    # Selezione della modalità
    mode_kb = st.radio(
        "Seleziona la modalità per interagire con la knowledge base:",
        ["Interroga la Knowledge Base", "Utilizza le Relazioni nella KB", "Grafo interattivo"]
    )

    if mode_kb == "Interroga la Knowledge Base":
        st.write("Puoi applicare i seguenti filtri alla tua ricerca:")
        
        # Filtri disponibili
        filter_options = {
            "Genere": "genre",
            "Anno di uscita": "year",
            "Mese di uscita": "month",
            "Giorno di uscita": "day",
            "Sviluppatore": "developer",
            "Piattaforma": "platform",
            "Punteggio minimo": "min_score"
        }
        
        # Selezione dei filtri
        selected_filters = st.multiselect(
            "Seleziona i filtri che vuoi applicare:",
            list(filter_options.keys())
        )
        
        # Dizionario per memorizzare i valori inseriti dall'utente
        filter_values = {}
        
        # Input manuale per i filtri selezionati
        for filter_name in selected_filters:
            filter_key = filter_options[filter_name]
            
            if filter_name == "Genere":
                genre_value = st.text_input("Inserisci il genere (es. Action, Adventure):").strip()
                if genre_value:
                    filter_values[filter_key] = genre_value
            
            elif filter_name == "Anno di uscita":
                year_value = st.text_input("Inserisci l'anno di uscita (es. 2008, 2010):").strip()
                if year_value and year_value.isdigit() and 1980 <= int(year_value) <= 2023:
                    filter_values[filter_key] = int(year_value)
                else:
                    st.warning("L'anno deve essere un numero tra 1980 e 2023. Verrà ignorato.")
            
            elif filter_name == "Mese di uscita":
                month_value = st.text_input("Inserisci il mese di uscita (1-12):").strip()
                if month_value and month_value.isdigit() and 1 <= int(month_value) <= 12:
                    filter_values[filter_key] = int(month_value)
                else:
                    st.warning("Il mese deve essere un numero tra 1 e 12. Verrà ignorato.")
            
            elif filter_name == "Giorno di uscita":
                day_value = st.text_input("Inserisci il giorno di uscita (1-31):").strip()
                if day_value and day_value.isdigit() and 1 <= int(day_value) <= 31:
                    filter_values[filter_key] = int(day_value)
                else:
                    st.warning("Il giorno deve essere un numero tra 1 e 31. Verrà ignorato.")
            
            elif filter_name == "Sviluppatore":
                developer_value = st.text_input("Inserisci lo sviluppatore (es. Nintendo, Sony):").strip()
                if developer_value:
                    filter_values[filter_key] = developer_value
            
            elif filter_name == "Piattaforma":
                platform_value = st.text_input("Inserisci la piattaforma (es. PC, PlayStation, Xbox):").strip()
                if platform_value:
                    filter_values[filter_key] = platform_value
            
            elif filter_name == "Punteggio minimo":
                min_score_value = st.text_input("Inserisci il punteggio minimo (es. 8.0, 9.5):").strip()
                if min_score_value and min_score_value.replace('.', '', 1).isdigit() and 0.0 <= float(min_score_value) <= 10.0:
                    filter_values[filter_key] = float(min_score_value)
                else:
                    st.warning("Il punteggio minimo deve essere un numero tra 0.0 e 10.0. Verrà utilizzato il valore di default (8.0).")
                    filter_values[filter_key] = 8.0

        # Interrogazione della KB
        if st.button("Cerca nella Knowledge Base"):
            # Se non è stato specificato un punteggio minimo, usiamo il valore di default
            if "min_score" not in filter_values:
                filter_values["min_score"] = 8.0
                
            # Esegui la query con i filtri selezionati
            results = query_knowledge_base(filter_values)
            
            if results:
                # Se ci sono più di 10 risultati, seleziona 10 in modo casuale
                if len(results) > 10:
                    results = random.sample(results, 10)

                st.write("**Risultati della ricerca (10 videogiochi casuali):**")
                for game in results:
                    st.write(f"- **Nome:** {game['Name']}, **Piattaforma:** {game['Platform']}, **Genere:** {game['Genre']}, **Punteggio:** {game['User_Score']}")
            else:
                st.write("Nessun risultato trovato con i filtri specificati.")
            
    elif mode_kb == "Utilizza le Relazioni nella KB":
        st.header("Relazione tra i Dati nella Knowledge Base")

        # Trova la piattaforma con più giochi con User_Score > 8.5
        if st.button("Trova la piattaforma con più giochi popolari tra gli Utenti"):
            platform_results = platform_with_most_games()
            if platform_results:
                st.write("**Piattaforma/e con più giochi popolari tra gli Utenti:**")
                for platform in platform_results:
                    st.write(f"- {platform}")
            else:
                st.write(error_message)

        # Trova lo sviluppatore con più giochi con User_Score > 8.5
        if st.button("Trova lo sviluppatore con più giochi popolari tra gli Utenti"):
            developer_results = developer_with_most_games()
            if developer_results:
                st.write("**Sviluppatore/i con più giochi popolari tra gli Utenti:**")
                for developer in developer_results:
                    st.write(f"- {developer}")
            else:
                st.write(error_message)

        # Trova i generi più popolari con User_Score > 8.5
        if st.button("Trova i generi più popolari tra gli Utenti"):
            genre_results = most_popular_genres()
            if genre_results:
                st.write("**Generi più popolari tra gli Utenti:**")
                for genre in genre_results:
                    st.write(f"- {genre}")
            else:
                st.write(error_message)

        # Trova i giochi con il punteggio più alto degli utenti
        if st.button("Trova i giochi con il punteggio più alto degli utenti"):
            top_rated_results = top_rated_games()
            if top_rated_results:
                st.write("**Giochi con il punteggio più alto degli utenti:**")
                for game in top_rated_results:
                    st.write(f"- {game}")
            else:
                st.write(error_message)

        # Trova i giochi più giocati (playtime > 50)
        if st.button("Trova i giochi più giocati"):
            most_played_results = most_played_games()
            if most_played_results:
                st.write("**Giochi più giocati (playtime > 50):**")
                for game in most_played_results:
                    st.write(f"- {game}")
            else:
                st.write(error_message)

        # Trova i giochi con il maggior numero di achievement
        if st.button("Trova i giochi con il maggior numero di achievement"):
            most_achievements_results = most_achievements_games()
            if most_achievements_results:
                st.write("**Giochi con il maggior numero di achievement:**")
                for game in most_achievements_results:
                    st.write(f"- {game}")
            else:
                st.write(error_message)

        # Trova i giochi più recenti (rilasciati dal 2020 in poi)
        if st.button("Trova i giochi più recenti"):
            most_recent_results = most_recent_games()
            if most_recent_results:
                st.write("**Giochi più recenti (rilasciati dal 2020 in poi):**")
                for game in most_recent_results:
                    st.write(f"- {game}")
            else:
                st.write(error_message)

    elif mode_kb == "Grafo interattivo":
        st.header("Grafo interattivo")
        
        # Pulsanti per la selezione del grafo
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Grafo 50"):
                graph_path = Path("kb/grafo_50.html")
        with col2:
            if st.button("Grafo 100"):
                graph_path = Path("kb/grafo_100.html")
        with col3:
            if st.button("Grafo 150"):
                graph_path = Path("kb/grafo_150.html")

        # Verifica se graph_path è stato definito
        if 'graph_path' in locals():
            # Carica il grafo selezionato
            load_graph(graph_path)
        else:
            st.info("Seleziona un grafo per visualizzarlo.")