# app.py
import streamlit as st
import random
import datetime

# List of 100 animals
animals = [
    'アフリカゾウ', 'アメリカバイソン', 'アメリカワニ', 'アライグマ', 'アルマジロ', 'イヌ', 'イヌワシ', 'イリエワニ', 'ウサギ', 'ウシ',
    'ウマ', 'オオカミ', 'オオコウモリ', 'オオサンショウウオ', 'オオツノシカ', 'オオハシ', 'オオワシ', 'オカピ', 'オランウータン', 'カバ',
    'カピバラ', 'カモノハシ', 'カンガルー', 'ガチョウ', 'ガラパゴスゾウガメ', 'キリン', 'クジャク', 'クマ', 'クマネズミ', 'クモザル',
    'クワガタムシ', 'ケツァール', 'コアラ', 'コウモリ', 'コウモリガイ', 'コオロギ', 'コブハクチョウ', 'コヨーテ', 'サイ', 'サカマキガイ',
    'サケ', 'サソリ', 'サル', 'シカ', 'シマウマ', 'シロクマ', 'シロナガスクジラ', 'ジャガー', 'ジャイアントパンダ', 'ジュゴン',
    'スイギュウ', 'スカンク', 'スズメ', 'スズメバチ', 'スナネズミ', 'スネール', 'スローロリス', 'セイウチ', 'セミ', 'タカ',
    'タコ', 'タスマニアデビル', 'タツノオトシゴ', 'タナゴ', 'タンチョウ', 'チーター', 'チンチラ', 'チンパンジー', 'ツキノワグマ', 'ティラノサウルス',
    'テナガエビ', 'テントウムシ', 'トカゲ', 'トガリネズミ', 'トナカイ', 'トラ', 'トリケラトプス', 'ナマケモノ', 'ナマコ', 'ニホンザル',
    'ニワトリ', 'ヌー', 'ネコ', 'ネズミ', 'ノコギリクワガタ', 'ハチドリ', 'ハリネズミ', 'バッタ', 'バンディクート', 'パンダアリ',
    'ヒト', 'ヒトデ', 'ヒツジ', 'ヒヨケザル', 'フェネック', 'フクロウ', 'フクロモモンガ', 'フラミンゴ', 'フンコロガシ', 'ペリカン',
    'ホッキョクギツネ', 'ホワイトタイガー', 'マダガスカルヒシオガエル', 'マダガスカルヒメアリ', 'マンモス', 'ミツバチ', 'ミミズ', 'ムカデ', 'メガネモチノウオ', 'モグラ'
]

# Function to generate a life recommendation in Japanese
def generate_recommendation(animal):
    # Replace with actual recommendations
    recommendations = {animal: f'{animal}に関連する人生の提案' for animal in animals}

    return recommendations[animal]

# Streamlit app
st.title('ChatGPT試用アプリ')
st.write('生年月日を入力してください。')

dob = st.date_input('生年月日', datetime.date(2000, 1, 1))

if st.button('結果を表示'):
    animal = random.choice(animals)
    recommendation = generate_recommendation(animal)
    st.write(f'あなたの動物: {animal}')
    st.write(f'あなたに関連する人生の提案: {recommendation}')
