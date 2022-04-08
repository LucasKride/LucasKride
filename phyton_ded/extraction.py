#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Function responsible for creating tickets """

import re

def is_resolved(subject):
    try:
        check = re.search("Resolvido", subject).group(0)

        if check is not 'NoneType':
            return True
        else:
            return False
    except:
        return False
        
def is_ack(subject):
    try:
        check = re.search("Em tratativa:", subject).group(0)
        
        if check is not 'NoneType':
            return True
        else:
            return False
    except:
        return False
    
def get_eventid(message):
    
    event_id = re.search("ID do problema original: ([0-9]+)", message).groups()[0]
    
    try:
        if len(event_id) > 0:
            return event_id
        
        else: 
            return False

    except:
        return False
