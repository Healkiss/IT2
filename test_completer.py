import projet
import automaton

# ---------- TEST COMPLETER ---------- #
aut = automaton.automaton(
        epsilons = ['0'], initials = [0], finals = [2],
        transitions = [
            (0,'a',0), (0,'b',1), (1,'a',2), (2,'b',1)
        ]
)

aut.display("Automate de depart")
aut2 = projet.completer(aut)
aut2.display("Automate complete")
