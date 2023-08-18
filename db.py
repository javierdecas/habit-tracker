import sqlite3
from datetime import date, timedelta, datetime
import datetime
from datetime import datetime


def get_db(name="main.db"):
    """
    Connect the db

    :param name: the name of the DB
    :return: on initialized sqLite3 database connection
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """
    Create the tables in the DB

    :param db: on initialized sqLite3 database connection
    """
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        periodicity TEXT,
        date_created DATE,
        current_streak INTEGER,
        longest_streak INTEGER)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date_completed DATE,
        habit_id INTEGER,
        FOREIGN KEY (habit_id) REFERENCES habits(id))""")

    db.commit()

    cursor.close()


def add_habit(db, name, periodicity):
    """
    Add a habit to 'habits' table

    :param db: on initialized sqLite3 database connection
    :param name: name of the habit
    :param periodicity: periodicity for the habit
    """
    cursor = db.cursor()
    date_created = date.today()
    cursor.execute("INSERT INTO habits VALUES (?, ?, ?, ?, ?, ?)", (None, name, periodicity, date_created, 0, 0))
    db.commit()
    cursor.close()


def delete_habit(db, habit_id):
    """
    Delete a habit from 'habits' table

    :param db: on initialized sqLite3 database connection
    :param habit_id: id of the habit
    """
    cursor = db.cursor()

    cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
    cursor.execute("DELETE FROM tracker WHERE habit_id = ?", (habit_id,))
    db.commit()
    cursor.close()

    print(f"Habit deleted successfully")


def complete_habit(db, habit_id, date_completed=None):
    """
    Complete a habit

    :param db: on initialized sqLite3 database connection
    :param habit_id: id of the habit
    :param date_completed: the date of today
    """
    cursor = db.cursor()
    if not date_completed:
        date_completed = date.today()
    cursor.execute("INSERT INTO tracker VALUES (?, ?)", (date_completed, habit_id))
    db.commit()
    cursor.close()

    print(f"Habit completed successfully")


def get_habit_data(db, name):
    """
    Get a habit with a certain name from 'habits' table

    :param db: on initialized sqLite3 database connection
    :param name: name of the habit
    :return: first row from the cursor
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM habits WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result is not None:
        return result
    cursor.close()


def get_all_habits(db):
    """
    Get all habits from DB

    :param db: on initialized sqLite3 database connection
    :return: all rows from the cursor
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM habits")
    return cursor.fetchall()

    cursor.close()


def get_habits_periodicity(db, periodicity):
    """
    Get all habits with a certain periodicity from 'habits' table

    :param db: on initialized sqLite3 database connection
    :param periodicity: periodicity for the habit
    :return: all rows from the cursor
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM habits WHERE periodicity = ?", (periodicity,))
    return cursor.fetchall()

    cursor.close()


def check_on_streak_daily(db, habit_id):
    """
    Check if the there is any record for a habit from yesterday

    :param db: on initialized sqLite3 database connection
    :param habit_id: id of the habit
    :return: first row of the cursor
    """
    cursor = db.cursor()
    # Get today's date
    today = date.today()

    # Calculate yesterday's date
    yesterday = today - timedelta(days=1)

    cursor.execute("SELECT * FROM tracker WHERE habit_id = ? AND date_completed = ?", (habit_id, yesterday))
    result = cursor.fetchone()
    if result is not None:
        return result
    cursor.close()


def check_on_streak_weekly(db, habit_id):
    """
    Check if the there is any record for a habit in the past week

    :param db: on initialized sqLite3 database connection
    :param habit_id: id of the habit
    :return: first row of the cursor
    """
    cursor = db.cursor()
    # Get today's date
    today = date.today()
    # Get date from 7 days ago
    last_week_day = today - timedelta(days=7)
    # Get last week's number
    year, last_week_number, day = last_week_day.isocalendar()

    cursor.execute("SELECT * FROM tracker WHERE habit_id = ? ORDER BY date_completed DESC", (habit_id,))
    result = cursor.fetchone()
    if result is not None:
        last_date_completed = datetime.strptime(result[0], '%Y-%m-%d').date()
    year, week_number, day = last_date_completed.isocalendar()
    print(week_number, last_week_number)
    if week_number == last_week_number:
        return 1
    cursor.close()


def add_streaks(db, habit_id, current_streak, longest_streak):
    """
    Add 'Current streak' and 'Longest streak' to 'habits' table

    :param db: on initialized sqLite3 database connection
    :param habit_id: id of the habit
    :param current_streak: current streak in days for the habit
    :param longest_streak: longest streak in days for the habit
    """
    cursor = db.cursor()

    cursor.execute("UPDATE habits SET current_streak = ?, longest_streak = ? WHERE id = ?",
                   (current_streak, longest_streak, habit_id))
    db.commit()
    cursor.close()

    print(f"Current streak: {current_streak}\n"
          f"Longest streak: {longest_streak}")


def check_name_exists(db, name):
    """
    Check if the name exits in 'habits' table

    :param db: on initialized sqLite3 database connection
    :param name: name of the habit
    :return: first row of the cursor
    """
    cursor = db.cursor()

    cursor.execute("SELECT * FROM habits WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result is not None:
        return result

    cursor.close()
