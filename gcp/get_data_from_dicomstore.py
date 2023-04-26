
from generate_credentials_client import generate_credentials_client

def list_dicom_stores(project_id, location, dataset_id):

    credentials, client = generate_credentials_client()

    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(project_id, location, dataset_id)
    dicom_stores = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .list(parent=dicom_store_parent)
        .execute()
        .get("dicomStores", [])
    )
    return dicom_stores

# DICOM ストアの詳細を取得する
def get_dicom_store(project_id, location, dataset_id, dicom_store_id):
    credentials, client = generate_credentials_client()

    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(project_id, location, dataset_id)
    dicom_store_name = "{}/dicomStores/{}".format(dicom_store_parent, dicom_store_id)

    dicom_stores = client.projects().locations().datasets().dicomStores()
    dicom_store = dicom_stores.get(name=dicom_store_name).execute()

    # print(json.dumps(dicom_store, indent=2))
    return dicom_store

def get_instance_ids_from_dicom_store(project_id, location, dataset_id, dicom_store_id):
    client = generate_credentials_client()
    # Healthcare APIのクライアントを作成し、認証情報を渡す
    dicom_store_parent = f"projects/{project_id}/locations/{location}/datasets/{dataset_id}/dicomStores/{dicom_store_id}"

    instance_list = []
    

    for study in client.list_dicom_store_studies(parent=dicom_store_parent):
        study_name = study.name
        for series in client.list_dicom_store_series(parent=study_name):
            series_name = series.name
            for instance in client.list_dicom_store_instances(parent=series_name):
                instance_id = instance.name.split('/')[-1]
                instance_list.append(instance_id)




if __name__ == "__main__":    
    # プロジェクト ID、リージョン、データセット名、DICOM ストア名、および DICOM インスタンス ID の設定
    project_id = "dicom-rensyuu"
    location = "asia-northeast1"
    dataset_id = "ohif-dataset"
    dicom_store_id = "ohif-datastore"

    lists = list_dicom_stores(project_id, location, dataset_id)
    for list in lists:
        print("dicom store一覧: ",list["name"])

    details = get_dicom_store(project_id, location, dataset_id, dicom_store_id)
    print("dicom store詳細: ",details)
    
    instance_list = get_instance_ids_from_dicom_store(project_id, location, dataset_id, dicom_store_id)
    # Instance IDを表示
    print(instance_list)