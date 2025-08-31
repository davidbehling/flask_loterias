from flask import Blueprint, render_template, request
from generate import check_hits, NUMBERS_LIMITED, QTDE_NUMBERS_MIN_AND_MAX

aba3_bp = Blueprint('aba3', __name__)

@aba3_bp.route("/", methods=["GET", "POST"], endpoint='aba3')
def aba3():
    games = list(QTDE_NUMBERS_MIN_AND_MAX.keys())
    game_selected = request.form.get('jogo') or games[0]
    selected_numbers = request.form.getlist('selected_numbers[]')
    int_numbers = [int(x) for x in selected_numbers]
    sorteios = check_hits(int_numbers, game_selected)

    if request.method == 'POST' and game_selected:
        int_numbers = [int(x) for x in selected_numbers]
        sorteios = check_hits(int_numbers, game_selected)


    return render_template(
        'aba3.html',
        active_tab='aba3',
        numbers_limited=NUMBERS_LIMITED,
        min_max_to_game=QTDE_NUMBERS_MIN_AND_MAX[game_selected],
        game_selected=game_selected,
        sorteios=sorteios
    )
