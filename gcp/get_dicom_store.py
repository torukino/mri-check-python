# DICOM ストアを取得する

from generate_credentials_client import generate_credentials_client


def get_dicom_store(project_id, location, dataset_id, dicom_store_id):
    """Gets the specified DICOM store.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
    before running the sample."""
    credentials, client = generate_credentials_client()

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
    # dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)

    dicom_stores = client.projects().locations().datasets().dicomStores()
    dicom_store = dicom_stores.get(name=dicom_store_name).execute()


    return dicom_store
