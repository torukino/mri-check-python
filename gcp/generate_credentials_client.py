from google.oauth2 import service_account
from googleapiclient import discovery
import os
# 認証情報を設定
def generate_credentials_client():
    api_version = "v1"
    service_name = "healthcare"
    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    # 認証情報の設定
    base_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_file = os.path.join(base_dir, '..', 'gcp_toruk.json') 
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    client = discovery.build(service_name, api_version, credentials=credentials)
    return credentials, client