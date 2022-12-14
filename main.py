# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from modules.facade import MovieFacade
import os

load_dotenv('environnement/key.env')
apiKey=os.environ.get('APIKEY')
expression=input('Which movie are you interested in? ')
title , rate =MovieFacade.get_rating(apiKey, expression)
print(f'{title} got a review of  {rate}/10')
