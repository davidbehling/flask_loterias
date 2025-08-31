from flask import Blueprint, render_template, request
from generate import get_drawn_numbers, QTDE_NUMBERS_MIN_AND_MAX

aba1_bp = Blueprint('aba1', __name__)

@aba1_bp.route("/", methods=["GET", "POST"], endpoint='aba1')
def aba1():
    games = list(QTDE_NUMBERS_MIN_AND_MAX.keys())
    game_selected = request.form.get('jogo') or games[0]
    drawn_numbers = get_drawn_numbers(game_selected)

    return render_template(
       'aba1.html',
       games=games,
       game_selected=game_selected,
       drawn_numbers=drawn_numbers
    )
