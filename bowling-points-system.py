def Score(obj, attempt):
    for obj in Frames:
        if obj.move > 0:
            obj.score += attempt
            obj.move -= 1

def SpareBonusThrow(obj, obj2):
    bonusAttempt = int(input("10. frame, bonus attempt: "))
    while bonusAttempt < 0 or bonusAttempt > 10:
        print("You can only knock down 0-10 pins.")
        bonusAttempt = int(input("10. frame, bonus attempt: ".format(i+1)))
    obj.score += bonusAttempt

    if obj2.move == 1:
        obj2.score += bonusAttempt
        obj2.move -= 1

def StrikeBounsThrows(obj, obj2):
    bonusAttempt1 = int(input("10. frame, 1. bonus attempt: "))
    while bonusAttempt1 < 0 or bonusAttempt1 > 10:
        print("You can only knock down 0-10 pins.")
        bonusAttempt1 = int(input("10. frame, 1. bonus attempt: ".format(i+1)))
    obj.score += bonusAttempt1

    if obj2.move == 1:
        obj2.score += bonusAttempt1
        obj2.move -= 1

    bonusAttempt2 = int(input("10. frame, 2. bonus attempt: "))
    while bonusAttempt2 < 0 or bonusAttempt2 > 10:
        print("You can only knock down 0-10 pins.")
        bonusAttempt2 = int(input("10. frame, 2. bonus attempt: ".format(i+1)))
    obj.score += bonusAttempt2

def PrintFrameScore(obj, score):
    for i in range(len(obj)):
        score += obj[i].score
        if obj[i].move == 0 and obj[i].printed == False and i < 9:
            print("Score in frame {0}. ---> {1}.".format(i+1, score))
            obj[i].printed = True
        if i == 9 and obj[i].printed == False:
            print("Score in frame {0}. ---> {1}.".format(i+1, score))
            obj[i].printed = True
    
class Frame:
    def __init__(self, attempt1, attempt2=0):
        self.attempt1 = attempt1
        self.attempt2 = attempt2

        if self.attempt1 == 10:
            self.move = 2
        elif self.attempt1 + self.attempt2 == 10:
            self.move = 1
        else:
            self.move = 0

        self.score = self.attempt1 + self.attempt2
        self.printed = False

Frames = []
score = 0

for i in range (10):
    
    attempt1 = int(input("{0}. frame, attempt 1: ".format(i+1)))
    while attempt1 < 0 or attempt1 > 10:
        print("You can only knock down 0-10 pins.")
        attempt1 = int(input("{0}. frame, attempt 1: ".format(i+1)))
    Score(Frames, attempt1)
    PrintFrameScore(Frames, score)

    if attempt1 < 10:
        attempt2 = int(input("{0}. frame, attempt 2: ".format(i+1)))
        while attempt2 < 0 or attempt2 > 10-attempt1:
            print("You can only knock down 0-{0} pins.".format(10-attempt1))
            attempt2 = int(input("{0}. frame, attempt 2: ".format(i+1)))
        Score(Frames, attempt2)
        PrintFrameScore(Frames, score)
        Frames.append(Frame(attempt1,attempt2))

        if i==9 and attempt1 + attempt2 == 10:
            SpareBonusThrow(Frames[i], Frames[i-1])
            PrintFrameScore(Frames, score)
    else:
        Frames.append(Frame(attempt1))

        if i==9 and attempt1 == 10:
            StrikeBounsThrows(Frames[i], Frames[i-1])
            PrintFrameScore(Frames, score)

    PrintFrameScore(Frames, score)
