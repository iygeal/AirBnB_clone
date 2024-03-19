#!/usr/bin/python3
"""Instantiate a FileStorage obj that stores objs"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
