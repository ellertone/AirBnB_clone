#!/usr/bin/env python3
"""Magic method for initializing storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()