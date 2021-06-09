from flask import Flask, request, render_template

from nltk.corpus.reader.chasen import test
import pandas as pd
from nltk.corpus import stopwords, util

import util.text_process as tp
import util.utils as utils

from core import process_user_input
from core import put_row_into_csv

app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('map.html')

@app.route('/', methods=['POST'])
def my_form_post():
    csv_path = 'static/event_coords_data.csv'
    text = request.form['text']
    print("\t[ Got string from front-end:", text, ']')

    d = process_user_input(text)

    print('\t[ Processed result:', d, ']')

    data_as_csv = put_row_into_csv(csv_path, d)
    print("\t[ Appended the following to " + csv_path + ":" + data_as_csv)

    return str(data_as_csv)
    
if __name__ == '__main__':
    app.debug = True
    app.run()