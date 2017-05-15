"""In this game there is a hidden history of destruction. The goal is to find all hidden items and remove them"""
#data
sad_history_hidden_list =["atomic bombs", "sadness", 'war', 'destruction', "rape", "trauma", "bombs", "racism", "sexism"]
what_user_wants_to_find = raw_input("What would you like to find and remove from history?")
position_to_pop = sad_history_hidden_list.index(what_user_wants_to_find)
pop_result = False

def pop_search(sad_history_hidden_list):
	sad_history_hidden_list.pop(position_to_pop)
	print what_user_wants_to_find +" has been removed from history"

for item in sad_history_hidden_list:
	if item == what_user_wants_to_find:
		pop_search(sad_history_hidden_list)
	else:
		print "That is not in the sad hidden history."



	