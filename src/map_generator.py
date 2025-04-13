import folium
from tsp_solver import tsp_brute_force, calculate_distance

def generate_map_with_selected_villes(villes_selectionnees):
    """Générer la carte avec le trajet optimal entre les villes sélectionnées"""
    if len(villes_selectionnees) < 2:
        print("Veuillez sélectionner au moins deux villes.")
        return

    # Creer une carte centre sur la premiere ville selectionnee
    depart = villes_selectionnees[0]
    carte = folium.Map(location=[depart['latitude'], depart['longitude']], zoom_start=6)

    # Forcer la premiere ville comme depart
    autres_villes = villes_selectionnees[1:]
    best_route_partielle, _ = tsp_brute_force(autres_villes)

    # Construire le trajet complet : depart + meilleur ordre pour les autres
    best_route = [0] + [i + 1 for i in best_route_partielle]  # ajuster les indices

    # Ajouter des marqueurs numerotes et calculer distance totale
    total_distance = 0
    for idx, i in enumerate(best_route):
        ville = villes_selectionnees[i]
        label = f"{idx}° Ville: {ville['name']}"
        folium.Marker(
            [ville['latitude'], ville['longitude']],
            popup=label,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(carte)

    # Tracer le chemin
    for i in range(len(best_route) - 1):
        ville1 = villes_selectionnees[best_route[i]]
        ville2 = villes_selectionnees[best_route[i + 1]]
        coords = [(ville1['latitude'], ville1['longitude']), (ville2['latitude'], ville2['longitude'])]
        total_distance += calculate_distance(ville1, ville2)
        folium.PolyLine(locations=coords, color='blue', weight=2.5, opacity=1).add_to(carte)

    # Fermer la boucle (retour à la premiere ville)
    ville1 = villes_selectionnees[best_route[-1]]
    ville2 = villes_selectionnees[best_route[0]]
    coords = [(ville1['latitude'], ville1['longitude']), (ville2['latitude'], ville2['longitude'])]
    total_distance += calculate_distance(ville1, ville2)
    folium.PolyLine(locations=coords, color='blue', weight=2.5, opacity=1).add_to(carte)

    # Ajouter distance totale sur la carte
    folium.Marker(
        location=[depart['latitude'], depart['longitude']],
        popup=f"Distance totale : {total_distance:.2f} km",
        icon=folium.Icon(color='green')
    ).add_to(carte)

    # Sauvegarder la carte
    carte.save("map/Votre_trajet.html")
    print(f"Trajet optimal terminé. Distance totale : {total_distance:.2f} km")
