""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
#import statements_lose_version
statements_lose_version = [  
	{"question1" : { 
		"synopsis": "Pandora was created by Hephaistos, the same creator who built atomatons? Do you want to know what atomatons are?",
		"options" : [ ("Yes".upper, True), ("No".upper, False)],
		"lose message": "Atomatons are metal statues of animal, men and monsters, from ancient Greek Myths. The best crafted ones can think and feel like humans. You lose and so does all humanity"
	}}, 
	{"question2" : {
		"synopsis": "Originally pandoras box was not a box. Was it a vase, a jar, or a basket?",
		"options": [ ("vase".lower, True), ("jar".lower, True), ("basket".lower, True), ('', False)],
		"lose message": "It was a JAR! You lose and so does humanity"
	}}, 
	{"question3" : {
		"synopsis": "The main trouble with cyborgs, of course , is that they are the illegitimate offspring of militarism and patriarchal capitalism...But illegitimate offspring are... Open Pandoras box to read the rest (open/No)",
		"options": [ ("Y".lower, True), ("N".lower, False)],
		"lose message": "often exceedingly unfaithful to their origins. Their fathers, after all, are inessential - Donna Haraway A Cyborg Manifesto. All of humanity is doomed and you lose."
	}} 
]


def welcome_statement():
	# asks user if they want to play the game
	welcome_answer= raw_input ("Welcome to Automaton. Would you like to play a game about curiosity and information? Y/N")
	if welcome_answer.upper() == "Y" :
		leading_statement = True 
	elif raw_input.upper == "N":
		print "Ok bye"
	else:
		print "Please enter Y or N"
def leading_statement(statements, question_number):
	pass #prints question 1
def pair_to_leading_statement():
	pass#list of corresponding answer statments
def you_lose():
	pass#list of versions of saying you lose
def you_win():
	pass#results of winning

welcome_statement()
if leading_statement:
	print statements_lose_version[0]["question1"]["synopsis"]
