Sales Report Analyzer

A Python command-line tool that reads sales data from a CSV file and automatically generates a sales report.

Features

- Reads sales data from a CSV file
- Allows the user to enter the CSV file path
- Calculates total revenue
- Calculates total units sold
- Shows revenue for each product
- Finds the product with the highest total revenue
- Handles invalid data without crashing
- Saves the generated report to a text file

How to Run

Make sure Python 3 is installed.

Run the program:

python main.py

The program will ask you to enter the path to your CSV file.

For example:

Enter CSV file path: sample_sales.csv

A sample CSV file ("sample_sales.csv") is included in this repository so you can test the program immediately.

CSV Format

The CSV file should contain these columns:

product,price,quantity
Keyboard,25,10
Mouse,15,20
Monitor,320,3
Headphones,90,9
Webcam,70,12

Example Output

===== SALES REPORT =====

Total revenue: 3,995
Products sold: 69

Product performance:
- Keyboard: 375
- Mouse: 450
- Monitor: 1,600
- Headphones: 810
- Webcam: 840

Best product: Monitor
Best revenue: 1,600

Report saved to sales_report.txt

Error Handling

If the CSV file cannot be found, the program displays:

File not found!

If a product contains invalid price or quantity data, the program skips that row and continues processing the remaining data.

Output

The generated report is automatically saved as:

sales_report.txt

Technologies

- Python 3
- CSV module
- File handling
- Dictionaries
- Loops
- Conditional statements
- Exception handling

Project Structure

sales-report-analyzer/
├── main.py
├── sample_sales.csv
├── README.md
└── sales_report.txt

Future Improvements

- Export reports to Excel
- Add charts and data visualization
- Add date-based sales analysis
- Generate automated email reports
- Add AI-powered sales summaries

Author

Mohamad Hossein
