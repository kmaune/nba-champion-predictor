import requests
from bs4 import BeautifulSoup
from csv import writer
from itertools import zip_longest
from parsers import *

seasons = ['2018-2019', '2017-2018', '2016-2017']

for season in seasons: 
	get_per_game_stats(season)
	get_advanced_stats(season)




	




	
