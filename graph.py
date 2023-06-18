import networkx as nx
import matplotlib.pyplot as plt
 
G = nx.Graph() # crear un grafo
 
#Añadir nodos
G.add_node("CDMX")
G.add_node("Toluca")
G.add_nodes_from(["Cuernavaca", "Tlaxcala", "Acapulco", "Sonora", "Jalisco"])
 
#Añadir aristas
G.add_edge("CDMX", "Acapulco")
G.add_edge("CDMX", "Cuernavaca")
G.add_edges_from([("Cuernavaca", "Tlaxcala"), ("Cuernavaca", "Acapulco"),  ("Toluca", "Tlaxcala"), ("Sonora", "CDMX"), ("Jalisco","Acapulco"), ("Cuernavaca", "Jalisco")])

print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)

nx.draw(G,with_labels=True)

plt.show()