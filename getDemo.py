from flask import *
app = Flask(__name__, template_folder='templates',static_folder="",static_url_path="")

@app.route('/')
def index():
    return 'hello world nono`!!!!!`'

@app.route('/')
def hello():
    return 'hello motherfxker'

@app.route('/login')
def login():
    return 'login success'

@app.route('/abort401')
def abort401():
    abort(401)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    if request.method == 'POST':
	return 'method = post, post %d'%post_id
    else:
        return 'method = get, post %d'%post_id

@app.route('/get/<username>')
def show_usr_name(username):
    return 'Usr name is %s' % username

@app.route('/getfile')
def send_file(name=None):
    return render_template('1.html', name=name)

if __name__ == '__main__':
   app.run(host = '0.0.0.0',port = '8000',debug = True)
