import math

def calcular_distancia(ponto_a, ponto_b):
    """Calcula a distância entre dois pontos no plano, usado para o peso de
    cada arresta"""
    dx = ponto_a[0] - ponto_b[0]
    dy = ponto_a[1] - ponto_b[1]
    return math.sqrt(dx*dx + dy*dy)

def encontrar_arvore_geradora_minima(pontos):
    """Encontra a árvore geradora mínima usando o algoritmo de Boruvka"""
    n = len(pontos)
    
    # Componente[p] = id do componente do ponto p
    componente = [i for i in range(n)]  
    
    #Lista para armazenar
    arvore = []
    
    while len(set(componente)) > 1:
        melhor_aresta = [None] * n  # Armazenará (ponto_origem, ponto_destino, distancia)
        menor_distancia = [math.inf] * n  # Menor distancia encontrada para cada componente
        
        # Achar a melhor aresta para cada componente
        for i in range(n):
            for j in range(n):
                if i != j and componente[i] != componente[j]:
                    dist = calcular_distancia(pontos[i], pontos[j])
                    if dist < menor_distancia[componente[i]]:
                        menor_distancia[componente[i]] = dist
                        melhor_aresta[componente[i]] = (pontos[i], pontos[j], dist)
        
        # Adicionar as melhores arestas encontradas
        for comp_id in set(componente):
            if melhor_aresta[comp_id] is not None:
                ponto_a, ponto_b, dist = melhor_aresta[comp_id]
                
                # Encontra os índices originais para verificação de componentes
                i = pontos.index(ponto_a)
                j = pontos.index(ponto_b)
                
                # Se os componentes ainda estiverem separados
                if componente[i] != componente[j]:
                    # Armazena os pontos completos na árvore
                    arvore.append((ponto_a, ponto_b, dist))
                    
                    # Unir os componentes
                    old_comp = componente[j]
                    new_comp = componente[i]
                    for p in range(n):
                        if componente[p] == old_comp:
                            componente[p] = new_comp
    
    return arvore


pontos_exemplo = [
    (0, 0),    
    (4, 0),    
    (4, 3),    
    (2, 4),    
    (0, 3),    
    (1, 1),   
    (3, 1),    
    (2, 2)     
]

agm = encontrar_arvore_geradora_minima(pontos_exemplo)
print("Arestas da Árvore Geradora Mínima (com pontos completos):")
for aresta in agm:
    print(f"{aresta[0]} ↔ {aresta[1]} (distância: {aresta[2]:.2f})")