import networkx as nx


cidade = nx.DiGraph()


cidade.add_weighted_edges_from([
    ("Centro", "Shopping", 4),
    ("Centro", "Hospital", 2),
    ("Hospital", "Shopping", 1),
    ("Hospital", "Universidade", 7),
    ("Shopping", "Praia", 3),
    ("Universidade", "Praia", 2),
    ("Shopping", "Universidade", 5)
])

print(" SISTEMA DE ROTAS ")


print("\nLocais disponíveis:")
for local in cidade.nodes:
    print(f"- {local}")


origem = input("\nDigite a origem: ")
destino = input("Digite o destino: ")

try:
    
    caminho = nx.dijkstra_path(cidade, origem, destino, weight='weight')

    
    distancia = nx.dijkstra_path_length(
        cidade,
        origem,
        destino,
        weight='weight'
    )

    print("\n RESULTADO ")
    print("Melhor rota encontrada:")

    for ponto in caminho:
        print(ponto)

    print(f"\nDistância total: {distancia} km")

except nx.NetworkXNoPath:
    print("\nNão existe caminho entre os pontos.")

except nx.NodeNotFound:
    print("\nLocal inválido digitado.")