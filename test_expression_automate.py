import projet

# ---------- TEST EXPRESSION VERS AUTOMATE ---------- #

E = ["*", ["+", ["a", [".", ["*", "b"], ["a"]]]]]
aut = projet.expression_vers_automate(E)
aut.display("Automate de l'expression E = [\"*\", [\"+\", [\"a\", [\".\", [\"*\", \"b\"], [\"a\"]]]]]")