import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# נתיב לקובץ האישורים
CREDENTIALS_FILE = 'client_secret_1064711230123-qa0rc8faojh9u3avu1lo8iepcvs9nhch.apps.googleusercontent.com.json'

# יצירת שירות גוגל דרייב
def create_drive_service():
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE)
    return build('drive', 'v3', credentials=creds)

# פונקציה להעלאת קובץ לדרייב ולשיתוף הקישור
def upload_file_to_drive(file_path):
    # יצירת שירות
    service = create_drive_service()

    # הגדרת נתוני הקובץ
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': ['your_drive_folder_id']  # אם יש תיקייה ספציפית, ציין את ה-ID שלה כאן
    }
    media = MediaFileUpload(file_path, resumable=True)

    # העלאת הקובץ לדרייב
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    # הגדרת שיתוף קישור
    file_id = file.get('id')
    service.permissions().create(
        fileId=file_id,
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    # יצירת קישור שיתוף
    link = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
    return link
