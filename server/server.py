#Set-ExecutionPolicy Unrestricted -Scope Process
#venv/bin/activate
# http://localhost:8080/api/home
from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/timeline", methods=['GET'])
def return_home():
    return jsonify([
    { "id": "item1", "group":1, "content": "PCSK9", "hyperlink": "https://patentimages.storage.googleapis.com/55/df/ca/09af3f5d4ce33d/US8809292.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2014-08-19', "title": "siRNA PCSK9"},
    { "id": "item2", "group":1, "content": "SNCA", "hyperlink": "https://patentimages.storage.googleapis.com/28/40/cd/b42ef8e3a84681/WO2023192977A2.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2023-10-05', "title": "siRNA SNCA"},
    { "id": "item3", "group":1, "content": "HTT", "hyperlink": "https://patentimages.storage.googleapis.com/25/2f/00/6e133bb7be71e1/WO2023076450A2.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2023-05-04', "title": "siRNA HTT"},
    { "id": "item4", "group":1, "content": "TTR", "hyperlink": "https://patentimages.storage.googleapis.com/28/b5/4b/1b0a9a9c0d0295/AU2023248138A1.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2023-10-12', "title": "siRNA TTR"},
    { "id": "item5", "group":2, "content": 'Study 1', "editable": "false", "type":'range', "className": "External", "start": '2022-06-16', "end": '2022-06-29', "title": "hello alynylam"},
       
    ])


if __name__ == "__main__":
    app.run(debug=True, port=8080)