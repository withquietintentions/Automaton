""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
import statements_lose_version

def welcome_statement():
	# asks user if they want to play the game
	raw_input ("Welcome to Automaton. Would you like to play a game about curiosity and information? Y/N")
	if raw_input.upper() == Y :
		leading_statment()
	elif raw_input.upper == N :
		print "Ok bye"
	else:
		print "Please enter Y or N"
def leading_statement(statements):
	print statements[0]#list of first part of statments that act as teasers to learn more
def pair_to_leading_statement():
	pass#list of corresponding answer statments
def you_lose():
	pass#list of versions of saying you lose
def you_win():
	pass#results of winning

welcome_statement()
leading_statement(statements_lose_version)
