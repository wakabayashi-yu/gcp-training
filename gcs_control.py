import os
import pandas as pd
from io import BytesIO
from google.cloud import storage

# サービスアカウントから発行したjsonファイル
storage_client  = storage.Client.from_service_account_json('サービスアカウントから発行したjsonファイル.json')

bucket_name = 'wakabayashi_gcs_training_bucket'

# ※以下の4つの操作は各々独立しているため、個々で動作させる（例：バケット作成を行う場合は、その他3つをコメントアウトして実行）
# バケット作成
bucket = storage_client.create_bucket(bucket_name, location = 'asia-northeast1')

# バケットの削除
bucket = storage_client.get_bucket(bucket_name)
bucket.delete()

# バケット内にファイルの作成
file_name = 'test.txt' #ファイル名
blob_name = 'test/test.txt' #送り先での名前
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(file_name)

# バケット内のオブジェクトの削除
blob_name = 'test/test.txt'
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.delete()