from generate_credentials_client import generate_credentials_client


def dicomweb_retrieve_instance(
    project_id,
    location,
    dataset_id,
    dicom_store_id,
    study_uid,
    series_uid,
    instance_uid,
):
    """Handles the GET requests specified in the DICOMweb standard.

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
    # study_uid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0'  # replace with the study UID
    # series_uid = '2.24.52329571877967561426579904912379710633'  # replace with the series UID
    # instance_uid = '1.3.6.2.4.2.14619.5.2.1.6280.6001.129311971280445372188125744148'  # replace with the instance UID
    url = "{}/projects/{}/locations/{}".format(base_url, project_id, location)

    dicom_store_path = "{}/datasets/{}/dicomStores/{}".format(
        url, dataset_id, dicom_store_id
    )

    dicomweb_path = "{}/dicomWeb/studies/{}/series/{}/instances/{}".format(
        dicom_store_path, study_uid, series_uid, instance_uid
    )

    file_name = "instance.dcm"

    # Set the required Accept header on the request
    headers = {"Accept": "application/dicom; transfer-syntax=*"}
    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()

    with open(file_name, "wb") as f:
        f.write(response.content)
        print(
            "Retrieved DICOM instance and saved to {} in current directory".format(
                file_name
            )
        )

    return response



if __name__ == "__main__": 
    project_id = "dicom-rensyuu"
    location = "asia-northeast1"
    dataset_id = "ohif-dataset"
    dicom_store_id = "ohif-datastore"
    dcm_file = "public/dicomsample2/1.2.840.113619.2.274.10502719.2140785.23669.1512516045.813.dcm"
    study_uid = "1.2.392.3680043.9.7242.123.1201.636840621399212263.879957638"
    series_uid ="1.2.392.3680043.9.7242.123.1202.636840621399212263.55872160.1"
    instance_uid = "1.2.392.3680043.9.7242.123.1203.636840621399212263.55872160.1.1"
    dicomweb_retrieve_instance(
        project_id,
        location,
        dataset_id,
        dicom_store_id,
        study_uid,
        series_uid,
        instance_uid,
    )