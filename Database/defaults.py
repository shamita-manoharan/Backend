"""
Description : Query to add default values 
"""

from Database.schema import BankSchema
from Database import Session
import csv
import traceback

session = Session()

def add_default():
    try:
        if(not session.query(BankSchema).first()):
            defaults = []
            c = 0
            with open("C:/Users/Ridhanya/Documents/Shamita/bank_branches.csv", mode ='r', encoding="utf8")as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    if c > 0:
                        # print(lines)
                        defaults.append(BankSchema(ifsc       = lines[0],\
                                                    bank_id  = lines[1],\
                                                    branch = lines[2],\
                                                    address    = lines[3],\
                                                    city    = lines[4],\
                                                    district= lines[5],\
                                                    state        = lines[6],\
                                                    bank_name        = lines[7]  ))
                    c=c+1
            session.bulk_save_objects(defaults)
            session.commit()
        
    except:
        print(traceback.print_exc())
        session.rollback()        