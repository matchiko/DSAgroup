from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/ListPage.html')
def ListPage():
    return render_template('ListPage.html')


@app.route('/templates/Memberpage.html')
def Memberpage():
    return render_template('Memberpage.html')

@app.route('/templates/ResultsPage.html')
def ResultsPage():
    return render_template('ResultsPage.html')


if __name__ == '__main__':
    app.run(debug=True)