# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:08:42 2022

@author: romain and sofia
"""

import requests

class IMDbRequests:
    
    _base_url = "https://imdb-api.com/en/API"
    
    @classmethod
    def get_response(cls,apiKey,expression):
        url = cls._base_url+f"/SearchMovie/{apiKey}/{expression}"
        response =  requests.get(url)
        return response
    
    
    def get_info_from_response(response,num_result=0,type_info='id'):
        return response.json()['results'][num_result][type_info]
    
    
    @classmethod
    def get_rating(cls,apiKey,id):
        url = cls._base_url+f"/Ratings/{apiKey}/{id}"
        response =  requests.get(url)
        return response.json()['imDb']