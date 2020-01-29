'''
Created on January 28, 2020

Created a method that provides probabilities for rolling sums on a set of dice.

@author: Nelson H
'''

from random import randint
import itertools
import string

class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides_list = []
        for i in range(1, self.number_of_sides + 1):
            self.sides_list.append(i)

    def __repr__(self):
        return {'number_of_sides': self.number_of_sides, 'sides_list': str(self.sides_list)}

    def __str__(self):
        return 'Dice(number_of_sides=' + str(self.number_of_sides) + ', sides_list=' + str(self.sides_list) + ')'

    def roll(self):
        return randint(1, self.number_of_sides)


class DiceChart:
    def __init__(self, dice_string):
        self.dice_list = self.parse_dice(dice_string)
        self.number_of_dice = len(self.dice_list)
        self.minimum_sum = len(self.dice_list)
        self.maximum_sum = self.calculate_max_dice_sum()
        self.possible_outcomes = self.calculate_possible_outcomes()
        self.base_probability = 1 / self.possible_outcomes
        self.dice_chart = self.generate_dice_chart()

    def parse_dice(self, dice_string):
        dice_string = dice_string.translate({ord(c): None for c in string.whitespace})  ## Removing whitespaces
        raw_dice_list = dice_string.split(",")
        dice_list = []
        for i in range(0, len(raw_dice_list)):
            raw_dice = raw_dice_list[i]
            d_position = int(raw_dice.find("d"))
            if self.is_int(raw_dice[:d_position]):
                num_dice = int(raw_dice[:d_position])
            else:
                num_dice = 1
            num_sides = int(raw_dice[d_position + 1:])
            for j in range(0, num_dice):
                dice_list.append(Dice(num_sides))
        return dice_list

    def is_int(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True

    def calculate_max_dice_sum(self):
        dice_sum = 0
        for i in range(0, len(self.dice_list)):
            dice = self.dice_list[i]
            dice_sum = dice_sum + dice.number_of_sides
        return dice_sum

    def calculate_possible_outcomes(self):
        dice_product = 1
        for i in range(0, len(self.dice_list)):
            dice = self.dice_list[i]
            dice_product = dice_product * dice.number_of_sides
        return dice_product

    def generate_dice_chart(self):
        dice_chart = []
        for i in range(self.minimum_sum, self.maximum_sum + 1):
            dice_chart.append([i, 0, 0, 0])

        dice_sides_list = []
        for i in range(0,len(self.dice_list)):
            dice_sides = self.dice_list[i].sides_list
            dice_sides_list.append(dice_sides)

        sides_product = []
        for element in itertools.product(*dice_sides_list):
            sides_product.append(element)

        for i in range(0, len(dice_chart)):
            for j in range(0, len(sides_product)):
                dice_rolls = sides_product[j]
                roll_sum = sum(dice_rolls)
                if roll_sum == dice_chart[i][0]:
                    dice_chart[i][1] = dice_chart[i][1] + 1

        for i in range(0, len(dice_chart)):
            p = self.base_probability
            dice_chart[i][2] = round(dice_chart[i][1] * p, 5)

        for i in range(0, len(dice_chart)):
            if i == 0:
                dice_chart[i][3] = 1
            else:
                dice_chart[i][3] = round(dice_chart[i - 1][3] - dice_chart[i - 1][2], 5)

        return dice_chart

    def printChart(self):
        for row in self.dice_chart:
            for elem in row:
                print(elem, end=' ')
            print()

def main():
    dice_string = str(sys.argv[1])

    if len(sys.argv) == 1:
        chart = DiceChart("1d10, 1d8")
        print("the dice's number of dice is:'")
        print(chart.number_of_dice)
        print("the total number of outcomes are")
        print(chart.possible_outcomes)
        print(chart.printChart())
    else:
        chart = DiceChart(dice_string)
        print("the dice's number of dice is:'")
        print(chart.number_of_dice)
        print("the total number of outcomes are")
        print(chart.possible_outcomes)
        print(chart.printChart())

if __name__ == '__main__':
    import sys
    main()