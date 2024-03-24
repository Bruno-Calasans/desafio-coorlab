# Resultado - Desáfio CoorLab

## Ferramentas - Front-End
Para o front-end, implementei usando:
- **Vue 3.0 (composition api)**
- **TypeScript** para tipagem dos dados
- **Tailwind** para estilização via classe
- **ShadCdn vue** para componentes pré-prontos, visto que fornece componentes bem customizáveis utilizando o Tailwind como base e podemos instalar apenas os componentes necessários

## Ferramentas - Back-End
Para o Back-End, implementei usando:
- ****python 3.12****
- **json** do próprio python
- **FastApi** para criação de api REST de forma fácil e rápida
- **Uvicorn** para criação de servidor web
- **Poethepoet** para execução de scripts no arquivo **pyproject.toml**

## Como foi implementado o Front-End
1. Criei o respositório com usando os arquivos fornecidos necessários

2. Criei e troquei para branch **front-end**

3. Instalei o **Vue**, **Typescript**, **Tailwind** e **ShadCdn**

4. Criei o layout da página, separando em duas partes: 
- **NavMenu** => menu de navegação
- **MainContent** => conteúdo principal

5. Criei o componente **calc-travel-form**, formado pelos sub-componentes:
- **CalcTravelForm** => formulário para receber os inputs **cidade** e **data da viagem** do usuário
- **CitySelector** => componente do **CalcTravelForm**, que serve para lista todas as cidades disponíveis
- **InvalidDataDialog** => modal que vai aparecer caso o usuário não preencha os dados corretamente

6. Criei o componente **result-area**, formado pelos sub-componentes:
- **ResultArea** => contâiner onde irá aparecer os resultados das viagens
- **TravelResult** => mostra os dados das viagens **mais rápidas e confortáveis** e **mais econômicas**

7. Juntei **calc-travel-form** e **result-area** no componente-layout **MainContent**, assim temos um site bem parecido com o protótipo

8. O **front** está quase pronto!

## Como foi implementado o Back-End
9. Cria e troquei para branch **api** para criação da api

10.  instalei as bibliotecas **FastApi**, **Uvicorn** e **Poethepoet**

11. Configurei (host, port) do servidor web usando **Uvicorn**

12. Configurei o script **dev** no arquivo **pyproject.toml** usando o **Poethepoet**

13. Criei todas as rotas necessárias usando **FastApi** 
- **GET /** => rota inicial, que servirá para saber se a api está online
- **GET /city** => retorna todas as cidades disponíveis
- **GET /travel/{city}** => retorna todas as viagens disponíveis naquela cidade **city**
- **GET /best-travels/{city}** => retorna as viagens **mais rápida e confortável** e **mais econômica** da cidade **city**.

14. Criei as funções **hoursToInt** e **moneyToFloat** para me auxiliarem
- **hoursToInt**  => converte horas em inteiro
- **moneyToFloat** => converte dinheiro para float

15. Configurei o **CORS** usando a **CORS middleware** do **FastApi**

16. Terminei de criar a api completamente

# Conectando o Front e Back
17. Criei e troquei para branch **dev**

18.  Fiz o merge das branchs **front-end** e **api** na branch **dev**

19. Conectei o front-end e o back-end usando o **useFetch** do **Vue.js** no componentes
- **CitySelector** => pega todas as cidades através da rota **GET /city** através da função **getCities**
- **CalcTravelForm** => usa a rota **GET /best-travels/{city}** através da função **getBestTravels**

20. Fiz todas as correções necessárias de estilo, renomeação de arquivos e refatorações no front-end

21. Agora temos o front e o back conectados

# Reta final
22. Configurei o arquivo **run.sh**
23. Fiz o merge das branches **main** e **dev**
24. Escrevi o arquivo **RESULT.md**
