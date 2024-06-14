class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

# Membuat object berdasarkan class Employee
employee = Employee("Synta", 30, 50000)

# Mengimplementasikan semua method yang ada
print("Initial Employee Details")
print("Name:", employee.get_name())
print("Age:", employee.get_age())
print("Salary:", employee.get_salary())

# Mengubah nilai atribut menggunakan set method
employee.set_name("Synta Nur")
employee.set_age(28)
employee.set_salary(55000)

# Menampilkan nilai atribut setelah diubah
print("\nUpdated Employee Details")
print("Name:", employee.get_name())
print("Age:", employee.get_age())
print("Salary:", employee.get_salary())
