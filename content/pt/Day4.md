# Explicação da arquitetura proposta

A arquitetura apresentada organiza o sistema em camadas modulares e especializadas, cada uma com responsabilidades bem definidas. Essa estrutura facilita escalabilidade, manutenibilidade, auditabilidade e confiabilidade, características essenciais para sistemas de moderação sensível, como a detecção de racismo e discriminação em plataformas digitais, especialmente no contexto do português brasileiro, onde LLMs generalistas apresentam limitações linguísticas e culturais.

O fluxo ocorre de cima para baixo: o conteúdo entra pela camada de aplicação, passa por processamento especializado, é analisado de forma contextual, resulta em uma decisão automatizada ou sinalização humana, e, por fim, gera uma resposta adequada ao usuário ou plataforma. A seguir, tem-se a explicação das camadas da Arquitetura proposta.

1. **Camada de Aplicação:** Esta é a porta de entrada do sistema. Ela permite que diferentes tipos de clientes, como, aplicações web, plataformas digitais, sistemas parceiros ou dashboards administrativos, enviem conteúdos para análise. O conteúdo enviado pelo usuário é representado por:

$$
x \in \mathcal{X}, \quad x = \text{input text (comentário, post ou mensagem)}
$$

O input pode ser recebido por diferentes canais:

$$
x \xrightarrow{\text{API / WebSocket / SDK}} \text{Camada de Processamento}
$$

Esta camada garante integração universal e coleta estruturada de dados.

Para isso, disponibiliza:
 - APIs REST e GraphQL para integração estruturada;
 - WebSockets para análise em tempo real;
 - SDKs para múltiplas linguagens, facilitando a adoção do sistema;
 - Dashboard administrativo, usado para monitoramento, auditoria e ajustes operacionais.

2. **Camada de Orquestração:** Após a entrada, o conteúdo passa pela camada responsável por organizar, proteger e distribuir as requisições. A orquestração distribui os inputs entre os módulos de forma confiável e balanceada:

$$
\{x\} \xrightarrow{\text{Load Balancer + Service Mesh}} \{x_1, x_2, ..., x_m\}
$$

Circuit breakers e rate limiting garantem operação segura:

$$
R(x_i) =
\begin{cases} 
0 & \text{se limite excedido} \\
x_i & \text{caso contrário}
\end{cases}
$$


Essa camada garante que o sistema funcione de forma estável mesmo sob alta carga, utilizando:
 - Service Mesh, para controle e observabilidade da comunicação entre serviços;
 - Balanceamento de carga inteligente, distribuindo requisições entre instâncias;
 - Circuit Breaker, evitando que falhas se propaguem;
 - Rate Limiting, prevenindo abuso e garantindo uso justo.

3. **Camada de Processamento:** Esta é a camada central de inteligência do sistema. O conteúdo é analisado por múltiplos módulos especializados, cada um treinado ou configurado para detectar um tipo específico de manifestação discriminatória. Cada módulo processa o conteúdo e produz uma **pontuação de risco** \(s_i\):

$$
s_i = g_i(x_i), \quad i = 1, 2, ..., n
$$

Exemplos de módulos:
- \(g_1(x)\) = BERT fine-tuned para linguagem direta pt-BR  
- \(g_2(x)\) = SVM + regras para microagressões  
- \(g_3(x)\) = XGBoost para estereótipos  
- \(g_4(x)\) = Regras + base de conhecimento histórico  
- \(g_5(x)\) = Embeddings para dog-whistles  

Vetor de outputs:

$$
\mathbf{s} = [s_1, s_2, ..., s_n]^T
$$

Exemplos:
 - Modelos baseados em BERT fine-tuned para linguagem direta;
 - SVM com regras para microagressões;
 - XGBoost para estereótipos;
 - Regras + base de conhecimento para referências históricas;
 - Embeddings para dog-whistles e linguagem implícita.

Todos os módulos operam em paralelo, produzindo pontuações e sinais independentes.

4. **Camada de Agregação:** Nesta camada, os resultados individuais dos módulos são combinados de forma interpretável. Os outputs são combinados em uma **pontuação agregada** \(S\):

$$
S = \sum_{i=1}^{n} w_i \cdot s_i, \quad \sum_{i=1}^{n} w_i = 1
$$

Ajuste pelo contexto:

$$
C = f(\text{região, histórico, plataforma})
$$

Pontuação final usada na decisão:

$$
S_C = S \cdot C
$$

Sendo esta camada responsável por:
 - Calcular uma média ponderada das pontuações (S = Σ(wᵢ × sᵢ));
 - Ajustar o resultado com base no contexto (região, histórico do usuário, tipo de plataforma);
 - Realizar calibração de confiança, reduzindo falsos positivos ou negativos;
 - Gerar explicações, indicando quais módulos influenciaram a decisão.

5. **Camada de Decisão:** Com base na pontuação final e no contexto, o sistema define qual ação tomar. Decisão baseada em \(S_C\) e thresholds θ₁, θ₂, θ₃:

$$
D =
\begin{cases} 
\text{BLOCK} & \text{se } S_C \ge \theta_1 \\
\text{FLAG\_HUMAN} & \text{se } \theta_2 \le S_C < \theta_1 \\
\text{EDUCATE} & \text{se } \theta_3 \le S_C < \theta_2 \\
\text{PASS} & \text{caso contrário}
\end{cases}
$$

A decisão segue regras claras e configuráveis:
 - Bloquear conteúdos altamente ofensivos;
 - Encaminhar para revisão humana em casos ambíguos;
 - Aplicar resposta educativa quando há potencial de conscientização;
 - Permitir a publicação quando não há indícios relevantes.
 - Os limiares (θ₁, θ₂, θ₃) podem ser ajustados conforme políticas da plataforma.

6. **Camada de Resposta:** Por fim, o sistema prepara e entrega a resposta. A decisão é transformada em ação prática:

$$
R = h(D, \text{user context}, \text{language})
$$

Sendo responsável por:
 - Formatada conforme o padrão da API ou plataforma;
 - Personalizada para o perfil do usuário ou contexto;
 - Capaz de incluir conteúdo educativo;
 - Compatível com múltiplos idiomas.

Na última camada, ou camada de resposta, é o momento onde a decisão técnica se transformar em ação prática e compreensível.

## Resumo do fluxo completo

$$
x \xrightarrow{\text{Aplicação + Orquestração}} 
\mathbf{s} = [g_1(x), ..., g_n(x)] 
\xrightarrow{\text{Agregação}} S_C 
\xrightarrow{\text{Decisão}} D 
\xrightarrow{\text{Resposta}} R
$$