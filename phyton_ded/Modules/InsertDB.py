#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Function to insert data in the table """

from Modules.ConfigSessionDB import *

def insert(id_zb, id_fs):   # Function responsible for entering data into the bank
        
        id_zabbix = id_zb
        id_freshservice = id_fs

        newDate = datetime.now()
        local_tz = timezone('America/Sao_Paulo')
        format_date = newDate.replace(tzinfo=local_tz)

        with session_scope() as session:    # Session initialization

            insert_dados = ZabbixCtrl(  # Defining table and its values
                zabbix_id = id_zabbix,
                freshService_id = id_freshservice,
                created_at = format_date
            )

            session.add(insert_dados)   # Adding table and its values (insertData) in the session to be saved in the bank
            session.flush() # Forcing the load for information