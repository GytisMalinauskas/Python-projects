"""Configuration module"""
import os

class Config:
    """Contains secret key which acts as a signature"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'