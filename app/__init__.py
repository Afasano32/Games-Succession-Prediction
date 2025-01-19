# app/__init__.py

# Importa funzioni e classi dai moduli del pacchetto
from .preprocess import (
    # Funzioni per il preprocessing
    preprocess_input,
    one_hot_encode_categorical,
    get_columns,  # Aggiunto get_columns
)

# Importa funzioni e classi dai moduli del pacchetto
from .kb_manager import (
    # Funzioni per interrogare la Knowledge Base
    query_knowledge_base,

    # Funzioni per le statistiche
    platform_with_most_games,
    developer_with_most_games,
    most_popular_genres,
    top_rated_games,
    top_multiplayer_games,
    games_by_genre,
    games_by_developer,
    games_by_year,
    games_by_player_type,
    games_by_platform,
    most_played_games,
    most_achievements_games,
    most_recent_games,
    
    load_graph,
)

from .main import (
    # Funzioni principali dell'app
    load_model,
)

# Definisci cosa viene esportato quando si fa `from app import *`
__all__ = [
    # Funzioni per il preprocessing
    'preprocess_input',
    'one_hot_encode_categorical',
    'get_columns',  # Aggiunto get_columns

    # Funzioni per interrogare la Knowledge Base
    'query_knowledge_base',

    # Funzioni per le statistiche
    'platform_with_most_games',
    'developer_with_most_games',
    'most_popular_genres',
    'top_rated_games',
    'top_multiplayer_games',
    'games_by_genre',
    'games_by_developer',
    'games_by_year',
    'games_by_player_type',
    'games_by_platform',
    'most_played_games',
    'most_achievements_games',
    'most_recent_games',
    
    'load_graph',

    # Funzioni principali dell'app
    'load_model',
]

# Configurazioni iniziali
APP_NAME = "Videogame Success Predictor"
VERSION = "1.0.0"

# Messaggio di avvio
print(f"{APP_NAME} v{VERSION} initialized.")