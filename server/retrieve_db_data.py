# %%
import sqlite3
import pandas as pd


def main():
    sqliteConnection = sqlite3.connect('external_data.db')

    sql_query = """SELECT name FROM sqlite_master  
    WHERE type='table';"""

    cursor = sqliteConnection.cursor()
    cursor.execute(sql_query)
    print(cursor.fetchall())

    df = pd.read_sql_query("SELECT * from Documents", sqliteConnection)

    # Verify that result of SQL query is stored in the dataframe
    print(df.columns)

    df = pd.read_sql_query("SELECT * from Experiments", sqliteConnection)

    # Verify that result of SQL query is stored in the dataframe
    print(df.columns)

    df = pd.read_sql_query("SELECT * from Sequences", sqliteConnection)

    # Verify that result of SQL query is stored in the dataframe
    print(df.columns)

    df = pd.read_sql_query("SELECT * from Data_Points", sqliteConnection)

    # Verify that result of SQL query is stored in the dataframe
    print(df.columns)

    df = pd.read_sql_query("SELECT * from Subjects", sqliteConnection)

    # Verify that result of SQL query is stored in the dataframe
    print(df.columns)

    df = pd.read_sql_query("SELECT * from Assays", sqliteConnection)

    # Verify that result of SQL query is stored in the dataframe
    print(df.columns)

    sqliteConnection.close()






if __name__ == "__main__":
	# We only want to run this if it's directly executed!
	main()
# %%
