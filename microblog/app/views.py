from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import LoginForm
import json,urllib, sys


@app.route('/login', methods=['GET', 'POST'])
def login():
	error=None
	if request.method =='POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error='zzzzzzzzzzzzzzzzzzz'
		else:
			return redirect(url_for('ws'))
	return render_template("login.html",
							error=error)


def index():
    user = {'nickname': 'Miguel'} 
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",					   
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/')
@app.route('/index')
def ws():	
	#link json
	data = urllib.urlopen("http://128.199.232.32/todo/api/v1.0/tasks").read()
	#manggil json
	resp_dict = json.loads(data)
	#menampilkan json
	print '----------------------------------------------------'
	print (resp_dict)
	print '----------------------------------------------------'
	print ('status :')
	print (resp_dict['tasks.uri'])  #parameter
	print '----------------------------------------------------'
	


	
	print '----------------------------------------------------'	
	return render_template("index.html",					   
                           title='Home',
                           resp_dict=resp_dict)

@app.route('/InputJual')
def InputJual():   
    return render_template("FormInputPenjualan.html",					   
                           title='input Penjualan')
