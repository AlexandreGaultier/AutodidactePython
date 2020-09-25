class Player:
    def __init__(self):
        self.name = ""
        self.side = ""


class Main:

    def __init__(self):
        print('!! Morpion !!')

        self.GameOver = False

        p1Name = str(input("Entrer le nom du joueur 1 : "))
        self.p1 = Player()
        self.p1.name = p1Name
        self.p1.side = "X"

        p2Name = str(input("Entrer le nom du joueur 2 : "))
        self.p2 = Player()
        self.p2.name = p2Name
        self.p2.side = "O"

        self.board = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]

    def DisplayBoard(self):
        for row in self.board:
            print("")
            for case in row:
                print("|", end="")
                print(case, end="")
                print("|", end="")

        print(" ")

    def Play(self, Player):
        print(" ")
        print(Player.name + " où voulez-vous jouer ?")
        choice = int(input())

        for i in range(len(self.board)):
            try:
                index = self.board[i].index(choice)
            except ValueError:
                index = -1
            if index != -1:
                self.board[i].remove(choice)
                self.board[i].insert(index, Player.side)

        self.DisplayBoard()

    def CheckWin(self):
        if (self.board[0][0] == self.board[0][1]) and (self.board[0][0] == self.board[0][2]) and (
                self.board[0][0] == 'X') or (self.board[1][0] == self.board[1][1]) and (
                self.board[1][0] == self.board[1][2]) and (self.board[1][0] == 'X') or (
                self.board[2][0] == self.board[2][1]) and (self.board[2][0] == self.board[2][2]) and (
                self.board[2][0] == 'X') or (self.board[0][0] == self.board[1][0]) and (
                self.board[0][0] == self.board[2][0]) and (self.board[0][0] == 'X') or (
                self.board[0][1] == self.board[1][1]) and (self.board[0][1] == self.board[2][1]) and (
                self.board[0][1] == 'X') or (self.board[0][2] == self.board[1][2]) and (
                self.board[0][2] == self.board[2][2]) and (self.board[0][2] == 'X') or (
                self.board[0][0] == self.board[1][1]) and (self.board[0][0] == self.board[2][2]) and (
                self.board[0][0] == 'X') or (self.board[0][2] == self.board[1][1]) and (
                self.board[0][2] == self.board[2][0]) and (self.board[0][2] == 'X'):
            self.GameOver = True
            print(self.j1 + "à gagné")

            if (self.board[0][0] == self.board[0][1]) and (self.board[0][0] == self.board[0][2]) and (
                    self.board[0][0] == 'O') or (self.board[1][0] == self.board[1][1]) and (
                    self.board[1][0] == self.board[1][2]) and (self.board[1][0] == 'O') or (
                    self.board[2][0] == self.board[2][1]) and (self.board[2][0] == self.board[2][2]) and (
                    self.board[2][0] == 'O') or (self.board[0][0] == self.board[1][0]) and (
                    self.board[0][0] == self.board[2][0]) and (self.board[0][0] == 'O') or (
                    self.board[0][1] == self.board[1][1]) and (self.board[0][1] == self.board[2][1]) and (
                    self.board[0][1] == 'O') or (self.board[0][2] == self.board[1][2]) and (
                    self.board[0][2] == self.board[2][2]) and (self.board[0][2] == 'O') or (
                    self.board[0][0] == self.board[1][1]) and (self.board[0][0] == self.board[2][2]) and (
                    self.board[0][0] == 'O') or (self.board[0][2] == self.board[1][1]) and (
                    self.board[0][2] == self.board[2][0]) and (self.board[0][2] == 'O'):
                self.GameOver = True
                print(self.j2 + "à gagné")


def Begin():
    # Demande aux joueurs où ils veulent placer leurs signes
    main = Main()
    print("_______")
    print("MORPION")
    print("_______")
    print(main.p1.name + "  vs  " + main.p2.name)
    print("_______")

    main.DisplayBoard()

    while main.GameOver == False:
        main.Play(main.p1)
        main.Play(main.p2)


if __name__ == '__main__':
    Begin()
