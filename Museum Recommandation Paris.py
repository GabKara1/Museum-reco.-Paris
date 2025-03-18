>>> # Cellule 1 : Base de données et classes
... 
... paris_museums = [
...     {"name": "Musée du Louvre", "address": "Rue de Rivoli, 75001 Paris", "type": "Art", "latitude": 48.8606, "longitude": 2.3376},
...     {"name": "Musée d'Orsay", "address": "1 Rue de la Légion d'Honneur, 75007 Paris", "type": "Art", "latitude": 48.8600, "longitude": 2.3250},
...     {"name": "Centre Pompidou", "address": "Place Georges-Pompidou, 75004 Paris", "type": "Modern Art", "latitude": 48.8606, "longitude": 2.3522},
...     {"name": "Musée Rodin", "address": "77 Rue de Varenne, 75007 Paris", "type": "Sculpture", "latitude": 48.8554, "longitude": 2.3158},
...     {"name": "Musée de l'Orangerie", "address": "Jardin des Tuileries, 75001 Paris", "type": "Art", "latitude": 48.8639, "longitude": 2.3227},
...     {"name": "Musée Carnavalet", "address": "23 Rue de Birague, 75004 Paris", "type": "Histoire", "latitude": 48.8575, "longitude": 2.3631},
...     {"name": "Musée National Picasso", "address": "5 Rue de Birague, 75003 Paris", "type": "Art", "latitude": 48.8599, "longitude": 2.3622},
...     {"name": "Musée de l’Armée", "address": "129 Rue de Grenelle, 75007 Paris", "type": "Histoire", "latitude": 48.8571, "longitude": 2.3118},
...     {"name": "Musée des Arts et Métiers", "address": "60 Rue Réaumur, 75003 Paris", "type": "Science", "latitude": 48.8660, "longitude": 2.3555},
...     {"name": "Musée Jacquemart-André", "address": "158 Boulevard Haussmann, 75008 Paris", "type": "Art", "latitude": 48.8753, "longitude": 2.3104},
...     {"name": "Musée de la Musique", "address": "221 Avenue Jean Jaurès, 75019 Paris", "type": "Musique", "latitude": 48.8897, "longitude": 2.3940},
...     {"name": "Musée Grévin", "address": "10 Boulevard Montmartre, 75009 Paris", "type": "Cire", "latitude": 48.8719, "longitude": 2.3446},
...     {"name": "Musée du Quai Branly", "address": "37 Quai Branly, 75007 Paris", "type": "Ethnographie", "latitude": 48.8609, "longitude": 2.2977},
...     {"name": "Petit Palais", "address": "Avenue Winston Churchill, 75008 Paris", "type": "Art", "latitude": 48.8660, "longitude": 2.3145},
...     {"name": "Musée Marmottan Monet", "address": "2 Rue Louis Boilly, 75016 Paris", "type": "Art", "latitude": 48.8593, "longitude": 2.2673},
...     {"name": "Musée de Montmartre", "address": "12 Rue Cortot, 75018 Paris", "type": "Histoire", "latitude": 48.8870, "longitude": 2.3406},
...     {"name": "Musée Nissim de Camondo", "address": "63 Rue de Monceau, 75008 Paris", "type": "Art Décoratif", "latitude": 48.8787, "longitude": 2.3128},
    {"name": "Musée de la Chasse et de la Nature", "address": "62 Rue des Archives, 75003 Paris", "type": "Nature", "latitude": 48.8612, "longitude": 2.3570},
    {"name": "Musée de la Vie Romantique", "address": "16 Rue Chaptal, 75009 Paris", "type": "Histoire", "latitude": 48.8808, "longitude": 2.3332},
    {"name": "Musée Bourdelle", "address": "18 Rue Antoine Bourdelle, 75015 Paris", "type": "Sculpture", "latitude": 48.8436, "longitude": 2.3187},
    {"name": "Musée Maillol", "address": "61 Rue de Grenelle, 75007 Paris", "type": "Art", "latitude": 48.8546, "longitude": 2.3248},
    {"name": "Musée Cognacq-Jay", "address": "8 Rue Elzévir, 75003 Paris", "type": "Art", "latitude": 48.8595, "longitude": 2.3618},
    {"name": "Musée de la Poste", "address": "34 Boulevard de Vaugirard, 75015 Paris", "type": "Histoire", "latitude": 48.8415, "longitude": 2.3178},
    {"name": "Musée de la Mode et du Textile", "address": "107 Rue de Rivoli, 75001 Paris", "type": "Mode", "latitude": 48.8625, "longitude": 2.3365},
    {"name": "Musée de l’Air et de l’Espace", "address": "Aéroport de Paris-Le Bourget, 93350 Le Bourget", "type": "Science", "latitude": 48.9473, "longitude": 2.4351},
    {"name": "Musée des Égouts de Paris", "address": "Pont de l’Alma, 75007 Paris", "type": "Histoire", "latitude": 48.8622, "longitude": 2.3025},
    {"name": "Musée de la Magie", "address": "11 Rue Saint-Paul, 75004 Paris", "type": "Insolite", "latitude": 48.8538, "longitude": 2.3620},
    {"name": "Musée des Plans-Reliefs", "address": "129 Rue de Grenelle, 75007 Paris", "type": "Histoire", "latitude": 48.8571, "longitude": 2.3118},
    {"name": "Musée de la Contrefaçon", "address": "16 Rue de la Faisanderie, 75016 Paris", "type": "Insolite", "latitude": 48.8678, "longitude": 2.2768},
    {"name": "Musée de la Poupée", "address": "Impasse Berthaud, 75003 Paris", "type": "Insolite", "latitude": 48.8618, "longitude": 2.3558},
    {"name": "Musée Gustave Moreau", "address": "14 Rue de la Rochefoucauld, 75009 Paris", "type": "Art", "latitude": 48.8779, "longitude": 2.3345},
    {"name": "Musée Zadkine", "address": "100 Bis Rue d’Assas, 75006 Paris", "type": "Sculpture", "latitude": 48.8418, "longitude": 2.3330},
    {"name": "Musée du Parfum", "address": "9 Rue Scribe, 75009 Paris", "type": "Insolite", "latitude": 48.8710, "longitude": 2.3305},
    {"name": "Musée de la Monnaie", "address": "11 Quai de Conti, 75006 Paris", "type": "Histoire", "latitude": 48.8569, "longitude": 2.3390},
    {"name": "Musée de l’Ordre de la Libération", "address": "129 Rue de Grenelle, 75007 Paris", "type": "Histoire", "latitude": 48.8571, "longitude": 2.3118},
    {"name": "Musée Cernuschi", "address": "7 Avenue Vélasquez, 75008 Paris", "type": "Art Asiatique", "latitude": 48.8798, "longitude": 2.3122},
    {"name": "Musée Guimet", "address": "6 Place d’Iéna, 75016 Paris", "type": "Art Asiatique", "latitude": 48.8654, "longitude": 2.2938},
    {"name": "Musée de la Publicité", "address": "107 Rue de Rivoli, 75001 Paris", "type": "Publicité", "latitude": 48.8625, "longitude": 2.3365},
    {"name": "Musée des Lunettes et Lorgnettes", "address": "1 Rue Moret, 75011 Paris", "type": "Insolite", "latitude": 48.8672, "longitude": 2.3790},
    {"name": "Musée de l’Histoire de France", "address": "60 Rue de Birague, 75004 Paris", "type": "Histoire", "latitude": 48.8560, "longitude": 2.3640},
    {"name": "Musée de la Préfecture de Police", "address": "4 Rue de la Montagne Sainte-Geneviève, 75005 Paris", "type": "Histoire", "latitude": 48.8498, "longitude": 2.3475},
    {"name": "Musée de la Franc-Maçonnerie", "address": "16 Rue Cadet, 75009 Paris", "type": "Histoire", "latitude": 48.8758, "longitude": 2.3432},
    {"name": "Musée de l’Érotisme", "address": "72 Boulevard de Clichy, 75018 Paris", "type": "Insolite", "latitude": 48.8834, "longitude": 2.3370},
    {"name": "Musée de la Chocolaterie", "address": "12 Boulevard Bonne Nouvelle, 75010 Paris", "type": "Insolite", "latitude": 48.8705, "longitude": 2.3518},
    {"name": "Musée des Arts Forains", "address": "53 Avenue des Terroirs de France, 75012 Paris", "type": "Insolite", "latitude": 48.8325, "longitude": 2.3880},
    {"name": "Musée Dapper", "address": "35 Bis Rue Paul Valéry, 75016 Paris", "type": "Art Africain", "latitude": 48.8708, "longitude": 2.2885},
    {"name": "Musée de l’Institut du Monde Arabe", "address": "1 Rue des Fossés Saint-Bernard, 75005 Paris", "type": "Art Arabe", "latitude": 48.8490, "longitude": 2.3572},
    {"name": "Musée de la Légion d’Honneur", "address": "2 Rue de la Légion d’Honneur, 75007 Paris", "type": "Histoire", "latitude": 48.8605, "longitude": 2.3245},
    {"name": "Musée Pasteur", "address": "25 Rue du Docteur Roux, 75015 Paris", "type": "Science", "latitude": 48.8400, "longitude": 2.3110}
]

class Musee:
    def __init__(self, nom, adresse, type_musee, latitude, longitude):
        self.nom = nom
        self.adresse = adresse
        self.type_musee = type_musee
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.nom} ({self.type_musee}) - {self.adresse}"


class RecommandeurMusees:
    def __init__(self):
        self.musees = [Musee(**m) for m in paris_museums]

    def recommander(self, type_prefere):
        """Recommande des musées selon le type préféré."""
        recommandations = [m for m in self.musees if type_prefere.lower() in m.type_musee.lower()]
        return recommandations if recommandations else "Aucun musée correspondant trouvé."


# Cellule 2 : Programme principal

def main():
    recommandeur = RecommandeurMusees()
    type_prefere = input("Quel type de musée préférez-vous (ex. Art, Histoire, Science) ? ")
    print("\n--- Recommandations ---")
    recommandations = recommandeur.recommander(type_prefere)
    if isinstance(recommandations, str):
        print(recommandations)
    else:
        for musee in recommandations:
            print(musee)


# Cellule 3 : Exécuter
