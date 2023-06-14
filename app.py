import pandas as pd
import boto3
from io import StringIO
import streamlit as st

# AWSのクレデンシャルを設定（AWS Management Consoleで確認できます）
AWS_ACCESS_KEY_ID = 'AKIAV27ZCYO3NIGWWEEZ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_BUCKET = 'skkeng'
AWS_S3_REGION_NAME = 'ap-northeast-1' # 例：'us-west-2'

s3 = boto3.client('s3', 
                  region_name=AWS_S3_REGION_NAME,
                  aws_access_key_id=AWS_ACCESS_KEY_ID, 
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def load_data():
    # S3からCSVを読み込み、DataFrameに変換
    obj = s3.get_object(Bucket=AWS_S3_BUCKET, Key='df.csv')
    df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
    return df

def save_data(df):
    # DataFrameをCSVに変換し、S3に保存
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=AWS_S3_BUCKET, Key='df.csv', Body=csv_buffer.getvalue())

def create_df():
    # 新たなDataFrameを作成
    df = pd.DataFrame({'ID': ['test', 'torajimax', 'kk'],
                       'PASS': ['test', 'torajimax', 'kk'],
                       '日付': ['2023/6/14', '2023/6/14', '2023/6/14'],
                       '身長': [180, 175, 160],
                       '体重': [70, 65, 60],
                       '体脂肪率': [10.50, 15.05, 20.60],
                       '年齢': [30, 34, 49],
                       '性別': ['男性', '男性', '女性'],
                       'タスク': ['１日1500kcal以内', '１日１万歩達成', '動画講義１章分視聴'],
                       '感想': ['良かった', '大きい', '強い']})
    return df

def app():
    st.title('S3 DataFrame App')

    if st.button('Create DataFrame'):
        df = create_df()
        save_data(df)
        st.write('DataFrame created and saved to S3')

    if st.button('Load DataFrame'):
        df = load_data()
        st.write(df)

if __name__ == "__main__":
    app()
