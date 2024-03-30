from database_db import Database

class Users:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        print(Database.connect_to_db(query,"select"))

    @staticmethod
    def insert(first_name, last_name, card_number, balance, phone_number, password):
        query = f"INSERT INTO users (first_name, last_name, card_number,balance, phone_number, password) VALUES ('{first_name}', '{last_name}', '{card_number}','{balance}','{phone_number}','{password}')"
        print(Database.connect_to_db(query, "insert"))

