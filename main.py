
from Class import Users
from database_db import Database


def balanc(phone_number, password):
    query = "SELECT * FROM users "
    data = Database.connect_to_db(query, "select")

    for i in data:
        if i[5] == phone_number and i[6] == password:
            if i[4] is None:
                print(f"Your balanc: 0")
                return servis(phone_number, password)
    print(f"Your balanc: {i[4]}")
    return servis(phone_number, password)


def pul_yechish(phone_number, password):

    query = f"SELECT balance FROM users WHERE phone_number = '{phone_number}'"
    data = Database.connect_to_db(query, "select")

    pul = int(input("""
    Qancha pul yechmoqchisiz ?
    Summani kiriting: """))
    pul2 = pul * 0.01
    pul3 = pul + pul2

    if int(pul) < int(data[0][0]):
        naxt = input(f"""
        Kiritilgan summa: {pul}
        Kammisiya: {pul2}
        Jammi summa: {pul3}
    
    1. Ha
    2. Yoq
        >>> """)
        if naxt == "1":
            history = "pul_yechish"
            query = f"UPDATE users SET balance = {data[0][0] - pul3} WHERE phone_number = '{phone_number}'"
            Database.connect_to_db(query, "update")
            query3 = f"SELECT users_id FROM users WHERE phone_number = '{phone_number}'"
            data = Database.connect_to_db(query3, "select")
            query2 = f"INSERT INTO payment (users_id,history, money) VALUES ('{data[0][0]}','{history}','{int(pul3)}')"
            Database.connect_to_db(query2, "insert")
            return servis(phone_number, password)

        elif naxt == "2":
            return servis(phone_number, password)
        else:
            print("Invalid")
            return pul_yechish(phone_number, password)


    else:
        print("Xisobingizda mablag' yetarli emas")
        return pul_yechish(phone_number, password)




def sms(phone_number, password):
    pass


def servis(phone_number, password):
    user = input("""
        1. Balance
        2. Pul yechish 
        3. SMS xabarnomani ulash
        0. Back 
            >>> """)

    if user == "1":
        return balanc(phone_number, password)
    elif user == "2":
        return pul_yechish(phone_number, password)
    elif user == "3":
        return sms(phone_number, password)
    elif user == "0":
        return main()
    else:
        print("Invalid")
        return servis(phone_number, password)



def login():
    phone_number = input("Enter your phone number: +998 ")
    password = input("Enter your password: ")

    query = "SELECT * FROM users "
    data = Database.connect_to_db(query, "select")

    for i in data:
        if i[5] == phone_number and i[6] == password:
            return servis(phone_number, password)
    print("Telefon raqam yoki password notog'ri")
    return login()



def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    card_number = input("Enter your card number: ")
    balance = input("Enter your balanc: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")

    Users.insert(first_name, last_name, card_number, balance, phone_number, password)
    return login()


def admin():
    pass


def main():
    user_input = input("""
    1. Login 
    2. Register
    3. Enter money to system
        >>> """)

    if user_input == "1":
        return login()
    elif user_input == "2":
        return register()
    elif user_input == "3":
        return admin()
    else:
        print("Invalid")
        return main()


if __name__ == "__main__":
    main()



















"""def bank():


    user_input = int(input("Enter money: "))
    bank_money = {
        '200': 15,
        '100': 12,
         '50': 8,
         '20': 20,
         '10': 35,
          '5': 40,
          '1': 55
    }

    print(bank_money[2])

    ikki = 0
    for i in bank_money:
        if i < user_input:
            ikki += 1
        else:
            ikki += 1"""

