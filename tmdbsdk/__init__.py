import os
import requests

TMDB_API_KEY = os.environ.get('TMDB_API_KEY', None)

api_session = requests.Session()
api_session.params = {}
api_session.params['api_key'] = TMDB_API_KEY

from tmdbsdk import tv