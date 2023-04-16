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

print("exercice 5")
LinearProgrammingExample5()
print("exercice 6")
LinearProgrammingExample6()
print("exercice 7")
LinearProgrammingExample7()
