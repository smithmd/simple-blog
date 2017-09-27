import markdown
import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask import g

app = Flask(__name__)
app.config.from_json('blog_configuration.json',True)


@app.before_request
def before_request():
    g.site_name = app.config["SIMPLEBLOG_SITE_NAME"]


@app.route('/')
def index():
    content = 'test'
    return render_template('index.html', **locals())


@app.route('/<content_type>/', defaults={'page_number': 0})
@app.route('/<content_type>/<int:page_number>')
def entry_list(content_type, page_number):
    # TODO: fix crash if folder not found. Handle gracefully
    markdown_files = os.listdir(os.path.join(app.static_folder, 'md_' + content_type))
    file_list = ''
    for md_file in markdown_files:
        file_list += '<li>' + md_file + '</li>'
    file_list = Markup(file_list)

    return render_template('entry_list.html', **locals())


@app.route('/<content_type>/<entry_file>')
def entry(content_type,entry_file):
    return render_template('entry.html', **locals())


if __name__ == '__main__':
    app.run()
