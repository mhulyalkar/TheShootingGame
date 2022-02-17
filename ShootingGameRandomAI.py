from random import randint

class ShootingGame:
    def __init__(self, Player1, Player2):
        self.Player1 = Player1
        self.Player2 = Player2

    def __str__(self):
        return str(self.num)
    def PlayGame(self):
        Player1 = self.Player1
        Player2 = self.Player2

        while True:
            Player1Move = Player1.getMove()
            Player2Move = Player2.getMove()
            if Player1Move != Player2Move:
                if Player1Move == "shoot" and Player2Move == "reload":
                    print(str(Player1.getName()) + " WINS")
                    break
                if Player2Move == "shoot" and Player1Move == "reload":
                    print(str(Player2.getName()) + " WINS")
                    break
            if Player1.getAmmo() >= 5 and Player2.getAmmo() >= 5:
                Player1.ammo -= 5
                Player2.ammo -= 5
            if Player1.getAmmo() >= 5:
                print(str(Player1.getName()) + " WINS")
                break
            if Player2.getAmmo() >= 5:
                print(str(Player2.getName()) + " WINS")
                break
            print(Player1.getName() + "'s Move: " + str(Player1Move))
            print(Player2.getName() + "'s Move: " + str(Player2Move))
        print(str(Player1.getName() + "'s Moves: " + str(Player1.MoveHistory)))
        print(str(Player2.getName() + "'s Moves: " + str(Player2.MoveHistory)))
    def PlayGameNoMessage(self):
        Player1 = self.Player1
        Player2 = self.Player2

        while True:
            Player1Move = Player1.getMove()
            Player2Move = Player2.getMove()
            if Player1Move != Player2Move:
                if Player1Move == "shoot" and Player2Move == "reload":
                    return 0
                if Player2Move == "shoot" and Player1Move == "reload":
                    return 1
            if Player1.getAmmo() >= 5 and Player2.getAmmo() >= 5:
                Player1.ammo -= 5
                Player2.ammo -= 5
            if Player1.getAmmo() >= 5:
                return 0
            if Player2.getAmmo() >= 5:
                return 1

class Player:
    def __init__(self, name="Player", ammo=0):
        self.ammo = ammo
        self.name = name
        self.MoveSet = ["shoot", "block", "reload"]
        self.MoveHistory = list()

    def __str__(self):
        return str(self.name) + " ammo:" + str(self.ammo)

    def getMove(self):
        userMove = input("What move would you like to do: ")
        if userMove not in self.MoveSet:
            userMove = input("Not Recognizable move, TRY AGAIN: ")
        elif userMove == "shoot" and self.ammo == 0:
            userMove = input("No Ammo, TRY AGAIN: ")
        elif userMove == "shoot":
            self.ammo -= 1
        if userMove == "reload":
            self.ammo += 1
        self.MoveHistory.append(userMove)
        return userMove
    def getAmmo(self):
        return self.ammo
    def getName(self):
        return self.name

class AI:
    def __init__(self, name="AI", ammo=0):
        self.ammo = ammo
        self.name = name
        self.MoveSet = ["shoot", "block", "reload"]
        self.MoveHistory = list()

    def __str__(self):
        return str(self.name) + " ammo:" + str(self.ammo)

    def getMove(self):
        if len(self.MoveHistory) == 0:
            self.MoveHistory.append("reload")
            return "reload"
        aiMove = self.MoveSet[randint(0, 2)]
        if self.ammo > 0:
            aiMove = self.MoveSet[randint(0, 2)]
        else:
            aiMove = self.MoveSet[randint(1, 2)]
        if aiMove == "reload":
            self.ammo += 1
        elif aiMove == "shoot":
            self.ammo -= 1
        self.MoveHistory.append(aiMove)
        return aiMove
    def getName(self):
        return self.name
    def getAmmo(self):
        return self.ammo

class RandomAggressionAI(AI):
    def __init__(self, name="AI", ammo=0, aggression=50):
        super().__init__(name, ammo)
        self.aggression = aggression

    def __str__(self):
        return super().__str__() + "aggression: " + str(self.aggression)

    def getMove(self):
        if len(self.MoveHistory) == 0:
            self.MoveHistory.append("reload")
            return "reload"
        if self.ammo > 0:
            if randint(0, 100) < self.aggression:
                if randint(0,1) == 1:
                    AIMove = "shoot"
                else:
                    AIMove = "reload"
            else:
                AIMove = "block"
        else:
            if randint(0, 100) < self.aggression:
                AIMove = "reload"
            else:
                AIMove = "block"
        if AIMove == "reload":
            self.ammo += 1
        elif AIMove == "shoot":
            self.ammo -= 1
        self.MoveHistory.append(AIMove)
        return AIMove

Game = ShootingGame(Player(),
                    RandomAggressionAI("I am Inevitable", 0, 70))
Game.PlayGame()
