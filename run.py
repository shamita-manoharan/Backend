"""
Description : Definition of APIs, Creation of Tables.
"""

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from Database import engine
from Database.schema import BankSchema

from Database import defaults

from Application import SEARCH
from Application import BRANCH

###################################################################################

BankSchema.metadata.create_all(engine)

# Loading default data to the tables
defaults.add_default()

###################################################################################

app = Flask(__name__)
api = Api(app)
CORS(app)


#search end point
@app.route('/')
def index():
    return '<h1>Hello...</h1>'
api.add_resource(SEARCH, '/api/search', endpoint='search')
api.add_resource(BRANCH, '/api/branch', endpoint='branch')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    #app.run()