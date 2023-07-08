#!/usr/bin/python3
"""filestore class call and storage instance definition"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
