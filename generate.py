import random
import global_values

QTDE_NUMBERS_MIN_AND_MAX = {
  'Mega-Sena': [6, 20],
  'Lotofacil': [15, 20],
  'Quina': [5, 15]
}

NUMBERS_LIMITED = {
  'Mega-Sena': 60,
  'Lotofacil': 25,
  'Quina': 80
}

HITS_MIN = {
  'Mega-Sena': 4,
  'Lotofacil': 13,
  'Quina': 2
}

def contido(a, b):
  return all(elem in b for elem in a)

def drawn_numbers(jogo):
  if jogo == 'Mega-Sena':
    return global_values.megasena   
  if jogo == 'Lotofacil':
    return global_values.lotofacil
  if jogo == 'Quina':
    return global_values.quina

def generate_numbers_(jogo, qtde=None, method=None):
  return globals()[method](jogo, qtde)    

def range_numbers(jogo, qtde=None):
  min_val, max_val = QTDE_NUMBERS_MIN_AND_MAX[jogo]
  qtde = qtde or min_val
  return sorted(random.sample(range(1, NUMBERS_LIMITED[jogo] + 1), qtde))

def undrawn_random_numbers(jogo, qtde=None):
  range_number = range_numbers(jogo, qtde)

  for number in drawn_numbers(jogo):
    if contido(number.balls_drawn, range_number):
      return undrawn_random_numbers(jogo, qtde)

  return range_number

def most_drawn_numbers(jogo, qtde):
  list_drawn_balls = global_values.recurrence_of_drawn_balls[jogo]
  return [k for k, v in sorted(list_drawn_balls.items(), key=lambda item: item[1], reverse=True)[:qtde]]

def least_drawn_numbers(jogo, qtde):
  list_drawn_balls = global_values.recurrence_of_drawn_balls[jogo]
  return [k for k, v in sorted(list_drawn_balls.items(), key=lambda item: item[1])[:qtde]]

def check_hits(numbers, jogo):
  results = []

  for draw_numbers in drawn_numbers(jogo):
    hits = set(numbers).intersection(set(draw_numbers.balls_drawn))
    hit_amount = len(hits)

    if hit_amount >= HITS_MIN[jogo]:
      obj = {
        'data': draw_numbers.draw_date,
        'numero': draw_numbers.draw_number,
        'bolas_sorteadas': draw_numbers.balls_drawn,
        'bolas_acertadas': hits,
        'pontuacao': hit_amount
      }
      
      results.append(obj)
    
  return results

def get_drawn_numbers(jogo):
  results = []

  for draw_numbers in drawn_numbers(jogo):
    obj = {
      'data': draw_numbers.draw_date,
      'numero': draw_numbers.draw_number,
      'bolas_sorteadas': draw_numbers.balls_drawn
    }
      
    results.append(obj)
      
    
  return results
