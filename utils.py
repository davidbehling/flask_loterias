import requests
import zipfile
import io
import pandas as pd
import random

URLS = {
    'Mega-Sena': 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Mega-Sena',
    'Lotofacil': 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotofácil',
    'Quina': 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Quina'
}

QTDE_NUMEROS = {
    'Mega-Sena': 6,
    'Lotofacil': 15
}

QTDE_NUMEROS_MIN_AND_MAX = {
    'Mega-Sena': [6, 20],
    'Lotofacil': [15, 20]
}

LIMITE_NUMEROS = {
    'Mega-Sena': 60,
    'Lotofacil': 25
}

def gerar_numeros_aleatorios(jogo, qtde=None):
    min_val, max_val = QTDE_NUMEROS_MIN_AND_MAX[jogo]
    qtde = qtde or min_val  # se não passar, usa o mínimo como default
    return sorted(random.sample(range(1, LIMITE_NUMEROS[jogo] + 1), qtde))

def baixar_e_ler_resultados(jogo):
    url = URLS[jogo]
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Erro ao baixar os dados da Caixa")

    try:
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        csv_files = [f for f in zip_file.namelist() if f.endswith('.csv')]
        if not csv_files:
            raise Exception("Nenhum CSV encontrado")

        with zip_file.open(csv_files[0]) as f:
            df = pd.read_csv(f, sep=';', encoding='latin1')
            df = df[['Concurso', 'Data sorteio', 'Dezena 1', 'Dezena 2', 'Dezena 3', 'Dezena 4',
                     'Dezena 5', 'Dezena 6'] + ([f'Dezena {i}' for i in range(7, 16)] if jogo == 'Lotofacil' else [])]
            df['Data sorteio'] = pd.to_datetime(df['Data sorteio'], dayfirst=True)
            return df
    except Exception as e:
        raise Exception("Erro ao processar o arquivo baixado: " + str(e))

def comparar_numeros(df, numeros_aleatorios):
    resultados = []
    for _, row in df.iterrows():
        dezenas = [int(row[f'Dezena {i}']) for i in range(1, len(numeros_aleatorios)+1) if not pd.isna(row.get(f'Dezena {i}'))]
        acertos = len(set(dezenas).intersection(set(numeros_aleatorios)))
        resultados.append({
            'data': row['Data sorteio'],
            'dezenas': dezenas,
            'acertos': acertos
        })
    return resultados
