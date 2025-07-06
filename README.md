# Car Rental Contract Solver Using Python

This project solves a **Constraint Satisfaction Problem (CSP)** by assigning rental car contracts to five customers. Each contract specifies a **rental duration**, **location**, and **car brand**. The assignment respects several constraints to ensure valid and unique combinations.

---

## Problem Description

We must assign rental contracts to:

- Freda
- Vicky
- Opal
- Sarah
- Penny

Each rental contract consists of:
- **Duration:** 2 to 6 days
- **Location:** Brownfield, Los Altos, Iowa Falls, Redding, Durham
- **Car Brand:** Dodge, Fiat, Hyundai, Jeep, Nissan

---

## Constraints

1. No two customers share the same **location** or **brand**.
2. Several logical constraints/hints are applied:
   - Vicky cannot rent in Los Altos or Durham, nor drive a Fiat.
   - No Jeep is in Iowa Falls or rented for 6 days.
   - Vicky rents a Nissan in either Los Altos or Redding.
   - The contract in Iowa Falls is exactly 5 days.
   - The Durham contract is 3 days longer than Opal’s.
   - Freda’s contract is either:
     - a 2-day rental not in Redding, or
     - Vicky's Nissan rental in Redding.
   - Opal’s contract is 1 day longer than the Hyundai contract.

---

## How It Works

1. **Define Variables:** Rental possibilities for each customer.
2. **Add Constraints:** Using the `python-constraint` library.
3. **Backtracking Algorithm:** Finds all valid assignments.
4. **Output:** Total solutions and the top 5 assignments printed clearly.

---

## Sample Output

The program found 40 valid solutions that satisfy all constraints. Here’s an example of what a valid solution looks like:

Freda: 2 days, Redding, Dodge
Vicky: 4 days, Los Altos, Nissan
Opal: 3 days, Durham, Hyundai
Sarah: 5 days, Iowa Falls, Jeep
Penny: 6 days, Brownfield, Fiat


---

## Customization

You can:
- Add more customers, car brands, or cities.
- Modify or add constraints using lambda functions.
- Change the number of printed solutions.

Example:
```python
problem.addConstraint(lambda s: s[0] == 5, ('Sarah',))  # Sarah rents for exactly 5 days
📸 Screenshots

(Included in the project PDF)

🛠 Installation

pip install -r requirements.txt
Then run:

python sourabh_chauhan_ex2.py
📂 File Structure

├── sourabh_chauhan_ex2.py         # Main solver implementation
├── Project_Idea+Screenshot_ex2.pdf # Project idea and constraints
├── README.md                      # Project description and guide
└── requirements.txt               # Python dependencies
👨‍💻 Author

Developed By Sourabh Chauhan
