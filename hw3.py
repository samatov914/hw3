# class Bank:
#     def __init__(self, __name):
#         self.__name = __name
#         self.__balance = 0
#     def money_x(self):
#         user = int(input("сколько вы хотите пополнить баланс: "))
#         self.__balance += user
#         return f"на вашем счёте: {self.__balance}, Имя владельца: {self.__name}"
#     def _kill(self):
#         user = int(input("сколько вы хотите обноличить: "))
#         if self.__balance >= user:
#             self.__balance -= user
#             return f"вы обноличили счёт на {user} остаток на карте {self.__balance}"
#         else:
#             return f"На вашем счете недостаточно средств: {self.__balance}"
#     def __jacpot(self):
#         return f"ваш счет ужножок на 10, ваш счет: {self.__balance * 10}"
#     def user(self,name,__balanse):
#         self.name = name
#         self.__balanse = __balanse
#         return f"Имя: {self.name}, Balanse: {self.__balanse + self.__balance}"
# ban = Bank("samat")
# print(ban.money_x())
# print(ban._kill())
