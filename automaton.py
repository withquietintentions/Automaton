""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
#import statements_lose_version
statements_lose_version = [  
	{"question" : { 
		"synopsis": "Pandora was created by Hephaistos, the same creator who built atomatons? Do you want to know what atomatons are?",
		"options" : [ ("Yes", True), ("No".upper, False)],
		"lose message": "Atomatons are metal statues of animal, men and monsters, from ancient Greek Myths. The best crafted ones can think and feel like humans. You lose and so does all humanity"
	}}, 
	{"question" : {
		"synopsis": "Originally pandoras box was not a box. Was it a vase, a jar, or a basket?",
		"options": [ ("vase".lower, True), ("jar".lower, True), ("basket".lower, True), ('', False)],
		"lose message": "It was a JAR! You lose and so does humanity"
	}}, 
	{"question" : {
		"synopsis": "The main trouble with cyborgs, of course , is that they are the illegitimate offspring of militarism and patriarchal capitalism...But illegitimate offspring are... Open Pandoras box to read the rest (open/No)",
		"options": [ ("Y".lower, True), ("N".lower, False)],
		"lose message": "often exceedingly unfaithful to their origins. Their fathers, after all, are inessential - Donna Haraway A Cyborg Manifesto. All of humanity is doomed and you lose."
	}} 
]
total_questions = len(statements_lose_version)
score = 0 #initial score
question_num = 0 #question started on
lets_play = True
def welcome_statement():
	"""Asks user if they want to play the game"""
	welcome_answer = raw_input ("Welcome to Automaton. Would you like to play a game about curiosity and information? Y/N")
	if welcome_answer.upper() == "Y" :
		print "lets play"
	elif welcome_answer.upper() == "N":
		print "Ok bye"
		global lets_play 
		lets_play= False
		exit()
	else:
		global lets_play 
		lets_play= False
		print "Please enter Y or N"
		
		

def leading_statement(statements, question_num):
	"""Asks question and fields response"""
	answer = raw_input (statements[question_num]["question"]["synopsis"])
	if statements[question_num]["question"]["options"]:
		print statements[question_num]["question"]["lose message"]
		print "Your final score was: (%d)" %score
		lets_play = False
	else:
		score += 1 #adds score when not losing
		question_num += 1 # goes to next question
		


welcome_statement()
while welcome_statement(): #and question_num <= total_questions:
	leading_statement(statements_lose_version,question_num)

	
