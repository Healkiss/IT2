import automaton
aut1 = automaton.automaton(
	epsilons = ['0'], states = [5] , initials = [0 ,1] , finals = [3 ,4] ,
	transitions = [
		(0 , 'a' ,1) , (1 ,'b' ,2) , (2 , 'b' ,2) , (2 , '0' ,3) , (3 , 'a' ,4)
	]
)
aut1.display()