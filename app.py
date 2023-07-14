import sys
import csv
import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="test_db"
)


def insert_data(table_name, path_csv):
    try:
        cursor = db.cursor()
        with open(path_csv, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            headers = next(reader, None)
            for row in reader:
                for i, val in enumerate(row):
                    if val == '':
                        row[i] = '0'
                query = f"INSERT INTO `{table_name}` (`{'`,`'.join(headers)}`) VALUES {tuple(row)}"
                cursor.execute(query)
                db.commit()
        print("inserted successfully!")
        db.close()
    except:
        raise


if __name__ == "__main__":
    table_name = sys.argv[1]
    path = sys.argv[2]
    insert_data(table_name, path)