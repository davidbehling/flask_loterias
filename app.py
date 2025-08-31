from flask import Flask
from loteria import get_draws

from views.aba1 import aba1_bp
from views.aba2 import aba2_bp
from views.aba3 import aba3_bp

app = Flask(__name__)
app.register_blueprint(aba1_bp, url_prefix="/")
app.register_blueprint(aba2_bp, url_prefix="/aba2")
app.register_blueprint(aba3_bp, url_prefix="/aba3")

if __name__ == "__main__":
    get_draws()
    app.run(debug=True)
