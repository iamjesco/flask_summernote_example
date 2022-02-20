from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models.forms import PostForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdser456345efgsdgse5srgs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

from models.db import Post


@app.route('/')
def home():
	return redirect(url_for('feed'))


@app.route('/feed/')
def feed():
	all_posts = Post.query.all()
	return render_template('feed.html', all_posts=all_posts)


@app.route('/feed/post/<int:pk>/')
def post(pk):
	post_detail = Post.query.get_or_404(pk)
	return render_template('post.html', post_detail=post_detail)


@app.route('/add/', methods=['GET', 'POST'])
def add():
	form = PostForm()
	if form.validate_on_submit():
		title = request.form.get('title')
		body = request.form.get('body')
		form_data = Post(title=title, body=body)
		db.session.add(form_data)
		db.session.commit()
		flash('Post created successfully', 'success')
		return redirect(url_for('add'))
	return render_template('blog-form.html', form=form)


@app.route('/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
	post = Post.query.get_or_404(pk)
	form = PostForm()
	if form.validate_on_submit():
		post.title = request.form.get('title')
		post.body = request.form.get('body')
		db.session.commit()
		flash('Post updated successfully', 'success')
		return redirect(url_for('post', pk=post.pk))
	elif request.method == 'GET':
		form.title.data = post.title
	return render_template('blog-form.html', form=form)


@app.route('/delete/<int:pk>/', methods=['GET', 'POST'])
def delete(pk):
	post = Post.query.get_or_404(pk)
	db.session.delete(post)
	db.session.commit()
	flash('Post deleted successfully', 'success')
	return redirect(url_for('feed'))
	

if __name__ == '__main__':
	app.run()
