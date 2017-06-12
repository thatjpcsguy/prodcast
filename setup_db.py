#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import json

conn = sqlite3.connect('prodcast.db')
db = conn.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS emails (
    email text primary key, 
    time_added text,
    ip text,
    browser text
)''')

