# Navegador de Rotas com Grafos (Estilo Waze)

## Disciplina

Estruturas de Dados Não Lineares

## Linguagem Utilizada

Python 3

## Objetivo do Projeto

Este projeto simula um sistema simples de navegação semelhante ao aplicativo Waze.

O sistema utiliza a teoria dos grafos para encontrar o menor caminho entre dois pontos de uma cidade.

O algoritmo utilizado é o algoritmo de Dijkstra, responsável por calcular:

* O menor caminho
* A melhor rota
* A distância total percorrida

---

# Conceitos Utilizados

## O que é um Grafo?

Um grafo é uma estrutura matemática composta por:

* Vértices (nós)
* Arestas (ligações)

Neste projeto:

| Elemento | Representação             |
| -------- | ------------------------- |
| Vértices | Locais da cidade          |
| Arestas  | Ruas                      |
| Peso     | Distância entre os locais |

---

# Modelagem do Problema

O sistema representa uma cidade com diferentes locais conectados.

## Locais disponíveis

* Centro
* Hospital
* Shopping
* Universidade
* Praia

## Ruas e Distâncias

| Origem       | Destino      | Distância |
| ------------ | ------------ | --------- |
| Centro       | Shopping     | 4 km      |
| Centro       | Hospital     | 2 km      |
| Hospital     | Shopping     | 1 km      |
| Hospital     | Universidade | 7 km      |
| Shopping     | Praia        | 3 km      |
| Universidade | Praia        | 2 km      |
| Shopping     | Universidade | 5 km      |

---

# Tipo de Grafo

O projeto utiliza um:

## Grafo Direcionado e Ponderado

### Direcionado

As ruas possuem sentido.

Exemplo:

Centro → Shopping

### Ponderado

Cada ligação possui um peso.

Exemplo:

Centro → Shopping = 4 km

---

# Algoritmo Utilizado

## Algoritmo de Dijkstra

O algoritmo de Dijkstra encontra o menor caminho entre dois pontos de um grafo.

Ele funciona:

1. Começando pela origem
2. Visitando os vizinhos mais próximos
3. Somando os custos das rotas
4. Escolhendo sempre o menor custo
5. Continuando até chegar ao destino

---

# Biblioteca Utilizada

## NetworkX

A biblioteca NetworkX foi utilizada para:

* Criar grafos
* Adicionar vértices
* Adicionar arestas
* Calcular menor caminho
* Trabalhar com algoritmos de grafos

---

# Código Completo

```python
import networkx as nx

# Criação do grafo direcionado
cidade = nx.DiGraph()

# Adicionando ruas e distâncias
cidade.add_weighted_edges_from([
    ("Centro", "Shopping", 4),
    ("Centro", "Hospital", 2),
    ("Hospital", "Shopping", 1),
    ("Hospital", "Universidade", 7),
    ("Shopping", "Praia", 3),
    ("Universidade", "Praia", 2),
    ("Shopping", "Universidade", 5)
])

print("=== SISTEMA DE ROTAS ===")

# Mostrar locais disponíveis
print("\nLocais disponíveis:")
for local in cidade.nodes:
    print(f"- {local}")

# Entrada do usuário
origem = input("\nDigite a origem: ")
destino = input("Digite o destino: ")

try:
    # Menor caminho
    caminho = nx.dijkstra_path(cidade, origem, destino, weight='weight')

    # Distância total
    distancia = nx.dijkstra_path_length(
        cidade,
        origem,
        destino,
        weight='weight'
    )

    print("\n=== RESULTADO ===")
    print("Melhor rota encontrada:")

    for ponto in caminho:
        print(ponto)

    print(f"\nDistância total: {distancia} km")

except nx.NetworkXNoPath:
    print("\nNão existe caminho entre os pontos.")

except nx.NodeNotFound:
    print("\nLocal inválido digitado.")
```

---

# Explicação do Código

## Importação da Biblioteca

```python
import networkx as nx
```

Importa a biblioteca NetworkX.

---

## Criação do Grafo

```python
cidade = nx.DiGraph()
```

Cria um grafo direcionado.

---

## Inserção das Arestas

```python
cidade.add_weighted_edges_from()
```

Adiciona:

* Origem
* Destino
* Peso da aresta

---

## Algoritmo de Dijkstra

```python
nx.dijkstra_path()
```

Calcula o menor caminho.

---

## Distância Total

```python
nx.dijkstra_path_length()
```

Calcula o custo total da rota.

---

# Como Executar

## 1. Instalar o Python

Baixe o Python:

[https://www.python.org/](https://www.python.org/)

---

## 2. Instalar a Biblioteca

Abra o terminal e execute:

```bash
pip install networkx
```

---

## 3. Salvar o Arquivo

Exemplo:

```text
main.py
```

---

## 4. Executar o Projeto

No terminal:

```bash
python main.py
```

---

# Exemplo de Execução

## Entrada

```text
Digite a origem: Centro
Digite o destino: Praia
```

## Saída

```text
=== RESULTADO ===
Melhor rota encontrada:
Centro
Hospital
Shopping
Praia

Distância total: 6 km
```

---

# Casos de Teste

## Caso 1

### Entrada

* Origem: Centro
* Destino: Praia

### Resultado Esperado

Centro → Hospital → Shopping → Praia

Distância: 6 km

---

## Caso 2

### Entrada

* Origem: Hospital
* Destino: Universidade

### Resultado Esperado

Hospital → Universidade

Distância: 7 km

---

## Caso 3

### Entrada

Origem inválida

### Resultado Esperado

Mensagem de erro.

---

# Estrutura do Projeto

```text
ProjetoGrafos/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# requirements.txt

```text
networkx
```

---

# Melhorias Futuras

O projeto pode receber diversas melhorias:

* Interface gráfica
* Integração com mapas reais
* Simulação de trânsito
* Atualização dinâmica das rotas
* Visualização do grafo
* Uso do Streamlit
* Exportação em HTML com Pyvis

---

# Conclusão

Este projeto demonstrou na prática como a teoria dos grafos pode ser aplicada em problemas reais.

A utilização do algoritmo de Dijkstra mostrou como sistemas de navegação conseguem calcular rotas eficientes utilizando estruturas matemáticas.

O projeto permitiu compreender:

* Grafos direcionados
* Grafos ponderados
* Menor caminho
* Algoritmos de busca
* Modelagem computacional
* Estruturas de dados não lineares

---

# Autor

Projeto desenvolvido para a disciplina de Estruturas de Dados Não Lineares utilizando Python e NetworkX.
# Navegador de Rotas com Grafos (Estilo Waze)

## Disciplina

Estruturas de Dados Não Lineares

## Linguagem Utilizada

Python 3

## Objetivo do Projeto

Este projeto simula um sistema simples de navegação semelhante ao aplicativo Waze.

O sistema utiliza a teoria dos grafos para encontrar o menor caminho entre dois pontos de uma cidade.

O algoritmo utilizado é o algoritmo de Dijkstra, responsável por calcular:

* O menor caminho
* A melhor rota
* A distância total percorrida

---

# Conceitos Utilizados

## O que é um Grafo?

Um grafo é uma estrutura matemática composta por:

* Vértices (nós)
* Arestas (ligações)

Neste projeto:

| Elemento | Representação             |
| -------- | ------------------------- |
| Vértices | Locais da cidade          |
| Arestas  | Ruas                      |
| Peso     | Distância entre os locais |

---

# Modelagem do Problema

O sistema representa uma cidade com diferentes locais conectados.

## Locais disponíveis

* Centro
* Hospital
* Shopping
* Universidade
* Praia

## Ruas e Distâncias

| Origem       | Destino      | Distância |
| ------------ | ------------ | --------- |
| Centro       | Shopping     | 4 km      |
| Centro       | Hospital     | 2 km      |
| Hospital     | Shopping     | 1 km      |
| Hospital     | Universidade | 7 km      |
| Shopping     | Praia        | 3 km      |
| Universidade | Praia        | 2 km      |
| Shopping     | Universidade | 5 km      |

---

# Tipo de Grafo

O projeto utiliza um:

## Grafo Direcionado e Ponderado

### Direcionado

As ruas possuem sentido.

Exemplo:

Centro → Shopping

### Ponderado

Cada ligação possui um peso.

Exemplo:

Centro → Shopping = 4 km

---

# Algoritmo Utilizado

## Algoritmo de Dijkstra

O algoritmo de Dijkstra encontra o menor caminho entre dois pontos de um grafo.

Ele funciona:

1. Começando pela origem
2. Visitando os vizinhos mais próximos
3. Somando os custos das rotas
4. Escolhendo sempre o menor custo
5. Continuando até chegar ao destino

---

# Biblioteca Utilizada

## NetworkX

A biblioteca NetworkX foi utilizada para:

* Criar grafos
* Adicionar vértices
* Adicionar arestas
* Calcular menor caminho
* Trabalhar com algoritmos de grafos

---

# Código Completo

```python
import networkx as nx

# Criação do grafo direcionado
cidade = nx.DiGraph()

# Adicionando ruas e distâncias
cidade.add_weighted_edges_from([
    ("Centro", "Shopping", 4),
    ("Centro", "Hospital", 2),
    ("Hospital", "Shopping", 1),
    ("Hospital", "Universidade", 7),
    ("Shopping", "Praia", 3),
    ("Universidade", "Praia", 2),
    ("Shopping", "Universidade", 5)
])

print("=== SISTEMA DE ROTAS ===")

# Mostrar locais disponíveis
print("\nLocais disponíveis:")
for local in cidade.nodes:
    print(f"- {local}")

# Entrada do usuário
origem = input("\nDigite a origem: ")
destino = input("Digite o destino: ")

try:
    # Menor caminho
    caminho = nx.dijkstra_path(cidade, origem, destino, weight='weight')

    # Distância total
    distancia = nx.dijkstra_path_length(
        cidade,
        origem,
        destino,
        weight='weight'
    )

    print("\n=== RESULTADO ===")
    print("Melhor rota encontrada:")

    for ponto in caminho:
        print(ponto)

    print(f"\nDistância total: {distancia} km")

except nx.NetworkXNoPath:
    print("\nNão existe caminho entre os pontos.")

except nx.NodeNotFound:
    print("\nLocal inválido digitado.")
```

---

# Explicação do Código

## Importação da Biblioteca

```python
import networkx as nx
```

Importa a biblioteca NetworkX.

---

## Criação do Grafo

```python
cidade = nx.DiGraph()
```

Cria um grafo direcionado.

---

## Inserção das Arestas

```python
cidade.add_weighted_edges_from()
```

Adiciona:

* Origem
* Destino
* Peso da aresta

---

## Algoritmo de Dijkstra

```python
nx.dijkstra_path()
```

Calcula o menor caminho.

---

## Distância Total

```python
nx.dijkstra_path_length()
```

Calcula o custo total da rota.

---

# Como Executar

## 1. Instalar o Python

Baixe o Python:

[https://www.python.org/](https://www.python.org/)

---

## 2. Instalar a Biblioteca

Abra o terminal e execute:

```bash
pip install networkx
```

---

## 3. Salvar o Arquivo

Exemplo:

```text
main.py
```

---

## 4. Executar o Projeto

No terminal:

```bash
python main.py
```

---

# Exemplo de Execução

## Entrada

```text
Digite a origem: Centro
Digite o destino: Praia
```

## Saída

```text
=== RESULTADO ===
Melhor rota encontrada:
Centro
Hospital
Shopping
Praia

Distância total: 6 km
```

---

# Casos de Teste

## Caso 1

### Entrada

* Origem: Centro
* Destino: Praia

### Resultado Esperado

Centro → Hospital → Shopping → Praia

Distância: 6 km

---

## Caso 2

### Entrada

* Origem: Hospital
* Destino: Universidade

### Resultado Esperado

Hospital → Universidade

Distância: 7 km

---

## Caso 3

### Entrada

Origem inválida

### Resultado Esperado

Mensagem de erro.

---

# Estrutura do Projeto

```text
ProjetoGrafos/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# requirements.txt

```text
networkx
```

---

# Melhorias Futuras

O projeto pode receber diversas melhorias:

* Interface gráfica
* Integração com mapas reais
* Simulação de trânsito
* Atualização dinâmica das rotas
* Visualização do grafo
* Uso do Streamlit
* Exportação em HTML com Pyvis

---

# Conclusão

Este projeto demonstrou na prática como a teoria dos grafos pode ser aplicada em problemas reais.

A utilização do algoritmo de Dijkstra mostrou como sistemas de navegação conseguem calcular rotas eficientes utilizando estruturas matemáticas.

O projeto permitiu compreender:

* Grafos direcionados
* Grafos ponderados
* Menor caminho
* Algoritmos de busca
* Modelagem computacional
* Estruturas de dados não lineares

---

# Autor

Projeto desenvolvido para a disciplina de Estruturas de Dados Não Lineares utilizando Python e NetworkX.
