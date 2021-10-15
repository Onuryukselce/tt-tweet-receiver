import config
import json
import requests
import svc_config

class Seeker(object):
    bearer_token  = ""
    def __init__(self,bearer_token):
        self.bearer_token = bearer_token

    def __init__(self):
        self.bearer_token = config.bearer_token



    def __send_request(self,request):
        return requests.request("GET", request['url'], headers=request['headers'])

    def __create_query(self, user,*args, **kwargs):
        query = dict()
        query['from'] = user
        for key,value in kwargs:
            query[key] = value
        return query

    def __set_fields(self):
        tweet_fields = ['created_at', 'lang', 'conversation_id', 'public_metrics']
        """ if(kwargs):
            if('tweet_fields' in kwargs):
                tweet_fields = kwargs.get('tweet_fields') """
        
        return tweet_fields
        
    def __create_request(self,query, tweet_fields):
        request = dict()
        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}
        query = self.__convert_dict_to_query_string(query)
        tweet_fields = self.__convert_array_to_string(tweet_fields)
        url = svc_config.api_base + "tweets/search/recent?query={}&tweet.fields={}".format(query, tweet_fields)
        request['headers'] = headers
        request['url'] = url
        return request

    def __convert_dict_to_query_string(self,dict):
        str = ""
        for key,value in dict.items():
            str += key+':'+value
            

        return str

    def __convert_array_to_string(self, array):
        str = ""
        for value in array:
            if(value != array[-1]):
                str+=value+','
            else:
                str+=value
        return str


    def __convert_response_to_json(self,response):
        return response.json()

    def __is_response_valid(self,response):
        return response.status_code == 200


    def get_user_tweets(self, user, **kwargs):
            query = self.__create_query(user, kwargs)
            tweet_fields = self.__set_fields()
            request = self.__create_request(query, tweet_fields)
            response = self.__send_request(request)
            if(self.__is_response_valid(response)):
                return self.__convert_response_to_json(response)
            
            return "An error has occured!"
    pass




