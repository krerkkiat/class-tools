# A simple server that parse the CS2401's Project 4 output file.
import os
import re

from flask import Flask, Request, request, redirect, url_for
from werkzeug import secure_filename

from mkhtml import parse_swatches

ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
# file size is limitted at 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_result(file):
    filename = secure_filename(file.filename)
    html = ''

    # Set up all variables and template.
    title = 'Swatches from ' + file.filename
    style = 'div{margin:auto;} table{padding-bottom:60px;}'
    header = '<html><head><title>' + title + \
        '</title><style type="text/css">' + style + \
        '</style></head><body><a href="' + url_for('upload_file') + '">back</a>'
    swatch_template = '<td><div style="background-color:#{color};width:{width}px;height:{height}px;"></div></td>'
    footer = '</body></html>'
    
    html = html + header

    try:
        raw_data = file.stream.read()
        data = raw_data.decode('ascii')
    except Exception:
        redirect(url_for('show_error', tetx='Error is encountered while decoding the content of the file. Please use ASCII file instead.'))
    
    body = parse_swatches(data.split('\n'))

    html = html + body + footer

    return html

@app.route('/disclaimer')
def show_disclaimer():
    return '''
    <!doctype html>
    <title>Make HTML (CS2401 - Project 4)</title>
    <h2>Make HTML (CS2401 - Project 4)</h2>
    <div>DISCLAIMER: I, KRERKKIAT CHUSAP, AM NOT RESPONSEIBLE FOR ANY PROBLEM OR DAMAGE THAT RESULT FROM USING THIS WEB APPLICATION.</div>
    <a href="''' + url_for('upload_file') + '''">back</a>
    '''

@app.route('/error')   
def show_error(text):
    return '''
    <!doctype html>
    <title>Make HTML (CS2401 - Project 4)</title>
    <h3 style="color: red;">{text}</h3>
    '''.format(text=text)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    #try:
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            return get_result(file)
    #except Exception:
    #    redirect(url_for('show_error', text='Unknown error.'))

    return '''
    <!doctype html>
    <title>Make HTML (CS2401 - Project 4)</title>
    <h2>Make HTML (CS2401 - Project 4)</h2>
    <h3>Upload new File</h3>
    <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file>
            <input type=submit value=Upload>
    </form>
    <br/><a href="''' + url_for('show_disclaimer') + '''">disclaimer</a>
    '''

if __name__ == '__main__':
    app.debug = False
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)