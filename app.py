from flask import Flask, request, render_template

from nltk.corpus.reader.chasen import test
import pandas as pd
from nltk.corpus import stopwords, util

import util.text_process as tp
import util.utils as utils

from core import process_user_input

app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('map.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    print("\t[ Got string from front-end:", text, ']')

    d = process_user_input(text)

    print('\t[ Processing result:', d, ']')

    return str(d)
    
if __name__ == '__main__':
    app.debug = True
    app.run()