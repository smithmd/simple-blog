import markdown as Markdown
import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask import g
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_json('blog_configuration.json',True)


@app.before_request
def before_request():
    g.site_name = app.config["SIMPLEBLOG_SITE_NAME"]


@app.route('/')
def index():
    content = 'test'
    return render_template('index.html', **locals())


@app.route('/b/<content_type>/', defaults={'page_number': 0})
@app.route('/b/<content_type>/<int:page_number>')
def entry_list(content_type, page_number):
    content_type = secure_filename(content_type)
    if os.path.exists(os.path.join(app.static_folder, 'md_' + content_type)):
        markdown_files = os.listdir(os.path.join(app.static_folder, 'md_' + content_type))
        file_list = ''
        for md_file in markdown_files:
            file_name = md_file[:-3]
            file_list += '<li><a href="/b/%(content_type)s/%(file_name)s">%(file_name)s</a></li>' % locals()
        file_list = Markup(file_list)
        return render_template('entry_list.html', **locals())
    else:
        return render_template('404.html', **locals())


@app.route('/b/<content_type>/<entry_file>')
def entry(content_type,entry_file):
    content_type = secure_filename(content_type)
    entry_file = secure_filename(entry_file)
    if os.path.exists(os.path.join(app.static_folder, 'md_' + content_type + '/' + entry_file + '.md')):
        md_file = os.path.join(app.static_folder, 'md_' + content_type + '/' + entry_file + '.md')
        with open(md_file, 'r') as f:
                md = f.read()
        entry_content = Markup(Markdown.markdown(md))
        return render_template('entry.html', **locals())
    else:
        return render_template('404.html', **locals())


if __name__ == '__main__':
    app.run()
