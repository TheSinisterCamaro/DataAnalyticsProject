import pandas as pd
from sqlalchemy import create_engine

# Connect to MySQL database
engine = create_engine('mysql+mysqlconnector://root:Adidas18*@localhost/CustomerFeedback')

# Load data into a DataFrame
df = pd.read_sql('SELECT * FROM Feedback', engine)

# Remove duplicates based on specific columns
df = df.drop_duplicates(subset=['Name', 'Email', 'Feedback', 'Rating', 'Date'])

# Fill missing values
df['Name'] = df['Name'].fillna('Unknown')
df['Email'] = df['Email'].fillna('unknown@example.com')
df['Feedback'] = df['Feedback'].fillna('No feedback provided.')
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())  # Fill missing ratings with average
df['Date'] = df['Date'].fillna(pd.to_datetime('today').strftime('%Y-%m-%d'))

# Save cleaned data back to the database or export as CSV
df.to_sql('CleanedFeedback', engine, if_exists='replace', index=False)
df.to_csv('CleanedFeedback.csv', index=False)

print("Data cleaning complete.")
