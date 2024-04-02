import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"your-path-to-service-account-key.json"
from csv2database.csv_import import LocalCSVImporter, GoogleDriveImporter,GoogleSheetImporter

def main():

    # Call the import_csv_to_mysql function for local CSV files
    local_folder_path = r"your-path-to-local-folder"  # Use raw string for Windows file paths
    success_local = LocalCSVImporter(local_folder_path, "host", "dbname", "user", "password", create_fresh=False).import_csv_to_mysql()
    if success_local:
        print("Local CSV files imported successfully.")
    else:
        print("Error importing local CSV files.")

    # Call the load_csv_to_mysql function for Google Drive file
    google_drive_file_id = "your google drive file id"
    success_google_drive = GoogleDriveImporter(google_drive_file_id,create_fresh=False).load_csv_to_mysql("host", "dbname", "user", "password")
    if success_google_drive:
        print("Google Drive CSV file imported successfully.")
    else:
        print("Error importing Google Drive CSV file.")
    
    spreadsheet_id="your-spreadsheet-id"
    sheet_name =  "your Sheet name"
    success_google_sheet = GoogleSheetImporter(spreadsheet_id,sheet_name,create_fresh=False).load_sheet_to_mysql("host", "dbname", "user", "password")
    if success_google_sheet:
        print("Data imported successfully from Google Sheet.")
    else:
        print("Failed to import data from Google Sheet.")


if __name__ == "__main__":
    main()

