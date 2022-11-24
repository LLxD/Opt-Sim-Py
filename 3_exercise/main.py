from pulp import *

prob = LpProblem("Mailing Personnel Problem", LpMinimize)

# Variables
x1 = LpVariable("Number of employees that work on monday", 0, None, LpInteger)
x2 = LpVariable("Number of employees that work on tuesday", 0, None, LpInteger)
x3 = LpVariable("Number of employees that work on wednesday",
                0, None, LpInteger)
x4 = LpVariable("Number of employees that work on thursday",
                0, None, LpInteger)
x5 = LpVariable("Number of employees that work on friday", 0, None, LpInteger)
x6 = LpVariable("Number of employees that work on saturday",
                0, None, LpInteger)
x7 = LpVariable("Number of employees that work on sunday", 0, None, LpInteger)

# Objective Function
# The mailing company wants to minimize the total number of employees that work in a week
# Every employee must work five consecutive days
# On mondays, at least 17 employees must be working
# On tuesdays, at least 13 employees must be working
# On wednesdays, at least 15 employees must be working
# On thursdays, at least 19 employees must be working
# On fridays, at least 14 employees must be working
# On satudays, at least 16 employees must be working
# On sundays, at least 11 employees must be working

prob += x1 + x2 + x3 + x4 + x5 + x6 + x7

# Constraints
prob += x1 + x2 + x3 + x4 + x5 >= 17
prob += x2 + x3 + x4 + x5 + x6 >= 13
prob += x3 + x4 + x5 + x6 + x7 >= 15
prob += x4 + x5 + x6 + x7 + x1 >= 19
prob += x5 + x6 + x7 + x1 + x2 >= 14
prob += x6 + x7 + x1 + x2 + x3 >= 16
prob += x7 + x1 + x2 + x3 + x4 >= 11


# Solve our problem
prob.solve()

# Print our decision variable values
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print our objective function value
print("Total Number of Employees = ", value(prob.objective))
