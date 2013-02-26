import automaton
def automate ():
	alphabet = ['a' ,'b' ,'c' ,'d' ]
	epsilons = []
	initiaux = [(0 ,0)]
	etats = []
	finaux = []
	transitions = []
	for a_moins_b in [0, 1, -1]:
		for c_moins_d in [0, 1, -1]:
			etats.append((a_moins_b, c_moins_d))
			finaux.append((a_moins_b, c_moins_d))
	for origine in etats:
		for lettre in alphabet:
			if lettre == 'a' :
				fin = (origine[0]+1, origine[1])
			elif lettre == 'b' :
				fin = (origine[0]-1, origine[1])
			elif lettre == 'c' :
				fin = (origine[0], origine[1]+1)
			else :
				fin = (origine[0], origine[1]-1)
			if abs(fin[0]) <= 1 and abs(fin[1]) <= 1 :
				transitions.append((origine, lettre, fin))
	return automaton.automaton(
		alphabet, epsilons, etats, initiaux, finaux ,transitions
	)
B = automate()
B.display()