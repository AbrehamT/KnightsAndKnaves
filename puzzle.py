from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    # A character can either be a knave or a knight
    Or(AKnight, AKnave),
    # A character cannot be both a knight or a knave
    Or(Not(AKnight), Not(AKnave)),
    # If a character is a knight then whatever said has to be true
    Implication(AKnight, And(AKnight, AKnave)),
    # If a character is a knave then whatever said has to be false
    Implication(AKnave, Not(And(AKnave, AKnight)))    
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),
    
    Or(BKnight, BKnave),
    Or(Not(BKnight), Not(BKnave)),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),
    
    Or(BKnight, BKnave),
    Or(Not(BKnight), Not(BKnave)),
    
    # Or(And(AKnight, BKnight), And(AKnave, BKnave)), # Cannot be true according to the rules of the game
    # Or(And(AKnight, BKnave), And(AKnave, BKnight)), # True according to the rules of the game

    # If A is a knight then both are the same kind, but both cannot be of the same kind
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave then it is false that both are of the same kind
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    
    # If B is a knight then we are of a different kinds should be true
        # To be of different kinds means either A is a knight and B is a knave or A is a knave and B is a knight
    # If B is a knave then we are of a different kinds should be false
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(Not(AKnight), Not(AKnave)),

    Or(BKnight, BKnave),
    Or(Not(BKnight), Not(BKnave)),
    
    Or(CKnight, CKnave),
    Or(Not(CKnight), Not(CKnave)),
    
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    
    Implication(BKnight, Implication(AKnight, BKnave)),
    Implication(BKnave, Implication(AKnave, Not(BKnave))),
    
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


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
