from flaskFlow import FlaskFlow

app = FlaskFlow(__name__)
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    render = app.renderJson("medicos", "index.html", "./data/data.json")
    return render
