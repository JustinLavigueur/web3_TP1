"""
Exercice de sécurité
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Sécurise l'accès à des données secrètes"""

    return render_template('index.jinja')
