import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.DiGraph()

# Agregar nodos y arcos con pesos
arcos = [
    (1, 4, 4), (1, 5, 7),
    (2, 4, 8), (2, 5, 5),
    (3, 4, 5), (3, 5, 6),
    (4, 6, 6), (4, 7, 4), (4, 8, 8), (4, 9, 4),
    (5, 6, 3), (5, 7, 6), (5, 8, 7), (5, 9, 7)
]

# Añadir los arcos al grafo con el peso como atributo
for origen, destino, peso in arcos:
    G.add_edge(origen, destino, weight=peso)

# Posiciones manuales para evitar solapamiento en la visualización
posiciones = {
    1: (0, 2), 2: (0, 1), 3: (0, 0),
    4: (2, 2), 5: (2, 0),
    6: (4, 2.5), 7: (4, 1.5), 8: (4, 0.5), 9: (4, -0.5)
}

# Dibujar nodos
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, posiciones, node_size=700, node_color='lightblue')
nx.draw_networkx_labels(G, posiciones, font_size=12, font_weight='bold')

# Dibujar arcos
nx.draw_networkx_edges(G, posiciones, arrowstyle='->', arrowsize=20, edge_color='gray', width=2)

# Etiquetar arcos con los pesos y ajustar la posición
etiquetas = {(origen, destino): f"{peso}" for origen, destino, peso in arcos}
nx.draw_networkx_edge_labels(G, posiciones, edge_labels=etiquetas, font_color='darkred', label_pos=0.3, font_size=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

plt.title("Grafo del Problema de Programación Lineal con Pesos", fontsize=15)
plt.axis("off")
plt.show()
