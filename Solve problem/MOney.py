from flask import Flask, render_template, request

app = Flask(__name__)

class Employee:
    def __init__(self, name, email, position, age):
        self.name = name
        self.email = email
        self.position = position
        self.age = age
        self.salary = self.calculate_salary()

    def calculate_salary(self):
        position_salaries = {
            'Manager': {
                (18, 27): 40000,
                (28, 37): 60000,
                (38, 47): 100000,
                (48, 57): 180000,
                (58, 77): 210000,
                (78, 80): 350000
            },
            'Developer': {
                (18, 27): 75000,
                (28, 37): 85000,
                (38, 47): 110000,
                (48, 57): 145000,
                (58, 67): 250000,
                (68, 77): 310000,
                (78, 80): 340000
            },
            'Designer': {
                (18, 27): 30000,
                (28, 37): 70000,
                (38, 47): 165000,
                (48, 57): 280000,
                (58, 67): 500000,
                (68, 77): 540000,
                (78, 80): +600000
            },
            'Doctor': {
                (18, 27): 75000,
                (28, 37): 85000,
                (38, 47): 110000,
                (48, 57): 145000,
                (58, 67): 250000,
                (68, 77): 650000,
                (78, 80): 800000
            }
        }

        return position_salaries.get(self.position, {}).get(self.get_age_group(), 0)
    
    def get_age_group(self):
        # Define age groups based on increments of 10 years
        age_groups = [
            (18, 27),
            (28, 37),
            (38, 47),
            (48, 57),
            (58, 67),
            (68, 77),
            (78, 80)
        ]

        for age_group in age_groups:
            if age_group[0] <= self.age <= age_group[1]:
                return age_group

        return None

# Employee data using instances of the Employee class
employee_entries = []

# Function to calculate the total salary of employees
def calculate_total_salary(employees):
    total_salary = sum(employee.salary for employee in employees)
    return total_salary

def is_valid_age(age):
    return age is not None and age.isdigit() and 18 <= int(age) <=80

# Route to display employee information
@app.route('/', methods =['GET', 'POST'])
def employee_info(employee_entries):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        position = request.form['position']
        age = request.form['age']




        if not is_valid_age(age):
            return render_template('info.html', employees=, Error = "Invalid age. Age must be a number and equal to ar greater than 18.")

        new_employee = Employee(name, email, position, int(age))
        employee_entries.append(new_employee)

        if len(employee_entries) % 3 == 0:
            total_salary_value = calculate_total_salary(employee_entries)
            return render_template('salary.html', employees=employee_entries, total_salary=total_salary_value)

    return render_template('info.html', employees=employee_entries)

if __name__ == '__main__':
    app.run(debug=True)


