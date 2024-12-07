import streamlit as st

# 充電器のアイコン
st.set_page_config(page_title="リンクラ スクステスタミナ計算機", page_icon="🔋")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# タイトル
st.title('スクステスタミナ計算機')

# SIsCa回復(0 ~ 40)
sica_recover = st.number_input('SIsCa回復(0~40)', value=6, min_value=0, max_value=40)

# デイリーライブ挑戦回数 0 ~ 24
daily_challenge_num = st.number_input('デイリーライブ挑戦回数(0~24)', value=24, min_value=0, max_value=24)

# ラーニングライブキャンペーン なし or 1.5倍 or 2倍
learning_live_campaign = st.radio('ラーニングライブキャンペーン', ('なし', '1.5倍', '2倍'))

# 何日分か
days = st.number_input('何日分か', value=1, min_value=1)

# 30lv -> 50Lv にできる回数
# 2390pt. 30Lv. -> 40Lv, 2620pt. 40Lv. -> 50Lv.
# 5スタミナ消化で 1回あたり5pt

# 自然回復分を含むかどうか
natural_recover = st.checkbox('自然回復分(288回/日)を含むかどうか')

natural_stamina = 0
if natural_recover:
    natural_stamina = 288

# 合計スタミナ
stamina = (sica_recover * 100 + daily_challenge_num * 50 + natural_stamina) * days

learning_live_campaign_rate = 1
if learning_live_campaign == '2倍':
    learning_live_campaign_rate = 2
elif learning_live_campaign == '1.5倍':
    learning_live_campaign_rate = 1.5

st.write('ラーニング回数: ', stamina // 5)
st.write('累計ラーニングPt.', stamina // 5 * 5)
st.write('30Lv -> 50Lv にできる回数: ', ((stamina // 5) * 5) * learning_live_campaign_rate / 5010)