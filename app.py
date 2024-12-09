from flask import Flask
from flask import jsonify
from flask_cors import CORS

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# add an api endpoint to flask app
@app.route('/api/hannah')
def get_hannah_data():
    InfoDb = []
    InfoDb.append({
        "FirstName": "Ben",
        "LastName": "Dovers",
        "Username": "Dendover$"
    })
    return jsonify(InfoDb)

@app.route('/api/carson')
def get_carson_data():
    InfoDb = []
    InfoDb.append({
        "FirstName": "Pubert",
        "LastName": "McLice",
        "Username": "Puberslice$"
    })
    return jsonify(InfoDb)

@app.route('/api/rhea')
def get_rhea_data():
    InfoDb = []
    InfoDb.append({
        "FirstName": "bob",
        "LastName": "gross",
        "Username": "bgross$"
    })
    InfoDb.append({
        "FirstName": "As.",
        "LastName": "Scrum",
        "DOB": "February 30",
    })
    return jsonify(InfoDb)

@app.route('/api/rowan')
def get_rowan_data():
    InfoDb = []
    InfoDb.append({
        "FirstName": "Gabe",
        "LastName": "Itch",
        "Username": "GabeI55"
    })
    InfoDb.append({
        "FirstName": "Best",
        "LastName": "Friend",
        "DOB": "February 24",
    })
    return jsonify(InfoDb)

# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h2>Hello, World!</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(port=5001)
