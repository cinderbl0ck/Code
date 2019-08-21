from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for, make_response)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import xlsxwriter
import io

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
	db = get_db()
	posts = db.execute(
		'SELECT p.id, title, body, created, author_id, username'
		' FROM post p JOIN user u ON p.author_id = u.id'
		' ORDER BY created DESC'
	).fetchall()
	return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
	if request.method == 'POST':
		title = request.form['title']
		body = request.form['body']
		error = None

		if not title:
			error = 'Title is required.'

		if error is not None:
			flash(error)

		else:
			db = get_db()
			db.execute(
				'INSERT INTO post (title, body, author_id)'
				' VALUES (?, ?, ?)',
				(title, body, g.user['id'])
			)
			db.commit()
			return redirect(url_for('blog.index'))

	return render_template('blog/create.html')

def get_post(id, check_author=True):
	post = get_db().execute(
		'SELECT p.id, title, body, created, author_id, username'
		' FROM post p JOIN user u ON p.author_id = u.id'
		' WHERE p.id = ?',
		(id,)
	).fetchone()

	if post is None:
		abort(404, "Post id {0} doesn't exist.".format(id))

	if check_author and post['author_id'] != g.user['id']:
		abort(403)

	return post

@bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
	post = get_post(id)

	if request.method == 'POST':
		title = request.form['title']
		body = request.form['body']
		error = None

		if not title:
			error = 'Title is required.'

		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				'UPDATE post SET title = ?, body = ?'
				' WHERE id = ?',
				(title, body, id)
			)
			db.commit()
			return redirect(url_for('blog.index'))

	return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
	get_post(id)
	db = get_db()
	db.execute('DELETE FROM post WHERE id = ?', (id,))
	db.commit()
	return redirect(url_for('blog.index'))

@bp.route('/export', methods=['GET'])
@login_required
def export():
	return render_template('blog/export.html')

@bp.route('/get_files/', methods=['GET', 'POST'])
@login_required
def get_files():
	conn = get_db()
	c = conn.execute(
		'SELECT p.id, title, body, created, author_id, username'
		' FROM post p JOIN user u ON p.author_id = u.id'
		' ORDER BY created DESC'
	)

	output = io.BytesIO()
	workbook = xlsxwriter.Workbook('Posts.xlsx', {'in_memory': True})
	worksheet = workbook.add_worksheet()

	row = 0
	col = 0

	c.execute("SELECT * FROM post")
	for item in c.fetchall():
		worksheet.write(row, col,   item[0])
		worksheet.write(row, col+1, item[1])
		worksheet.write(row, col+2, item[2])
		worksheet.write(row, col+3, item[3])
		worksheet.write(row, col+4, item[4])
		row += 1

	workbook.close()
	output.seek(0)

	response = make_response(bytes(output))
	response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	response.headers['Content-Disposition'] = 'attachment; filename="Posts.xlsx"'

	conn.commit()
	conn.close()

	return response

