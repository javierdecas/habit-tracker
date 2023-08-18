from db import get_all_habits, get_habits_periodicity, get_longest_streak, get_habit_data


def show_all_habits(db):
    """
    Show data from all habits

    :param db: on initialized sqLite3 database connection
    """
    for habit in get_all_habits(db):
        print("Name: " + str(habit[1]) + " Periodicity: " + str(habit[2]))


def show_habits_periodicity(db, periodicity):
    """
    Show data from habits with a certain periodicity

    :param db: on initialized sqLite3 database connection
    :param periodicity: periodicity of the habit
    """
    for habit in get_habits_periodicity(db, periodicity):
        print("Name: " + str(habit[1]))


def show_longest_streak(db, name):
    """
    Show the longest streak for a certain habits

    :param db: on initialized sqLite3 database connection
    :param name: name of the habit
    """
    habit = get_habit_data(db, name)
    print("Longest streak: " + str(habit[5]))


def show_all_longest_streak(db):
    """
    Show the longest streaks for all habits

    :param db: on initialized sqLite3 database connection
    """
    for habit in get_all_habits(db):
        print("Name: " + str(habit[1]) + " Longest streak: " + str(habit[5]))
