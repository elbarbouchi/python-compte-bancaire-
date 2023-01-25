import uuid
from abc import ABC

class Compte(ABC):
    """
         Abstract class Compte
    """
    def __init__(self, nom_Proprietaire,numero_compte, solde,  **kwargs) :
        self.nom_proprietaire = nom_Proprietaire
        self.numero_compte = numero_compte
        self.solde = solde
    def retrait (self, montant):
        self.solde -= montant
    def versement (self, montant) :
        if montant <= 0:
            raise Exception
        self.solde += montant
    def afficher_solde(self): # pragma : no cover
           pass
    def __repr__(self): return f"compteCourant - solde :{self.solde}"
class CompteCourant(Compte):
    def __init__(self, numero_compte, agios, montantmaxdecouvert, solde, nom_proprietaire, **kwargs):
        self.agios = agios
        self.montantmaxdecouvert = montantmaxdecouvert
        super().__init__(numero_compte, nom_proprietaire, solde)
    def appliquer_agios(self, montant):
        if self.solde < 0:
            self.solde -= montant*self.agios
class CompteEpargne(Compte):
    def __init__(self,numero_compte,interets, solde, nom_proprietaire, **kwargs):
        self.interets = interets
        super().__init__(numero_compte, nom_proprietaire, solde)
    def appliquer_interets(self):
        if self.montant > 0:
            self.solde = self.montant *(1 + (10/100))
        return self.solde

