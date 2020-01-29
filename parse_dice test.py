"""
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
"""
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

def parse_dice(dice_string):
    dice_string = dice_string.translate({ord(c): None for c in string.whitespace})  ## Removing whitespaces
    raw_dice_list = dice_string.split(",")
    dice_list = []
    for i in range(0, len(raw_dice_list)):
        raw_dice = raw_dice_list[i]
        d_position = int(raw_dice.find("d"))
        if isinstance(raw_dice[:d_position], int):
            num_dice = int(raw_dice[:d_position])
        else:
            num_dice = 1
        num_sides = int(raw_dice[d_position + 1:])
        for j in range(0, num_dice):
            dice_list.append(Dice(num_sides))
    return dice_list

dice = parse_dice("d6")

for i in range(0,len(dice)):
    print(dice[i])