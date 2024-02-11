#!/usr/bin/python3

"""
initialize package
to create a unique fileStorage instance
for the application
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

