#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Remplace toutes les occurrences d'un élément par un autre dans une nouvelle liste.
    
    Args:
        my_list: La liste initiale
        search: L'élément à remplacer dans la liste
        replace: Le nouvel élément
        
    Returns:
        Une nouvelle liste avec les remplacements effectués
    """
    # Crée une nouvelle liste en utilisant une compréhension de liste
    new_list = [replace if element == search else element for element in my_list]
    
    return new_list