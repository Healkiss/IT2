import automaton
#Fichier contenant toutes les fonctions


# ---------- COMPLETER ---------- #
def completer( aut ):
    puits  = False
    alphabet = aut.get_alphabet()
    states = aut.get_states()
    for state in states:
        for lettre in alphabet:
            if aut.delta(lettre, [state])    ==    set():
                if puits == False:
                    aut.add_state('P')
                    puits = True
                aut.add_transition( (state,lettre,'P') )
    return aut

# ---------- UNION ---------- #
def union( aut1, aut2 ):
    aut1.renumber_the_states()
    aut2.translate(aut1.get_maximal_id()+1)
    aut = automaton.automaton()
    alphabet = aut1.get_alphabet()
	#On cree une liste pour mettre les couples de sommets traites et a traiter
    setStates = []
	#pour chaque etat initial de l'automate 1
    for s1 in aut1.get_initial_states():
		#on l'ajoute en tant que etat initial
        setStates.append((s1,0))
	#pour chaque etat initial de l'automate 2
    for s2 in aut2.get_initial_states():
		#on l'ajoute en tant que etat initial
        setStates.append((0,s2))
	#pour chaque couple
    for S in setStates:
		#pour chaque lettre
        for lettre in alphabet:
			#on divise notre couple en deux
            sub_etat1 = list(S)[0]
            sub_etat2 = list(S)[1]
			#on cherche les etats d'arrives pour chaque partie de notre couple
            s1 = aut1.delta(lettre, [sub_etat1])
            s2 = aut2.delta(lettre, [sub_etat2])
            if s1:
                sub_stat1 = list(s1)[0]
            else:
                sub_stat1 = 0
                
            if s2:
                sub_stat2 = list(s2)[0]
            else:
                sub_stat2 = 0
			#si le couple ne mene nul part par aucun des deux sommet du couple
            if not(sub_stat1 == 0 and sub_stat2 == 0):
                aut.add_transition((S,lettre,(sub_stat1,sub_stat2)))
				#si l'etat/couple n'existe pas dans la liste, on le rajoute
                if (sub_stat1,sub_stat2) not in setStates:
                    setStates.append((sub_stat1,sub_stat2))
	#on lit tous nos couples
	for S in aut.get_states():
		#on divise notre couple en deux
		sub_etat1 = list(S)[0]
		sub_etat2 = list(S)[1]
		#si l'un des deux etats du couple est respectivement etat final de son automate
		if sub_etat1 in aut1.get_final_states() or sub_etat2 in aut2.get_final_states():
			#on rajoute le couple en etat final
			aut.add_final_state(S)
	for S in aut.get_states():
		#on divise notre couple en deux
		sub_etat1 = list(S)[0]
		sub_etat2 = list(S)[1]
		#si l'un des deux etats du couple est respectivement etat initial de son automate
		if sub_etat1 in aut1.get_initial_states() or sub_etat2 in aut2.get_initial_states():
			#on rajoute le couple en etat final
			aut.add_initial_state(S)
    return aut


 
# ---------- INTERSECTION ---------- #
def intersection( aut1, aut2 ):
    #On renome les etats des deux automates
    aut1.renumber_the_states()
    aut2.translate(aut1.get_maximal_id()+1)
    
    aut = automaton.automaton()
    alphabet = aut1.get_alphabet()
    #On cree une liste pour mettre les couples de sommets traites et a traiter
    setStates = []
	#pour chaque etat initial de l'automate 1
    for s1 in aut1.get_initial_states():
		#pour chaque etat initial de l'automate 2
        for s2 in aut2.get_initial_states():
			#on ajoute les couple d'état initiaux
            setStates.append((s1,s2))
	#on parcours enfin notre liste de couples de sommets
	#pour chaque couple
    for S in setStates:
		#pour chaque lettre
        for lettre in alphabet:
			#on divise notre couple en deux
            sub_etat1 = list(S)[0]
            sub_etat2 = list(S)[1]
			#on cherche les etats d'arrives pour chaque partie de notre couple
            s1 = aut1.delta(lettre, [sub_etat1])
            s2 = aut2.delta(lettre, [sub_etat2])
            if s1:
                sub_stat1 = list(s1)[0]
            else:
                sub_stat1 = 0
            if s2:
                sub_stat2 = list(s2)[0]
            else:
                sub_stat2 = 0
			#on rajoute la transition du couple lu par la lettre en cours vers les sommets trouves
            aut.add_transition((S,lettre,(sub_stat1,sub_stat2)))
			#si l'etat/couple n'existe pas dans la liste, on le rajoute
            if (sub_stat1,sub_stat2) not in setStates:
                setStates.append((sub_stat1,sub_stat2))
	#on lit tous nos couples
	for S in aut.get_states():
		#on divise en deux
		sub_etat1 = list(S)[0]
		sub_etat2 = list(S)[1]
		#si les deux etats du couple sont respectivement etats finaux de leur automate
		if sub_etat1 in aut1.get_final_states():
			if sub_etat2 in aut2.get_final_states():
				#on rajoute le couple en etat final
				aut.add_final_state(S)
	#on lit tous nos couples
	for S in aut.get_states():
		#on divise en deux
		sub_etat1 = list(S)[0]
		sub_etat2 = list(S)[1]
		#si les deux etats du couple sont respectivement etats initiaux de leur automate
		if sub_etat1 in aut1.get_initial_states():
			if sub_etat2 in aut2.get_initial_states():
				#on rajoute le couple en etat initial
				aut.add_initial_state(S)
    return aut            


# ---------- MIRROIR ---------- #
def miroir(aut):
    #on cree un nouvel automate avec les memes etats, le meme alphabet et on echange les etats finaux et initiaux
    aut2=automaton.automaton(
        alphabet = aut.get_alphabet(),
        states = aut.get_states(),
        finals = aut.get_initial_states(),
        initials = aut.get_final_states())
    #pour toutes les transitions on echange leur sens
    for t in aut.get_transitions():
        aut2.add_transition((list(t)[2], list(t)[1], list(t)[0]))
    return aut2



# ---------- DETERMINISATION ---------- #
def determinisation (aut):
    #on renome les etats de l'automate pour que ca soit plus simple
    aut.renumber_the_states()
    aut2=automaton.automaton()
    setStates = []
	#pour chaque etat initial de l'automate
    for i in aut.get_initial_states():
		#on l'ajoute a notre set a parcourir
        setStates.append(i)
	#on freeze l'etat pour pouvoir le rajouter
    initialState = frozenset(setStates)
    aut2.add_initial_state(initialState)
    setStates = [setStates]
    alphabet = aut.get_alphabet()
	#pour chacun de nos etat a parcourir
    for S in setStates:
		#pour chaque lettre
        for lettre in alphabet:
            tmpState = list()
			#pour chaque partie de notre etat (dans le cas d'un couple, liste ..)
            for s in S:
                myDelta = aut.delta(lettre, [s])
				#pour chaque sommet d'arrive par la lettre en cours
                for i in myDelta:
					#on le rajoute a un set temporaire
                    tmpState.append(i)
            newS2 = frozenset(S)
			#qu'on gele
            tmpState2 = frozenset(tmpState)
            if tmpState2 != frozenset():
				#pour le rajouter en tant que etat d'arrive de la nouvelle transistion cree.
                aut2.add_transition((newS2, lettre, tmpState2))
			#si l'etat d'arrive n'exite pas dans notre liste a parcourir
            if tmpState not in setStates:
				#alors on le rajoute
                setStates.append((tmpState))
	#pour chaque etat du nouvel automate
    for S in aut2.get_states():
		#pour chaque partie de l'etat
        for s in S:
			#si il est etat final dans le premier automate
            if s in aut.get_final_states():
				#alors on le rajoute a nos etats finaux du nouvel automate
                aut2.add_final_state(S)
                break
    return aut2
            


# ---------- COMPLEMENT ---------- #
def complement(aut):
    #on determinise et complete l'automate
    aut=determinisation(aut)
    aut=completer(aut)
    #on affiche l'automate apres ces deux etapes
    aut.display("Automate de depart determinise et complete")
    #on cree un nouvel automate avec le meme alphabet, les memes etats (les initiaux reste initiaux), les memes transitions
    aut2=automaton.automaton(
            alphabet = aut.get_alphabet(),
            states = aut.get_states(),
            transitions = aut.get_transitions(),
            initials = aut.get_initial_states())
    #Tout les etats qui ne sont pas finaux (sauf le puit) deviennent finaux dans le nouvel automate
    for s in aut.get_states():
        if s not in (aut.get_final_states()) and s != 'P':
            aut2.add_final_state(s)
    return aut2



# ---------- MINIMISER ---------- #
def minimiser(aut):
    #Utilisation de l'algorithme de double renversement
    '''
	#pas a pas
    aut1 = miroir(aut)
    aut1.display("aut1 : aut miroir")
    aut2 = determinisation(aut1)
    aut2.display("aut2 : aut1 determinisation")
    aut3 = miroir(aut2)
    aut3.display("aut3 : aut2 miroir")
    aut4 = determinisation(aut3)
    return aut4
    '''
	# ou selon la formule d(r(d(r(Aut)))) :
    return determinisation(miroir(determinisation(miroir(aut))))


        
# ---------- EXPRESSION VERS AUTOMATE ---------- #

# Fontion ETOILE :
def etoile(aut):
    #on cree un nouvel automate avec les memes etats, les memes transitions et le meme alphabet
    aut2=automaton.automaton(
            alphabet = aut.get_alphabet(),
            states = aut.get_states(),
            transitions = aut.get_transitions())
    #on rajoute un super etat final et un super final
    aut2.add_initial_state('I')
    aut2.add_final_state('F')
    #on rajoute des etats de transitions
    aut2.add_states(['i','f'])
    #on rajoute les epsilons transitions entre les etats qu'on vient de rajouter
    aut2.add_transitions([('I','0','i'),('I','0','F'),('f','0','F'),('f','0','i')])
    #on rajoute les epsilons transition entre l'etats i et les etats initiaux de l'automate de depart
    for i in aut.get_initial_states():
        aut2.add_transition(('i','0',i))
    #on rajoute les epsilons transition entre l'etats f et les etats finaux de l'automate de depart
    for f in aut.get_final_states():
        aut2.add_transition((f,'0','f'))
    return aut2


# Fonction CONCATENATION :
def concatenation(aut1, aut2):
    #on renome les etats des deux automates pour que ca soit plus simple
    aut1.renumber_the_states()
    aut2.translate(aut1.get_maximal_id()+1)
    #on cree un nouvel automate avec les etats, les transitions et l'alphabet de l'automate 1
    aut3 = automaton.automaton(
            alphabet = aut1.get_alphabet(),
            states = aut1.get_states(),
            transitions = aut1.get_transitions())
    #on ajoute l'alphabet, les transitions et les etats de l'automate 2
    aut3.add_characters(aut2.get_alphabet())
    aut3.add_states(aut2.get_states())
    aut3.add_transitions(aut2.get_transitions())
    #on cree un super etat initial et un super etat final
    aut3.add_initial_state('I')
    aut3.add_final_state('F')
    #on rajoute les epsilons transitions
    for i in aut1.get_initial_states():
        aut3.add_transition(('I','0',i))
    for f in aut2.get_final_states():
        aut3.add_transition((f,'0','F'))
    for f in aut1.get_final_states():
        for i in aut2.get_initial_states():
            aut3.add_transition((f,'0',i))
    return aut3


# Fonction Finale :
def expression_vers_automate(E):
    #on utilise ici un algorithme recursif pour analyser chaque partie de l'expression une a une
    e = E[0]
    if e == '+':
        aut = union(expression_vers_automate(E[1][0]),expression_vers_automate(E[1][1]))
    if e == '.' :
        aut = concatenation(expression_vers_automate(E[1]),expression_vers_automate(E[2]))
    if e == '*':
        aut = etoile(expression_vers_automate(E[1]))
    if e.isalpha() :
        aut = automaton.automaton(
            epsilons = ['0'],
            initials = [0] , finals = [1],
            transitions = [(0,e,1)])
    return aut


'''
def getSommet(pile):
	if not len(pile)==0:
		tmp = pile.pop()
		pile.append(tmp)
	else:
		tmp = None
	return tmp

def infixToPrefix(s):
	#il faut s'y prendre un peu differement, il s'agit pas d'ouvrir des parentheses mais de creer une autre liste contenant ce qu'on va calculer
	#donc il faut plutot faire qqch de reccurcif. Meme si je vois pas bien comment faire pour le moment
	po = [] #pile operateur
	pl = [] #pile lettre
	res = []
	oldToken = -1
	cpt = 0
	for i, token in enumerate(s):
		print("i et token : ", i, token)
		if token == "(":
			po.append('(')
			#look for the next close parenthesis
			# on modifie le token pour que le symbole soit traite normalement
			#attention a bien remettre toutes les conditions en dessous de celle ci
			for j, tmp in enumerate(s):
				if tmp == ')':
					token = s[j+1]
					print("apres parenthese : ", token)
			#look for the next close parenthesis
		if token.isalpha() :
			if not isinstance( oldToken, int ):
				if oldToken.isalpha():
					po.append(".")
					oldToken = token
					pl.append(token)
		if token == '+':
			po.append('+')
			res.append("\"+\", [")
			if pl.__len__() <= 0:
				print("error()")
				cptPoints = 0
			while getSommet(po) == '.' :
				cptPoints = cptPoints+1
				res.append("\".\",[")
			while getSommet(pl) != None:
				res.append("\"")
				res.append(getSommet(pl))
				pl.pop()
				res.append("\"],[")
			for i in range(cptPoints):
				res.append("]")
		if token == ')':
			res.append("\"]")
		if token == '*':
			res.append("[\"*\"")
			
	print("res : ", res)
 '''               
                