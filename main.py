import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv('employee.csv')

def read_dataframe(file):
    emp_1 = pd.DataFrame(columns=["UNIQUE_ID_POSITION_TITLE"])
    emp_2 = pd.read_csv(file)
    for x in range(len(emp_2)):
        string = ( str( emp_2.iloc[0:, 0][x]) + "_" + str( emp_2.iloc[0:, 1][x]))
        emp_1.loc[x] = string
    return emp_1

def remove_column(emp, string):
    copy = emp.copy()
    del copy[string]
    return copy

def lowest_salaries(emp, m, n):
    copy = emp.copy()
    copy = copy.sort_values(by=["HIRE_DATE"], ascending=False)
    copy = copy[:m]
    copy = copy.groupby(["POSITION_TITLE"]).agg({"BASE_SALARY":["mean"]})
    copy = copy["BASE_SALARY"]["mean"][:n]
    return copy

def salaries_per_department(emp):
    copy = emp.copy()
    copy = copy.groupby(["DEPARTMENT", "POSITION_TITLE", "GENDER"]).agg({"BASE_SALARY": ["mean", "median"]})
    return copy

# ZADANIE 1
emp_1 = read_dataframe("employee.csv")
print(emp_1)

# ZADANIE 2
emp_2 = remove_column(emp, "UNIQUE_ID")
print(emp_2)

# ZADANIE 3
n = 5
m = 10
emp_3 = lowest_salaries(emp, m, n)
print(emp_3)

# ZADANIE 4
emp_4 = salaries_per_department(emp)
print(emp_4)

# ZADANIE 5
copy = emp.copy()
copy = copy.groupby(["DEPARTMENT", "EMPLOYMENT_TYPE"]).agg({"BASE_SALARY": ["min", "max"]})
wykres = copy.plot.bar(colormap='Paired')
plt.legend(title = "Legenda", loc = 2, labels = ["Minimalne wynagrodzenie", "Maksymalne wynagrodzenie"])
wykres.set_xlabel("Stanowiska w departamentach")
wykres.set_ylabel("Zarobki")
plt.title("Zarobki w poszczególnych departamentach\n w zależnośći od formy zatrunienia")
plt.show()

