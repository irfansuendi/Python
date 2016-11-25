from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')    
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
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
@app.route('/Profile')
def Profile():
    user = {'nickname': 'Sandi'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Ricky'}, 
            'body': 'Beautiful day in Fin!' 
        },
        { 
            'author': {'nickname': 'rizz'}, 
            'body': 'so cool!' 
        }
    ]
    return render_template("Profile.html",
                           title='Profile',
                           user=user,
                           posts=posts)

@app.route('/')
@app.route('/Gallery')
def Gallery():
    user = {'nickname': 'Raph'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Don'}, 
            'body': 'Beautiful day in west!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'HOT' 
        }
    ]
    return render_template("Gallery.html",
                           title='Gallery',
                           user=user,
                           posts=posts)
                           


