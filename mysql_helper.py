import mysql.connector
import pandas as pd


def create_db(table_cursor, db_name):
    print(f"Creating Database {db_name}")
    table_cursor.execute(f"CREATE DATABASE {db_name};")


def use_db(table_cursor, db_name):
    print(f"Using Database {db_name}")
    table_cursor.execute(f"USE {db_name};")


def create_table(table_cursor, table_name):
    # cursor.execute(f"CREATE TABLE {table_name} ("
    #                "reg_no int(20) NOT NULL,"
    #                "name varchar(50) NOT NULL,"
    #                "department varchar(120) NOT NULL,"
    #                "email varchar(120) NOT NULL,"
    #                "dob date NOT NULL"
    #                ");")

    table_cursor.execute(f"CREATE TABLE {table_name} "
                   "(name varchar(100), "
                   "mfr varchar(100), "
                   "type varchar(10), "
                   "calories int, "
                   "protein int, "
                   "fat int, "
                   "sodium int, "
                   "fiber float, "
                   "carbo float, "
                   "sugars int, "
                   "potass int, "
                   "vitamins int, "
                   "shelf int, "
                   "weight float, "
                   "cups float, "
                   "rating float)")


def insert_into_table(table_cursor, table_name, row_data):
    print(f"Inserting the row {row_data}")
    table_cursor.execute(
        f"INSERT INTO {table_name} "
        "VALUES "
        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        row_data)


def read_cereal_data(table_cursor, conn):
    file_path = "/home/paranthaman/Downloads/cereal.csv"
    cereals_df = pd.read_csv(file_path)
    for row in cereals_df.itertuples():
        row_data = (tuple(row)[1:])
        insert_into_table(table_cursor, "cereals", row_data)
        conn.commit()


if __name__ == "__main__":
    connection = mysql.connector.connect(
        user="paranthaman",
        password="mysql123",
        host="127.0.0.1",
    )

    cursor = connection.cursor()
    cereals_db = "cerealsdb"
    # create_db(cursor, cereals_db)
    use_db(cursor, cereals_db)
    # create_table(cursor, "cereals")
    read_cereal_data(cursor, connection)
    cursor.close()
    connection.close()


