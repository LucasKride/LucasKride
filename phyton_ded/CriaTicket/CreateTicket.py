#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Function responsible for creating tickets """



import sys
from ConfigImport import *
def create_ticket(sendto, subject, message, host):

    # URL API
    api = 'https://kumulus.freshservice.com/api/v2/tickets/'

    # Authentication in API
    authen = ("andre.marsaioli@kumulus.com.br", "D7252ded")

    empresa = int(host)
    
    dic_ticket = {
        "department_id": empresa,
        "group_id": 10000376538, 
        "responder_id": 10001408821,
        "type": "Incident",
        "subject": subject,
        "description": message,
        "email": "suporte@kumulus.com.br",
        "priority": 1,
        "status": 2,
        "category": "Alerta",
        "sub_category": "UP/DOWN",
        "cc_emails": [sendto]
    }

    upload = requests.post(api, auth=authen, json=dic_ticket)  # POST ticket

    # Transforming json to dictionary for manipulation
    data_fs = upload.json()
    data_zb = message

    # GET and Save ID
    id_fs = repr(data_fs["ticket"]["id"])  # FreshService
    id_zb = re.search("Id do Alerta: ([0-9]+)", data_zb).groups()[0]  # Zabbix

    save_id = [id_zb, id_fs]

    return save_id