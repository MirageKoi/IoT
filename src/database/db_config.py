from peewee_async import PostgresqlDatabase

db = PostgresqlDatabase("postgres", user="postgres", password="pass", host="localhost", port=5432)
