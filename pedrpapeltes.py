class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, selecione pedra, papel, tesoura, lagarto ou spock: ".format(name = self.name))
        print("{name} selecionou {choice}".format(name = self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher = {
            "pedra": 0,
            "papel": 1,
            "tesoura": 2,
            "lagarto": 3,
            "spock": 4
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]

        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("O resultado do round foi {result}".format(result = self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
        else:
            print("Pontos para ninguem")

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def awardPoints(self):
        print("implement")
    def getResultAsString(self, result):
        res = {
            0: "empate",
            1: "vitoria",
            -1: "derrota"
        }
        return res[result]    

class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant(input("Player 1: "))
        self.secondParticipant = Participant(input("Player 2: "))
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue? y/n. ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("O jogo acabou, {p1name} tem {p1points} e {p2name} tem {p2points}".format(p1name=self.participant.name, p1points=self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True 

    def determineWinner(self):
        resultString = "Deu empate"
        if self.participant.points > self.secondParticipant.points:
            resultString = "O vencedor é {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "O vencedor é {name}".format(name=self.secondParticipant.name)
        
        print(resultString)

game = Game()
game.start()