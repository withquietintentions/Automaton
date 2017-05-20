""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
from statements_lose_version import statements_lose_version

total_questions = len(statements_lose_version)
question_number = 0 #question started on


def welcome_statement(lets_play):
	"""Asks user if they want to play the game"""
	
	welcome_answer = raw_input ("Welcome to Automaton. Would you like to play a game about curiosity and information? Y/N ")
	if welcome_answer.upper() == "Y" :
		print "OK let's play!"
		lets_play = True
	elif welcome_answer.upper() == "N":
		print "Ok bye"
		lets_play = False
		leave_game()
		
	else:
		lets_play = 2
		# call function that is a loop so if it is 2, it asks a question again
		repeat_question()
	return lets_play
	
	

def leave_game():
	exit()

def repeat_question():
	# repeat question if lets play 2



def leading_statement(statements, question_num, score):
	"""Asks question and fields response"""

	answer = raw_input (statements[question_num]["question"]["synopsis"])
	global score

	if statements[question_num]["question"]["options"]:
		print statements[question_num]["question"]["lose message"]
		print "Your final score was %d" %score
		lets_play == False
		return lets_play
	else:
		score += 1 #adds score when not losing
		question_num += 1 # goes to next question


def main():
	"""
	this is your driver 
	"""
	score= None
	lets_play = None
	play = welcome_statement(lets_play)
	if play == True:
		leading_statement( ..... score)
	elif play == 2:
		# ask question again
	 else:
	 	#exit game
 
 
## look in lecture notes for this below
 # if  ... =='__main__':
 # 	main()





	
