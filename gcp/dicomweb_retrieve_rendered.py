from generate_credentials_client import generate_credentials_client
from PIL import Image

def dicomweb_retrieve_rendered(
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

    dicomweb_path = "{}/dicomWeb/studies/{}/series/{}/instances/{}/rendered".format(
        dicom_store_path, study_uid, series_uid, instance_uid
    )

    file_name = "rendered_image.png"

    # Sets the required Accept header on the request for a PNG image
    headers = {"Accept": "image/png"}
    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()

    with open(file_name, "wb") as f:
        f.write(response.content)
        print(
            "Retrieved rendered image and saved to {} in current directory".format(
                file_name
            )
        )
        # Open and display the saved image.
        img = Image.open("rendered_image.png")
        img.show()

    return response
