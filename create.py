from database_db import Database

def create():

    users = """
    CREATE TABLE IF NOT EXISTS users (
    users_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    card_number VARCHAR(16),
    balance INTEGER,
    phone_number VARCHAR(9),
    password VARCHAR(4),
    creat_date TIMESTAMP DEFAULT now())"""


    payments = """
    CREATE TABLE IF NOT EXISTS payment (
    payment_id SERIAL PRIMARY KEY,
    users_id INT REFERENCES users(users_id),
    history VARCHAR(100),
    money INT,
    creat_date TIMESTAMP DEFAULT now())"""


    sms = """
    CREATE TABLE IF NOT EXISTS sms (
    sms_id SERIAL PRIMARY KEY,
    users_id int REFERENCES users(users_id),
    status VARCHAR(30),
    creat_date TIMESTAMP DEFAULT now())"""


    data = {
        "users": users,
        "payments": payments,
        "sms": sms
    }

    for i in data:
        print(f"{i} => {Database.connect_to_db(data[i], 'create')}")


if __name__ == "__main__":
    create()