import itertools
import geopy.distance
from config import VILLES

def calculate_distance(ville1, ville2):
    """Calculer la distance entre deux villes"""
    coords_1 = (ville1['latitude'], ville1['longitude'])
    coords_2 = (ville2['latitude'], ville2['longitude'])
    return geopy.distance.geodesic(coords_1, coords_2).km

def tsp_brute_force(villes):
    """Algorithme de résolution du TSP en utilisant la méthode brute (permutations)"""
    # Generer toutes les permutations possibles des indices des villes
    all_routes = list(itertools.permutations(range(len(villes))))
    
    best_route = None
    min_distance = float('inf')
    
    # Tester chaque permutation pour calculer la distance totale
    for route in all_routes:
        distance = 0
        for i in range(len(route) - 1):
            distance += calculate_distance(villes[route[i]], villes[route[i+1]])
        # Fermer la boucle (retour a ville de depart)
        distance += calculate_distance(villes[route[-1]], villes[route[0]])

        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance
