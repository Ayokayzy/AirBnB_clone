#!/usr/bin/python3
"""
models/__init__.py
"""
from models.engine.file_storage import FileStorage
from models.engine.file_storage import all_class


storage = FileStorage()
storage.reload()
