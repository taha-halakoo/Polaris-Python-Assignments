# Polaris Python Assignments 🚀

This repository contains all of my assignments from the **Polaris Artificial Intelligence Program**.  
The program focuses on learning Python step by step through structured weekly projects that emphasize **problem-solving, clean logic, and real-world use cases**.

The main goal of this repository is to:
- document my learning progress,
- showcase my coding style and thinking process,
- and build a solid foundation for future **AI, ML, robotics, and engineering projects**.

---

## 📚 Assignments Overview

---

## 📌 Assignment #1 — Python Basics

**Focus:**  
Understanding how Python programs work from input to output and learning how to think algorithmically.

### Topics Covered
- Basic Python syntax  
- Variables  
- Conditionals  
- User input & output  
- Working with VS Code  
- Introduction to Git & GitHub  

### Mini-Projects

| File | Description |
|-----|------------|
| `hundred_years_calculator.py` | Asks the user’s name and age, then calculates the year they will turn 100. |
| `simple_calculator.py` | Performs basic arithmetic operations on two user-entered numbers. |
| `positive_negative.py` | Determines whether a number is positive, negative, or zero. |
| `grader.py` | Prints **Passed** or **Failed** based on the user’s exam score. |

---

## 📌 Assignment #2 — Loops, Data Structures & Libraries

**Focus:**  
Learning how to control program flow, repeat operations, handle errors, and use built-in libraries.

### Topics Covered
- Loops (`for`, `while`)  
- Nested loops  
- Error handling (`try-except`)  
- Python standard libraries (`random`, `datetime`)  
- Writing interactive CLI programs  

### Mini-Projects

| File | Description |
|-----|------------|
| `countdown.py` | Counts down from a user-defined number and finishes with **"Ateşle! 🚀"**. |
| `sum_calculator.py` | Calculates the sum of numbers from 1 to N. |
| `multiplecation_table.py` | Generates a multiplication table using nested loops. |
| `number_check.py` | Validates user input and prevents crashes caused by invalid input. |
| `guessing_game.py` | Random number guessing game with higher/lower hints. |
| `midterm_counter.py` | Calculates remaining time until the next exam using `datetime`. |

---

## 📌 Assignment #3 — Data Hunters (Files, Regex & Testing)

**Focus:**  
Working with **realistic, messy data** and making programs more reliable, reusable, and testable.

This assignment introduces three important engineering skills:
1. **Data persistence** (files do not disappear when the program closes)
2. **Data cleaning** using Regular Expressions
3. **Verification** using unit tests

### Topics Covered
- File I/O (reading from and writing to files)  
- Regular Expressions (Regex)  
- Data extraction and cleaning  
- Interactive CLI design using loops  
- Unit testing with `pytest`  

### Mini-Projects

| File | Description |
|-----|------------|
| `data_hunter.py` | Extracts emails and phone numbers from broken data using Regex. The user can choose between loading data from a file or pasting raw data manually. Cleaned results are saved to output files. |
| `password_security.py` | Interactive password validation system that checks for uppercase letters, numbers, and special characters. The program runs in a loop and provides clear feedback. |
| `test_security.py` | Unit tests written with `pytest` to verify the password validation logic under multiple scenarios. |
| `lvl1_bozuk_veri.txt` | Noisy sample data containing mixed valid and invalid contact information. |
| `lvl2_bozuk_veri.txt` | More complex broken data with duplicates and log-style entries for advanced cleaning. |

---

## 📌 Assignment #4 — Object-Oriented Programming (OOP)

**Focus:**  
Transitioning to **Object-Oriented Programming (OOP)** by understanding classes, objects, methods, and encapsulation.

This assignment acts as a bridge to understanding the architecture of AI models and advanced software systems.

### Topics Covered
- Classes and Objects  
- The `__init__` constructor  
- Instance attributes and methods  
- State management inside objects  

### Mini-Projects

| File | Description |
|-----|------------|
| `rocket_simulation.py` | A `Rocket` class that tracks fuel levels. Includes methods to launch the rocket (consuming fuel) and refuel. Runs in a continuous interactive CLI loop. |
| `personal_assistant.py` | An `Assistant` class that acts as a simple AI chatbot. It tracks its own operation count invisibly and provides a status report, greeting, and current time. |

---

## 📌 Assignment #5 — The Pythonic Summit (Final Assignment)

**Focus:**  
Mastering advanced Python features to write shorter, more elegant, and highly efficient code ("Pythonic" code). This is the final step before diving into Artificial Intelligence.

### Topics Covered
- List Comprehensions (One-liners for `for` loops and `if` conditions)
- Advanced functions with `*args` and `**kwargs`
- Data filtering and manipulation

### Mini-Projects

| File | Description |
|-----|------------|
| `data_wizard.py` | A CLI simulation that generates a dataset of people and uses **list comprehensions** to filter them by age and name. It also features a robust `analyze_data` function showcasing the use of `*args` and `**kwargs` for flexible data processing. |

---

# 🤖 THE NEW ERA — Artificial Intelligence

Welcome to the second phase of the program! After mastering the "tools" of Python, we are now building systems that can "think" and solve problems using classical AI algorithms.

## 📌 AI Assignment #1 — Search Algorithms

**Focus:**  
Building the foundation of AI search agents. Understanding how pathfinding works using different frontier structures.

### Topics Covered
- Search Problems & State Spaces
- **Depth-First Search (DFS)** vs **Breadth-First Search (BFS)**
- Stack (LIFO) and Queue (FIFO) logic
- Class Inheritance for efficient code structure

### Mini-Projects

| File | Description |
|-----|------------|
| `search_structures.py` | A simulation where you can see exactly how Nodes are added and removed in DFS and BFS logic using Stack and Queue classes. |

---

## 📌 AI Assignment #2 — Knowledge & Logic

**Focus:**  
Building a **Deductive Inference Engine**. Understanding how an AI agent maintains a state (Knowledge Base), updates it with evidence, and makes logical decisions.

### Topics Covered
- Propositional Logic & Inference
- State Management (Knowledge Base)
- Logical Elimination (The "Clue" Game Philosophy)
- Clean OOP for decision-making systems

### Mini-Projects

| File | Description |
|-----|------------|
| `logic_deduction.py` | A `Detective` class simulation that maintains a list of suspects and uses logical elimination to find the culprit based on incoming evidence. |

---

## 📌 AI Assignment #3 — Uncertainty & Markov Models

**Focus:**  
Understanding how AI deals with uncertainty. Moving from absolute true/false logic to probabilistic reasoning using Markov Models to predict future states based on current realities.

### Topics Covered
- Uncertainty in AI
- The Markov Assumption
- Transition Probabilities
- Modeling state changes over time using OOP

### Mini-Projects

| File | Description |
|-----|------------|
| `weather_simulation.py` | A `Weather` class simulation that uses a Markov Model to predict the weather over a 10-day period based on weighted probabilities of transition between states. |

---

## 📁 Repository Structure

Polaris/
│

├── Polaris_Assignment_#1/

│   ├── hundred_years_calculator.py

│   ├── simple_calculator.py

│   ├── positive_negative.py

│   ├── grader.py

│

├── Polaris_Assignment_#2/

│   ├── countdown.py

│   ├── sum_calculator.py

│   ├── multiplecation_table.py

│   ├── number_check.py

│   ├── guessing_game.py

│   ├── midterm_counter.py

│

├── Polaris_Assignment_#3/

│   ├── data_hunter.py

│   ├── password_security.py

│   ├── test_security.py

│   ├── lvl1_bozuk_veri.txt

│   ├── lvl2_bozuk_veri.txt
│
├── Polaris_Assignment_#4/

│   ├── personal_assistant.py

│   ├── rocket_simulation.py

│

├── Polaris_Assignment_#5/

│   ├── data_wizard.py

│

├── Polaris_Assignment_AI_#1/

│   ├── search_structures.py

│

├── Polaris_Assignment_AI_#2/

│   ├── logic_deduction.py

│

├── Polaris_Assignment_AI_#3/

│   ├── weather_simulation.py

│

...

---

## 🎯 Purpose of This Repository

- Track my development as a Python & AI programmer  
- Build a structured and readable coding portfolio  
- Document my progress throughout the Polaris AI Program  
- Prepare for future work in **AI, robotics, electronics, and engineering systems**  

---

## 🛠️ Technologies Used

- Python 3  
- VS Code  
- Git & GitHub  
- Python Standard Library  
- pytest  

---

## 👤 Author

**Mohammad Taha Halakooei**  
Polaris AI Program Participant  
Biomedical Engineering Student @ Yildiz Technical University  

Interests: **Robotics • Electronics • AI • Problem-Solving**
