"""
Description:

This file is for defining the Schema for all the required tables
Required Tables - Processor, Queues, DocumentType, Fields
Mapped Tables   - MapQueuesProcessor, MapQueuesDocument
"""

from sqlalchemy import Column, Integer, String, Sequence, ARRAY, DateTime, func, Boolean, UniqueConstraint
from Database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Schema for Processor Table
class BankSchema(Base):

    __tablename__ = 'bank'
    
    id_seq = Sequence('id_seq', metadata=Base.metadata)
    id = Column(Integer,id_seq, server_default=id_seq.next_value(), primary_key=True)
    ifsc = Column(String, nullable= False)
    bank_id = Column(Integer, nullable= False)#, unique=True)
    branch = Column(String, nullable= False)
    address = Column(String, nullable= False)
    city = Column(String, nullable= False)
    district = Column(String, nullable=False)
    state =Column(String, nullable= False)
    bank_name = Column(String, nullable= False)

    def __init__(self, ifsc, bank_id, branch, address, city, district, state, bank_name):
        self.ifsc = ifsc
        self.bank_id = bank_id
        self.branch = branch
        self.address = address
        self.city = city
        self.district = district
        self.state = state
        self.bank_name = bank_name
