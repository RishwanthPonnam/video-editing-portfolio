# app/__init__.py

from flask import Flask
from .factory import create_app

app = create_app()

from app import routes  # Ensure this imports the routes module where 'clients' is defined
