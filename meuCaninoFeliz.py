from petShop import PetShop


class MeuCaninoFeliz(PetShop):
    def __init__(self):
        self._valor = None
        self._distancia = 2000
        self._nome = "Meu Canino Feliz"

    # Propriedade para o atributo valor
    @property
    def valor(self):
        return self._valor

    # Propriedade para o atributo distancia
    @property
    def distancia(self):
        return self._distancia

    # Propriedade para o atributo nome
    @property
    def nome(self):
        return self._nome

    def calcula_valor(self, final_de_semana, num_caes_pequenos, num_caes_grandes):
        if num_caes_pequenos < 0 or num_caes_grandes < 0:
            raise ValueError("O número de cães não pode ser negativo.")

        if final_de_semana:
            self._valor = (num_caes_pequenos * 24) + (num_caes_grandes * 48)
        else:
            self._valor = (num_caes_pequenos * 20) + (num_caes_grandes * 40)


