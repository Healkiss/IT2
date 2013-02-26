import automaton
def automate_des_mots_contenant_l_alphabet(alphabet):
	initiaux = [automaton.pretty_set()]
	epsilons = []
	finaux = [automaton.pretty_set(alphabet )]
	etats = set(automaton.pretty_set () )
	pile = [automaton.pretty_set () ]
	transitions = []
	while len (pile) > 0:
		origine = pile.pop ()
		for lettre in alphabet :
			fin = origine.union ([lettre])
			if not (fin in etats):
				etats.add (fin)
				pile.append(fin)
			transitions.append ((origine, lettre, fin))
	return automaton.automaton(
		alphabet , epsilons , etats , initiaux , finaux , transitions
	)
A = automate_des_mots_contenant_l_alphabet ( [ 'a' , 'b' , 'c'] )
A.display ()