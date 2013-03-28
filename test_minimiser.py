import projet
import automaton

# ---------- TEST MINIMISER ---------- #
aut = automaton.automaton(
        epsilons = ['0'], initials = [0], finals = [0,3,4,6,7],
        transitions = [
            (0,'a',2), (0,'b',1), (1,'a',2), (1,'b',1), (2,'a',3), (2,'b',2), (3,'a',2), (3,'b',6), (4,'a',5), (4,'b',4),
            (5,'a',6), (5,'b',5), (6,'a',5), (6,'b',7), (7,'a',5),(7,'b',3)
            ]
)


aut.display("Automate de depart")
aut2 = projet.minimiser(aut)
aut2.display("Automate minimise")