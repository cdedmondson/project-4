class ComboLock:
    combination = []  # Combination list to store dial input
    correct_combination = ['right', 1, 'left', 2, 'right', 3]  # Hold correct lock combination

    # Constructor
    def __init__(self, number):
        self.number = number

    # Reset lock combination to 0
    def reset(self):
        self.combination = 0

    # If combination is correct open lock
    def open(self):
        if self.combination == self.correct_combination:
            return print('Combo lock open!')
        else:
            return print('Incorrect combination')

    # Turn lock left n numbers
    def turnLeft(self, num):
        ComboLock.combination.append('left')
        ComboLock.combination.append(num)

    # Turn lock right n numbers
    def turnRight(self, num):
        ComboLock.combination.append('right')
        ComboLock.combination.append(num)


lock = ComboLock(0)  # Create and initialize lock object

# Test1
print("Test#1")
lock.turnRight(1)
lock.turnLeft(2)
lock.turnRight(3)
lock.open()

lock.reset()
print()

# Test2
print("Test#2")
lock.turnRight(1)
lock.turnLeft(4)
lock.turnRight(3)

lock.open()
