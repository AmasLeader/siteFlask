from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Accueil')
    
@app.route('/cv')
def cv():
    return render_template('cv.html', title='Curriculum')
    
@app.route('/hobby')
def hobby():
    return render_template('hobby.html', title='Passe-temps')
    
@app.route('/drawing')
def drawing():
    return render_template('drawing.html', title='Galerie')
