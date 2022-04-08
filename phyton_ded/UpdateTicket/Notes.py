#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: André Marsaioli """

""" Function responsible for update a ticket to ack """

from ConfigImport import *
def notes_ticket(id_fs, message):

    api = 'https://kumulus.freshservice.com/api/v2/tickets/'+str(id_fs)+'/notes'

    authen = ("andre.marsaioli@kumulus.com.br",
              "D7252ded")     # Authentication in API

    headers={'Content-type':'application/json'}

    dic_json = {
        "body": message
    }
        
    # Calls api to put in ticket
    r = requests.post(api, auth=authen, json=dic_json, headers=headers)