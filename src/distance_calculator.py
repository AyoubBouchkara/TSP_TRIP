from geopy.distance import geodesic

def calculer_distance(ville1, ville2):
    coord1 = (ville1['latitude'], ville1['longitude'])
    coord2 = (ville2['latitude'], ville2['longitude'])
    return geodesic(coord1, coord2).km

def afficher_distances(villes):
    for i, ville1 in enumerate(villes):
        for ville2 in villes[i+1:]:
            distance = calculer_distance(ville1, ville2)
            print(f"Distance entre {ville1['name']} et {ville2['name']}: {distance:.2f} km")

if __name__ == "__main__":
    from config import VILLES
    afficher_distances(VILLES)
