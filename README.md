# Demographic Data Analyzer

This project analyzes U.S. Census demographic data using Pandas in Python. It calculates insights such as education level, income distribution, work hours, and occupation patterns across different races and countries.

It was built as part of the freeCodeCamp Data Analysis with Python Projects certification.

---

What It Does

- Uses the adult.data.csv dataset from the 1994 U.S. Census.
- Defines a function calculate_demographic_data() inside demographic_data_analyzer.py.
- Computes insights like:
  - Race count distribution
  - Average age of men
  - % with Bachelor's degrees
  - Rich vs. education levels
  - Min work hours and % rich among them
  - Country with highest % of people earning >50K
  - Top occupation for rich people in India

---

Example Usage

from demographic_data_analyzer import calculate_demographic_data

results = calculate_demographic_data(print_data=True)

---

Sample Output

Number of each race:
 White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4
Higher education rich: 46.5
Lower education rich: 17.4
Overall rich percentage: 23.5
Min work time: 1 hours/week
Rich among min workers: 10.0
Country with highest % rich: Iran
Highest %: 41.9
Top IN occupation: Prof-specialty

---

Project Structure

boilerplate-demographic-data-analyzer/
├── adult.data.csv                # Dataset (1994 Census data)
├── demographic_data_analyzer.py # Main logic function
├── main.py                      # Script to run and test the function
├── test_module.py               # Unit tests (used by freeCodeCamp)
└── README.md                    # This file

---

How to Run the Project

python main.py

---

Run the Test Suite

To validate your solution with the tests provided by freeCodeCamp:

python -m unittest test_module.py

Expected output:

..........
----------------------------------------------------------------------
Ran 10 tests in 0.097s

OK

---

Dataset Source

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository.
Irvine, CA: University of California, School of Information and Computer Science.

---

License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

Author

Kelvin Tinashe Chada
https://github.com/KTJETRO

---

Disclaimer

This project was developed as part of the
freeCodeCamp Data Analysis with Python certification.
I do not claim ownership of the original project idea, dataset, or instructions.
This repository contains my personal solution only, shared for educational purposes.
