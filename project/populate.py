import psycopg2
import csv
import os
import json
  

def insert_descargas():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="adminselfsolutions",
                                    host="54.232.132.113",
                                    port="5432",
                                    database="postgres")
        print(connection)

        file = open("data/goes16_glm_flashes.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:

            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO app_descargas ( latitude, longitude, intensidade, timestamp) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (row[1], row[2], '1',  row[3])
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into table")

        file.close()

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table:", error)


    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_alvos():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="adminselfsolutions",
                                    host="54.232.132.113",
                                    port="5432",
                                    database="postgres")

        directory = 'data/alvos/'
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                print(f)
                file = open(f)
                data = json.load(file)
                for i in data['features']:
                    # print(i['properties']['nome'])
                    # print(i['geometry']['coordinates'])

                    cursor = connection.cursor()

                    postgres_insert_query = """ INSERT INTO app_alvo ( buffer_id, empresa_id, satelite_id, coordenadas, nome) VALUES (%s,%s,%s,%s,%s)"""
                    record_to_insert = (1,1,1, i['geometry']['coordinates'], i['properties']['nome'])
                    cursor.execute(postgres_insert_query, record_to_insert)

                    connection.commit()
                    count = cursor.rowcount
                    print(count, "Record inserted successfully into table")

                file.close()

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table:", error)


    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

insert_alvos()