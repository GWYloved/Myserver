from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
	return 'username = %s' % request.form['username']

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True) 
