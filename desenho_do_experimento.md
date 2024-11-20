# Experimento Controlado: GraphQL vs REST

## 1. Desenho do Experimento

### A. Hipóteses
- **Hipótese Nula (H₀):** Não há diferença significativa no tempo de resposta ou no tamanho das respostas entre APIs GraphQL e REST.
- **Hipótese Alternativa (H₁):** Há diferenças significativas no tempo de resposta ou no tamanho das respostas entre APIs GraphQL e REST.

### B. Variáveis Dependentes
1. **Tempo de resposta** (em segundos): Tempo total desde o envio da requisição até o recebimento completo da resposta.
2. **Tamanho da resposta** (em caracteres): Quantidade de dados transferidos para completar a consulta.

### C. Variáveis Independentes
1. **Tipo de API:** GraphQL ou REST.

### D. Tratamentos
- **Tratamento 1:** Consultas realizadas via API GraphQL.
- **Tratamento 2:** Consultas realizadas via API REST.

### E. Objetos Experimentais
- Repositórios públicos no GitHub

### F. Tipo de Projeto Experimental
- **Projeto experimental do tipo "between-Subjects Design"**, onde cada API é testada separadamente com as mesmas entradas.

### G. Quantidade de Medições
- Realizar **50 medições** para cada tipo de consulta.

### H. Ameaças à Validade
- **Ameaças internas:**
  - Variações na performance do servidor durante os testes.
- **Ameaças externas:**
  - Diferenças em implementações específicas de GraphQL e REST.
