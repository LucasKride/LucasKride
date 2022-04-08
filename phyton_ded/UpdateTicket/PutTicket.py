#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Function responsible for deleting a ticket """




from ConfigImport import *
def put_ticket(id_fs, subject):

    api = 'https://kumulus.freshservice.com/api/v2/tickets/'    # URL API

    authen = ("alerta@kumulus.com.br",
              "+++kumuluS+++")     # Authentication in API

    dic_json = {
        "subject": subject,
        "status": 4
    }
    # Calls api to put in ticket
    requests.put(api + str(id_fs), auth=authen, json=dic_json)
