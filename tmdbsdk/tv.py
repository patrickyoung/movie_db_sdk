from . import api_session

TMDB_API_URL = 'https://api.themoviedb.org/3'
ITEMS_PER_PAGE = 20

class TV(object):
  def __init__(self, id):
    self.id = id
  
  def info(self):
    path = '{}/tv/{}'.format(TMDB_API_URL, self.id)
    response = api_session.get(path)
    return response.json()

  @staticmethod
  def popular():
    top_num = (100 // ITEMS_PER_PAGE) + 1
    response = []
    for page in range(1, top_num):
      path = '{}/tv/popular?page={}'.format(TMDB_API_URL, page)
      response += api_session.get(path).json()['results']
    return response