from flask import render_template, request, redirect, flash

def install(app):
  app.config.apps.register('parameters', 'Parameters', '/parameters')

  @app.route('/parameters', methods=['GET', 'POST'])
  def parameters():
    return render_template('parameters.html')
