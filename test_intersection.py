import projet
import automaton

# ---------- TEST INTERSECTION ---------- #
aut1 = automaton.automaton(
        epsilons = ['0'], initials = [1], finals = [2,3],
        transitions = [
            (1,'a',2), (2,'b',3), (3,'a',1), (3,'b',2)
        ]
)

aut2 = automaton.automaton(
        epsilons = ['0'], initials = [1,3], finals = [2],
        transitions = [
            (1,'a',2), (1,'b',3), (2,'b',2), (2,'a',3), (3,'a',1)
        ]
)

aut1.display("Automate 1")
aut2.display("Automate 2")
aut = projet.intersection(aut1,aut2)
aut.display("Intersection de l'automate 1 et de l'automate 2")