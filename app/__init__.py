"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa79rhp8u791gsin50-a",
        database="todo_e363",
        user="root",
        password="cQpIPGvv49cFqknRRjcRlJsxy1hk21uh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
