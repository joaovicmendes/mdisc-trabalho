import sys, time

# Classe que gerencia o problema
class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.board = []
        self.generate_board()

    # Função que gera o tabuleiro utilizando self.w e self.h
    def generate_board(self):
        for i in range(self.h):
            self.board.append([0]*self.w)

    # Função opcional para imprimir o tabuleiro
    def print_board(self):
        print("  ")
        print("------")
        for elem in self.board:
            print(elem)
        print("------")
        print("  ")

    # Gera uma lista de possiveis posições, dada uma lista cur_pos com [x, y]
    def generate_legal_moves(self, cur_pos):
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos

    # Para ser mais eficiente, é mais fácil visitar os vizinhos sozinhos
    # no começo, já que eles ficam nas bordas do tabuleiro, e talvez não
    # possam ser alcançados depois
    def sort_lonely_neighbors(self, to_visit):
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[ neighbor[0] ][ neighbor[1] ]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            for m in moves:
                if self.board[ m[0] ][ m[1] ] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours


    # Função recursiva do Passeio do Cavalo (Knight's Tour)
    # n: profundidade da árvore de busca
    # path: caminho atual
    # to_visit: vértice para visitar
    def tour(self, n, path, to_visit):
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit) #append the newest vertex to the current point
        print("Visitando: ", to_visit)

        if n == self.w * self.h: #if every grid is filled
            self.print_board()
            print(path)
            print("Finalizado!")
            end = time.time()
            print("Tempo de execução: ", end - start)
            sys.exit(1)

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n+1, path, neighbor)

            #If we exit this loop, all neighbours failed so we reset
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print("Voltando para: ", path[-1])
            except IndexError:
                print("Nenhum caminho encontrado")
                sys.exit(1)

kt = KnightsTour(8, 8)

start = time.time()
kt.tour(1, [], (0,0))
kt.print_board()
