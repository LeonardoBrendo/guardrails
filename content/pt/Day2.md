# Limitações técnicas dos LLMs para moderação étnica 

## Alguns dados relevantes no contexto de LLMs considerando a linguística e grupos étnicos:

1. Viés Estrutural dos Modelos:

De acordo com a distribuição linguística em datasets de treino (Fonte: BLOOM, 2023), chegou-se nos valores:
```
distribuicao_linguistica = {
    "ingles": 46.2,
    "chines": 23.5,
    "espanhol": 7.8,
    "portugues": 1.7,  # Desses, português BR: ~0.9%
    "outros": 20.8
}
```

A representação de grupos étnicos (Fonte: Ethical AI, 2024) teve as seguintes pontuações:
```
representacao_etnica = {
    "europeus": 72.4,
    "norte_americanos": 15.3,
    "asiaticos": 8.2,
    "africanos": 2.1,
    "latino_americanos": 1.3,
    "indigenas": 0.7
}
```

## Dificuldade de usar Guardrails com LLM no contexto do português brasileiro

Quando usamos IA para classificação de conteúdo, como identificar discursos racistas em textos, enfrentamos o problema da explicabilidade. Isso significa que, embora o modelo possa fornecer uma resposta ou classificação, não é evidente como ele chegou a essa decisão.

### Problema da Explicabilidade (Explainable AI – XAI)

Ao usar IA para classificação de conteúdo, como identificar discursos racistas em textos, enfrentamos o problema da explicabilidade. Ou seja, mesmo que o modelo forneça uma classificação, não é claro como ele chegou a essa decisão. Para um modelo matemático:

$$
f(x) = y
$$

onde:  

$$
x = \text{input text (texto enviado para análise)}
$$  

$$
y = \text{classificação (racista / não racista)}
$$  

Em **LLMs**, o gradiente é praticamente não interpretável:

$$
\frac{\partial y}{\partial x} \approx 0
$$

Isso significa que **não podemos responder perguntas simples**, como:  “Por que esta frase foi considerada racista?”. Além disso, **LLMs treinados majoritariamente em inglês apresentam limitações no português brasileiro**, especialmente ao lidar com **gírias, expressões regionais ou nuances culturais**, tornando ainda mais difícil aplicar **guardrails precisos**. 

LLMs apresentam limitações no português brasileiro, pois são treinados majoritariamente em inglês e funcionam como caixas-pretas, dificultando explicações sobre decisões de moderação de conteúdo. Nos próximos slides, tem-se a Arquitetura e sua explicação, estabelecendo assim, uma proposta de solução para este problema.