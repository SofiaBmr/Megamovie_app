# -*- coding: utf-8 -*-

from IMDB_requests import IMDbRequests

class MovieFacade:
    
    
    
    def get_rating(apiKey,expression):
        response=IMDbRequests.get_response(apiKey,expression)
        id_movie=IMDbRequests.get_info_from_response(response,num_result=0,type_info='id')
        title=IMDbRequests.get_info_from_response(response,num_result=0,type_info='title')
        rate=IMDbRequests.get_rating(apiKey,id_movie)
        return title,rate
