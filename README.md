# Algoritmo Petshop

O problema consiste em ajudar o Senhor Eduardo, proprietário de um canil em Belo Horizonte, a encontrar o melhor petshop para levar seus cães para o banho. Existem três petshops na região, cada um com preços diferentes para banho em cães pequenos e grandes, e os preços podem variar de acordo com o dia da semana.

Os três petshops disponíveis são:

Meu Canino Feliz: Localizado a 2 km do canil, oferece preços de banho mais baixos durante a semana, mas com aumento de 20% nos finais de semana.

Vai Rex: Localizado na mesma avenida do canil, a 1,7 km de distância. Os preços são diferentes para dias úteis e finais de semana, sendo mais caros nos finais de semana.

ChowChawgas: Localizado a 800 m do canil, oferece preços fixos para o banho em todos os dias da semana.

O objetivo é encontrar o petshop que oferece o menor valor total para o banho dos cães de acordo com o número de cães pequenos e grandes que o Senhor Eduardo deseja levar. Em caso de empate nos preços, o critério de desempate é escolher o petshop mais próximo do canil. Para resolver o problema, foi desenvolvida uma solução em Python que calcula os valores em cada petshop e identifica o melhor para o Senhor Eduardo com base nos critérios estabelecidos.


# Premissas Assumidas

1 - Disponibilidade dos PetShops: assume-se que os três petshops mencionados (Meu Canino Feliz, Vai Rex e ChowChawgas) estão disponíveis e em funcionamento para realizar os banhos nos cães.

2 -  Precisão dos Dados: pressupõe-se que os dados fornecidos pelo usuário (data da visita, número de cachorros pequenos e grandes) são válidos e corretos. Isso inclui a inserção correta da data no formato 'DD/MM/AAAA', bem como a quantidade apropriada de cães.

3 - Condições de Preços: supõe-se que os preços informados para os banhos em cada petshop são precisos e corretos, tanto para dias úteis quanto para finais de semana.

4 - Cálculo de Valor: é assumido que os cálculos de valor realizados para cada petshop estão corretos, de acordo com as regras estabelecidas para os preços de banho, levando em consideração a quantidade de cães pequenos e grandes, bem como a condição de ser ou não final de semana.

5 - Ambiente de Execução: Assume-se que o ambiente em que o código será executado possui o Python instalado.


# Decisões de Projeto

## Linguagem de Programação Python:
Foi escolhida a linguagem de programação Python devido à sua inteligibilidade. A sintaxe clara e concisa do Python torna o código mais fácil de ser compreendido e mantido. Também foi levado em consideração o fato de a biblioteca datetime ser padrão da linguagem.

## Biblioteca datetime:
Utilizou-se a biblioteca datetime do Python para manipulação de datas. Essa biblioteca é um componente padrão da linguagem que simplifica as operações de conversão de strings para objetos datetime, permitindo a verificação precisa de datas e dias da semana com precisão. Além disso, ela se destaca por sua facilidade de entendimento e utilização, quando comparada a bibliotecas de outras linguagens, como a biblioteca 'Chronos' em C++, que também foi avaliada.

## Programação Orientada a Objetos (POO):
A POO foi adotada para modelar o problema do canil, visando a organização e estruturação do código. As classes PetShop, VaiRex, ChowChawgas e MeuCaninoFeliz foram criadas para representar os diferentes petshops, permitindo o reuso de código e facilitando a extensibilidade do sistema.

## Encapsulamento e Segurança:
A POO foi utilizada para encapsular os atributos das classes dos petshops. O encapsulamento protege os dados internos das classes, permitindo acesso controlado apenas por meio de métodos públicos, proporcionando maior segurança do sistema e evitando alterações indevidas nos dados dos petshops. Para garantir a privacidade dos atributos, foi adotada a convenção de adicionar um underline antes de seus nomes. Os valores desses atributos podem ser obtidos por meio de métodos 'get', que são implementados implicitamente em Python utilizando os decoradores @property.

## Herança e Escalabilidade:
Foi aplicada a herança entre as classes PetShop, VaiRex, ChowChawgas e MeuCaninoFeliz. A classe abstrata PetShop contém os métodos comuns a todos os petshops, enquanto as subclasses especializam o comportamento e informações específicas de cada estabelecimento. Essa abordagem torna o código mais escalável, permitindo adicionar facilmente novos tipos de petshops no futuro.

## Tratamento de Erros e Exceções:
Foram adicionadas verificações para tratar erros e exceções no código. Ao calcular o valor do banho, verifica-se se o número de cães é negativo, lançando um ValueError com uma mensagem de erro adequada caso seja. Além disso, ao verificar se a data inserida pelo usuário é um final de semana, um bloco try-except é utilizado para capturar erros de conversão de data, interrompendo a execução do restante do código e fornecendo um feedback claro ao usuário em caso de data inválida

## Testes Unitários: 
Foram realizados testes unitários para garantir a corretude e a robustez da solução. Diversos casos de teste foram considerados para verificar o correto funcionamento do programa em diferentes cenários


Essas decisões de projeto resultaram em uma solução eficiente, confiável e de fácil manutenção para o problema passado.

# Instruções para executar o sistema: 
Deve-se, primeiramente, clonar o repositório pelo github ou baixar os arquivos zip.
## Opção 1:
- Verifique se o Python está instalado na sua máquina.
- Em algum editor de código, navegue até o diretório onde os arquivos Python estão localizados.
- Digite “python main.py” no terminal e pressione Enter

## Opção 2:
- Instale uma IDE de Python, como o PyCharm
- Abra a pasta do projeto na IDE
- Clique em “Run” para executar o sistema

# Instruções para executar os testes unitários:
Deve-se, primeiramente, clonar o repositório pelo github ou baixar os arquivos zip.
## Opção 1:
- Verifique se o Python está instalado na sua máquina.
- Em algum editor de código, navegue até o diretório onde os arquivos Python estão localizados.
- Digite “python main_test.py” no terminal e pressione Enter

## Opção 2:
- Instale uma IDE de Python, como o PyCharm
- Abra a pasta do projeto na IDE
- Selecione o arquivo main_test.py na barra lateral e clique em “Run”
