"""In this game there is a hidden history of sad things. The goal is to find all hidden items and remove them. 
Eventually you will also add to the list nice things. On the other side of the cube the game exists with the lists switchedso you add bad things and remove good ones"""
#data
from apikeys import KEY
from addgame import sad_history_hidden_list
import json
import ast
import requests
from pprint import pprint
url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2/war/json"
response = requests.get(url)
dict = ast.literal_eval(response.content)
pprint(dict.get("noun")) #debug
#gets into nouns 


def url_request(what_user_wants_to_find)
"""makes url to talk to API"""
search_word_url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2//json"
index = search_word_url.find ("/json")
output_search_url = search_word_url[:index] + what_user_wants_to_find + search_word_url[index:]
return output_search_url
#print output_search_url #debugging



# if a synonym is checked in list it tells them what they wanted to find has been removed. 



def pop_search(sad_list, index):
	sad_list.pop(index)
	print what_user_wants_to_find +" has been removed from history"
	print "%d items are left in history that need to be removed" %len(sad_list)

def find_item_in_list(what_user_wants_to_find,sad_history_hidden_list):
	if what_user_wants_to_find in sad_history_hidden_list:
		index_what_user_wants_to_find = sad_history_hidden_list.index(what_user_wants_to_find)
		pop_search(sad_history_hidden_list, index_what_user_wants_to_find)
	else:
		search_word_url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2/" + what_user_wants_to_find + "/json"
		response_for_word = requests.get(search_word_url)
		dict = ast.literal_eval(response_for_word.content)
		nouns = (dict.get('noun'))
		pprint(nouns.get("syn"))#debug prints 
		synonyms = (nouns.get("syn")) # gets into synonyms
		print what_user_wants_to_find + " could not be removed from history"




#main(sad_history_hidden_list):
"""Driver"""
game_in_play = True
while game_in_play:
	if len(sad_history_hidden_list) > 0:
		what_user_wants_to_find = raw_input("What would you like to find and remove from history?")
		find_item_in_list(what_user_wants_to_find,sad_history_hidden_list)
	else:
		print "You win."
		exit()








	
	


	



	