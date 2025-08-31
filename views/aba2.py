from flask import Blueprint, render_template, request
from generate import generate_numbers_, check_hits, QTDE_NUMBERS_MIN_AND_MAX

aba2_bp = Blueprint('aba2', __name__)

@aba2_bp.route("/", methods=["GET", "POST"], endpoint='aba2')
def aba2():
    generators = [
      ("range_numbers", "Números aleatórios"),
      ("undrawn_random_numbers", "Números aleatórios não sorteados"),
      ("most_drawn_numbers", "Números mais sorteados"),
      ("least_drawn_numbers", "Números menos sorteados")
    ]

    generate_numbers = []
    sorteios = []
    games = list(QTDE_NUMBERS_MIN_AND_MAX.keys())
    game_selected = request.form.get('jogo') or games[0]
    qtde_numbers = request.form.get('qtde') or str(QTDE_NUMBERS_MIN_AND_MAX[game_selected][0])
    method_ = request.form.get('generator') or 'range_numbers'

    if request.method == 'POST' and game_selected:
        generate_numbers = generate_numbers_(game_selected, int(qtde_numbers), method_)
        sorteios = check_hits(generate_numbers, game_selected)

    return render_template(
        'aba2.html',
        games=games,
        min_max_to_game=QTDE_NUMBERS_MIN_AND_MAX,
        generate_numbers=(', '.join(str(num) for num in generate_numbers)),
        game_selected=game_selected,
        qtde_numbers=qtde_numbers,
        generators=generators,
        generator_selected=method_,
        sorteios=sorteios
    )
