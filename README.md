#  Navegador de Rotas com Grafos

Projeto desenvolvido para a disciplina de Estruturas de Dados Não Lineares.

---

#  Tema Escolhido

## Tema B — Navegador de Rotas estilo Waze

O projeto simula um sistema de navegação capaz de encontrar a menor rota entre dois pontos de uma cidade utilizando teoria dos grafos e o algoritmo de Dijkstra.

---

#  Integrantes

- Seu Nome
- Nome do Colega

---

#  Objetivo

Criar uma aplicação em Python que modele ruas e locais como um grafo direcionado e ponderado, permitindo calcular o menor caminho entre dois pontos.

---

#  Modelagem Matemática

O problema foi modelado utilizando um:

## Grafo Direcionado e Ponderado

### Vértices
Representam locais da cidade:
- Centro
- Shopping
- Hospital
- Universidade
- Praia

### Arestas
Representam ruas conectando os locais.

### Pesos
Representam a distância entre os pontos.

---

#  Algoritmo Utilizado

## Algoritmo de Dijkstra

O algoritmo foi utilizado para calcular:
- Menor caminho
- Melhor rota
- Distância total

---

#  Tecnologias Utilizadas

- Python 3
- NetworkX

---

#  Estrutura do Projeto

```text
ProjetoGrafos/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

#  Como Executar

## 1. Instalar dependências

```bash
pip install networkx
```

---

## 2. Executar o projeto

```bash
python main.py
```

---

#  Exemplo de Execução

```text
Digite a origem: Centro
Digite o destino: Praia

Melhor rota encontrada:
Centro
Hospital
Shopping
Praia

Distância total: 6 km
```

---

#  Funcionalidades

- Listagem de locais disponíveis
- Escolha de origem e destino
- Cálculo automático da menor rota
- Exibição da distância total
- Tratamento de erros para locais inválidos

---

#  Conceitos Aplicados

- Grafos
- Grafos direcionados
- Grafos ponderados
- Caminho mínimo
- Algoritmo de Dijkstra
- Estruturas de dados não lineares

---

#  Conclusão

O projeto demonstrou na prática como a teoria dos grafos pode ser aplicada em sistemas reais de navegação e roteamento, utilizando estruturas matemáticas e algoritmos de otimização.

---

#  Licença

Projeto acadêmico desenvolvido para fins educacionais.
