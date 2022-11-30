# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:35:05 2022

@author: romain and sofia
"""
from dotenv import load_dotenv
from facade import MovieFacade
import os

load_dotenv('key.env')
apiKey=os.environ.get('APIKEY')
expression=input('Film you want the rate: ')
title , rate =MovieFacade.get_rating(apiKey, expression)
print(f'{title} obtain {rate}/10')