import requests
import pandas as pd
import os

from dataclasses import dataclass
from datetime import date
from typing import List

from collections import defaultdict

import global_values

@dataclass
class ResultadoLotoFacil:
    draw_number: int
    draw_date: date
    balls_drawn: List[int]

def file_path(modality):
    base_path = os.path.join(os.path.dirname(__file__), "public", "files")
    modality_map = {
        'Mega-Sena': 'MEGA_SENA',
        'Lotofacil': 'LOTOFACIL',
        'Quina': 'QUINA'
    }

    today = date.today().strftime("%Y.%m.%d")
    file_name = f"{today}_{modality_map[modality]}.xlsx"
    return os.path.join(base_path, file_name)

def download_and_save_file(modality, path):
    response = requests.get(url(modality))

    if response.status_code != 200:
        raise Exception(f"Erro ao baixar os dados da Caixa para {modality}")

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'wb') as f:
        f.write(response.content)

def url(modality):
  return f"https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade={modality}"

def import_draws(modality, total_balls):
  #response = requests.get(url(modality))
  #if response.status_code != 200:
  #  raise Exception("Erro ao baixar os dados da Caixa")
  #excel_file = pd.read_excel(response.content)

  path = file_path(modality)

  if not os.path.exists(path):
      download_and_save_file(modality, path)

  excel_file = pd.read_excel(path)

  results = []

  for _, row in excel_file.iterrows():
    draw_number = int(row["Concurso"])

    if "Data Sorteio" in row:
      draw_date = pd.to_datetime(row["Data Sorteio"]).date()
    elif "Data do Sorteio" in row:
      draw_date = pd.to_datetime(row["Data do Sorteio"]).date()
    else:
      draw_date = None
    
    balls_drawn = [int(row[f"Bola{i}"]) for i in range(1, total_balls + 1)]
    
    result = ResultadoLotoFacil(
      draw_number=draw_number,
      draw_date=draw_date,
      balls_drawn=balls_drawn
    )

    results.append(result)
      
  return results

def recurrence_of_drawn_balls(drawn_numbers):
  count = defaultdict(int)

  for draw_numbers in drawn_numbers:
     for number in draw_numbers.balls_drawn:
        count[number] += 1
  
  return dict(count)

def get_draws():
  global_values.megasena = import_draws('Mega-Sena', 6)
  global_values.lotofacil = import_draws('Lotofacil', 15)
  global_values.quina = import_draws('Quina', 5)

  global_values.recurrence_of_drawn_balls['Mega-Sena'] = recurrence_of_drawn_balls(global_values.megasena)
  global_values.recurrence_of_drawn_balls['Lotofacil'] = recurrence_of_drawn_balls(global_values.lotofacil)
  global_values.recurrence_of_drawn_balls['Quina'] = recurrence_of_drawn_balls(global_values.quina)

