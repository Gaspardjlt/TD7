import tkinter as tk
import math as m
from random import randint

class Graph:
    def __init__(self, graph, can, pos):
        self.__can = can
        self.__graph = graph
        self.__terminateID = str()
        self.__pos = pos
        self.__number_vertices = len(graph)
        self.__color = COLORS[:self.__number_vertices]
        self.__values = {i:i for i in range(self.__number_vertices)}

    def draw(self, can, graph, pos):
        for i, node in enumerate(self.__graph):
            for j in node:
                self.__can.create_line(self.__pos[i][0], self.__pos[i][1], self.__pos[j][0], self.__pos[j][1])
        for i, (x, y) in enumerate(self.__pos):
            self.__can.create_oval(x-7, y-7, x+7, y+7, fill=COLORS[i])
            self.__can.create_text(x, y, text=i, font=('Times','9','bold'), fill='black')
    
    def getPos(self):
        return self.__pos
    
    def getDist(self):
        return self.__dist
    
    def getGraph(self):
        return self.__graph
    
    def __str__(self):
        return f"The graph represented is : {self.__graph}"
    
    def min_local(self,i):
        neighbours = []
        for x in range(self.__number_vertices) : 
            if x == i:
                for y in self.__graph[x]:
                    neighbours.append(y)
            else:
                for y in self.__graph[x]:
                    if y == i :
                        neighbours.append(x)
        values = []
        for neighbour in neighbours:
            values.append(self.__values[neighbour])   ####prendre en compte neighbours !!!!!
        minimum = min(values)
        COLORS[i]=COLORS[minimum]
        self.__values[i] = minimum


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("500x500")

    can = tk.Canvas(root, width=500, height=500)
    can.grid(row=0, column=0)

    COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
    positions = [[131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198]]
    matrix = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]
    G = Graph(matrix,can,positions)
    G.min_local(9)
    G.draw(can, matrix, positions)

    #example in the TD  (FAIRE UNE DEUXIEME FENETRE)
    '''
    graph = [[2], [], [4], [1], [6], [3], [7], [5]]
    pos = [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200], [350, 200], [250, 200], [300, 200]]
    G = Graph(graph, can, pos)
    G.min_local(0)
    G.draw(can, graph, positions)
    '''

    root.mainloop()

    # EXERCISE 3

    #def spread(G):
# version n aive : on teste à chaque iteration si tous les sommets ont tous leurs voisins de la meme couleur





