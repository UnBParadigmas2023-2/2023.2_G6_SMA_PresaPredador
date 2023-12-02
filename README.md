# Simulação de Presa-Predador

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo:**: 06<br>
**Paradigma**: Sistemas Multiagentes<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/2015103  |  Debora Caires de Souza Moreira |
| 20/2016480  |  Hellen Fernanda Mendonça de Faria |
| 19/0090901  |  Laura Pinos de Oliveira |
| 21/2005426  |  Lucas Gomes Caldas |
| 19/0037997  |  Sidney Fernando Ferreira Lemes |

## Sobre 

O projeto visa simular dinâmicas de um ecossistema presa-predador usando a biblioteca Mesa em Python. Através da criação de um modelo baseado em agentes, o objetivo é observar como a interação entre presas, predadores e plantas pode influenciar nas populações ao longo do tempo.

Utilizando a simulação baseada em agentes, o projeto busca explorar como fatores como reprodução, alimentação, crescimento de plantas, predatórios e mortalidade podem impactar a dinâmica e a estabilidade do ecossistema. Ao ajustar parâmetros e observar as interações entre os agentes, a simulação procura oferecer insights sobre os padrões emergentes resultantes dessas interações complexas no contexto do modelo presa-predador.

- Nascimento das Plantas
  - No início da simulação, um número determinado de plantas é criado em posições aleatórias no grid. Essas plantas possuem um contador regressivo para indicar o tempo até estarem totalmente crescidas e prontas para serem consumidas pelas presas.
- Posicionamento aletório de Presas e Predadores
  - Tanto as presas quanto os predadores são posicionados aleatoriamente no grid na inicialização do modelo.
  - As presas e os predadores têm atributos como vida, idade, idade fértil, sexo, entre outros.
- Alimentação das Presas e Predadores:
  - As presas têm a capacidade de se alimentar das plantas. Quando uma presa ocupa a mesma célula que uma planta totalmente crescida, ela a consome, aumentando sua vida em uma quantidade específica.
  - Por sua vez, os predadores se alimentam das presas. Quando um predador ocupa a mesma célula que uma presa, ele a consome, aumentando sua própria vida.
- Reprodução das Presas e Predadores:
  - As presas e os predadores fêmeas têm a possibilidade de se reproduzir se estiverem na idade fértil. Isso acontece com uma probabilidade determinada.
  - Quando ocorre a reprodução, um novo agente (presa ou predador) é gerado na mesma célula que o agente progenitor. No entanto, o agente progenitor perde metade da sua vida após a reprodução bem-sucedida.
- Envelhecimento e Mortalidade:
  - Ao longo do tempo, a idade dos agentes (presas e predadores) aumenta. Além disso, a vida dos agentes vai diminuindo.
  - Se um agente atinge uma idade superior a um valor específico (como 50 passos, por exemplo) ou se a vida de um agente chega a zero, ele morre e é removido do modelo.

## Screenshots

<img src="assets/screenshot_1.png" width=50%>

<img src="assets/screenshot_2.png" width=50%>

<img src="assets/screenshot_3.png" width=50%>

## Instalação 
**Linguagens**: [Python 3.x](https://www.python.org/)<br>
**Tecnologias**: [Mesa](https://mesa.readthedocs.io/en/stable/)<br>

O Mesa é uma biblioteca em Python que possibilita a criação, visualização e análise de modelos baseados em agentes

- Instale os requirements: ```pip install -r requirements.txt```

## Uso
- Instale o Python
- Execute o código ```run.py``` para iniciar a aplicação.
- O servidor provavelmente ficará aguardando conexões em localhost:8521 (ou seja, no seu próprio computador, na porta 8521). Você poderá acessar essa interface por meio de um navegador da web digitando http://localhost:8521 na barra de endereços.

### Uso da interface

A página exibida no navegador é a seguinte:

<img src="assets/screenshot_4.png" width = 80%>

Onde:
1. Inicia ou para a simulação;
2. Avança 1 passo na simulação;
3. Reincia a simulação;
4. Escolhe a altura da grade;
5. Escolhe a largura da grade;
6. Número de presas que iniciam a simulação;
7. Escolhe em quantos passos as plantas comidas voltam a crescer;
8. Número de predadores que iniciam na simulação
9. Quantos passos avançam em cada segundo;
10. Gráfico com número de presas e predadores a cada passo;

Ao mudar os valores, a simulação deve ser reiniciada.


## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto.
Procure: 
(i) Introduzir o projeto;
(ii) Mostrar passo a passo o código, explicando-o, e deixando claro o que é de terceiros, e o que é contribuição real da equipe;
(iii) Apresentar particularidades do Paradigma, da Linguagem, e das Tecnologias, e
(iV) Apresentar lições aprendidas, contribuições, pendências, e ideias para trabalhos futuros.
OBS: TODOS DEVEM PARTICIPAR, CONFERINDO PONTOS DE VISTA.
TEMPO: +/- 15min

## Participações
Apresente, brevemente, como cada membro do grupo contribuiu para o projeto.
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
| Débora C. de S. Moreira |  Minha contribuição para o projeto incluiu o início da estruturação do projeto para a implementação do MESA, além da criação de padrões para os agentes. Criei a lógica de comer das presas e dos predadores, além de que também inicei as lógicas de morte das presas e dos predadores. Além disso, auxiliei alguns colegas no entendimento geral da estrutura do MESA. | Excelente |
| Sidney Fernando F. Lemes |  Minha contribuição para o projeto incluiu a pesquisa e apresentação de ideias de projetos para o grupo, bem como a organização mais eficiente dos módulos do projeto. Além disso, implementei funcionalidades que permitiram aos agentes terem sexos distintos, introduzi um mecanismo de mortalidade para os agentes e desenvolvi a lógica de reprodução para eles. Estas adições permitiram uma representação mais realista e dinâmica do comportamento dos agentes no modelo de simulação do ecossistema presa-predador. | Excelente |
| Lucas Gomes Caldas |  Minha contribuição para o projeto incluiu a organização mais eficiente dos módulos do projeto, girando em torno do agente Planta, que serve de comida para as Presas e para os Predadores. Além disso, implementei a lógica de atualização aleatória, onde é capturado os movimentos de cada agente, sendo fundamental para o funcionamento do gráfico, também implementado por mim. | Excelente |
| Laura Pinos de Oliveira |  Para criação e implementação do projeto eu estudei a implementação do MESA, contribui na criação de presas e predadores. | Excelente |
| Hellen Fernanda M. |  Minha contribuição nesse projeto foi na elaboração inicial do projeto, juntamente com a Debora, estudamos os conceitos e conseguimos implementar alguns agentes iniciais. Além disso, conseguimos desenvolver algumas ações dos agentes. | Excelente |

## Outros 

Durante o desenvolvimento deste projeto, o grupo aprendeu várias lições valiosas:

* Colaboração Eficiente: A colaboração eficiente foi crucial para o sucesso do projeto. A troca constante de ideias, revisões de código e resolução colaborativa de problemas permitiram um progresso consistente.
* MESA: O entendimento da biblioteca MESA foi uma lição importante. A necessidade de entender como os agentes interagem, como o ambiente é modelado e como o modelo evolui ao longo do tempo foi essencial para o desenvolvimento do simulador.
* Modelagem de Agentes: A modelagem de agentes em um sistema multiagente é uma tarefa desafiadora que requer uma compreensão profunda do domínio do problema. Definir comportamentos realistas e interações entre os agentes foi crucial.
* Complexidade Emergente: Observamos que, mesmo com regras relativamente simples para presas, predadores e plantas, a simulação resulta em dinâmicas complexas e padrões emergentes. Isso destaca a complexidade que pode surgir de interações entre agentes simples.
* Fragilidades: Durante o desenvolvimento, enfrentamos alguns desafios, como a necessidade de entender a biblioteca MESA porém esses desafios também proporcionaram uma grande curva de aprendizado.

Trabalhos Futuros
* Refinamento do Modelo: O modelo pode ser refinado ainda mais para incluir mais detalhes e fatores que afetam o ecossistema presa-predador.
* Visualizações Adicionais: A adição de visualizações adicionais e métricas de desempenho pode ajudar na análise e compreensão mais aprofundada dos resultados da simulação.
* Otimização e Desempenho: Dependendo da escala da simulação, otimizações no código e considerações de desempenho podem ser exploradas.

## Fontes
- [A Multi-Agent System in Python](https://medium.com/agents-and-robots/a-multi-agent-system-in-python-74701f256c3a)
- [SMA-Prey-Predator-project](https://github.com/jerome-auguste/SMA-Prey-Predator-project)
