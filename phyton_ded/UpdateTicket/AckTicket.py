#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: André Marsaioli """

""" Function responsible for update a ticket to ack """

from ConfigImport import *
def ack_ticket(id_fs, subject):

    api = 'https://kumulus.freshservice.com/api/v2/tickets/'    # URL API

    authen = ("andre.marsaioli@kumulus.com.br",
              "D7252ded")     # Authentication in API

    dic_json = {
        "status": 7,
        "subject": subject
    }
      
    # Calls api to put in ticket
    requests.put(api +str(id_fs), auth=authen, json=dic_json)
    	