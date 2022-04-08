#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Business rules """
import sys
from CriaTicket.CreateTicket import *
from UpdateTicket.PutTicket import *
from Modules.InsertDB import *
from Modules.SelectDB import *
from extraction import *
from UpdateTicket.PostEntry import *
from UpdateTicket.AckTicket import *
from UpdateTicket.Notes import *

def controller(sendto, subject, message, host):

    resolve = is_resolved(subject)  # returns True if it is a resolved ticket
    ack = is_ack(subject)

    if resolve:
        
        problem_id = get_eventid(message)        
        
        # Searching and saving return from the select function
        search = select(problem_id)
        
        freshService_id = search[1]     # Search for the fresh service id

        # Responsible for creating time_entry
        post_time_entry(freshService_id)

        # Responsible for changing the ticket status to resolved
        put_ticket(freshService_id, subject)
    
    elif ack:
                
        problem_id = get_eventid(message)  # returns the problem ID
        
        search = select(problem_id)
        
        freshService_id = search[1]

        notes_ticket(freshService_id, message)
        
        ack_ticket(freshService_id,subject)
                
    else:
        
        #ESCOLHE EMPRESA
        EMPRESA = [ {'empresa': 'ABCR', 'nr': '10000198185'},
                    {'empresa': 'Apter', 'nr': '10000213194'},
                    {'empresa': 'AWS_TOTALEXPRESS_NVIRGINIA', 'nr': '10000230273'},
                    {'empresa': 'AWS_TOTALEXPRESS_SAOPAULO', 'nr': '10000230273'},
                    {'empresa': 'Cataguases', 'nr': '10000198186'},
                    {'empresa': 'Datora', 'nr': '10000182891'},
                    {'empresa': 'Esferatur', 'nr': '10000198179'},
                    {'empresa': 'Fibra', 'nr': '10000230269'},
                    {'empresa': 'Gera', 'nr': '10000225865'},
                    {'empresa': 'Kumulus', 'nr': '10000227886'},
                    {'empresa': 'LIBBS', 'nr': '10000237261'},
                    {'empresa': 'SalesLogics', 'nr': '10000237841'},
                    {'empresa': 'LINX', 'nr': '10000226717'},
                    {'empresa': 'SKF', 'nr': '10000198187'},
                    {'empresa': 'SLM', 'nr': '10000198176'},
                    {'empresa': 'Tecfy', 'nr': '10000228480'},
                    {'empresa': 'Quinel', 'nr': '10000210944'},
                    {'empresa': 'Knewin', 'nr': '10000210473'},
                    {'empresa': 'TotalExpress', 'nr': '10000230273'}]
                    
        for elm in EMPRESA:

            if host == (elm['empresa']):
                host = elm['nr']
                print(host)
        

        # Create the ticket and save the IDs in the variable
        save_id = create_ticket(sendto, subject, message, host)
        
        # Insert the saved IDs into the variable "save_id" in the bank
        insert(id_zb=save_id[0], id_fs=save_id[1])