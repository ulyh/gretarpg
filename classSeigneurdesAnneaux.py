#-------------------------------------------------------------------------------
# Name:        classSDA
# Author:      h
# Created:     04/06/2021
#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-

##################################################################
# création d'une liste de personnages humains
dicohuman = {}
with open("human.txt") as filehuman:
    for i in filehuman:
        key, value = i.split(sep="::")
        dicohuman[key] = value

listhuman = []
for key in dicohuman.keys():
    listhuman.append(key)
#print(listhuman)

# création d'une liste de personnages orques
listorc = []
with open("orc.txt") as fileorc:
    for i in fileorc:
        for element in i.split():
            listorc.append(element)
#print("orques :",listorc)

# création d'une liste de personnages nains
diconain ={}
with open("nain.txt") as filenain:
    count = 0
    for ligne in filenain:
        if count % 2 == 0:
            key, value = ligne.split("eest")
            diconain[key] = value
        count += 1
listnain = []
for key in diconain.keys():
    listnain.append(key)
#print(listnain)

# création d'une liste de personnages hobbits
dicohobbit = {}
with open("hobbit.txt") as filehobbit:
    for ligne in filehobbit:
        key, value = ligne.split("..")
        dicohobbit[key] = value
listhobbit = []
for key in dicohobbit.keys():
    listhobbit.append(key)
#print(listhobbit)

# création d'une liste de personnages maiars
dicomaiar = {}
with open("maiar.txt") as filemaiar:
    for ligne in filemaiar:
        key, value = ligne.split(",")
        dicomaiar[key] = value
listmaiar = []
for key in dicomaiar.keys():
    listmaiar.append(key)
#print(listmaiar)
######################################################################

def arrondi(arg):
    """donne l'arrondi à l'entier le plus proche"""
    arr = 0
    if arg >= int(arg)+ 0.5:
        arr = int(arg) + 1
    else:
        arr = int(arg)
    return arr

class Maiar():
    """Création de la "race" Maiar
    Gandalf est un maiar"""

    # constructeur
    def __init__(self):
        self.race = "Maiar"
        self.force = 150
        self.endurance = 90
        self.rapidite = 120
        self.intelligence = 150
        self.agilite = 130


class Elfe():
    """Création de la "race" Elfe"""

    # constructeur
    def __init__(self):
        self.race = "Elfe"
        self.force = 70
        self.endurance = 60
        self.rapidite = 100
        self.intelligence = 90
        self.agilite = 100


class Humain():
    """Création de la "race" Humain"""

    # constructeur
    def __init__(self):
        self.race = "Humain"
        self.force = 80
        self.endurance = 70
        self.rapidite = 70
        self.intelligence = 100
        self.agilite = 70


class Hobbit():
    """Création de la "race" Hobbit"""

    # constructeur
    def __init__(self):
        self.race = "Hobbit"
        self.force = 65
        self.endurance = 75
        self.rapidite = 85
        self.intelligence = 80
        self.agilite = 60


class Nain():
    """Création de la "race" Nain"""

    # constructeur
    def __init__(self):
        self.race = "Nain"
        self.force = 50
        self.endurance = 50
        self.rapidite = 55
        self.intelligence = 40
        self.agilite = 60

class Orque():
    """Création de la "race" Orque"""

    # constructeur
    def __init__(self):
        self.race = "Orque"
        self.force = 100
        self.endurance = 25
        self.rapidite = 10
        self.intelligence = 20
        self.agilite = 30




class MagicienElfe(Elfe):
    """Création du type magicien elfique"""

    # constructeur
    def __init__(self):
        # Héritage
        Elfe.__init__(self)

        self.pointsmagie = 100

    def FaireMagie(self, ptsmagie):
        """Effectue un tour de magie pour soigner"""
        if self.pointsmagie - ptsmagie >= 0:
            self.magie = arrondi(self.intelligence * 0.1 + self.force * 0.005 + \
            self.agilite * 0.05 + ptsmagie)

            self.pointsmagie = self.pointsmagie - ptsmagie
            return self.magie
        else:
            print("Points de magie insuffisant. {} possède {} points de magie."\
            .format(self.nom, self.pointsmagie))
            return None

    def Soigner(self, autrePersonnage, pointsmagie):
        """Soigne l'autrePersonnage en lui apportant des points de vie"""
        if self.Etat() and autrePersonnage.Etat():
            if autrePersonnage.vie == autrePersonnage.viedefaut:
                print("{} n'a pas besoin d'être soigné.".format(autrePersonnage.nom))
            elif self.FaireMagie(pointsmagie):
                autrePersonnage.vie = autrePersonnage.vie + self.magie
                if autrePersonnage.vie > autrePersonnage.viedefaut:
                    autrePersonnage.vie = autrePersonnage.viedefaut
                print("{0} soigne {1} et lui fournit {2} points de vie"\
                .format(self.nom, autrePersonnage.nom, self.magie))
                # affiche le nbre de points de vie gagnés lors du soin
                autrePersonnage.AugmenterVie(self.magie)
            else:
                print("zut! ya plus de magie!")

        elif autrePersonnage.Etat():
            print("{} est mort et donc ne peut pas soigner {}".format(self.nom,
            autrePersonnage.nom))

        else:
            print("{} est mort et donc ne peut être soigné.".format(autrePersonnage.nom))

class MagicienMaiar(Maiar):
    """Création du type magicien maiaresque"""

    # constructeur
    def __init__(self):
        # Héritage
        Maiar.__init__(self)

        self.pointsmagie = 100

    def FaireMagie(self, ptsmagie):
        """Effectue un tour de magie pour soigner"""
        if self.pointsmagie - ptsmagie >= 0:
            self.magie = arrondi(self.intelligence * 0.1 + self.force * 0.005 + \
            self.agilite * 0.05 + ptsmagie)

            self.pointsmagie = self.pointsmagie - ptsmagie
            return self.magie
        else:
            print("Points de magie insuffisant. {0} possède {1} points de magie."\
            .format(self.nom, self.pointsmagie))
            return None

    def Soigner(self, autrePersonnage, pointsmagie):
        """Soigne l'autrePersonnage en lui apportant des points de vie"""
        if self.Etat() and autrePersonnage.Etat():
            if autrePersonnage.vie == autrePersonnage.viedefaut:
                print("{} n'a pas besoin d'être soigné.".format(autrePersonnage.nom))
            elif self.FaireMagie(pointsmagie):
                autrePersonnage.vie = autrePersonnage.vie + self.magie
                if autrePersonnage.vie > autrePersonnage.viedefaut:
                    autrePersonnage.vie = autrePersonnage.viedefaut
                print("{0} soigne {1} et lui fournit {2} points de vie"\
                .format(self.nom, autrePersonnage.nom, self.magie))
                # affiche le nbre de points de vie gagnés lors du soin
                autrePersonnage.AugmenterVie(self.magie)
            else:
                print("zut! ya plus de magie!")

        elif autrePersonnage.Etat():
            print("{} est mort et donc ne peut pas soigner {}".format(self.nom,
            autrePersonnage.nom))

        else:
            print("{} est mort et donc ne peut être soigné.".format(autrePersonnage.nom))


##################### création des personnages ##########################
class PersonnageElfe(MagicienElfe, Elfe):
    """Création du personnage elfique"""

    # constructeur
    def __init__(self, vie, nom="Arwen"):

        # Héritage
        MagicienElfe.__init__(self)
        Elfe.__init__(self)

        self.estVivant = True
        self.nom = nom
        self.vie = vie
        self.viedefaut = vie
        self.pointsdegats = 0

        self.Caracteristiques()

    def Etat(self):
        """Bouléen sur la vitalité du personnage"""
        return self.estVivant

    def NiveauVie(self):
        if self.Etat():
            print("{1}, de race {2}, possède actuellement {0} points de vie."\
        .format(self.vie, self.nom, self.race))
        else:
            print("{} est mort.".format(self.nom))

    def Caracteristiques(self):
        """Affiche les caractéristiques du personnage"""
        print("-"*10,"Les caractéristiques du personnage","-"*10)
        print("Nom : {0}\nRace : {1}\nForce : {2}\nEndurance : {3}\
        \nRapidité : {4}\nIntelligence : {5}\nAgilité : {6}".format(self.nom,
        self.race, self.force, self.endurance, self.rapidite, self.intelligence,
        self.agilite))

    def DiminuerVie(self, ptspedus):
        if self.Etat():
            if ptsperdus > 0:
                print("Attention {0} a subi une attaque et a perdu {1} points de vie."\
                .format(self.nom, ptsperdus))
                print("{0} a maintenant {1} points de vie".format(self.nom, self.vie))

            else:
                print("{} n'a reçu aucune attaque".format(self.nom))

        else:
            print("{} y succombe.".format(self.nom))
            print("GAME OVER")


    def AugmenterVie(self, ptsdonnes):
        if self.Etat():
            if ptsdonnes > 0:
                print("{0} a été soigné et a maintenant {1} points de vie."\
                .format(self.nom, self.vie))
            else:
                print("{} n'a reçu aucun soin".format(self.nom))
        else:
            print("{} est mort !".format(self.nom))



    def Offensive(self, autrePersonnage):
        """Attaque de autrePersonnage sur self"""
        if self.race == autrePersonnage.race:
            if not self.estVivant or not autrePersonnage.estVivant:
                print("Difficile de combattre qui que ce soit en étant mort !")

            print("Combat impossible entre les membres d'une même famille.")
            print("{0} et {1} sont tous deux des {2}s"\
            .format(self.nom, autrePersonnage.nom, self.race))

        elif self.Etat() and autrePersonnage.Etat():
            if arrondi(self.rapidite * 1.2) > autrePersonnage.force:
                print("{0} esquive l'attaque de {1}."\
                .format(self.nom, autrePersonnage.nom))
                print("Avec {0} de rapidité face à {3} de force de {2}, {1} échappe à l'attaque de {2}"\
                .format(self.rapidite, self.nom, autrePersonnage.nom, autrePersonnage.force))
            else:
                self.pointsdegats = arrondi(0.6 * autrePersonnage.force)
                if self.pointsdegats <= self.vie:
                    self.vie = self.vie - self.pointsdegats
                    # affiche le nbre de points vie perdus lors du combat
                    self.DiminuerVie(self.pointsdegats)
                else:
                    self.vie = 0
                    self.estVivant = False
                    print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
                    autrePersonnage.nom, self.pointsdegats))
                    self.DiminuerVie(self.pointsdegats)

        elif autrePersonnage.Etat():
            print("{} est déjà mort. Inutile de s'acharner !".format(self.nom))
        else:
            print("{} est mort. Difficile pour ce personnage d'attaquer qui que ce soit !"\
            .format(autrePersonnage.nom))


class PersonnageMaiar(MagicienMaiar, Maiar):
    """Création du personnage """

    # constructeur
    def __init__(self, vie, nom="Gandalf"):

        # Héritage
        MagicienMaiar.__init__(self)
        Maiar.__init__(self)

        self.estVivant = True
        self.nom = nom
        self.vie = vie
        self.viedefaut = vie
        self.pointsdegats = 0

        self.Caracteristiques()

    def Etat(self):
        """Bouléen sur la vitalité du personnage"""
        return self.estVivant

    def NiveauVie(self):
        if self.Etat():
            print("{1}, de race {2}, possède actuellement {0} points de vie."\
        .format(self.vie, self.nom, self.race))
        else:
            print("{} est mort.".format(self.nom))

    def Caracteristiques(self):
        """Affiche les caractéristiques du personnage"""
        print("-"*10,"Les caractéristiques du personnage","-"*10)
        print("Nom : {0}\nRace : {1}\nForce : {2}\nEndurance : {3}\
        \nRapidité : {4}\nIntelligence : {5}\nAgilité : {6}".format(self.nom,
        self.race, self.force, self.endurance, self.rapidite, self.intelligence,
        self.agilite))

    def DiminuerVie(self, ptspedus):
        if self.Etat():
            if ptsperdus > 0:
                print("Attention {0} a subi une attaque et a perdu {1} points de vie."\
                .format(self.nom, ptsperdus))
                print("{0} a maintenant {1} points de vie".format(self.nom, self.vie))

            else:
                print("{} n'a reçu aucune attaque".format(self.nom))

        else:
            print("{} y succombe.".format(self.nom))
            print("GAME OVER")


    def AugmenterVie(self, ptsdonnes):
        if self.Etat():
            if ptsdonnes > 0:
                print("{0} a été soigné et a maintenant {1} points de vie."\
                .format(self.nom, self.vie))
            else:
                print("{} n'a reçu aucun soin".format(self.nom))
        else:
            print("{} est mort !".format(self.nom))



    def Offensive(self, autrePersonnage):
        """Attaque de autrePersonnage sur self"""
        if self.race == autrePersonnage.race:
            if not self.estVivant or not autrePersonnage.estVivant:
                print("Difficile de combattre qui que ce soit en étant mort !")

            print("Combat impossible entre les membres d'une même famille.")
            print("{0} et {1} sont tous deux des {2}s"\
            .format(self.nom, autrePersonnage.nom, self.race))

        elif self.Etat() and autrePersonnage.Etat():
            if arrondi(self.rapidite * 1.2) > autrePersonnage.force:
                print("{0} esquive l'attaque de {1}."\
                .format(self.nom, autrePersonnage.nom))
                print("Avec {0} de rapidité face à {3} de force de {2}, {1} échappe à l'attaque de {2}"\
                .format(self.rapidite, self.nom, autrePersonnage.nom, autrePersonnage.force))
            else:
                self.pointsdegats = arrondi(0.6 * autrePersonnage.force)
                if self.pointsdegats <= self.vie:
                    self.vie = self.vie - self.pointsdegats
                    # affiche le nbre de points vie perdus lors du combat
                    self.DiminuerVie(self.pointsdegats)
                else:
                    self.vie = 0
                    self.estVivant = False
                    print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
                    autrePersonnage.nom, self.pointsdegats))
                    self.DiminuerVie(self.pointsdegats)

        elif autrePersonnage.Etat():
            print("{0} est déjà mort. Inutile de s'acharner !".format(self.nom))
        else:
            print("{0} est mort. Difficile pour ce personnage d'attaquer qui que ce soit !"\
            .format(autrePersonnage.nom))



class PersonnageHumain(Humain):
    """Création du personnage combatif humain
    Héritage : Humain """

    # constructeur
    def __init__(self, vie, nom="Aragorn"):
        # Héritage
        Humain.__init__(self)

        self.estVivant = True
        self.nom = nom
        self.vie = vie
        self.viedefaut = vie
        self.pointsdegats = 0

        self.Caracteristiques()

    def Etat(self):
        """Bouléen sur la vitalité du personnage"""
        return self.estVivant

    def NiveauVie(self):
        if self.Etat():
            print("{1}, de race {2}, possède actuellement {0} points de vie."\
        .format(self.vie, self.nom, self.race))
        else:
            print("{} est mort.".format(self.nom))

    def Caracteristiques(self):
        """Affiche les caractéristiques du personnage"""
        print("-"*10,"Les caractéristiques du personnage","-"*10)
        print("Nom : {0}\nRace : {1}\nForce : {2}\nEndurance : {3}\
        \nRapidité : {4}\nIntelligence : {5}\nAgilité : {6}".format(self.nom,
        self.race, self.force, self.endurance, self.rapidite, self.intelligence,
        self.agilite))

    def DiminuerVie(self, ptsperdus):
        if self.Etat():
            if ptsperdus > 0:
                print("Attention {0} a subi une attaque et a perdu {1} points de vie."\
                .format(self.nom, ptsperdus))
                print("{0} a maintenant {1} points de vie".format(self.nom, self.vie))

            else:
                print("{0} n'a reçu aucune attaque".format(self.nom))

        else:
            print("{} y succombe.".format(self.nom))
            print("GAME OVER")


    def AugmenterVie(self, ptsdonnes):
        if self.Etat():
            if ptsdonnes > 0:
                print("{0} a été soigné et a maintenant {1} points de vie."\
                .format(self.nom, self.vie))
            else:
                print("{} n'a reçu aucun soin".format(self.nom))
        else:
            print("{} est mort !".format(self.nom))


    def Offensive(self, autrePersonnage):
        """Attaque de autrePersonnage sur self"""
        if self.race == autrePersonnage.race:
            if not self.estVivant or not autrePersonnage.estVivant:
                print("Difficile de combattre qui que ce soit en étant mort !")

            print("Combat impossible entre les membres d'une même famille.")
            print("{0} et {1} sont tous deux des {2}s"\
            .format(self.nom, autrePersonnage.nom, self.race))

        elif self.Etat() and autrePersonnage.Etat():
            if arrondi(self.rapidite * 1.2) > autrePersonnage.force:
                print("{0} esquive l'attaque de {1}."\
                .format(self.nom, autrePersonnage.nom))
                print("Avec {0} de rapidité face à {3} de force de {2}, {1} échappe à l'attaque de {2}"\
                .format(self.rapidite, self.nom, autrePersonnage.nom, autrePersonnage.force))
            else:
                self.pointsdegats = arrondi(0.6 * autrePersonnage.force)
                if self.pointsdegats <= self.vie:
                    self.vie = self.vie - self.pointsdegats
                    # affiche le nbre de points vie perdus lors du combat
                    self.DiminuerVie(self.pointsdegats)
                else:
                    self.vie = 0
                    self.estVivant = False
                    print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
                    autrePersonnage.nom, self.pointsdegats))
                    self.DiminuerVie(self.pointsdegats)

        elif autrePersonnage.Etat():
            print("{} est déjà mort. Inutile de s'acharner !".format(self.nom))
        else:
            print("{} est mort. Difficile pour ce personnage d'attaquer qui que ce soit !"\
            .format(autrePersonnage.nom))



class PersonnageOrque(Orque):
    """Création du personnage combatif orquesque
    Héritage : Orque """

    # constructeur
    def __init__(self, vie, nom="Azog"):
        # Héritage
        Orque.__init__(self)

        self.estVivant = True
        self.nom = nom
        self.vie = vie
        self.viedefaut = vie
        self.pointsdegats = 0

        self.Caracteristiques()

    def Etat(self):
        """Bouléen sur la vitalité du personnage"""
        return self.estVivant

    def NiveauVie(self):
        if self.Etat():
            print("{1}, de race {2}, possède actuellement {0} points de vie."\
        .format(self.vie, self.nom, self.race))
        else:
            print("{} est mort.".format(self.nom))

    def Caracteristiques(self):
        """Affiche les caractéristiques du personnage"""
        print("-"*10,"Les caractéristiques du personnage","-"*10)
        print("Nom : {0}\nRace : {1}\nForce : {2}\nEndurance : {3}\
        \nRapidité : {4}\nIntelligence : {5}\nAgilité : {6}".format(self.nom,
        self.race, self.force, self.endurance, self.rapidite, self.intelligence,
        self.agilite))

    def DiminuerVie(self, ptspedus):
        if self.Etat():
            if ptsperdus > 0:
                print("Attention {0} a subi une attaque et a perdu {1} points de vie."\
                .format(self.nom, ptsperdus))
                print("{0} a maintenant {1} points de vie".format(self.nom, self.vie))

            else:
                print("{} n'a reçu aucune attaque".format(self.nom))

        else:
            print("{} y succombe.".format(self.nom))
            print("GAME OVER")

    def AugmenterVie(self, ptsdonnes):
        if self.Etat():
            if ptsdonnes > 0:
                print("{0} a été soigné et a maintenant {1} points de vie."\
                .format(self.nom, self.vie))
            else:
                print("{} n'a reçu aucun soin".format(self.nom))
        else:
            print("{} est mort !".format(self.nom))
            print("{} ne peut pas être soigné.".format(self.nom))



    def Offensive(self, autrePersonnage):
        """Attaque de autrePersonnage sur self"""
        if self.race == autrePersonnage.race:
            if not self.estVivant or not autrePersonnage.estVivant:
                print("Difficile de combattre qui que ce soit en étant mort !")

            print("Combat impossible entre les membres d'une même famille.")
            print("{0} et {1} sont tous deux des {2}s"\
            .format(self.nom, autrePersonnage.nom, self.race))

        elif self.Etat() and autrePersonnage.Etat():
            if arrondi(self.rapidite * 1.2) > autrePersonnage.force:
                print("{0} esquive l'attaque de {1}."\
                .format(self.nom, autrePersonnage.nom))
                print("Avec {0} de rapidité face à {3} de force de {2}, {1} échappe à l'attaque de {2}"\
                .format(self.rapidite, self.nom, autrePersonnage.nom, autrePersonnage.force))
            else:
                self.pointsdegats = arrondi(0.6 * autrePersonnage.force)
                if self.pointsdegats <= self.vie:
                    self.vie = self.vie - self.pointsdegats
                    # affiche le nbre de points vie perdus lors du combat
                    self.DiminuerVie(self.pointsdegats)
                else:
                    self.vie = 0
                    self.estVivant = False
                    print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
                    autrePersonnage.nom, self.pointsdegats))
                    self.DiminuerVie(self.pointsdegats)

        elif autrePersonnage.Etat():
            print("{} est déjà mort. Inutile de s'acharner !".format(self.nom))
        else:
            print("{} est mort. Difficile pour ce personnage d'attaquer qui que ce soit !"\
            .format(autrePersonnage.nom))

class PersonnageHobbit(Hobbit):
    """Création du personnage combatif hobbitique
    Héritage : Hobbit """

    # constructeur
    def __init__(self, vie, nom="Frodon"):
        # Héritage
        Hobbit.__init__(self)

        self.estVivant = True
        self.nom = nom
        self.vie = vie
        self.viedefaut = vie
        self.pointsdegats = 0

        self.Caracteristiques()

    def Etat(self):
        """Bouléen sur la vitalité du personnage"""
        return self.estVivant

    def NiveauVie(self):
        if self.Etat():
            print("{1}, de race {2}, possède actuellement {0} points de vie."\
        .format(self.vie, self.nom, self.race))
        else:
            print("{} est mort.".format(self.nom))

    def Caracteristiques(self):
        """Affiche les caractéristiques du personnage"""
        print("-"*10,"Les caractéristiques du personnage","-"*10)
        print("Nom : {0}\nRace : {1}\nForce : {2}\nEndurance : {3}\
        \nRapidité : {4}\nIntelligence : {5}\nAgilité : {6}".format(self.nom,
        self.race, self.force, self.endurance, self.rapidite, self.intelligence,
        self.agilite))

    def DiminuerVie(self, ptspedus):
        if self.Etat():
            if ptsperdus > 0:
                print("Attention {0} a subi une attaque et a perdu {1} points de vie."\
                .format(self.nom, ptsperdus))
                print("{0} a maintenant {1} points de vie".format(self.nom, self.vie))

            else:
                print("{} n'a reçu aucune attaque".format(self.nom))

        else:
            print("{} y succombe.".format(self.nom))
            print("GAME OVER")


    def AugmenterVie(self, ptsdonnes):
        if self.Etat():
            if ptsdonnes > 0:
                print("{0} a été soigné et a maintenant {1} points de vie."\
                .format(self.nom, self.vie))
            else:
                print("{} n'a reçu aucun soin".format(self.nom))
        else:
            print("{} est mort !".format(self.nom))



    def Offensive(self, autrePersonnage):
        """Attaque de autrePersonnage sur self"""
        if self.race == autrePersonnage.race:
            if not self.estVivant or not autrePersonnage.estVivant:
                print("Difficile de combattre qui que ce soit en étant mort !")

            print("Combat impossible entre les membres d'une même famille.")
            print("{0} et {1} sont tous deux des {2}s"\
            .format(self.nom, autrePersonnage.nom, self.race))

        elif self.Etat() and autrePersonnage.Etat():
            if arrondi(self.rapidite * 1.2) > autrePersonnage.force:
                print("{0} esquive l'attaque de {1}."\
                .format(self.nom, autrePersonnage.nom))
                print("Avec {0} de rapidité face à {3} de force de {2}, {1} échappe à l'attaque de {2}"\
                .format(self.rapidite, self.nom, autrePersonnage.nom, autrePersonnage.force))
            else:
                self.pointsdegats = arrondi(0.6 * autrePersonnage.force)
                if self.pointsdegats <= self.vie:
                    self.vie = self.vie - self.pointsdegats
                    # affiche le nbre de points vie perdus lors du combat
                    self.DiminuerVie(self.pointsdegats)
                else:
                    self.vie = 0
                    self.estVivant = False
                    print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
                    autrePersonnage.nom, self.pointsdegats))
                    self.DiminuerVie(self.pointsdegats)

        elif autrePersonnage.Etat():
            print("{} est déjà mort. Inutile de s'acharner !".format(self.nom))
        else:
            print("{} est mort. Difficile pour ce personnage d'attaquer qui que ce soit !"\
            .format(autrePersonnage.nom))

class PersonnageNain(Nain):
    """Création du personnage combatif nainesque
    Héritage : Nain """

    # constructeur
    def __init__(self, vie, nom="Thorin II"):
        # Héritage
        Nain.__init__(self)

        self.estVivant = True
        self.nom = nom
        self.vie = vie
        self.viedefaut = vie
        self.pointsdegats = 0

        self.Caracteristiques()

    def Etat(self):
        """Bouléen sur la vitalité du personnage"""
        return self.estVivant

    def NiveauVie(self):
        if self.Etat():
            print("{1}, de race {2}, possède actuellement {0} points de vie."\
        .format(self.vie, self.nom, self.race))
        else:
            print("{} est mort.".format(self.nom))

    def Caracteristiques(self):
        """Affiche les caractéristiques du personnage"""
        print("-"*10,"Les caractéristiques du personnage","-"*10)
        print("Nom : {0}\nRace : {1}\nForce : {2}\nEndurance : {3}\
        \nRapidité : {4}\nIntelligence : {5}\nAgilité : {6}".format(self.nom,
        self.race, self.force, self.endurance, self.rapidite, self.intelligence,
        self.agilite))

    def DiminuerVie(self, ptspedus):
        if self.Etat():
            if ptsperdus > 0:
                print("Attention {0} a subi une attaque et a perdu {1} points de vie."\
                .format(self.nom, ptsperdus))
                print("{0} a maintenant {1} points de vie".format(self.nom, self.vie))

            else:
                print("{} n'a reçu aucune attaque".format(self.nom))

        else:
            print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
            autrePersonnage.nom, self.pointsdegats))
            print("{} y succombe.".format(self.nom))
            print("GAME OVER")


    def AugmenterVie(self, ptsdonnes):
        if self.Etat():
            if ptsdonnes > 0:
                print("{0} a été soigné et a maintenant {1} points de vie."\
                .format(self.nom, self.vie))
            else:
                print("{} n'a reçu aucun soin".format(self.nom))
        else:
            print("{} est mort !".format(self.nom))



    def Offensive(self, autrePersonnage):
        """Attaque de autrePersonnage sur self"""
        if self.race == autrePersonnage.race:
            if not self.estVivant or not autrePersonnage.estVivant:
                print("Difficile de combattre qui que ce soit en étant mort !")

            print("Combat impossible entre les membres d'une même famille.")
            print("{0} et {1} sont tous deux des {2}s"\
            .format(self.nom, autrePersonnage.nom, self.race))

        elif self.Etat() and autrePersonnage.Etat():
            if arrondi(self.rapidite * 1.2) > autrePersonnage.force:
                print("{0} esquive l'attaque de {1}."\
                .format(self.nom, autrePersonnage.nom))
                print("Avec {0} de rapidité face à {3} de force de {2}, {1} échappe à l'attaque de {2}"\
                .format(self.rapidite, self.nom, autrePersonnage.nom, autrePersonnage.force))
            else:
                self.pointsdegats = arrondi(0.6 * autrePersonnage.force)
                if self.pointsdegats <= self.vie:
                    self.vie = self.vie - self.pointsdegats
                    # affiche le nbre de points vie perdus lors du combat
                    self.DiminuerVie(self.pointsdegats)
                else:
                    self.vie = 0
                    self.estVivant = False
                    print("{1} a lancé une attaque de {2} points sur {0}.".format(self.nom,
                    autrePersonnage.nom, self.pointsdegats))
                    self.DiminuerVie(self.pointsdegats)

        elif autrePersonnage.Etat():
            print("{} est déjà mort. Inutile de s'acharner !".format(self.nom))
        else:
            print("{} est mort. Difficile pour ce personnage d'attaquer qui que ce soit !"\
            .format(autrePersonnage.nom))



#--- Programme principal -------------------------------------------------------



# listes de noms des personnages
listhuman
listhobbit
listmaiar
listnain
listorc

if __name__ == '__main__':

    Gandalf = PersonnageMaiar(100)
    Sauron = PersonnageMaiar(100, "Sauron")

    Aragorn = PersonnageHumain(180)
    Arwen = PersonnageElfe(100)
    Frodon = PersonnageHobbit(100)
    ThoronII = PersonnageNain(100)
    Azog = PersonnageOrque(120)
    Orc = PersonnageOrque(120, "Orc")


## combat entre Aragorn et Sauron
    Aragorn.Offensive(Sauron)
    Gandalf.Soigner(Aragorn, 10)
    Aragorn.Offensive(Sauron)
    Sauron.Offensive(Aragorn)
    Aragorn.Offensive(Sauron)
    Aragorn.Offensive(Sauron)
