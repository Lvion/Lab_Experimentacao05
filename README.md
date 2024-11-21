# Um experimento controlado - GraphQL e REST

## Introdução

As APIs Web são fundamentais para integrar sistemas modernos, sendo **REST** e **GraphQL** as abordagens mais utilizadas. Enquanto o REST utiliza endpoints com operações pré-definidas, o GraphQL permite consultas flexíveis, onde os clientes especificam exatamente os dados desejados, prometendo maior eficiência na transferência de dados.

Este experimento avalia, de forma quantitativa, as diferenças entre APIs GraphQL e REST em relação ao tempo de resposta e ao tamanho das respostas. Utilizando um banco de dados comum e consultas equivalentes, busca-se fornecer insights práticos para a escolha entre as duas abordagens no desenvolvimento de sistemas.

## Metodologia

A metodologia utilizada para este experimento foi o **Between-Subjects Design**, no qual cada grupo foi tratado de maneira independente, com medições realizadas separadamente para cada API (GraphQL e REST). Uma única consulta foi utilizada para ambos os tratamentos, garantindo equivalência na comparação. A análise foi baseada em **10 medições por API** com foco em duas variáveis dependentes: o tempo de resposta e o tamanho das respostas. Esta abordagem permitiu avaliar de forma direta e controlada as diferenças entre as API's, limitando variáveis externas que pudessem afetar os resultados

## Resultados

### RQ1: Respostas às consultas GraphQL são mais rápidas que respostas às consultas REST?

Não. Ao analisar os tempos (graphql-times e rest-times), percebemos que, em geral, as respostas REST têm tempos ligeiramente menores do que as do GraphQL.
- A média dos tempos de GraphQL é maior do que a dos tempos de REST.
- Em alguns casos específicos, o GraphQL foi mais rápido, mas a tendência geral favorece REST em termos de tempo de resposta.

### RQ2: Respostas às consultas GraphQL tem tamanho menor de respostas às consultas REST?

Sim. Ao analisar o tamanho das respostas (graphql-lengths e rest-lengths), observamos que o GraphQL retornou um tamanho constante de 945 bytes, enquanto o REST retornou 57.927 bytes.

Essa diferença se deve à capacidade do GraphQL de selecionar especificamente os dados a serem buscados, algo que o REST não permite.

##  Discussão dos resultados obtidos

Os resultados indicam que, embora o GraphQL tenha respostas menores, o REST apresentou tempos de resposta mais rápidos na maioria das medições. A diferença de tempo pode ser explicada pela disputa de recursos na máquina durante o experimento. Sendo assim, a escolha entre as duas API's depende do equilíbrio desejado entre tamanho de resposta e velocidade.
