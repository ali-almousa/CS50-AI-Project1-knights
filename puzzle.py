from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")



##############################################################################################################
# Puzzle 0
##############################################################################################################
# A says "I am both a Knight and a Knave."
knowledge0 = And(
    # A can be a knave or a knight but not both
    Implication(AKnave, Not(AKnight)),
    # if what A is saying is not true then he has to be a knave
    Implication(Not(And(AKnight, AKnave)), AKnave)
)

##############################################################################################################
# Puzzle 1
##############################################################################################################
# A says "We are both knaves"
# B says nothing
knowledge1 = And(
    # By definition every character is either a knight or a knave but not both
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    # if A is a knight then what he said is true: A and B are knaves (even though this is contradictory but this
    # is how the information is represented. will let the AI do his part and inference that A is lying!(knave)).
    Implication(AKnight, And(AKnave, BKnave)),
    # if A is knave then he is lying about the identity of B
    Implication(AKnave, Not(BKnave))
)

##############################################################################################################
# Puzzle 2
##############################################################################################################
# A says "We are the same kind"
# B says "We are of different kind"
knowledge2 = And(
    # By definition every character is either a knight or a knave but not both
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    # if the piece of info told by A is true then A and B must be knights
    Implication(Or(And(AKnight, BKnight), And(AKnave, BKnave)), And(AKnight, BKnight)),
    # if the piece of info told by B is true then B must be a knight and A must be a knave
    Implication(Or(And(AKnight, BKnave), And(AKnave, BKnight)), And(BKnight, AKnave)),
    # if B is a knight then A is a knave, since B is opposing A
    Implication(BKnight, AKnave),
)
# The following is Extra knowledge for KB2 that is not needed to reach the conclusion
# nonetheless, I added them just in case I made a mistake above:
## if the piece of info told by B is not true then B must be a knave
# Implication(Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))), BKnave),
## if the piece of info told by A is not true then A must be a knave
# Implication(Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))), AKnave),
## finally if A is a knight then B is a knight too, since A is saying we are the same kind
# Implication(AKnight, BKnight)

##############################################################################################################
# Puzzle 3
##############################################################################################################
# A says either "I am a knight." or "I am a knave", but you don't know which
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # By definition every character is either a knight or a knave but not both
    And(Or(AKnight, AKnave), Or(BKnave, BKnight), Or(CKnight, CKnave)),
    # if A is a knight then, C is saying the truth (knight), B is saying the untruth about what A said since
    # A can't say but the truth about himself and therefore B is knave.
    Implication(AKnight, And(CKnight, BKnave)),
    # if C is a knight then, A is a knight and B is a knave since he is lying
    Implication(CKnight, And(AKnight, BKnave)),
    # if A is a knave then, B is a knave too since A can't be saying the truth about himself, and C is a knight,
    # as B can't be saying the truth about C.
    Implication(AKnave, And(BKnave, CKnight)),
)
# Extra knowledge for KB3 that will not alter the result at all because they are already implied previously:
## if B is a knight then, C is a knave, and A is a knave then C can't be saying the truth about A.
# Implication(BKnight, And(CKnave, AKnave)),
## if B is a knave then, C is a knight, and A is a knight
# Implication(BKnave, And(AKnight, CKnight))
## if C is a knave, then B is saying the truth (knight), and A is a knave since C can't be saying the truth about A.
# Implication(CKnave, And(BKnight, AKnave)),



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
