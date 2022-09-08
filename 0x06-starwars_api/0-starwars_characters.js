#!/usr/bin/env python3
"""A script that prints all characters of a star war movie"""
import requests


api_url = "https://swapi-api.hbtn.io/api/"
response = requests.get(api_url)
response.json()
