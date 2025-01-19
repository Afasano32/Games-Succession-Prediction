import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

#--------------------UTILS: Predizioni--------------------

# Funzione per ottenere le colonne categoriche
def get_columns():
    df = pd.read_csv('data/processed/Preprocessed_dataset_completo.csv')
    
    # Estrai i valori unici per ciascuna colonna categorica
    genere_columns = df['genery'].unique().tolist()
    platform_columns_unique = df['platform'].unique().tolist()
    publisher_columns = df['publisher'].unique().tolist()
    developer_columns = df['developer'].unique().tolist()
    
    return genere_columns, platform_columns_unique, publisher_columns, developer_columns


# Funzione di preprocessing per il modello
def preprocess_input(input_data, variance_threshold=0.90):
    """
    Preprocessa i dati di input per il modello di regressione.
    """
    # Debug: Stampa i dati di input originali
    print("Input data originale:", input_data)

    # Carica il dataset completo (template)
    template = pd.read_csv('data/processed/Preprocessed_dataset_completo.csv')

    # Aggiungi i dati di input al template come ultima riga
    input_data['user_score'] = 0  # Aggiungi una colonna fittizia per 'user_score'
    template = pd.concat([template, input_data], ignore_index=True)

    # Debug: Stampa le dimensioni del template dopo l'aggiunta dei dati di input
    print("Dimensioni del template dopo l'aggiunta dei dati di input:", template.shape)

    # Inizializza gli encoder per le variabili categoriche
    genre_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    platform_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

    # Applica l'encoding alle colonne categoriche del template
    genre_encoded_data = genre_encoder.fit_transform(template[['genery']])
    platform_encoded_data = platform_encoder.fit_transform(template[['platform']])

    # Crea DataFrame dalle colonne codificate
    genre_encoded_data_df = pd.DataFrame(genre_encoded_data, columns=genre_encoder.get_feature_names_out(['genery']))
    platform_encoded_data_df = pd.DataFrame(platform_encoded_data, columns=platform_encoder.get_feature_names_out(['platform']))

    # Rimuovi le colonne categoriche originali e aggiungi quelle codificate
    template = template.drop(['genery', 'platform'], axis=1)
    template = pd.concat([template, genre_encoded_data_df, platform_encoded_data_df], axis=1)

    # Seleziona solo le colonne dummy (quelle generate dall'encoding)
    dummy_columns = genre_encoded_data_df.columns.union(platform_encoded_data_df.columns)
    dummy_data = template[dummy_columns]

    # Applica PCA con varianza cumulativa del 90%
    pca = PCA(n_components=variance_threshold)
    pca_data = pca.fit_transform(dummy_data)

    # Crea un DataFrame con i componenti principali
    n_components = pca.n_components_  # Numero di componenti selezionati
    pca_columns = [f'PC{i+1}' for i in range(n_components)]
    pca_data_df = pd.DataFrame(pca_data, columns=pca_columns)

    # Rimuovi le colonne dummy originali e aggiungi i componenti principali
    template = template.drop(dummy_columns, axis=1)
    template = pd.concat([template, pca_data_df], axis=1)

    # Rimuovi colonne non necessarie per la predizione
    drop_columns = ['name', 'user_score', 'developer', 'publisher']
    template = template.drop(drop_columns, axis=1)

    # Gestione dei valori mancanti
    template = template.fillna(0)  # Sostituisci i valori NaN con 0

    # Normalizzazione
    scaler = MinMaxScaler()
    template_normalized = pd.DataFrame(scaler.fit_transform(template), columns=template.columns)

    # Debug: Stampa i dati normalizzati
    print("Dati normalizzati:", template_normalized.tail(1))

    # Estrai solo l'ultima riga (corrispondente ai dati di input)
    processed_data = template_normalized.iloc[[-1]]

    return processed_data