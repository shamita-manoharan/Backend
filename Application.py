from flask_restful import Resource
from flask import request, make_response, jsonify
import traceback
import os

from sqlalchemy import asc, desc
from Database.schema import BankSchema
from Database import Session
session = Session()
import os, requests, json


class SEARCH(Resource):
    def __init__(self, **kwargs):
        pass    
    
    def get(self, *args, **kwargs):
        try:
            q = request.args.get('q')
            q = q.upper()
            limit = request.args.get('limit')       
            offset = request.args.get('offset') 
            # print(q,type(q), limit, offset)

            cond = BankSchema.city == q
            query = session.query(BankSchema).filter(cond).order_by(asc(BankSchema.ifsc))   # order by ascending

            if limit:
                query = query.limit(limit)
            if offset: 
                query = query.offset(offset)
            results = query.all()

            if results:
                output = []
                for result in results:
                    row_as_dict = result.__dict__
                    row_as_dict = {k:v for k,v in row_as_dict.items() if k not in ['id','_sa_instance_state']}
                    output.append(row_as_dict)
                
                response = {"city":output}
                return make_response(jsonify(response), 200)

            else:
                return make_response(jsonify({'message':'No Record Available'}), 200)
                
        except:
            print(traceback.print_exc())
            return make_response(jsonify({'message': 'Bad Request'}), 400)  
        
class BRANCH(Resource):
    def __init__(self, **kwargs):
        pass    
    
    def get(self, *args, **kwargs):
        try:
            q = request.args.get('q')
            q = q.upper()
            limit = request.args.get('limit')       
            offset = request.args.get('offset') 
            # print(q,type(q), limit, offset)

            cond = BankSchema.branch == q
            query = session.query(BankSchema).filter(cond).order_by(desc(BankSchema.ifsc))  # Order by descending

            if limit:
                query = query.limit(limit)
            if offset: 
                query = query.offset(offset)
            results = query.all()

            if results:
                output = []
                for result in results:
                    row_as_dict = result.__dict__
                    row_as_dict = {k:v for k,v in row_as_dict.items() if k not in ['id','_sa_instance_state']}
                    output.append(row_as_dict)
                
                response = {"branches":output}
                return make_response(jsonify(response), 200)

            else:
                return make_response(jsonify({'message':'No Record Available'}), 200)
                
        except:
            print(traceback.print_exc())
            return make_response(jsonify({'message': 'Bad Request'}), 400)  
       