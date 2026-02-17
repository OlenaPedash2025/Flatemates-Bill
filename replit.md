# Flatmates Bill Splitter

## Overview
A Python CLI application that splits bills between flatmates based on the number of days each person stayed in the house. It generates a PDF report with the breakdown.

## Project Architecture
- **main.py** - Entry point, handles user input via CLI
- **Bill.py** - Bill dataclass (amount, period)
- **Flatmate.py** - Flatmate dataclass (name, days_in_house)
- **BillSplitter.py** - Business logic for splitting bills proportionally
- **PDFReport.py** - Generates PDF reports using fpdf
- **ValidationError.py** - Custom exception class
- **files/** - Contains assets (house.png) and generated PDFs

## Setup
- **Language**: Python 3.11
- **Dependencies**: fpdf, filestack-python, trafaret, requests (see requirements.txt)
- **Workflow**: Console-based CLI app (no web server)

## Recent Changes
- 2026-02-17: Initial import and setup in Replit environment
