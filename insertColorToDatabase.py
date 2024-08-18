import mysql.connector
import json

def main():

    # Colors
    collections  = 'colorMedleyCollection.json'
    # Configuration
    config = {
        'user' : 'root',
        'password' : '',
        'host' : 'localhost',
        'database' : 'cml_paint_db',
        'raise_on_warnings' : True
    }

    with open(collections, 'r') as file:
        data = json.load(file)  # Parse the JSON array into a Python list

    connection = mysql.connector.connect(**config)

    insertColors = (
        "INSERT INTO pallets "
        "(code, name, rgb)"
        "VALUES (%(Code)s, %(Name)s, %(rgbCode)s)"
    )

    if connection and connection.is_connected():
        with connection.cursor() as cursor:
            for info in data:
                cursor.execute(insertColors, info)
                connection.commit()

            cursor.close()
            connection.close()
    else:
        print("Can't connect")
        connection.close()

    

if __name__ == "__main__":
    main()




