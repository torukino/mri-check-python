import json

from generate_credentials_client import generate_credentials_client

def dicomweb_search_instance(project_id, location, dataset_id, dicom_store_id):
    """Handles the GET requests specified in DICOMweb standard.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
    before running the sample."""
    



    
    # Imports Python's built-in "os" module
    import os

    # Imports the google.auth.transport.requests transport
    from google.auth.transport import requests

    # Imports a module to allow authentication using a service account
    from google.oauth2 import service_account

    # Gets credentials from the environment.
    credentials, client = generate_credentials_client()
    scoped_credentials = credentials.with_scopes(
        ["https://www.googleapis.com/auth/cloud-platform"]
    )
    # Creates a requests Session object with the credentials.
    session = requests.AuthorizedSession(scoped_credentials)

    # URL to the Cloud Healthcare API endpoint and version
    base_url = "https://healthcare.googleapis.com/v1"

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
    # dicom_store_id = 'my-dicom-store' # replace with the DICOM store ID
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, location)

    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/instances".format(
        url, dataset_id, dicom_store_id
    )

    # Sets required application/dicom+json; charset=utf-8 header on the request
    headers = {"Content-Type": "application/dicom+json; charset=utf-8"}

    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()

    instances = response.json()

    # print("Instances:")
    # print(json.dumps(instances[0], indent=2))

    return instances

if __name__ == "__main__": 
    PatientName = "00100010"
    PatientID = "00100020"
    PatientBirthDate = "00100030"
    PatientSex = "00100040"
    SliceThickness = "00180050"
    KVP = "00180060"
    StudyInstanceUID = "0020000D"
    SeriesInstanceUID = "0020000E"
    InstanceUID = "00080018"
    StudyID = "00200010"
    SeriesNumber = "00200011"
    InstanceNumber = "00200013"
    SamplesPerPixel = "00280002"
    Rows = "00280010"
    Columns = "00280011"
    BitsAllocated = "00280100"
    BitsStored = "00280101"
    HighBit = "00280102"
    PixelRepresentation = "00280103"
    
    project_id = "dicom-rensyuu"
    location = "asia-northeast1"
    dataset_id = "ohif-dataset"
    dicom_store_id = "ohif-datastore"
    dcm_file = "public/dicomsample2/1.2.840.113619.2.274.10502719.2140785.23669.1512516045.813.dcm"
    
    instances = dicomweb_search_instance(project_id, location, dataset_id, dicom_store_id)
    print("study uid",instances[0][StudyInstanceUID])
    print("series uid",instances[0][SeriesInstanceUID])
    print("instance uid",instances[0][InstanceUID])
    
    
