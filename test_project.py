from db import *
from habit import Habit
import os


class TestHabitTracker:

    def setup_method(self):
        self.db = get_db("test.db")

        # Habit no streak no longest daily
        add_habit(self.db, "test 1", "Daily")
        complete_habit(self.db, 1, date.today() - timedelta(days=2))
        complete_habit(self.db, 1, date.today() - timedelta(days=3))

        complete_habit(self.db, 1, date.today() - timedelta(days=6))
        complete_habit(self.db, 1, date.today() - timedelta(days=7))
        complete_habit(self.db, 1, date.today() - timedelta(days=8))

        complete_habit(self.db, 1, date.today() - timedelta(days=11))

        complete_habit(self.db, 1, date.today() - timedelta(days=14))
        complete_habit(self.db, 1, date.today() - timedelta(days=15))

        complete_habit(self.db, 1, date.today() - timedelta(days=19))

        complete_habit(self.db, 1, date.today() - timedelta(days=23))

        complete_habit(self.db, 1, date.today() - timedelta(days=25))

        complete_habit(self.db, 1, date.today() - timedelta(days=28))

        complete_habit(self.db, 1, date.today() - timedelta(days=30))

        add_streaks(self.db, 1, 1, 3)

        # Habit no streak no longest weekly
        add_habit(self.db, "test 2", "Weekly")
        complete_habit(self.db, 2, date.today() - timedelta(weeks=2))
        complete_habit(self.db, 2, date.today() - timedelta(weeks=3))

        add_streaks(self.db, 2, 1, 2)

        # Habit streak longest daily
        add_habit(self.db, "test 3", "Daily")

        complete_habit(self.db, 3, date.today() - timedelta(days=1))
        complete_habit(self.db, 3, date.today() - timedelta(days=2))

        complete_habit(self.db, 3, date.today() - timedelta(days=6))
        complete_habit(self.db, 3, date.today() - timedelta(days=7))

        complete_habit(self.db, 3, date.today() - timedelta(days=11))

        complete_habit(self.db, 3, date.today() - timedelta(days=14))
        complete_habit(self.db, 3, date.today() - timedelta(days=15))

        complete_habit(self.db, 3, date.today() - timedelta(days=19))

        complete_habit(self.db, 3, date.today() - timedelta(days=23))

        complete_habit(self.db, 3, date.today() - timedelta(days=25))

        complete_habit(self.db, 3, date.today() - timedelta(days=28))

        complete_habit(self.db, 3, date.today() - timedelta(days=30))

        add_streaks(self.db, 3, 2, 3)

        # Habit streak longest weekly
        add_habit(self.db, "test 4", "Weekly")
        complete_habit(self.db, 4, date.today() - timedelta(weeks=1))
        complete_habit(self.db, 4, date.today() - timedelta(weeks=2))

        complete_habit(self.db, 4, date.today() - timedelta(weeks=4))

        add_streaks(self.db, 4, 2, 2)

        # Habit streak no longest daily
        add_habit(self.db, "test 5", "Daily")

        complete_habit(self.db, 5, date.today() - timedelta(days=1))
        complete_habit(self.db, 5, date.today() - timedelta(days=2))

        complete_habit(self.db, 5, date.today() - timedelta(days=6))
        complete_habit(self.db, 5, date.today() - timedelta(days=7))

        complete_habit(self.db, 5, date.today() - timedelta(days=11))

        complete_habit(self.db, 5, date.today() - timedelta(days=14))
        complete_habit(self.db, 5, date.today() - timedelta(days=15))
        complete_habit(self.db, 5, date.today() - timedelta(days=16))
        complete_habit(self.db, 5, date.today() - timedelta(days=17))

        complete_habit(self.db, 5, date.today() - timedelta(days=19))

        complete_habit(self.db, 5, date.today() - timedelta(days=23))

        complete_habit(self.db, 5, date.today() - timedelta(days=25))

        complete_habit(self.db, 5, date.today() - timedelta(days=28))

        complete_habit(self.db, 5, date.today() - timedelta(days=30))

        add_streaks(self.db, 5, 3, 5)

        # Habit streak no longest weekly
        add_habit(self.db, "test 6", "Weekly")

        complete_habit(self.db, 6, date.today() - timedelta(weeks=1))

        complete_habit(self.db, 6, date.today() - timedelta(weeks=3))
        complete_habit(self.db, 6, date.today() - timedelta(weeks=4))
        complete_habit(self.db, 6, date.today() - timedelta(weeks=5))

        add_streaks(self.db, 6, 1, 4)

    def test_habit(self):
        # Habit no streak no longest
        habit = Habit("test 1")
        habit_data = habit.get_data(self.db)
        habit.check_streaks(self.db, habit_data)
        habit.complete(self.db, habit_data)
        habit_data = habit.get_data(self.db)

        assert habit_data[4] == 1
        assert habit_data[5] == 3

        habit = Habit("test 2")
        habit_data = habit.get_data(self.db)
        habit.check_streaks(self.db, habit_data)
        habit.complete(self.db, habit_data)
        habit_data = habit.get_data(self.db)

        assert habit_data[4] == 1
        assert habit_data[5] == 2

        # Habit streak longest
        habit = Habit("test 3")
        habit_data = habit.get_data(self.db)
        habit.check_streaks(self.db, habit_data)
        habit.complete(self.db, habit_data)
        habit_data = habit.get_data(self.db)

        assert habit_data[4] == 3
        assert habit_data[5] == 3

        habit = Habit("test 4")
        habit_data = habit.get_data(self.db)
        habit.check_streaks(self.db, habit_data)
        habit.complete(self.db, habit_data)
        habit_data = habit.get_data(self.db)

        assert habit_data[4] == 3
        assert habit_data[5] == 3

        # Habit streak no longest
        habit = Habit("test 5")
        habit_data = habit.get_data(self.db)
        habit.check_streaks(self.db, habit_data)
        habit.complete(self.db, habit_data)
        habit_data = habit.get_data(self.db)

        assert habit_data[4] == 4
        assert habit_data[5] == 5

        habit = Habit("test 6")
        habit_data = habit.get_data(self.db)
        habit.check_streaks(self.db, habit_data)
        habit.complete(self.db, habit_data)
        habit_data = habit.get_data(self.db)

        assert habit_data[4] == 2
        assert habit_data[5] == 4

    def teardown_method(self):
        self.db.close()

        os.remove("test.db")
