# Карточная игра "Пьяница"


from random import shuffle # импортируем метод для того, чтобы перемешать колоду карт


class Card: # класс, отвечающий за карты (создание объектов карт и их сравнение)
    
    suits = ["пикей", "червей", "бубей", "треф"] # переменная класса, которая хранит список мастей в порядке возрастания их силы
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "валета", "даму", "короля", "туза"] # аналогичная переменная со значениями карт

    def __init__(self, value, suit):
        # suit и value - целые числа
        self.value = value
        self.suit = suit

    def __lt__(self, other): # метод, позволяющий сравнивать два объекта карт (<) и возвращать True или False
        if self.value < other.value: # сравниваем значения карт, если значение первой карты меньше второй, возвращаем True
            return True
        if self.value == other.value: # если значение равны, сравниваем по масти
            if self.suit < other.suit:
                return True
            else:
                return False

    def __gt__(self, other): # метод, позволяющий сравнивать два объекта карт (>) и возвращать True или False
        if self.value > other.value:
            return True
        if self.value == other.value:  # действия, аналогичные методу __lt__ только с другим знаком
            if self.suit > other.suit:
                return True
            else:
                return False

    def __repr__(self):
        value = self.values[self.value] + " " + self.suits[self.suit]
        return value



class Deck: # класс, отвечающий за колоду (создание, перемешивание и вывод карт)
    
    def __init__(self):
        self.cards = [] # создаём список для карт (колоду)
        for i in range(2,15): # цикл от 2 до 15, т.к. значения карт - от 2 до туза (52 карты)
            for j in range(4): # цикл из 4 итераций, т.к. 4 масти
                self.cards.append(Card(i,j)) # добавляем объекта класса Card в созданный список (колоду)
        shuffle(self.cards) # перемешиваем колоду

    def take_card(self): # следим за тем, заканчивается ли колода, либо берём очередную карту
        if len(self.cards) == 0: # если длина списка (колоды) равна нулю, возвращаем None
            return
        return self.cards.pop() # удаляем последний на данный момент элемент списка (карту из колоды) и возвращаем



class Player: # класс, представляющий игрока (имя, карта, количество выигранных раундов)

    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0



class Game: # класс, предсталяющий саму игру
    
    def __init__(self): 
        name1 = input("Введите имя первого игрока: ")
        name2 = input("Введите имя второго игрока: ")
        self.deck = Deck() # создаём колоду
        self.player1 = Player(name1)
        self.player2 = Player(name2) # создаём игроков

    def round(self, winner): # выводим информацию о том, кто выиграл текущий раунд
        message = "{} забирает карты".format(winner)
        print(message)

    def draw(self, nameOfPlayer1, cardOfPlayer1, nameOfPlayer2, cardOfPlayer2): # выводим информацию о том, какие карты вытянули игроки из колоды в данном раунде
        message1 = "{} кладёт {}, а {} кладёт {}".format(nameOfPlayer1, cardOfPlayer1, nameOfPlayer2, cardOfPlayer2)
        print(message1)

    def winner(self, player1, player2): # определяем победителя
        if player1.wins > player2.wins:
            return player1.name
        elif player1.wins < player2.wins:
            return player2.name
        else:
            return "дружба"

    def play_game(self):
        cards = self.deck.cards # присваиваем переменной cards список (колоду) объекта deck класса Deck
        print("Игра началась! Поехали!")

        while len(cards) >= 2: # пока в колоде есть по крайней мере 2 карты
            response = input("Нажмите X для выхода или любую другую клавишу для продолжения: ")
            if response == "X":
                break
            cardOfPlayer1 = self.deck.take_card() # игроки вытягивают карты из колоды
            cardOfPlayer2 = self.deck.take_card() 
            nameOfPlayer1 = self.player1.name   # задаём имена игроков
            nameOfPlayer2 = self.player2.name
            self.draw(nameOfPlayer1, cardOfPlayer1, nameOfPlayer2, cardOfPlayer2) # выводим информацию о картах игроков
            if cardOfPlayer1 > cardOfPlayer2: # сравниваем карты игроков и определяем победителя раунда
                self.player1.wins += 1 #  в случае выигрыша увеличиваем на 1 счётчик побед в раундах
                self.round(self.player1.name) # выводим информацию об итогах раунда
            else:
                self.player2.wins += 1 # аналогично ветки if
                self.round(self.player2.name)

        victory = self.winner(self.player1, self.player2) # узнаём победителя игры, вызвав функцию winner
        print("Игра окончена! Победил(а) {}!".format(victory)) # выводим информацию о результатах игры
        
                              
        
game = Game() # создаём игру (объект класса Game)
game.play_game() # начинаем играть 
