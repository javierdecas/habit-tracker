import questionary

# from analyze import calculate_count
from habit import Habit
from db import *
from analyze import *


def cli():
    db = get_db()

    stop = False
    while not stop:
        choice = questionary.select(
            "What do you want to do?",
            choices=["Create", "Complete", "Delete", "Analyze", "Exit"]
        ).ask()

        if choice == "Create":
            name = questionary.text("What's the name of the habit?").ask()
            if check_name_exists(db, name):
                print(f"Habit with name {name} already exists")
            else:
                peridiocity = questionary.select(
                    "What's the periodicity of your habit?",
                    choices=["Daily", "Weekly"]).ask()
                habit = Habit(name, peridiocity)
                habit.store(db)
                print(f"Habit created successfully with name {name}")
        elif choice == "Complete":
            name = questionary.text("What's the name of the habit?").ask()
            habit = Habit(name)
            habit_data = habit.get_data(db)
            if habit_data:
                habit.check_streaks(db, habit_data)
                habit.complete(db, habit_data)
            else:
                print(f"Habit does not exist")
        elif choice == "Delete":
            name = questionary.text("What's the name of the habit?").ask()
            habit = Habit(name)
            habit_data = habit.get_data(db)
            if habit_data:
                habit.delete(db, habit_data)
            else:
                print(f"Habit does not exist")
        elif choice == "Analyze":
            choice = questionary.select(
                "What data would you like to see?",
                choices=["All Habits", "Habits with same periodicity", "Longest run streak",
                         "Longest run streak for a certain habit"]).ask()
            if choice == "All Habits":
                show_all_habits(db)
            elif choice == "Habits with same periodicity":
                periodicity = questionary.select("What periodicity?", choices=["Daily", "Weekly"]).ask()
                show_habits_periodicity(db, periodicity)
            elif choice == "Longest run streak":
                show_all_longest_streak(db)
            elif choice == "Longest run streak for a certain habit":
                name = questionary.text("What's the name of the habit?").ask()
                show_longest_streak(db, name)
        else:
            print("Bye!")
            stop = True


if __name__ == '__main__':
    cli()
