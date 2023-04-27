import pydicom
import matplotlib.pyplot as plt

def display_dicom_tags_and_image(file_path):
    # DICOMファイルを読み込む
    ds = pydicom.dcmread(file_path)

    # タグ一覧を表示する
    print("DICOM タグ一覧:")
    print(ds)

    # DICOM画像データを取得する
    image_data = ds.pixel_array

    # 画像を表示する
    plt.imshow(image_data, cmap=plt.cm.gray)
    plt.show()

# ここにDICOMファイルのパスを入力してください
dicom_file_path = "instance.dcm"
display_dicom_tags_and_image(dicom_file_path)
