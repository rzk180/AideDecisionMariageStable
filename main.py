from algorithms.stable_matching import gale_shapley
from algorithms.satisfaction import calculate_candidate_satisfaction, calculate_establishment_satisfaction
from algorithms.preferences import generate_preferences

def main():
    # Génération des préférences
    candidates, establishments = generate_preferences(5, 5)

    # Exécution de Gale-Shapley
    matchings = gale_shapley(candidates, establishments)

    # Calcul des satisfactions
    candidate_satisfaction = calculate_candidate_satisfaction(matchings, candidates)
    establishment_satisfaction = calculate_establishment_satisfaction(matchings, establishments)

    # Résultats
    print("Appariements :", matchings)
    print("Satisfaction des candidats :", candidate_satisfaction)
    print("Satisfaction des établissements :", establishment_satisfaction)

if __name__ == "__main__":
    main()
