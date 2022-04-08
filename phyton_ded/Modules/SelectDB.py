#!/usr/bin/python
# -*- coding: utf-8 -*-

""" created by: Breno Barbieri """

""" Function that makes the select in the database """

from Modules.ConfigSessionDB import *

def select(zabbix_id):  # Function responsible for searching the database

        with session_scope() as session:    # Session initialization
            existent_control = session.query(   # Variable receiving search settings
                ZabbixCtrl
            ).filter(
                ZabbixCtrl.zabbix_id == zabbix_id
            ).first()

            if not existent_control:
                return None

            else:
                iddb_zabbix = existent_control.zabbix_id
                iddb_freshservice = existent_control.freshService_id
                return iddb_zabbix, iddb_freshservice


