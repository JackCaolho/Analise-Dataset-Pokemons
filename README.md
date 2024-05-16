<h1>Analisando Pokémons.</h1>

Peguei uma base no Kaggle com atributos, origem e tipo de todos os Pokémon, e trabalhei nela com princípios básicos de Python e as bibliotecas matplotlib, pandas e seaborn, a tríade dos gráficos.
Para começar, vamos falar sobre o tipo de gráfico boxplot. Gosto bastante dele porque entrega muita informação de maneira organizada. Brevemente, um gráfico boxplot mostra a distribuição de um conjunto de dados, destacando a mediana, quartis e possíveis outliers.

Primeiro, queria saber qual geração tem os Pokémon mais fortes. Criei um valor que chamei de CP, que é apenas a soma de todos os atributos, e verifiquei os Pokémon mais fortes por geração. Porém, notei que existiam grandes outliers e que a força variava bastante, sem muito padrão.

![1](https://github.com/JackCaolho/analise-pokemons/assets/113406494/4bc037b3-06ae-4e88-a6ab-f55ff91e74e7)

Para resolver isso, analisei os dados e vi que Pokémon lendários ou aqueles com nomes MEGA ou Gigan usam do suco, fugindo de todos os padrões. Então, resolvi descartá-los das análises. Vejam como tudo ficou mais equilibrado e sem outliers. Olha, a 4º geração é um pouco acima da média, mas ainda dá uma boa briga com as demais, apesar da 3ª geração ter os mais fortes, acho eles sem graça, então fico a 4ª.

![WhatsApp Image 2024-05-14 at 16 35 58](https://github.com/JackCaolho/analise-pokemons/assets/113406494/61b8a634-8ee5-4abe-a20e-ca7adf6d51b1)

Nessa busca por poder, fui ver então qual o tipo era mais forte. Para surpresa de 0 pessoas, é o tipo Dragão, que domina geral. Isso piora porque eles só têm fraqueza para elementos Gelo e Fada, que se mostraram bem fracos na média e no conjunto de Pokémons mais fracos. Comecei a achar bem desbalanceado.

![3](https://github.com/JackCaolho/analise-pokemons/assets/113406494/508cd164-3e49-4963-976b-50b58ec509f5)

Fui ver se existiam muitos Pokémon Dragão para verificar a existência de uma possível ditadura dragonaria no mundo Pokémon, mas nisso está tudo bem na média. Existem mais Pokémon de Água, seguidos de Normais e Grama, algo perfeitamente normal considerando que Pokémon são inspirados em animais reais e biomas reais do nosso mundo. Porém, quais os tipos menos comuns? Fadas e Gelo... Que coisa, vida fácil para os dragõezinhos.

![4](https://github.com/JackCaolho/analise-pokemons/assets/113406494/acb67133-2b84-498f-95bf-b65a4d45dcff)

Por último, fiz um heatmap comparando os atributos em si, não apenas o valor total, para entender as relações. Nada que me brilhasse os olhos: Pokémon com mais HP ou defensivos são mais lentos, e os com maior ataque são mais rápidos.

![WhatsApp Image 2024-05-14 at 16 40 32](https://github.com/JackCaolho/analise-pokemons/assets/113406494/c6b085c7-30ec-49a4-98b4-4230e7f507c3)

Bom, é isso. Espero que tenham curtido.

