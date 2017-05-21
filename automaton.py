""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
from statements_lose_version import statements_lose_version

statements = statements_lose_version
total_questions = len(statements_lose_version)
question_num = 0 #question started on
score= 0



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
		repeat_question(lets_play)
	return lets_play
	
	

def leave_game():
	exit()

def repeat_question(lets_play):
	print "Please input Y or N"
	welcome_statement(lets_play)


def leading_statement(statements,question_num,score):
	"""Asks question and fields response"""
	answer = raw_input (statements[question_num]["question"]["synopsis"]) # is a string
	options = statements[question_num]["question"]["options"] # options is a list with a dictionary in it
	lose_message = statements[question_num]["question"]["lose_message"] # is a string

	for tupletest in options:
		if answer in tupletest[1]:
			#print "its in there" + tupletest[0]
			#checks to see if in possible answers.
			return tupletest[0]
			if tupletest[0] == "YES":
				print statements[question_num]["question"]["lose message"]
				print "Your final score was %d" %score
				lets_play == False
				leave_game()
			elif tupletest[0] == "NO":
				score += 1 #adds score when not losing
				question_num += 1 # goes to next question
		else:
			print "please type an understandable response"
			#this could be expanded to print all the options in the lists in the tuples.
	return score
	


def main():
	"""
	this the your driver 
	"""
	lets_play = None
	play = welcome_statement(lets_play)
	if play == True:
		leading_statement(statements,question_num,score)
	elif play == 2:
		repeat_question(lets_play)
	else:
	 	leave_game()
 
 #runs the main function
if __name__=='__main__':
	main()
