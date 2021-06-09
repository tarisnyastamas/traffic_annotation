from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('map.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    return str(processed_text)
    
if __name__ == '__main__':
    app.debug = True
    app.run()