from dicomweb_retrieve_instance import dicomweb_retrieve_instance
from dicomweb_search_studies import dicomweb_search_studies
from generate_credentials_client import generate_credentials_client
from list_dicom_stores import list_dicom_stores
from get_dicom_store import get_dicom_store
from dicomweb_search_instance import dicomweb_search_instance
from google.auth.transport import requests
import json


def dicomweb_store_instance(project_id, location, dataset_id, dicom_store_id, dcm_file):
    client, credentials = generate_credentials_client() 
    scoped_credentials = credentials.with_scopes(
        ["https://www.googleapis.com/auth/cloud-platform"]
    )
    # Creates a requests Session object with the credentials.
    session = requests.AuthorizedSession(scoped_credentials)

    # URL to the Cloud Healthcare API endpoint and version
    base_url = "https://healthcare.googleapis.com/v1" 
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, location)

    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies".format(
        url, dataset_id, dicom_store_id
    )

    with open(dcm_file, "rb") as dcm:
        dcm_content = dcm.read()
        # Sets required "application/dicom" header on the request
    headers = {"Content-Type": "application/dicom"}

    response = session.post(dicomweb_path, data=dcm_content, headers=headers)
    response.raise_for_status()
    print("Stored DICOM instance:")
    print(response.text)
    return response



if __name__ == "__main__": 
    project_id = "dicom-rensyuu"
    location = "asia-northeast1"
    dataset_id = "ohif-dataset"
    dicom_store_id = "ohif-datastore"
    dcm_file = "public/dicomsample2/1.2.840.113619.2.274.10502719.2140785.23669.1512516045.813.dcm"
    
    # dicomweb_store_instance(project_id, location, dataset_id, dicom_store_id, dcm_file)
    
    # dicomweb_search_instance(project_id, location, dataset_id, dicom_store_id)

    # dicom_store = get_dicom_store(project_id, location, dataset_id, dicom_store_id)
    # print(json.dumps(dicom_store, indent=2))
    
    # dicomweb_search_studies(project_id, location, dataset_id, dicom_store_id)

    # list_dicom_stores(project_id, location, dataset_id)

    dicomweb_search_instance(project_id, location, dataset_id, dicom_store_id)

    # dicomweb_retrieve_instance(
    #     project_id,
    #     location,
    #     dataset_id,
    #     dicom_store_id,
    #     study_uid,
    #     series_uid,
    #     instance_uid,
    # )