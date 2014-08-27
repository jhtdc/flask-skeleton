from flask import render_template, request, redirect, flash

def install(app):
  app.config.apps.register('login', 'Login', '/login')

  @app.route('/login', methods=['GET', 'POST'])
  def login():
    return render_template('login.html')
