from flask import Flask
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	    return render_template('hello.html', name=name)
app = Flask(__name__)

#@app.route('/')
@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username
#def hello_world():
# return 'Hello World!'

	@app.route('/post/<int:post_id>')
	def show_post(post_id):
		return 'Post %d' % post_id

if __name__ == '__main__':
	 
	 app.run()

