import markdown
import os
from flask import Flask
from flask import Markup
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    content = 'test'
    return render_template('index.html', **locals())


@app.route('/games/', defaults={'page_number': 0})
@app.route('/games/<int:page_number>')
def games(page_number):
    markdown_files = os.listdir(os.path.join(app.static_folder, 'games_md'))
    file_list = ''
    for md_file in markdown_files:
        file_list += '<li>' + md_file + '</li>'
    file_list = Markup(file_list)
    return render_template('entry_list.html', **locals())


@app.route('/games/<game>')
def game(game):
    return render_template('game.html', **locals())


if __name__ == '__main__':
    app.run()
