"""In this game there is a hidden history of destruction. The goal is to find all hidden items and remove them. O
Eventually you can also add to the list nice things. On the other side of the cube the game exists with the lists switchedso you add bad things and remove good ones"""
#data
sad_history_hidden_list =["bombs", "sadness", 'war', "cello"]
game_in_play = True

def pop_search(sad_list, index):
	sad_list.pop(index)
	print what_user_wants_to_find +" has been removed from history"

def find_item_in_list(what_user_wants_to_find,sad_history_hidden_list):
	if what_user_wants_to_find in sad_history_hidden_list:
		index_what_user_wants_to_find = sad_history_hidden_list.index(what_user_wants_to_find)
		pop_search(sad_history_hidden_list, index_what_user_wants_to_find)
	else:
		print what_user_wants_to_find + " could not be removed from history"


while game_in_play:
	if len(sad_history_hidden_list) > 0:
		what_user_wants_to_find = raw_input("What would you like to find and remove from history?")
		find_item_in_list(what_user_wants_to_find,sad_history_hidden_list)
	else:
		print "You win."
		exit()






	
	


	



	