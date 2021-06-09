# save this as app.py
from flask import Flask, escape, request, render_template, url_for
import os

app = Flask(__name__)

@app.route('/traffic')
def taffic():
    name = request.args.get("name", "World")
    return render_template('map.html')

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
 	app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))