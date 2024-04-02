from random import sample

goals = [str(n) for n in input('Enter a new goal: ')]

get_goals = sample(goals, k=3)