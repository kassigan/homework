class User:

    def __init__(self, user_id, name, access_level="user"):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

# Геттеры
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

# Сеттеры
    def set_name(self, new_name):
        self.__name = new_name

    def set_access_level(self, new_level):
        self.__access_level = new_level

class Admin(User):
    _user_list = [] # список всех пользователей объектов Админ

    def __init__(self, user_id, name, access_level="admin"):
        super().__init__(user_id, name, access_level)



    def add_user(self, user):
        if isinstance(user, User):
            Admin._user_list.append(user)
            print(f"User '{user.get_name()}' has been added.")
        else:
            print("Only User instances can be added.")

    def delete_user(self, user_id):
         for user in Admin._user_list:
            if user.get_user_id() == user_id:
                Admin._user_list.remove(user)
                print(f"User with ID {user_id} has been deleted.")
                return
         print(f"User with ID {user_id} not found.")

    def show_users(self):
        print("List of all users in the system")
        for user in Admin._user_list:
            print(f" - {user.get_name()} (ID: {user.get_user_id()}, access: {user.get_access_level()})")



# создаём пользователей
user1 = User(1, "Tolik")
user2 = User(2, "Anton", "read_only")
admin = Admin(3, "Admin Olga")
admin1 = Admin(1,"Admin Alexandra")

# показываем пользователей
admin.show_users()

# добавляем пользователей
admin.add_user(user1)
admin1.add_user(user2)

# показываем пользователей
admin1.show_users()
admin.show_users()



# print(user1.user_id, user1.name, user1._access_level)
# print(user2.user_id, user2.name, user2._access_level)
# print(user3.user_id, user3.name, user3._access_level)