#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Essayer d'accéder aux éléments dans les deux listes
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            
            # Essayer de diviser les éléments
            division_result = value_1 / value_2
            
            # Vérifier si le résultat est un nombre (int ou float)
            if not isinstance(division_result, (int, float)):
                raise TypeError
                
            result.append(division_result)
            
        except ZeroDivisionError:
            # Gérer la division par zéro
            print("division by 0")
            result.append(0)
            
        except (TypeError, ValueError):
            # Gérer les erreurs de type (si les éléments ne sont pas des nombres)
            print("wrong type")
            result.append(0)
            
        except IndexError:
            # Gérer le cas où une liste est trop courte
            print("out of range")
            result.append(0)
            
        finally:
            # Ce bloc s'exécute toujours mais ne fait rien de spécial ici
            pass
            
    return result