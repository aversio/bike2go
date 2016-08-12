import os
import yaml

from flask import render_template
from flask import Flask
app = Flask(__name__)

if not os.path.isfile('data/config.yaml'):
    import base64
    with open('data/config.yaml', 'w+') as f:
        yaml.dump({'SECRET_KEY': base64.b64encode(os.urandom(30))}, f)

with open('data/config.yaml', 'r') as f:
    app.config.update(yaml.load(f))


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/u-pas')
def u_pas():
    return render_template('upas.html')
	
@app.route('/reparatie')
def reparatie():
    return render_template('reparatie.html')
	
@app.route('/contact')
def contact():
    return render_template('contact.html')
