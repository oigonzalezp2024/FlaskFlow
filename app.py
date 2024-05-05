from flaskFlow import FlaskFlow

app = FlaskFlow(__name__)
@app.route('/')
def hello():
    render = app.renderJson('Collaborators', 'index.html', './data/data.json')
    return render
