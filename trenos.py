#EXERCÍCIO EM TRENÓS

end_sala = 0

class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices  
        self.graph = graph 

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0 
        visited = {}  
        parents = {}  
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get) 
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

def menor_tempo(rotas, sala_start):
  
    dijkstra = Dijkstra(tuple(rotas.keys()), rotas)

    p, v = dijkstra.find_route(sala_start, end_sala)

    menor_tempo = v[end_sala]
    #caminho = dijkstra.generate_path(p, sala_start, end_sala)

    #print(caminho, menor_tempo)
    return menor_tempo


#INICIANDO

try:
    linha1 = input().split()
except: ...

M = int(linha1[0])

E = int(linha1[1])
N = int(linha1[2])
C = int(linha1[3])

linha2 = input().split()
linha3 = input().split()

#ler cada consulta a ser realizada
consultas = []
for i in range(C):
    consultas.append(int(input()))

entrada = linha2
vent = linha3


#TRANSFOMANDO ENTRADAS CORREDORES
entrada_split = [ [int(entrada[c]),int(entrada[c+1]),float(entrada[c+2])] for c in range(0,len(entrada), 3)]
nos={}
nos_vent={}

for c in entrada_split:
    nos[c[0]]={}
    nos[c[1]]={}
    nos_vent[c[0]]={}
    nos_vent[c[1]]={}

for c in entrada_split:
    nos[c[0]].update({c[1]:c[2]})
    nos[c[1]].update({c[0]:c[2]})
    nos_vent[c[0]].update({c[1]:c[2]})
    nos_vent[c[1]].update({c[0]:c[2]})

#TRASFORM CAMINHO VENTILÇÃO
entrada = vent
entrada_split = [ [int(entrada[c]),int(entrada[c+1])] for c in range(0,len(entrada), 2)]
for c in entrada_split:
    if c[1] in nos_vent[c[0]]:
        if nos_vent[c[0]][c[1]]>1.0:
            nos_vent[c[0]].update({c[1]:1.0})
            nos_vent[c[1]].update({c[0]:1.0})
    else: 
        nos_vent[c[0]].update({c[1]:1.0})
        nos_vent[c[1]].update({c[0]:1.0})

    #nos_vent[c[1]].update({c[0]:1})

#CONSULTANDO
for consulta in consultas:
    normal= menor_tempo(nos, int(consulta))
    impostor = menor_tempo(nos_vent, int(consulta))
    #print(normal, impostor)

    if normal<=impostor or normal-impostor<0.000000000000001: print('victory')#,normal, impostor)
    else: print('defeat')#,normal, impostor)




