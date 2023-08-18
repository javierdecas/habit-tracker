from db import add_habit, delete_habit, complete_habit, get_habit_data, check_on_streak_daily, add_streaks, \
    check_on_streak_weekly


class Habit:
    def __init__(self, name: str, periodicity: str = None):
        """
        Habit class

        :param name: name of the habit
        :param periodicity: periodicity of the habit
        """
        self.id = id
        self.name = name
        self.periodicity = periodicity
        self.current_streak = 0
        self.longest_streak = 0

    def store(self, db):
        """
        Store habit data

        :param db: on initialized sqLite3 database connection
        """
        add_habit(db, self.name, self.periodicity)

    def get_data(self, db):
        """
        Get habit data

        :param db: on initialized sqLite3 database connection
        :return: all habit data
        """
        habit = get_habit_data(db, self.name)

        return habit

    def complete(self, db, habit_data):
        """
        Complete a habit

        :param db: on initialized sqLite3 database connection
        :param habit_data: all habit data
        """
        complete_habit(db, habit_data[0])

    def delete(self, db, habit_data):
        """
        Delete habit

        :param db: on initialized sqLite3 database connection
        :param habit_data: all habit data
        """
        delete_habit(db, habit_data[0])

    def check_streaks(self, db, habit_data):
        """
        Check if the habit is on streak and updates the longest streak

        :param db: on initialized sqLite3 database connection
        :param habit_data: all habit data
        """
        if habit_data[2] == "Daily":
            if check_on_streak_daily(db, habit_data[0]):
                current_streak = habit_data[4] + 1
            else:
                current_streak = 1
        elif habit_data[2] == "Weekly":
            if check_on_streak_weekly(db, habit_data[0]):
                current_streak = habit_data[4] + 1
            else:
                current_streak = 1
        if current_streak > habit_data[5]:
            longest_streak = current_streak
        else:
            longest_streak = habit_data[5]
        add_streaks(db, habit_data[0], current_streak, longest_streak)

    def __str__(self):
        return f"Name: {self.name} - Periodicity: {self.periodicity} - Current streak: {self.current_streak} - " \
               f"Longest streak: {self.longest_streak}"
