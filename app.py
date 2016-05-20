from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/authorization-completed/', defaults={'code': ''})
@app.route('/authorization-completed/<code>')
def authorization_completed(code):
	code = request.args.get('code')
	return render_template('authorization-completed.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)
