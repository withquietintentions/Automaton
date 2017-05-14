"""questions, and outcomes"""
statements_lose_version = [  
	{"question1" : { 
		"synopsis": "Pandora was created by Hephaistos, the same creator who built atomatons? Do you want to know what atomatons are?",
		"options" : [ ("Yes".upper, True), ("No".upper, False)]
		"lose message": "Atomatons are metal statues of animal, men and monsters, from ancient Greek Myths. The best crafted ones can think and feel like humans. You lose and so does all humanity"
	}}, 
	{"question2" : {
		"synopsis": "Originally pandoras box was not a box. Was it a vase, a jar, or a basket?"
		"options" : [ ("vase".lower, True), ("jar".lower, True), ("basket".lower, True) ("", False)]
		"lose message": "It was a JAR! You lose and so does humanity"
	}} 

]



"""("Pandora was created by Hephaistos, the same creator who built atomatons? Do you want to know what Atomatons are?": "Atomatons are metal statues of animal, men and monsters, from ancient Greek Myths. The best crafted ones can think and feel like humans. You lose and so does all humanity",
"It was a jar.")
("Originally pandoras box was not a box. I was a vase, a jar, or a basket?": "a jar")
("The main trouble with cyborgs, of course , is that they are the illegitimate offspring of militarism and patriarchal capitalism...But illegitimate offspring are... Open Pandoras box to read the rest (open/No)"



]

related_statements_lose_version [
,
"...often exceedingly unfaithful to their origins. Their fathers, after all, are inessential - Donna Haraway A Cyborg Manifesto. All of humanity is doomed and you lose."

]

open_the_box_or_not_statements [ "If so open Pandoras box. Y/N", "Type your guess OR type Nah to not open Pandoras Box."]
