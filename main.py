
from flask import Flask, render_template, request

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/learning-paths')
def learning_paths():
    return render_template('learning-paths.html')

@app.route('/literature')
def literature():
    return render_template('literature.html')

if __name__ == '__main__':
    app.run(debug=True)
