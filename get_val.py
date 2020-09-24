import os
from flask import Flask, render_template, request,Response,redirect,url_for
import pass_gen
import enc_dec
import random

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("index.html",x="")

response=Response()
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route("/", methods=["GET", "POST"])
def login():
	paramList=[]
	encode=""
	decode=""
	enkey=iv = ''.join([chr(random.randint(33, 125)) for i in range(16)])
	iv = ''.join([chr(random.randint(33, 125)) for i in range(16)])
	if request.method == "POST":
		plength = request.form["plength"]
		if(request.form.get('num_param')):
			paramList.append(request.form.get('num_param'))
		else:
			paramList.append(request.form.get('num_false_param'))
		if(request.form.get('char_param')):
			paramList.append(request.form.get('char_param'))
		else:
			paramList.append(request.form.get('char_false_param'))
		if(request.form.get('up_param')):
			paramList.append(request.form.get('up_param'))
		else:
			paramList.append(request.form.get('up_false_param'))
		if(request.form.get('lw_param')):
			paramList.append(request.form.get('lw_param'))
		else:
			paramList.append(request.form.get('lw_false_param'))
	passwordx=pass_gen.generate(int(plength),paramList)
	encode=enc_dec.encoder(passwordx,enkey,iv)
	return render_template('index.html',x=passwordx,y=encode,z=enkey,a=iv)


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

