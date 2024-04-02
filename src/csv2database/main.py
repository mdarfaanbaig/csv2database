import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\Beginest_Project\beginest-service-account-key.json"
from csv2database.csv_import import LocalCSVImporter, GoogleDriveImporter,GoogleSheetImporter

def main():

    # Call the import_csv_to_mysql function for local CSV files
    local_folder_path = r"D:\MY Datasets"  # Use raw string for Windows file paths
    success_local = LocalCSVImporter(local_folder_path, "localhost", "my_database", "root", "Arfaan@123456", create_fresh=False).import_csv_to_mysql()
    if success_local:
        print("Local CSV files imported successfully.")
    else:
        print("Error importing local CSV files.")

    # Call the load_csv_to_mysql function for Google Drive file
    google_drive_file_id = "1meuL4jkluBZhrcYBriaIgLrFfwt5q-JO"
    success_google_drive = GoogleDriveImporter(google_drive_file_id,create_fresh=False).load_csv_to_mysql("localhost", "my_database", "root", "Arfaan@123456")
    if success_google_drive:
        print("Google Drive CSV file imported successfully.")
    else:
        print("Error importing Google Drive CSV file.")
    
    spreadsheet_id="1eTwI6jKzQiKrvaYUUIAluFTykFNFnNfY6Kf6ibhdjas"
    sheet_name =  "WaterData"
    success_google_sheet = GoogleSheetImporter(spreadsheet_id,sheet_name,create_fresh=False).load_sheet_to_mysql("localhost", "my_database", "root", "Arfaan@123456")
    if success_google_sheet:
        print("Data imported successfully from Google Sheet.")
    else:
        print("Failed to import data from Google Sheet.")


if __name__ == "__main__":
    main()

