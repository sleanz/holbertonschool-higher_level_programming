#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convertit un chiffre romain en entier.
    
    Args:
        roman_string: Une chaîne de caractères représentant un chiffre romain
        
    Returns:
        La valeur entière du chiffre romain, ou 0 si l'entrée n'est pas une chaîne ou est None
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    valeurs_romaines = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    valeur_precedente = 0
    
    # Parcourir la chaîne de droite à gauche
    for caractere in reversed(roman_string):
        valeur_courante = valeurs_romaines.get(caractere, 0)
        
        # Si la valeur courante est supérieure ou égale à la valeur précédente, on l'ajoute
        if valeur_courante >= valeur_precedente:
            total += valeur_courante
        # Si la valeur courante est inférieure à la valeur précédente, on la soustrait
        else:
            total -= valeur_courante
            
        valeur_precedente = valeur_courante
    
    return total