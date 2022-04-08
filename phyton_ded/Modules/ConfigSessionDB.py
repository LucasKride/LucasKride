#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
Database and import settings for health

created by: Breno Barbieri
"""

"""Layer with sqlalchemy utilities"""

from sqlalchemy import create_engine , Table, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from contextlib import contextmanager
from datetime import datetime
from pytz import timezone
#import urllib

# Configuration variable for accessing the database (SQL Server).
#params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
#                                 "SERVER=sql-kum-automation.database.windows.net;"
#                                 "DATABASE=db-zabbix-automation;"
#                                 "UID=admin_kuml;"
#                                 "PWD=Kumulus@2019xdf")

# Variable responsible for the connection where the variable "params" is used, which is the entire connection configuration of the bank.
engine = create_engine("mysql+pymysql://integrzabb:kdvdjpq7Mh@52.255.177.250:3306/API_Zabbix")

# base statement
Base = declarative_base()


@contextmanager
# Bank connection function and recording error handling
def session_scope(): 
    # Session Configuration and Creation
    Session = sessionmaker(bind=engine) 
    session = Session()
    
    # Error handling
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise  # Exception Main Program Protection (leave it here!)
    finally:
        session.close()

# class mentions table to be modified in applications
class ZabbixCtrl(Base):
    __table__ = Table(
        'automation_zabbix',
        MetaData(),
        autoload=True,
        autoload_with=engine
    )
