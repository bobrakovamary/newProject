
class Salary:

    def __init__(self, salary=0):
        self.__salary=0
        if self.__check_salary(salary):
            self.__salary = salary

    def set_salary(self, new_salary):
        if self.__check_salary(new_salary):
            self.__salary = new_salary
    def get_salary(self):
        return self.__salary
    @staticmethod
    def __check_salary(new_salary):
        return isinstance(new_salary, int) and 0 < new_salary < 100000000

t1 = Salary(43500)
print(t1.get_salary())

print('bye')
print('hi')
print('hello')



