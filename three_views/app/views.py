# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/first_view')
@app.route('/')
def first_view():
	return render_template('first_view.html')

@app.route('/two')
def two():
	return render_template('second_view.html')


@app.route('/three')
def three():
	return render_template('third_view.html')


