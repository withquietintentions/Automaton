"""In this game there is a hidden history of sad things. The goal is to find all hidden items and remove them. 
Eventually you will also add to the list nice things. On the other side of the cube the game exists with the lists switchedso you add bad things and remove good ones"""
#data
from apikeys import KEY
#from addgame import sad_history_hidden_list
import json
import ast
import requests
from pprint import pprint
#url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2/war/json"
#response = requests.get(url)
#dict = ast.literal_eval(response.content)
#pprint(dict.get("noun")) #debug
#gets into nouns 



"""def url_request(what_user_wants_to_find):
	makes url to talk to API
	search_word_url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2//json"
	index = search_word_url.find ("/json")
	url = search_word_url[:index] + what_user_wants_to_find + search_word_url[index:]
	return url
	response_for_word = requests.get(url)
	dict = ast.literal_eval(response_for_word.content)
	nouns = (dict.get('noun'))
	pprint(nouns.get("syn"))#debug prints 
	synonyms = (nouns.get("syn")) # gets into synonyms
#print output_search_url #debugging"""


#print what_user_wants_to_find + " could not be removed from history"
# if a synonym is checked in list it tells them what they wanted to find has been removed. 



"""def pop_search(sad_list, index):
	sad_list.pop(index)
	print what_user_wants_to_find +" has been removed from history"
	print "%d items are left in history that need to be removed" %len(sad_list)"""

def synonym_pop(sad_history_hidden_list, synonyms, what_user_wants_to_find, try_again):
	for item in synonyms:
			if item in sad_history_hidden_list:
				index = sad_history_hidden_list.index(item)
				sad_history_hidden_list.pop(index)
				print "close enough!" + item + "has been removed from history"
				print "%d items are left in history that need to be removed" %len(sad_list)

def find_item_in_list(what_user_wants_to_find, sad_history_hidden_list):
	if what_user_wants_to_find in sad_history_hidden_list:
		index_what_user_wants_to_find = sad_history_hidden_list.index(what_user_wants_to_find)
		pop_search(sad_history_hidden_list, index_what_user_wants_to_find)
	else:
		game_in_play = False
		#pulls dictionary of synonyms
		search_word_url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2//json"
		index = search_word_url.find ("/json")
		url = search_word_url[:index] + what_user_wants_to_find + search_word_url[index:]
		response_for_word = requests.get(url)
		dict = ast.literal_eval(response_for_word.content)
		nouns = (dict.get('noun'))
		#pprint(nouns.get("syn"))#debug prints 
		synonyms = (nouns.get("syn"))
		try_again = 0
		for item in synonyms:
			if item in sad_history_hidden_list:
				index = sad_history_hidden_list.index(item)
				sad_history_hidden_list.pop(index)
				print "close enough!" + item + "has been removed from history"
				print "%d items are left in history that need to be removed" %len(sad_history_hidden_list)
				#print sad_history_hidden_list #debugging only
				try_again = try_again +1
				game_in_play = True
		return try_again




def main(sad_history_hidden_list, try_again):
	"""Driver"""

sad_history_hidden_list =["bombs", "sadness", 'war', "trauma", "rape", "fear", "flower"]
game_in_play = True
while game_in_play:
	if len(sad_history_hidden_list) > 0:
		what_user_wants_to_find = raw_input("What would you like to find and remove from history?")
		if what_user_wants_to_find == "Q":
			exit()
		else:
			try_again = find_item_in_list(what_user_wants_to_find,sad_history_hidden_list)
			if try_again < 1:
		 		print "Sorry this cannot be removed, try again?"
	else:
		print "You win."
		exit()

 #runs the main function
#if __name__=='__main__':
main()








	
	


	



	