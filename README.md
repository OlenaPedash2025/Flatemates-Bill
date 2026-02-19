# 🏠 Flatmates Bill Splitter

A professional Python command-line application that calculates house bills between roommates based on their stay duration. It automates the math and generates a clean PDF report.

## 🚀 Live Demo
You can test the application immediately in the browser via Replit:

[![Run on Replit](https://replit.com/badge/github/OlenaPedash2025/Flatemates-Bill)](https://flatemates-bill--olenapedash.replit.app)

---

## ✨ Key Features
* **Dynamic CLI**: User-friendly terminal interface for data entry.
* **Proportional Logic**: Calculates costs based on the exact number of days each person stayed.
* **PDF Reporting**: Automatically generates a formatted `flatmates_bill.pdf` with tables.
* **Robust Architecture**: Built using Object-Oriented Programming (OOP) for high maintainability.

## 🛠 Best Practices Implemented

In this project, I focused on writing professional, maintainable, and robust code by implementing the following practices:

* **Object-Oriented Programming (OOP)**: Clear separation of concerns between logic (`BillSplitter`), reporting (`PDFReport`), and configuration (`Config`).
* **Automated Testing**: Included a suite of Unit Tests using the `unittest` framework to ensure calculation accuracy and handle edge cases.
* **Persistent Logging**: Implemented a dual-handler logging system that records application events and errors both to the console and to a local `app.log` file.
* **Robust Error Handling**: Used `try...except` blocks and custom exception handling to manage invalid user inputs and network issues gracefully.
* **Configuration Management**: Centralized all paths, API keys, and constants into a `Config` class for easier maintenance.
* **Environment Reproducibility**: Managed dependencies via `requirements.txt` and used Python virtual environments (`.venv`).
* **Clean Code**: Followed PEP 8 naming conventions and added docstrings for better code readability.

## 🛠️ Installation & Setup
To run this project locally on your machine:

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/OlenaPedash2025/Flatemates-Bill.git](https://github.com/OlenaPedash2025/Flatemates-Bill.git)
   cd Flatemates-Bill
