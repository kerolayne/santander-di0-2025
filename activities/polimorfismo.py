class ave:
    def voar(self):
        print("A ave está voando!")

class papagaio(ave):
    def voar(self):
        return super().voar()
    
class galinha(ave):
    def voar(self):
        print("A galinha não voa muito bem!")

class avião(ave):
    def voar(self):
        print("O avião está voando alto!")


def plano_voo(ave_obj):
    if isinstance(ave_obj, ave):
        ave_obj.voar()
    else:
        print("O objeto não é uma ave.")


plano_voo(papagaio())
plano_voo(galinha())
plano_voo(avião())