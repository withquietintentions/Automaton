""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
from statements_lose_version import statements_lose_version

total_questions = len(statements_lose_version)
score = 0 #initial score
question_number = 0 #question started on


def welcome_statement():
	"""Asks user if they want to play the game"""
	
	lets_play = True
	welcome_answer = raw_input ("Welcome to Automaton. Would you like to play a game about curiosity and information? Y/N")
	if welcome_answer.upper() == "Y" :
		print "OK let's play!"
	elif welcome_answer.upper() == "N":
		print "Ok bye"
		exit()
	'''else:
		print "Please enter Y or N"
		lets_play = False
		return lets_play'''
	
	

def leave_game_or_replay(lets_play):
	if welcome_statement(lets_play) == False:
		print "Try Again Soon"
		exit()



def leading_statement(statements, question_num,lets_play):
	"""Asks question and fields response"""
	if welcome_statement(lets_play) == True:
		answer = raw_input (statements[question_num]["question"]["synopsis"])
		global score

		if statements[question_num]["question"]["options"]:
			print statements[question_num]["question"]["lose message"]
			print "Your final score was %d" %score
			welcome_statement(lets_play) == False
			return lets_play
		else:
			score += 1 #adds score when not losing
			question_num += 1 # goes to next question
		


welcome_statement()
 #and question_num <= total_questions:
leading_statement(statements_lose_version,question_number,lets_play)
leave_game_or_replay(lets_play)


	
