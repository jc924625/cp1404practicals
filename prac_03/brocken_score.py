
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
def main():
    #score = float(input("Enter score: "))
    score = random.randint(0, 100)
    scores = sort_score(score)
    print(f"Your score {score} has the grade {sort_score(score)}")

def sort_score(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"

main()