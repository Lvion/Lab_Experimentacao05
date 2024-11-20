# Experimento Controlado: GraphQL vs REST

## 1. Desenho do Experimento

### A. Hipóteses
- **Hipótese Nula (H₀):** Não há diferença significativa no tempo de resposta ou no tamanho das respostas entre APIs GraphQL e REST.
- **Hipótese Alternativa (H₁):** Há diferenças significativas no tempo de resposta ou no tamanho das respostas entre APIs GraphQL e REST.

### B. Variáveis Dependentes
1. **Tempo de resposta** (em milissegundos): Tempo total desde o envio da requisição até o recebimento completo da resposta.
2. **Tamanho da resposta** (em bytes): Quantidade de dados transferidos para completar a consulta.

### C. Variáveis Independentes
1. **Tipo de API:** GraphQL ou REST.
2. **Complexidade da consulta:** Número de campos e profundidade da estrutura solicitada na consulta.

### D. Tratamentos
- **Tratamento 1:** Consultas realizadas via API GraphQL.
- **Tratamento 2:** Consultas realizadas via API REST.

### E. Objetos Experimentais
- Um banco de dados comum simulado com estrutura equivalente para ambas as APIs.
- Dados representando um sistema fictício com tabelas como *usuários*, *produtos*, *pedidos* e *categorias*.

### F. Tipo de Projeto Experimental
- **Projeto experimental do tipo "between-Subjects Design"**, onde cada API é testada separadamente com as mesmas entradas.

### G. Quantidade de Medições
- Realizar **50 medições** para cada tipo de consulta, distribuídas entre:
  - Consultas simples (Buscar apenas um campo, como o nome do usuário).
  - Consultas complexas (Buscar dados relacionados em várias tabelas, como pedidos de um usuário e os itens de cada pedido).

### H. Ameaças à Validade
- **Ameaças internas:**
  - Diferenças nas configurações das APIs podem influenciar os resultados.
  - Variações na performance do servidor durante os testes.
- **Ameaças externas:**
  - Generalização dos resultados para APIs de produção com maior complexidade.
  - Diferenças em implementações específicas de GraphQL e REST.