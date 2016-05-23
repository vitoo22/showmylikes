from flask import Flask, render_template, request, redirect, url_for
from get_instagrams_token import *
import urllib.request
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/authorization-completed/', defaults={'code': ''})
@app.route('/authorization-completed/<code>')
def authorization_completed(code):
	code = request.args.get('code')
	access_token = api.exchange_code_for_access_token(code)
	url = 'https://api.instagram.com/v1/users/self/media/liked?access_token=' + access_token[0]
	response = urllib.request.urlopen(url)
	string = response.read().decode('utf-8')
	json_data = json.loads(string)
	return render_template('authorization-completed.html', code=access_token, json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)
