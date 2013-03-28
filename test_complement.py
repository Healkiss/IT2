import projet
import automaton

# ---------- TEST COMPLEMENT ---------- #
aut = automaton.automaton(
        epsilons = ['0'], initials = [1,3], finals = [2],
        transitions = [
            (1,'a',2), (1,'b',3), (2,'b',2), (2,'a',3), (3,'a',1)
        ]
)


aut.display("Automate de depart")
aut2 = projet.complement(aut)
aut2.display("Automate complement")