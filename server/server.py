#Set-ExecutionPolicy Unrestricted -Scope Process
#.\venv\Scripts\activate
# http://localhost:8080/api/timeline
# pip install .\llama_cpp_python-0.2.24-cp311-cp311-win_amd64.whl
#docker run -p "127.0.0.1:8080:8080" -d server
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import pickle
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
import datetime

load_dotenv()
# load
#with open("my_docs.pkl", "rb") as f:
#    docs = pickle.load(f)
# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/timeline", methods=['GET'])
def return_timeline():
    return jsonify([
    { "id": "item1", "group":1, "displayName": "PCSK9",  "hyperlink": "https://patentimages.storage.googleapis.com/55/df/ca/09af3f5d4ce33d/US8809292.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2014-08-19', "title": "siRNA PCSK9"},
    { "id": "item2", "group":1, "displayName": "SNCA", "hyperlink": "https://patentimages.storage.googleapis.com/28/40/cd/b42ef8e3a84681/WO2023192977A2.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2023-10-05', "title": "siRNA SNCA"},
    { "id": "item3", "group":1, "displayName": "HTT", "hyperlink": "https://patentimages.storage.googleapis.com/25/2f/00/6e133bb7be71e1/WO2023076450A2.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2023-05-04', "title": "siRNA HTT"},
    { "id": "item4", "group":1, "displayName": "TTR", "hyperlink": "https://patentimages.storage.googleapis.com/28/b5/4b/1b0a9a9c0d0295/AU2023248138A1.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2023-10-12', "title": "siRNA TTR"},
    { "id": "item5", "group":1, "displayName": "ANGPTL7", "hyperlink": "https://patentimages.storage.googleapis.com/68/26/0a/c060ee00f0d055/WO2023056478A1.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2022-09-30', "title": "siRNA ANGPTL7"},  
    
    
    { "id": "item6", "group":1, "displayName": "ATXN2", "hyperlink": "https://patentimages.storage.googleapis.com/cc/f3/67/8df6cfe87f1403/WO2022026531A1.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2021-07-28', "title": "siRNA ATXN2"},  
    { "id": "item7", "group":1, "displayName": "SCN9A", "hyperlink": "https://patentimages.storage.googleapis.com/d2/4d/0c/efce7039b09874/WO2021207189A1.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2021-04-06', "title": "The disclosure relates to double-stranded ribonucleic acid (dsRNA) compositions targeting SCN9A, and methods of using such dsRNA compositions to alter (e.g., inhibit) expression of SCN9A"},  
    { "id": "item8", "group":1, "displayName": "MAPT", "hyperlink": "https://patentimages.storage.googleapis.com/cc/f3/67/8df6cfe87f1403/WO2022026531A1.pdf", "editable": "false", "type":'box', "className": "Patent", "start": '2021-03-17', "title": "siRNA MAPT"},  

    { "id": "item9", "group":2, "displayName": 'A status report on RNAi therapeutics', 'hyperlink': "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2908561/", "editable": "false", "type":'box', "className": "Paper", "start": '2010-07-08', "title": "This review attempts to summarize the current understanding on siRNA lead discovery, the delivery of RNAi therapeutics, typical in vivo pharmacological profiles, preclinical safety evaluation and an overview of the 14 programs that have already entered clinical practice."},
    
    { "id": "item10", "group":3, "displayName": 'NCT05231785', "hyperlink" : "https://clinicaltrials.gov/study/NCT05231785", "editable": "false", "type":'range', "className": "ClinicalTrial", "start": '2022-02-04', "end": '2025-07-01', "title": "A Randomized, Double-blind, Placebo-controlled Single Ascending Dose and Open-label Multi-dose Study to Evaluate the Safety, Tolerability, Pharmacokinetics and Pharmacodynamics of Intrathecally Administered ALN-APP in Adult Patients With Early-onset"},
    { "id": "item10", "group":3, "displayName": 'NCT03759379', "hyperlink" : "https://clinicaltrials.gov/study/NCT03759379", "editable": "false", "type":'range', "className": "ClinicalTrial", "start": '2019-02-14', "end": '2020-11-01', "title": "The purpose of this study is to evaluate the efficacy and safety of vutrisiran (ALN-TTRSC02) in participants with hereditary transthyretin amyloidosis (hATTR amyloidosis). Participants will receive vutrisiran subcutaneous (SC) injection once every 3 months (q3M) or the reference comparator patisiran intravenous (IV) injection once every 3 weeks (q3w) during the 18 month Treatment Period. This study will use the placebo arm of the APOLLO study (NCT01960348) as an external comparator for the primary and most other efficacy endpoints during the 18 Month Treatment Period. Following the 18 Month Treatment Period, all participants will be randomized to receive vutrisiran SC injection once every 6 months (q6M) or q3M in the Randomized Treatment Extension (RTE) Period."},
    
    ])

@app.route("/api/question", methods=['POST'])
def answer_question():
    if not request.json or not 'question' in request.json:
        abort(400)
    return jsonify(
    { "question":  request.json['question'], "response": "hello world"},
    
    )

@app.route("/api/timelinetoo", methods=['GET'])
def return_timelinetoo():
    sqliteConnection = sqlite3.connect('external_data.db')
    df = pd.read_sql_query("SELECT * from Documents where Source = 'Alnylam'", sqliteConnection)
    return df.to_json( orient= 'records')

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/api/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run(host = "0.0.0.0",  port=8080)