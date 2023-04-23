from random import randint

class Particule:
    """Classe définissant les attributs de particules et leurs méthodes associées"""

    def __init__(self, x, y, taille, xvitesse, yvitesse, masse, couleur):
        """Initialise un objet Particule

        :param x: (int) coordonnée x de la particule
        :param y: (int) coordonnée y de la particule
        :param taille: (int) rayon de la particule en pixel
        :param xvitesse: (int) vitesse horizontale de la particule
        :param yvitesse: (int) vitesse verticale de la particule
        :param masse: (int) masse virtuelle de la particule
        :param couleur: (tuple) tuple de 3 valeurs RGB en format décimal

        :return: (Particule) instance de la classe Particule"""
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.taille = taille
        self.xvitesse = xvitesse
        self.yvitesse = yvitesse
        self.masse = masse
        self.acceleration = 0
        self.couleur = couleur


    

    def changementCouleur(self, lst_particules):
        """Change la couleur de la particule en fonction du nombre de particule voisines

        :param lst_particules: (list) liste d'instances de la classe Particule

        :return: None"""
        particules_proches = 0

        for particule in lst_particules:
            d = distance(self, particule)
            if d < 45:
                particules_proches += 1
        
        r, g, b = 255, 0, 0

        g += 50 * particules_proches
        b += 10 * particules_proches

        g = min(255, g)
        b = min(255, b)

        self.couleur = (r, g, b)


    def calculeAcceleration(self, lst_particules, centre, attraction,
                            largeur, hauteur):
        """Calcule l'accéleration de la particule en fonction du centre de gravité (souris),
            mais gère aussi les actions liées aux boutons de la souris

            :param lst_particules: (list) liste d'instances de la classe Particule
            :param centre: (Particule) instance de la classe Particule correspondant au centre de gravité
            :param attraction: (tuple) tuple de booléen représentant l'état des boutons de la souris
            :param largeur: (int) largeur de l'écran en pixel
            :param hauteur: (int) hauteur de l'écran en pixel

            :return: None"""
        for particule in lst_particules:
            d = distance(self, particule)
            if d > 80:
                self.acceleration += (centre.masse  *
                                      self.masse / d**2) * .000005

                if attraction[0] == 1 :
                    dx = (centre.x - self.x) * 0.05
                    dy = (centre.y - self.y) * 0.05

                    self.xvitesse = self.xvitesse * 0.2 + dx
                    self.yvitesse = self.yvitesse * 0.2 + dy

                elif attraction[2] == 1 :
                    dx = randint(-8, 8)
                    dy = randint(-8, 8)

                    self.xvitesse = self.xvitesse * 0.5 + dx
                    self.yvitesse = self.yvitesse * 0.5 + dy

                else:
                    dx = (centre.x - self.x) * self.acceleration
                    dy = (centre.y - self.y) * self.acceleration

                    self.xvitesse += dx
                    self.yvitesse += dy

                if self.coords[0] > largeur or self.coords[0] < 0:
                    self.xvitesse = -(self.xvitesse)
                if self.coords[1] > hauteur or self.coords[1] < 0:
                    self.xvitesse = -(self.yvitesse)


    def mettreMouvement(self):
        """Met en mouvement la particule en ajoutant la valeur de sa vitesse 
        à ses coordonnées

        :return: None"""
        self.x += self.xvitesse
        self.y += self.yvitesse
        self.coords = (self.x, self.y)


def distance(a, b):
    """Renvoie la distance en pixel entre 2 particules

    :param a: (Particule) instance de la classe Particule
    :param b: (Particule) instance de la classe Particule

    :return: (float) Distance entre les 2 particules"""
    return ((b.x - a.x)**2 + (b.y - a.y)**2) ** .5



