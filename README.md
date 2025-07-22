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
