**CSV to Database Importer**

This Python package provides functionality to import CSV files into a MySQL database. It supports both local CSV files and CSV files stored on Google Drive.You can also import Google Sheets to MYsql.


**Installation**

You can install the package using pip:
pip install csv2database


**Usage**

**Local CSV Import**

To import local CSV files into your MySQL database, you can use the LocalCSVImporter class provided by this package. Here's an example of how to use it:

from csv2database.csv_import import LocalCSVImporter

#Specify the folder path containing your CSV files

folder_path = "/path/to/your/csv/files"

#Initialize LocalCSVImporter and call the import_csv_to_mysql method

success = LocalCSVImporter(folder_path, "localhost", "my_database", "root", "password").import_csv_to_mysql()

if success:
    print("Local CSV files imported successfully.")
else:
    print("Error importing local CSV files.")


**Google Drive CSV Import**

To import CSV files from Google Drive into your MySQL database, you can use the GoogleDriveImporter class provided by this package. Here's an example of how to use it:

from csv2database.csv_import import GoogleDriveImporter

#Specify the file ID of the CSV file on Google Drive

file_id = "your_google_drive_file_id"

#Initialize GoogleDriveImporter and call the load_csv_to_mysql method

success = GoogleDriveImporter(file_id).load_csv_to_mysql("localhost", "my_database", "root", "password")

if success:
    print("Google Drive CSV file imported successfully.")
else:
    print("Error importing Google Drive CSV file.")


 **Google Sheet Import**

To import data from Google Sheets into your MySQL database, you can use the GoogleSheetImporter class provided by this package. Here's an example of how to use it:

from csv2database.csv_import import GoogleSheetImporter

#Specify the spreadsheet ID and sheet name from Google Sheets

spreadsheet_id = "your_google_sheets_spreadsheet_id"
sheet_name = "YourSheetName"

#Initialize GoogleSheetImporter and call the load_sheet_to_mysql method

success = GoogleSheetImporter(spreadsheet_id, sheet_name).load_sheet_to_mysql("localhost", "my_database", "root", "password")

if success:
    print("Data imported successfully from Google Sheet.")
else:
    print("Failed to import data from Google Sheet.")


**Dependencies:**
numpy >= 1.0.0
pandas >= 1.0.0
mysql-connector-python >= 8.0.0
google-api-python-client >= 2.0.0


**License**
This project is licensed under the MIT License. See the LICENSE file for details.
