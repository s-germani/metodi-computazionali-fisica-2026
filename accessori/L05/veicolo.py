class Veicolo():
    """
    Classe per rappresentare i veicoli a ruote
    
    Parametri
    -------------------------------------------

    nome    : nome veicolo
    ruote   : numero ruote
    potenza : potenza motore 
    """
    
    def __init__(self, nome, ruote, potenza):
        self.nome    = nome
        self.ruote   = ruote
        self.potenza = potenza
        
    def __repr__(self):
        return 'Veicolo: {:} + {:} + {:}'.format(self.nome, self.ruote, self.potenza)
    
    def __str__(self):
        return 'Veicolo: {:} - {:} - {:}'.format(self.nome, self.ruote, self.potenza)
        
    def __eq__(self, other):
        return  self.ruote == other.ruote and self.potenza == other.potenza


    def __lt__(self, other):
        return self.potenza < other.potenza

    def __gt__(self, other):
        return self.potenza > other.potenza
    
    def minore(self, other):
        return self.potenza < other.potenza

    def descrizione():
        print('----------------------------------')
        print('Veicolo   {:}'.format(self.nome   ))        
        print('  ruote   {:}'.format(self.ruota  ))
        print('  potenza {:}'.format(self.potenza))
        print('----------------------------------')
