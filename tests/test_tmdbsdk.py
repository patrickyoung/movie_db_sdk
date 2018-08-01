# tests/test_tmdbsdk.py

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import vcr
from pytest import fixture
from tmdbsdk.tv import TV

@fixture
def tv_keys():
  return ['id', 'origin_country', 'poster_path', 'name', 
          'overview', 'popularity', 'backdrop_path', 
          'first_air_date', 'vote_count', 'vote_average']

@vcr.use_cassette('tests/vcr_cassettes/tv-info.yaml', filter_query_parameters=['api_key'])
def test_tv_info(tv_keys):
  """Tests an API call to get TV show info"""

  tv_instance = TV(1396)
  response = tv_instance.info()

  assert isinstance(response, dict)
  assert response['id'] == 1396, "The ID should be in the response"
  assert set(tv_keys).issubset(response.keys()), "All keys should be in response"

@vcr.use_cassette('tests/vcr_cassettes/tv-popular.yaml', filter_query_parameters=['api_key'])
def test_tv_popular(tv_keys):
  response = TV.popular()

  assert isinstance(response, list)
  assert isinstance(response[0], dict)
  assert set(tv_keys).issubset(response[0].keys())
  assert len(response) == 100