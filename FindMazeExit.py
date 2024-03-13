#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-


# Map character configuration
wall = '#'
hall = '.'
traversed = '='
wrong = 'x'
solution = '@'
entrance = 'E'
exit__ = 'S'


class Maze(object):
    def __init__(self):
        self.map_ = None
        self.entrance = None
        self.exit__ = None

    def read_map(self, text):
        """Reads a map; it must have an entrance and an exit_."""
        self.map_ = text.split('\n')

        for i, l in enumerate(self.map):
            # Find entrance:
            p = l.find(entrance)
            if p >= 0:
                self.entrance = (i, p)
            # Find exit_:
            p = l.find(exit_)
            if p >= 0:
                self.exit_ = (i, p)

            # Convert string to list
            self.map_[i] = list(l)

        if not self.entrance:
            raise ValueError("The map does not have an entrance!")
        if not self.exit_:
            raise ValueError("The map does not have an exit!")

    def read_map_file(self, file):
        """Reads a map from a file."""
        f = open(file)
        self.read_map_(f.read())
        f.close()

    def __str__(self):
        m = []
        for l in self.map_:
            m.append(''.join(l))
        return '\n'.join(m)

    def solve(self):
        """Solves the maze, attempting to find the exit_.

        If the exit_ is found, returns True; otherwise, returns False.
        """
        def valid_position(row, col):
            """Function to check if the position is within the map."""
            if row > len(self.map_) or col > len(self.map_[row]):
                """Invalid position; outside of the map."""
                return False
            else:
                return True


        def find_exit(row, col):
            if self.map_[row][col] == exit_:
                "If it's at the base of recursion, it's on top of the output"
                return True
            else:
                """Mark as traversed and enter recursion.
                In this case, we'll go right, then up, left, and
                then down.
                Remembering that this is a recursion and that we mark our path,
                We magically have the memory of the paths already tested.
                """
                self.map_[ row ][ col ] = traversed
                find_it = False

                if not find_it and \
                       valid_position( row, col + 1 ) and \
                       self.map_[ row ][ col + 1 ] in ( hall, exit ):
                    """Ainda não encontrou e
                    a posição à direita é hall ou é a saída.
                    Prossiga pela direita."""
                    find_it = find_exit( row, col + 1 )

                if not find_it and \
                       valid_position( row - 1, col ) and \
                       self.map_[ row - 1 ][ col ] in ( hall, exit ):
                    """Ainda não encontrou e
                    a posição acima é hall ou é a saída.
                    Prossiga para cima."""
                    find_it = find_exit( row - 1, col )

                if not find_it and \
                       valid_position( row, col - 1 ) and \
                       self.map_[ row ][ col - 1 ] in ( hall, exit ):
                    """Ainda não encontrou e
                    a posição à esquerda é hall ou é a saída.
                    Prossiga para esquerda."""
                    find_it = find_exit( row, col - 1 )

                if not find_it and \
                       valid_position( row + 1, col ) and \
                       self.map_[ row + 1 ][ col ] in ( hall, exit ):
                    """Ainda não encontrou e
                    a posição abaixo é hall ou é a saída.
                    Prossiga para baixo."""
                    find_it = find_exit( row + 1, col )

                # Caso o caminho adotado foi correto, marque como solução
                # senão marque como wrong
                if find_it:
                    self.map_[ row ][ col ] = solution
                else:
                    self.map_[ row ][ col ] = wrong
                    
                return find_it
        # find_exit()
        
        return find_exit( self.entrance[ 0 ], self.entrance[ 1 ] )
    # resolve()
# Labirinto

# Exemplo de uso:
m = Maze()
m.read_map(
    """
#############
   3 #.......#..E#
   4 #.#########.#
   5 #.....#.....#
   6 # ###.#.#####
   7 #.....#....##
   8 ###.###.#####
   9 ###.....#####
  10 #####.####.##
  11 ####...##..##
  12 #...#.#....##
  13 ###.#.#.#.#.#
  14 #...#...#...S
  15 #############"
 """)
print(m)
print ("find_it? ")
if m.solve()==True:
    print("OUI! ")
else:
    print("Ne pas, non...")
print(m)
