
def calculer_moyenne(notes):
    total = 0

    for note in notes:
        total += note

    return total / len(notes)


def chercher_utilisateur(utilisateurs, nom):
    for utilisateur in utilisateurs:
        if utilisateur["nom"] == nom:
            return utilisateur

    return None


def afficher_resultat(notes, utilisateurs, nom):
    moyenne = calculer_moyenne(notes)
    utilisateur = chercher_utilisateur(utilisateurs, nom)

    print("Utilisateur :", utilisateur["nom"])
    print("Moyenne :", moyenne)


notes = [12, 15, 18]
utilisateurs = [
    {"nom": "Alice"},
    {"nom": "Bob"}
]

afficher_resultat([], utilisateurs, "Charlie")
