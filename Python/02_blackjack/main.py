import random


class BlackJack:
    deck_cards = [('2 бубны', 2), ('2 черви', 2), ('2 крести', 2), ('2 пики', 2),
                  ('3 бубны', 3), ('3 черви', 3), ('3 крести', 3), ('3 пики', 3),
                  ('4 бубны', 4), ('4 черви', 4), ('4 крести', 4), ('4 пики', 4),
                  ('5 бубны', 5), ('5 черви', 5), ('5 крести', 5), ('5 пики', 5),
                  ('6 бубны', 6), ('6 черви', 6), ('6 крести', 6), ('6 пики', 6),
                  ('7 бубны', 7), ('7 черви', 7), ('7 крести', 7), ('7 пики', 7),
                  ('8 бубны', 8), ('8 черви', 8), ('8 крести', 8), ('8 пики', 8),
                  ('9 бубны', 9), ('9 черви', 9), ('9 крести', 9), ('9 пики', 9),
                  ('10 бубны', 10), ('10 черви', 10), ('10 крести', 10), ('10 пики', 10),
                  ('Валет бубны', 10), ('Валет черви', 10), ('Валет крести', 10), ('Валет пики', 10),
                  ('Дама бубны', 10), ('Дама черви', 10), ('Дама крести', 10), ('Дама пики', 10),
                  ('Колорь бубны', 10), ('Король черви', 10), ('Король крести', 10), ('Король пики', 10),
                  ('Туз бубны', 11), ('Туз черви', 11), ('Туз крести', 11), ('Туз пики', 11)
                  ]


class Player:

    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.on_hands = []
        for _ in range(2):
            self.issuing_card()

    def issuing_card(self):
        card = random.choice(BlackJack.deck_cards)
        self.on_hands.append(card[0])
        BlackJack.deck_cards.remove(card)
        if self.score > 21 and card[1] == 11:
            self.score += 1
        else:
            self.score += card[1]

    def info_card_on_hand(self):
        print('Карты на руках у {} - {}, кол-во очков: {}'.format(self.name, self.on_hands, self.score))


dealer = Player('Dealer')
player = Player('Ben')

print('Игра начинается!\n')

while player.score < 21:
    player.info_card_on_hand()
    answer = int(input('Будете брать карту(1 - "Да"; 0 - "Нет"): '))
    if answer == 1:
        player.issuing_card()
    elif answer == 0:
        break
    else:
        print('Неверная команда!')

print()
if 21 >= player.score > dealer.score:
    print('Вы выиграли! Вскрываем карты.')
elif player.score == dealer.score:
    print('Ничья')
else:
    print('Вы проиграли! Вскрываем карты.')

player.info_card_on_hand()
dealer.info_card_on_hand()


