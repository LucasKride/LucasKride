#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Function responsible for created time_entry of ticket """

from ConfigImport import *
def post_time_entry(id_fs):
       
    #api = 'https://kumulus.freshservice.com/api/v2/tickets/' + \
    #    id_fs+' /time_entries'    # URL API
        
    api = ('https://kumulus.freshservice.com/api/v2/tickets/'+str(id_fs)+'/time_entries')    # URL API
        
    authen = ("alerta@kumulus.com.br",
              "+++kumuluS+++")     # Authentication in API

    dic_json = {
        "time_entry": {
            "agent_id": 10001408821,
            "time_spent": "00:01"
        }
    }
        
    # Calls api to post entry
    requests.post(api, auth=authen, json=dic_json)
