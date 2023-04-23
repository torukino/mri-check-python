from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request


import os


def get_instance_ids_from_dicomestore():
    # 認証情報の設定
    base_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_file = os.path.join(base_dir, '..', 'gcp_toruk.json') 
    credentials = service_account.Credentials.from_service_account_file(credentials_file)

    # Healthcare API クライアントの作成
    healthcare_service = build('healthcare', 'v1', credentials=credentials)

    # プロジェクト ID、リージョン、データセット名、DICOM ストア名、および DICOM インスタンス ID の設定
    project_id = "dicom-rensyuu"
    region = "asia-northeast1"
    dataset_id = "ohif-dataset"
    dicom_store_id = "ohif-datastore"

    # DICOM ストアから DICOM インスタンス ID を取得
    dicom_store_path = f"projects/{project_id}/locations/{region}/datasets/{dataset_id}/dicomStores/{dicom_store_id}"
    url = f"{healthcare_service._baseUrl}{dicom_store_path}/dicomWeb/studies"
        # Retrieve the access token.
    access_token = credentials.token if credentials.token else credentials.refresh(Request()).token

    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        instances = healthcare_service._http.request(url, headers=headers)
    except HttpError as error:
        print(f"An error occurred: {error}")
        instances = None

    if instances:
        print("Instances:")
        print(instances[1].decode('utf-8'))
    else:
        print("No instances found.")
    
    

if __name__ == "__main__":
    get_instance_ids_from_dicomestore()