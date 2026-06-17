from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
                
    def display_info(self):
        emp_type = 'Full-time'
        if isinstance(self, PartTimeEmployee): # kiểm tra thuộc về class nào hay không
            emp_type = 'Part-time'
        elif isinstance(self, InternEmployee):
            emp_type = 'Intern'
        
        print(f"Ma NV: {self.employee_id:<5} | Ho ten: {self.name:<15} | Loai: {emp_type}")
        
    @abstractmethod
    def calculate_salary(self):     
        pass
    
class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
        
    def calculate_salary(self):
        return self.base_salary + self.bonus
        
class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
        
    def calculate_salary(self):
        return self.working_hours * self.hourly_rate
        
class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance
        
    def calculate_salary(self):
        return self.allowance
    
def display_emp(employee):
    print("----- DANH SACH NHAN VIEN -----")
    for emp in employee:
        emp.display_info()
        
def display_salaries(employees):
    print("----- BANG LUONG NHAN VIEN -----")
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.employee_id:<5} | {emp.name:<15} | Luong: {salary} VND")
        
employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]
        
def main():
    while True:
        choice = input('''
=== EMPLOYEE SALARY MANAGER ===
1. Xem danh sách nhân viên
2. Tính lương toàn bộ nhân viên
3. Thoát chương trình
================================
Chọn chức năng (1-3): ''')
        if not choice.isdigit():
            print("Lua chon chua hop le!")
            continue
        choice = int(choice)
        match choice:
            case 1:
                display_emp(employees)
            
            case 2:
                display_salaries(employees)
            
            case 3:
                print("Thoat chuong trinh !")
                break
            
            case _:
                print("Lua chon chua hop le!")
                
if __name__ == "__main__":
    main()