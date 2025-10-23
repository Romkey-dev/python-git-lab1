class Employee:
    def __init__(self, id_empl, name, department, base_salary):
        self.__id = id_empl
        self.__name = name
        self.__department = department
        self.__base_salary = base_salary  # исправлена опечатка!

    def get_all(self):
        return (self.__id, self.__name, self.__department, self.__base_salary)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID должен быть положительным целым числом")
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Имя не должно быть пустой строкой")
        self.__name = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Отдел не должен быть пустой строкой")
        self.__department = value

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.__base_salary = value

    def __str__(self):
        return f"Сотрудник [id: {self.__id}, имя: {self.__name}, отдел: {self.__department}, базовая зарплата: {self.__base_salary}]"


if __name__ == "__main__":
    emp1 = Employee(1, "Анна Петрова", "Бухгалтерия", 45000.0)
    emp2 = Employee(2, "Пётр Сидоров", "Продажи", 55000.0)

    print(emp1)
    print(emp2)