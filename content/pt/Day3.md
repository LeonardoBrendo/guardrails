# Arquitetura da solução "Sentinela étnico-cultural"

1. A seguir, tem-se a explicação da arquitetura proposta e como esta busca resolver o problema do racismo em plataformas digitais. A arquitetura proposta adota uma abordagem baseada em **guardrails sem uso de LLM**, combinando regras determinísticas, análise léxica e validações contextuais para avaliar conteúdos publicados em plataformas digitais.

2. A arquitetura da solução **Sentinela Étnico-Cultural** foi projetada para contornar as limitações dos LLMs no português brasileiro, que apresentam desempenho inferior e funcionam como caixas-pretas, dificultando explicações sobre decisões de moderação de conteúdo. 

3. A solução combina módulos especializados (BERT fine-tuned, regras, XGBoost, embeddings) com calibração de confiança e geração de explicações, permitindo que a camada de decisão defina ações automáticas, sinalização humana ou mensagens educativas, enquanto a camada de resposta apresenta decisões contextualizadas. 

4. Dessa forma, o Sentinela integra guardrails confiáveis e interpretáveis, garantindo moderação eficiente e auditável em plataformas digitais no contexto brasileiro. 

5. A seguir, tem-se as Figuras da Arquiteura e o Fluxo em camadas da solução Sentinela Étnico-Cultural.

![Arquitetura em camadas da solução Sentinela Étnico-Cultural](content/pt/images/arquitetura.png)

![Fluxo da solução Sentinela Étnico-Cultural](content/pt/images/fluxo.png)
