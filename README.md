# Student Result Analyser

An interactive Python project to analyze student performance in exams using data analysis and visualization.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)

## 📋 Project Overview

This project analyzes the **Students Performance in Exams** dataset to provide meaningful insights such as:
- Average scores in Math, Reading, and Writing
- Pass/Fail statistics
- Top performing students
- Gender-wise performance comparison
- Visual representations of the data

## 🗂 Dataset

- **Source**: [Students Performance in Exams - Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **File**: `students.csv`
- **Rows**: 1000 students
- **Columns**: Gender, Race/Ethnicity, Parental Level of Education, Lunch, Test Preparation Course, Math Score, Reading Score, Writing Score

## 🚀 Features

- Data loading and exploration
- Statistical analysis (averages, pass/fail, top scorers)
- Gender-wise performance comparison
- Multiple visualizations (Bar charts, Pie chart, Histogram)

## 🛠 Technologies Used

- **Python**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Enhanced statistical visualizations

## 📁 Project Structure

```bash
Student-Result-Analyser/
├── students.csv
├── analysis.py
├── visualisation.py
├── main.py
├── charts/
│   ├── avg_scores.png
│   ├── pass_fail.png
│   ├── score_distribution.png
│   └── gender_comparison.png
└── README.md
