import warnings
from constraint import Problem

warnings.filterwarnings("ignore")

################ Creating a new problem instance #################
problem = Problem()

################# Information is available in the exercise, and you can add or more items in below lists ###############
trip_durations = [2, 3, 4, 5, 6]
customer_name = ['Freda', 'Vicky', 'Opal', 'Sarah', 'Penny']
available_locations = ['Brownfield', 'Los Altos', 'Iowa Falls', 'Redding', 'Durham']
car_brands = ['Dodge', 'Fiat', 'Hyundai', 'Jeep', 'Nissan']
###########################################################################

#### Add variable for Assign a contract (duration, location, brand) for each customer available in the exercise ####
problem.addVariable('Freda', [(d, loc, brand) for d in trip_durations for loc in available_locations for brand in car_brands])
problem.addVariable('Vicky', [(d, loc, brand) for d in trip_durations for loc in available_locations for brand in car_brands])
problem.addVariable('Opal', [(d, loc, brand) for d in trip_durations for loc in available_locations for brand in car_brands])
problem.addVariable('Sarah', [(d, loc, brand) for d in trip_durations for loc in available_locations for brand in car_brands])
problem.addVariable('Penny', [(d, loc, brand) for d in trip_durations for loc in available_locations for brand in car_brands])

############ Adding Constraint for All customers have unique available locations and car brands ##############
problem.addConstraint(lambda f, v, o, s, p: len({f[1], v[1], o[1], s[1], p[1]}) == 5,
                      ('Freda', 'Vicky', 'Opal', 'Sarah', 'Penny'))
problem.addConstraint(lambda f, v, o, s, p: len({f[2], v[2], o[2], s[2], p[2]}) == 5,
                      ('Freda', 'Vicky', 'Opal', 'Sarah', 'Penny'))


############# Specific information provide in the exercise to resolve the puzzle ##############


problem.addConstraint(lambda v: v[1] not in ['Los Altos', 'Durham'] and v[2] != 'Fiat',
                      ('Vicky',)) # Vicky, Los Altos, Durham, and Fiat are all different contracts


problem.addConstraint(lambda f, v, o, s, p: all([c[2] != 'Jeep' or c[1] != 'Iowa Falls' for c in [f, v, o, s, p]]),
                      ('Freda', 'Vicky', 'Opal', 'Sarah', 'Penny')) # The Jeep contract is not in Iowa Falls


problem.addConstraint(lambda v, f, o, s, p: (v[1] in ['Los Altos', 'Redding'] and v[2] == 'Nissan'),
                      ('Vicky', 'Freda', 'Opal', 'Sarah', 'Penny')) # Vicky and the Nissan contract are in Los Altos or Redding

problem.addConstraint(lambda p: p[0] != 6, ('Penny',)) # Penny contract is not for 6 days


problem.addConstraint(lambda f, v, o, s, p: any([c[0] == 5 and c[1] == 'Iowa Falls' for c in [f, v, o, s, p]]),
                      ('Freda', 'Vicky', 'Opal', 'Sarah', 'Penny')) # Contract in Iowa Falls is for 5 days


problem.addConstraint(lambda o, s: s[0] == o[0] + 3 if s[1] == 'Durham' else True,
                      ('Opal', 'Sarah')) # contract in Durham is 3 days longer than Opal

problem.addConstraint(lambda f, v: (f[0] == 2 and f[1] != 'Redding') or (v[2] == 'Nissan' and v[1] == 'Redding'),
                      ('Freda', 'Vicky')) # Nissan contract and the 2-day contract involve Redding or Freda

problem.addConstraint(lambda f, v, o, s, p: all([c[2] != 'Jeep' or c[0] != 6 for c in [f, v, o, s, p]]),
                      ('Freda', 'Vicky', 'Opal', 'Sarah', 'Penny')) # Jeep contract is not for 6 days

problem.addConstraint(lambda o, f, v, s, p: any([o[0] == c[0] + 1 and c[2] == 'Hyundai' for c in [f, v, s, p]]),
                      ('Opal', 'Freda', 'Vicky', 'Sarah', 'Penny')) # Opal contract is 1 day longer than the Hyundai contract

#################### Get the all possible solutions by algo. #################
solutions = problem.getSolutions()


################## This Function to check if a solution fulfills all hints ####################
def check_if_it_valid_solution(solution):
    ############ Extracting customer contracts ########
    Freda, Vicky, Opal, Sarah, Penny = solution['Freda'], solution['Vicky'], solution['Opal'], solution['Sarah'], \
    solution['Penny']

    ############ Checking the hints against the solution provided ##########
    if Vicky[1] in ['Los Altos', 'Durham'] or Vicky[2] == 'Fiat':
        return False
    if any([c[2] == 'Jeep' and c[1] == 'Iowa Falls' for c in [Freda, Vicky, Opal, Sarah, Penny]]):
        return False
    if not (Vicky[1] in ['Los Altos', 'Redding'] and Vicky[2] == 'Nissan'):
        return False
    if Penny[0] == 6:
        return False
    if not any([c[0] == 5 and c[1] == 'Iowa Falls' for c in [Freda, Vicky, Opal, Sarah, Penny]]):
        return False
    if not (Sarah[1] == 'Durham' and Sarah[0] == Opal[0] + 3):
        return False
    if not ((Freda[0] == 2 and Freda[1] != 'Redding') or (Vicky[2] == 'Nissan' and Vicky[1] == 'Redding')):
        return False
    if any([c[2] == 'Jeep' and c[0] == 6 for c in [Freda, Vicky, Opal, Sarah, Penny]]):
        return False
    if not any([Opal[0] == c[0] + 1 and c[2] == 'Hyundai' for c in [Freda, Vicky, Sarah, Penny]]):
        return False

    ###### return true If all hints are satisfied #####
    return True


########### Filtering out valid solutions ################
found_valid_solutions = [solution for solution in solutions if check_if_it_valid_solution(solution)]

########### Show the total number of valid solutions ##############
total_founded_valid_solutions = len(found_valid_solutions)
print(f"Total number of valid solutions found for the problem: {total_founded_valid_solutions}")

# If there are valid solutions, display the top 5
if total_founded_valid_solutions > 0:
    top_5_solutions = found_valid_solutions[:5]
    for i, solution in enumerate(top_5_solutions, 1):
        print(f"\nTop Valid Solution {i}:")
        for customer_name, contract in solution.items():
            print(f"Customer Name: {customer_name} ----> Duration: {contract[0]} days, Location: {contract[1]}, Car Brand: {contract[2]}")
else:
    print("No valid solutions found for the problem.")

