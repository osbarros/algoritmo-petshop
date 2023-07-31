import unittest
from datetime import datetime
from main import MeuCaninoFeliz, VaiRex, ChowChawgas, define_melhor_pet_shop, verifica_se_eh_final_de_semana

class TestMelhorPetShop(unittest.TestCase):

    def test_melhor_pet_shop_semana_1(self):
        # Teste para dias de semana
        data_inserida = "31/07/2023"  # Uma segunda-feira
        final_de_semana = verifica_se_eh_final_de_semana(data_inserida)
        num_cachorros_pequenos = 2
        num_cachorros_grandes = 3

        meu_canino_feliz = MeuCaninoFeliz()
        meu_canino_feliz.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        vai_rex = VaiRex()
        vai_rex.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        chow_chawgas = ChowChawgas()
        chow_chawgas.calcula_valor(num_cachorros_pequenos, num_cachorros_grandes)

        melhor_pet_shop = define_melhor_pet_shop(meu_canino_feliz, vai_rex, chow_chawgas)

        self.assertEqual(melhor_pet_shop.nome, "Meu Canino Feliz")

    def test_melhor_pet_shop_semana_2(self):
        # Teste para dias de semana
        data_inserida = "31/07/2023"  # Uma segunda-feira
        final_de_semana = verifica_se_eh_final_de_semana(data_inserida)
        num_cachorros_pequenos = 6
        num_cachorros_grandes = 2

        meu_canino_feliz = MeuCaninoFeliz()
        meu_canino_feliz.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        vai_rex = VaiRex()
        vai_rex.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        chow_chawgas = ChowChawgas()
        chow_chawgas.calcula_valor(num_cachorros_pequenos, num_cachorros_grandes)

        melhor_pet_shop = define_melhor_pet_shop(meu_canino_feliz, vai_rex, chow_chawgas)

        self.assertEqual(melhor_pet_shop.nome, "Vai Rex")

    def test_melhor_pet_shop_final_semana_1(self):
        # Teste para final de semana
        data_inserida = "30/07/2023"  # Um domingo
        final_de_semana = verifica_se_eh_final_de_semana(data_inserida)
        num_cachorros_pequenos = 10
        num_cachorros_grandes = 2

        meu_canino_feliz = MeuCaninoFeliz()
        meu_canino_feliz.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        vai_rex = VaiRex()
        vai_rex.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        chow_chawgas = ChowChawgas()
        chow_chawgas.calcula_valor(num_cachorros_pequenos, num_cachorros_grandes)

        melhor_pet_shop = define_melhor_pet_shop(meu_canino_feliz, vai_rex, chow_chawgas)

        self.assertEqual(melhor_pet_shop.nome, "Vai Rex")


    def test_melhor_pet_shop_final_semana_2(self):
        # Teste para final de semana
        data_inserida = "30/07/2023"  # Um domingo
        final_de_semana = verifica_se_eh_final_de_semana(data_inserida)
        num_cachorros_pequenos = 0
        num_cachorros_grandes = 1

        meu_canino_feliz = MeuCaninoFeliz()
        meu_canino_feliz.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        vai_rex = VaiRex()
        vai_rex.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        chow_chawgas = ChowChawgas()
        chow_chawgas.calcula_valor(num_cachorros_pequenos, num_cachorros_grandes)

        melhor_pet_shop = define_melhor_pet_shop(meu_canino_feliz, vai_rex, chow_chawgas)

        self.assertEqual(melhor_pet_shop.nome, "ChowChawgas")

    def test_melhor_pet_shop_mesmo_preco(self):
    
        data_inserida = "31/07/2023"  # Uma segunda-feira
        final_de_semana = verifica_se_eh_final_de_semana(data_inserida)
        num_cachorros_pequenos = 4
        num_cachorros_grandes = 2

        #O preço em ambos os petshops "Meu Canino Feliz" e "Vai Rex" dão 160 reais
        #O melhor pet shop deve ser, então, o Vai Rex, que é mais perto do canil

        meu_canino_feliz = MeuCaninoFeliz()
        meu_canino_feliz.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        vai_rex = VaiRex()
        vai_rex.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

        chow_chawgas = ChowChawgas()
        chow_chawgas.calcula_valor(num_cachorros_pequenos, num_cachorros_grandes)

        melhor_pet_shop = define_melhor_pet_shop(meu_canino_feliz, vai_rex, chow_chawgas)

        self.assertEqual(melhor_pet_shop.nome, "Vai Rex")

if __name__ == "__main__":
    unittest.main()
