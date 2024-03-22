from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define the database model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    payment_mode = db.Column(db.String(50), nullable=False)
    entry_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    month = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month_year = db.Column(db.String(20), nullable=False)

# Read Excel sheet and store data in database
@app.route('/import')
def import_data():
    excel_file = 'Prashanth - Expense Tracker.xlsx'
    df = pd.read_excel(excel_file)
    for index, row in df.iterrows():
        expense = Expense(date=row['Date'], description=row['Description'],
                          category=row['Category'], payment_mode=row['Payment mode'],
                          entry_type=row['Type'], amount=row['Amount'],
                          month=row['Month'], year=row['Year'],
                          month_year=row['Month - Year'])
        db.session.add(expense)
    db.session.commit()
    return 'Data imported successfully'

if __name__ == '__main__':
    app.run(debug=True)
