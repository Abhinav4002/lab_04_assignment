class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def search_by_age(self, target_age):
        result = []
        for employee in self.employees:
            if employee.age == target_age:
                result.append(employee)
        return result

    def search_by_name(self, target_name):
        result = []
        for employee in self.employees:
            if employee.name == target_name:
                result.append(employee)
        return result

    def search_by_salary(self, operator, target_salary):
        result = []
        if operator == "<":
            for employee in self.employees:
                if employee.salary < target_salary:
                    result.append(employee)
        elif operator == ">":
            for employee in self.employees:
                if employee.salary > target_salary:
                    result.append(employee)
        elif operator == "<=":
            for employee in self.employees:
                if employee.salary <= target_salary:
                    result.append(employee)
        elif operator == ">=":
            for employee in self.employees:
                if employee.salary >= target_salary:
                    result.append(employee)
        return result

if __name__ == "__main__":
    table = EmployeeTable()

    table.add_employee("161E90", "Raman", 41, 56000)
    table.add_employee("161F91", "Himadri", 38, 67500)
    table.add_employee("161F99", "Jaya", 51, 82100)
    table.add_employee("171E20", "Tejas", 30, 55000)
    table.add_employee("171G30", "Ajay", 45, 44000)

    print("Search options:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter the target age: "))
        result = table.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the target name: ")
        result = table.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter the operator (<, >, <=, >=): ")
        target_salary = float(input("Enter the target salary: "))
        result = table.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")

    if result:
        print("Search Results:")
        for employee in result:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No results found.")
