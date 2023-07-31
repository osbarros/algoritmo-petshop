from datetime import datetime
from chowChawgas import ChowChawgas
from meuCaninoFeliz import MeuCaninoFeliz
from vaiRex import VaiRex
import sys


def verifica_se_eh_final_de_semana(data_str):

    try:
        # Converte a string da data para um objeto datetime
        data = datetime.strptime(data_str, '%d/%m/%Y')

        # Obtém o número do dia da semana (0 a 6, representando segunda-feira a domingo).
        dia_da_semana = data.weekday()

        if dia_da_semana == 5 or dia_da_semana == 6:
            return True
        else:
            return False
    except ValueError:
        print("Data inválida. Certifique-se de digitar a data no formato 'DD/MM/AAAA'.")
        sys.exit(1)


def define_melhor_pet_shop(pet_shop1, pet_shop2, pet_shop3):
    pet_shops = [pet_shop1, pet_shop2, pet_shop3]
    pet_shops.sort(key=lambda pet_shop: (pet_shop.valor, pet_shop.distancia))
    return pet_shops[0]


def main():
    data_inserida = input("Digite uma data no formato 'DD/MM/AAAA': ")
    final_de_semana = verifica_se_eh_final_de_semana(data_inserida)
    num_cachorros_pequenos = int(input("Número de cachorros pequenos: "))
    num_cachorros_grandes = int(input("Número de cachorros grandes: "))

    #Inicializa os petShops e calcula seus valores de acordo com a entrada
    meu_canino_feliz = MeuCaninoFeliz()
    meu_canino_feliz.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

    vai_rex = VaiRex()
    vai_rex.calcula_valor(final_de_semana, num_cachorros_pequenos, num_cachorros_grandes)

    chow_chawgas = ChowChawgas()
    chow_chawgas.calcula_valor(num_cachorros_pequenos, num_cachorros_grandes)

    melhor_pet_shop = define_melhor_pet_shop(meu_canino_feliz, vai_rex, chow_chawgas)

    print(f"O petshop {melhor_pet_shop.nome} é a melhor escolha, com o valor de R${melhor_pet_shop.valor},00. ")


if __name__ == "__main__":
    main()