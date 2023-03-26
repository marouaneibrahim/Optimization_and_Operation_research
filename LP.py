from ortools.linear_solver import pywraplp


def LinearProgrammingExample1():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    print('Number of variables =', solver.NumVariables())

    # Constraint 0: 8x + 10y <= 3400.
    solver.Add(6 * x + 19 * y <= 3400)

    # Constraint 1: x >= 0.
    solver.Add(x >= 0.0)

    # Constraint 2: 2x + 3y <= 960.
    solver.Add(2 * x + 3 * y <= 960)

    # Constraint 3: y >= 0.
    solver.Add(y >= 0.0)

    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 22x + 28y.
    solver.Maximize(22 * x + 28 * y)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 1:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())

def LinearProgrammingExample2():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    w = solver.NumVar(0, solver.infinity(), 'w')
    z = solver.NumVar(0, solver.infinity(), 'z')

    print('Number of variables =', solver.NumVariables())

    # Constraint 0: x<=700.
    solver.Add(x <= 700.0)

    # Constraint 1: y <= 700.
    solver.Add(y <= 700.0)

    # Constraint 2: z<=600.
    solver.Add(z<=600)

    # Constraint 3: w <= 800.
    solver.Add(w <= 800.0)
     # Constraint 4: x>=500.
    solver.Add(x >= 500.0)

    # Constraint 5: y >= 500.
    solver.Add(y >= 500.0)

    # Constraint 6: z>=500.
    solver.Add(z>=500)

    # Constraint 7: w >= 500.
    solver.Add(w >= 500.0)

    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 15(x+y+z+w) + 3(3*x + 2*y + z - 3950)
    solver.Minimize(24 * x + 21 * y + 18 * z + 15 * w - 11850) 

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 2:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
def LinearProgrammingExample3():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
 

    print('Number of variables =', solver.NumVariables())

    # Constraint 0: -x + y>=-2.
    solver.Add(-x + y >= -2)

    # Constraint 1: y <= 5.
    solver.Add(y <= 5)

    # Constraint 2: x + y<=10.
    solver.Add(x + y<=10)

    # Constraint 3: y >= 0.
    solver.Add(y >= 0.0)
     # Constraint 4: x>=0.
    solver.Add(x >= 0.0)

   


    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 3x + y
    solver.Maximize(3 * x + y) 

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 3:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
def LinearProgrammingExample4():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
 

    print('Number of variables =', solver.NumVariables())

    # Constraint 0: 3x + y>=6.
    solver.Add(3 * x + y >= 6)

    # Constraint 1: y >= 3.
    solver.Add(y >= 3)

    # Constraint 2: x <=4.
    solver.Add(x <=4)

    # Constraint 3: y >= 0.
    solver.Add(y >= 0.0)
     # Constraint 4: x>=0.
    solver.Add(x >= 0.0)

   


    print('Number of constraints =', solver.NumConstraints())

    # Objective function: x + y
    solver.Minimize(x + y) 

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 4:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
def LinearProgrammingExample5():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
 

    print('Number of variables =', solver.NumVariables())

    # Constraint 0: x <=6.
    solver.Add(x <= 6)

    # Constraint 1: -x + y <= 2.
    solver.Add(-x + y <= 2)

    # Constraint 2: x + 2y <=8.
    solver.Add(x + 2 * y <=8)

    # Constraint 3: y >= 0.
    solver.Add(y >= 0.0)
     # Constraint 4: x>=0.
    solver.Add(x >= 0.0)

   


    print('Number of constraints =', solver.NumConstraints())

    # Objective function: x + 2y
    solver.Maximize(x + 2 * y) 

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 5:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    
def LinearProgrammingExample6():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
 

    print('Number of variables =', solver.NumVariables())

    # Constraint 0: x + y >= 4.
    solver.Add(x + y >= 4)

    # Constraint 1: -x + y <= 4.
    solver.Add(-x + y <= 4)

    # Constraint 2: -x + 2y >= -4.
    solver.Add(-x + 2 * y >= -4)

    # Constraint 3: y >= 0.
    solver.Add(y >= 0.0)
     # Constraint 4: x>=0.
    solver.Add(x >= 0.0)

   


    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 3x + y
    solver.Maximize(3 * x + y) 

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 6:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
def LinearProgrammingExample7():
    """Linear programming sample."""
    # Instantiate a Glop solver, naming it LinearExample.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create the two variables and let them take on any non-negative value.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
 

    print('Number of variables =', solver.NumVariables())
    
    # Constraint 0: -x + y >= 4.
    solver.Add(-x + y >= 4)

    # Constraint 1: -x + 2y >= -4.
    solver.Add(-x + 2 * y >= -4)

    # Constraint 2: y >= 0.
    solver.Add(y >= 0.0)
     # Constraint 3: x>=0.
    solver.Add(x >= 0.0)

   


    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 3x + y
    solver.Maximize(3 * x + y) 

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution of exercice 7:')
        print('Objective value =', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())    
print("exercice 1")
LinearProgrammingExample1()
print("exercice 2")
LinearProgrammingExample2()
print("exercice 3")
LinearProgrammingExample3()
print("exercice 4")
LinearProgrammingExample4()
print("exercice 5")
LinearProgrammingExample5()
print("exercice 6")
LinearProgrammingExample6()
print("exercice 7")
LinearProgrammingExample7()
