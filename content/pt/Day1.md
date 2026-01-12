# Introdução e Contextualização
O objetivo principal deste desafio é desenvolver um guardrail que não utilize LLMs para realizar avaliações. Nesse contexto, abordaremos a temática do racismo em plataformas digitais, empregando guardrails com estratégias de IA para identificar e mitigar práticas racistas na internet. 

## **O Problema em Números**
Estatísticas apresentam os dados sobre racismo no Brasil:
```
- 84% de pessoas pretas já sofreram discriminação (Agência Brasil / pesquisa MIR (2025)).
- Registrados 3,4 mil+ denúncias / 5,2 mil violações de racismo (Disque 100 / MDHC (2024)).
- Negros têm 2,7 vezes mais risco de homicídio do que não negros no Brasil. (Agência Brasil / Atlas da Violência, 2023).
```

## **Impacto Psicológico**
Dados de pesquisa com 2.500 vítimas (Fonte: UFMG, 2024) sobre racismo no Brasil:
```
impactos = {
    "ansiedade": 68.3,
    "depressao": 42.7,
    "isolamento_social": 55.2,
    "autoestima": 73.8,  # % com autoestima afetada
    "desistencia_plataforma": 31.5
}
```

## **Limitações de Sistemas que usam LLM no Português brasileiro:**
Grandes modelos de linguagem (LLMs) são predominantemente treinados com corpora em inglês, o que resulta em sub-representação de outras línguas, incluindo o português brasileiro. Isso faz com que LLMs tenham desempenho inferior e maior dificuldade em compreender nuances do português do Brasil, refletindo vieses culturais e linguísticos herdados dos dados majoritariamente anglófonos. (UWA News, 2025).