from generate_credentials_client import generate_credentials_client


def list_dicom_stores(project_id, location, dataset_id):
    # Lists the DICOM stores in the given dataset.
    credentials, client = generate_credentials_client()

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    dicom_stores = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .list(parent=dicom_store_parent)
        .execute()
        .get("dicomStores", [])
    )

    print("DICOM stores list\n")
    for dicom_store in dicom_stores:
        print(dicom_store)

    return dicom_stores
