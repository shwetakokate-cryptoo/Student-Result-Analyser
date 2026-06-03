import pandas as pd

# ====================== STUDENT RESULT ANALYSER ======================
# Phase 1: Data Loading and Statistical Analysis - Shweta's Part
# ===================================================================

# Load the dataset
print("🔄 Loading dataset...")
df = pd.read_csv('students.csv')

# ====================== 1. DATA EXPLORATION ======================
print("\n" + "="*60)
print("📊 DATASET OVERVIEW")
print("="*60)
print(f"Total number of students: {len(df)}")
print(f"Number of columns: {df.shape[1]}")
print("\nFirst 5 rows of data:")
print(df.head())

print("\n" + "="*60)
print("📋 DATA INFORMATION")
print("="*60)
print(df.info())

print("\n" + "="*60)
print("📈 STATISTICAL SUMMARY")
print("="*60)
print(df.describe())

# ====================== 2. AVERAGE MARKS PER SUBJECT ======================
print("\n" + "="*60)
print("📊 AVERAGE MARKS PER SUBJECT")
print("="*60)
print(f"Math Score Average    : {df['math score'].mean():.2f}")
print(f"Reading Score Average : {df['reading score'].mean():.2f}")
print(f"Writing Score Average : {df['writing score'].mean():.2f}")

# ====================== 3. PASS / FAIL ANALYSIS ======================
# Calculate average score
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3

# Define Pass/Fail (Pass if average >= 40)
df['result'] = df['average_score'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

print("\n" + "="*60)
print("✅ PASS / FAIL COUNT")
print("="*60)
print(df['result'].value_counts())
print(f"\nPass Percentage: {(df['result'].value_counts()['Pass'] / len(df) * 100):.2f}%")

# ====================== 4. TOP 5 SCORERS ======================
print("\n" + "="*60)
print("🏆 TOP 5 SCORERS")
print("="*60)
top_5 = df.nlargest(5, 'average_score')[
    ['gender', 'race/ethnicity', 'parental level of education', 
     'lunch', 'test preparation course', 'average_score']
]
print(top_5.round(2))

# ====================== 5. GENDER-WISE AVERAGE ======================
print("\n" + "="*60)
print("👥 GENDER-WISE AVERAGE SCORES")
print("="*60)
gender_avg = df.groupby('gender')[['math score', 'reading score', 'writing score', 'average_score']].mean()
print(gender_avg.round(2))

# ====================== FINAL MESSAGE ======================
print("\n" + "="*60)
print("✅ ANALYSIS COMPLETE! All statistics calculated successfully.")
print("="*60)
