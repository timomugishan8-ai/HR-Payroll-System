"""
CSC2105: Object-Oriented Programming Using Python
Topic 5 Group Project – HR / Payroll System

Group 6 Members
1. Timothy Mugisha - S25B38/041
2.  Ndambire Harry Bosco - M25B38/030
3. Mutagamba Jasmine Martha - S25B38/28
4. Natuyamba Conrad - S25B38/027
5. Musiime Miracle Ephraim - M25B38/012
6. Tana Micheal Wasolo - M25B38/035
"""
# =====================================================
# CONSTANTS
# =====================================================

REGULAR_HOURS = 40
OVERTIME_RATE_MULTIPLIER = 1.5
TAX_THRESHOLD = 100000
TAX_RATE = 0.10

# =======================================================
# EMPLOYEE CLASS
# =====================================================

class Employee:
    """
    Represents one employee in the payroll system.
    Stores employee information and performs salary calculations.
    """

    def __init__(self, name, employee_number, hours_worked, hourly_rate):
        self.name = name
        self.employee_number = employee_number
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

        # Validate immediately when object is created.
        self.validate_inputs()

# ---------------------------------------------
# Validation Method
# ---------------------------------------------
    def validate_inputs(self):
        if not self.name.strip():
            raise ValueError("Employee name cannot be empty.")

        if self.hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")

        if self.hourly_rate <= 0:
            raise ValueError("Hourly rate must be greater than zero.")

# ---------------------------------------------
# Regular Pay
# ---------------------------------------------
    def calculate_regular_pay(self):
        regular_hours = min(self.hours_worked, REGULAR_HOURS)
        return regular_hours * self.hourly_rate

# ---------------------------------------------
# Overtime Hours
# ---------------------------------------------
    def calculate_overtime_hours(self):
        return max(0, self.hours_worked - REGULAR_HOURS)

# ---------------------------------------------
# Overtime Pay
# ---------------------------------------------
    def calculate_overtime_pay(self):
        overtime_hours = self.calculate_overtime_hours()
        overtime_rate = self.hourly_rate * OVERTIME_RATE_MULTIPLIER
        return overtime_hours * overtime_rate
      
      
# ---------------------------------------------
# Gross Pay
# ---------------------------------------------
    def calculate_gross_pay(self):
        return self.calculate_regular_pay() + self.calculate_overtime_pay()

# ---------------------------------------------
# Tax
# ---------------------------------------------
    def calculate_tax(self):
        gross_pay = self.calculate_gross_pay()

        if gross_pay <= TAX_THRESHOLD:
            return 0

        taxable_amount = gross_pay - TAX_THRESHOLD
        return taxable_amount * TAX_RATE

# ---------------------------------------------
# Net Pay
# ---------------------------------------------
    def calculate_net_pay(self):
        return self.calculate_gross_pay() - self.calculate_tax()

# ---------------------------------------------
# Payslip Generator
# ---------------------------------------------
    def generate_payslip(self):
        gross = self.calculate_gross_pay()
        tax = self.calculate_tax()
        net = self.calculate_net_pay()

        payslip = f"""

                WEEKLY EMPLOYEE PAYSLIP

    Employee Name    : {self.name}
    Employee Number  : {self.employee_number}

    Hours Worked     : {self.hours_worked}
    Hourly Rate      : UGX {self.hourly_rate:,.0f}

    Regular Pay      : UGX {self.calculate_regular_pay():,.0f}
    Overtime Hours   : {self.calculate_overtime_hours()}
    Overtime Pay     : UGX {self.calculate_overtime_pay():,.0f}

    Gross Pay        : UGX {gross:,.0f}
    Tax Deducted     : UGX {tax:,.0f}

    NET PAY          : UGX {net:,.0f}

    """
        return payslip

    # ---------------------------------------------
        
    # String Representation
    # ---------------------------------------------
    def __str__(self):
        return (f"{self.employee_number} | "
            f"{self.name} | "
            f"Net Pay: UGX {self.calculate_net_pay():,.0f}")

  
  
# =====================================================
# PAYROLL SYSTEM CLASS
# =====================================================

class PayrollSystem:
    """
    Stores and manages multiple employees.
    """

    def __init__(self):
        self.employees = []

# ---------------------------------------------
# Add Employee
# ---------------------------------------------
    def add_employee(self, employee):

        # Check duplicate employee number
        for emp in self.employees:
            if emp.employee_number == employee.employee_number:
                raise ValueError(
                    f"Employee number {employee.employee_number} already exists."
                )

        self.employees.append(employee)
        print(f"Employee '{employee.name}' added successfully.")


# ---------------------------------------------
# Find Employee
# ---------------------------------------------
    def find_employee(self, employee_number):
        for employee in self.employees:
            if employee.employee_number == employee_number:
                return employee

        return None
# ---------------------------------------------
# Display All Payslips
# ---------------------------------------------
    def display_all_payslips(self):
        print("\n========== ALL EMPLOYEE PAYSLIPS ==========")

        for employee in self.employees:
            print(employee.generate_payslip())
# ---------------------------------------------
# Weekly Payroll Summary
# ---------------------------------------------
    def weekly_summary(self):

        total_gross = 0
        total_tax = 0
        total_net = 0

        for employee in self.employees:
            total_gross += employee.calculate_gross_pay()
            total_tax += employee.calculate_tax()
            total_net += employee.calculate_net_pay()

        print("\n============== WEEKLY PAYROLL SUMMARY ==============")
        print(f"Total Employees : {len(self.employees)}")
        print(f"Total Gross Pay : UGX {total_gross:,.0f}")
        print(f"Total Tax Paid  : UGX {total_tax:,.0f}")
        print(f"Total Net Pay   : UGX {total_net:,.0f}")
        print("===================================================")



# =====================================================
# INPUT VALIDATION HELPER FUNCTIONS
# =====================================================

def get_non_empty_string(prompt):
    """Gets a non-empty string from the user."""
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Error: This field cannot be empty.")
        else:
            return value


def get_hours_worked():
    """Gets valid hours worked."""
    while True:
        try:
            hours = float(input("Hours Worked This Week: "))

            if hours < 0:
                print("Error: Hours worked cannot be negative.")

            elif hours > 168:
                print("Error: A week only has 168 hours.")

            else:
                return hours

        except ValueError:
            print("Error: Please enter a valid number.")


def get_hourly_rate():
    """Gets a valid hourly rate."""
    while True:
        try:
            rate = float(input("Hourly Rate (UGX): "))

            if rate <= 0:
                print("Error: Hourly rate must be greater than zero.")

            else:
                return rate

        except ValueError:
            print("Error: Please enter a valid amount.")


def get_menu_choice():
    """Gets a valid menu option."""
    while True:
        choice = input("Enter your choice (1-5): ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            return choice

        print("Invalid choice. Please enter a number between 1 and 5.")



# =====================================================
# DEMONSTRATION
# =====================================================

def main():

    payroll = PayrollSystem()

    print("\nCreating employees...\n")

    try:
        employee1 = Employee(
            "John Okello",
            "EMP001",
            35,
            6000
        )
        payroll.add_employee(employee1)

        employee2 = Employee(
            "Sarah Nakato",
            "EMP002",
            47,
            8000
        )
        payroll.add_employee(employee2)

        employee3 = Employee(
            "Timothy Mugisha",
            "EMP003",
            52,
            10000
        )
        payroll.add_employee(employee3)

    except ValueError as error:
        print("Error:", error)


     # Invalid Employee
    print("\nTrying invalid employee...\n")

    try:
        invalid_employee = Employee(
            "Peter",
            "EMP004",
            -5,
            7000
        )
        payroll.add_employee(invalid_employee)

    except ValueError as error:
        print("Error:", error)

    # Duplicate Employee Number
    print("\nTrying duplicate employee number...\n")

    try:
        duplicate_employee = Employee(
            "Grace Auma",
            "EMP002",
            40,
            9000
        )
        payroll.add_employee(duplicate_employee)

    except ValueError as error:
        print("Error:", error)

     # Search Employee
    print("\nSearching employee EMP002...\n")

    found = payroll.find_employee("EMP002")

    if found:
        print(found.generate_payslip())
    else:
        print("Employee not found.")


    # Display all payslips
    payroll.display_all_payslips()

    # Weekly summary
    payroll.weekly_summary()


# =====================================================
# PROGRAM ENTRY POINT
# =====================================================

if __name__ == "__main__":
    main()