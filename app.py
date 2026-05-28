import streamlit as st
from googleapiclient.discovery import build

st.title("🔍 구글 팩트체크 분석기")

# Streamlit Cloud의 Secrets에서 키를 안전하게 불러옵니다.
# 로컬에서 테스트할 때는 코드 하단에 설명을 참고하세요!
try:
    API_KEY = st.secrets["API_KEY"]
    CX = st.secrets["CX"]
except:
    st.error("API 키가 설정되지 않았습니다. Streamlit Secrets 설정을 확인하세요.")
    st.stop()

user_input = st.text_input("검증할 내용을 입력하세요:")

if st.button("검색"):
    if user_input:
        try:
            # 구글 검색 서비스 연결
            service = build("customsearch", "v1", developerKey=API_KEY)
            res = service.cse().list(q=user_input, cx=CX).execute()
            
            # 검색 결과 출력
            if 'items' in res:
                for item in res['items'][:3]:
                    st.write(f"### {item['title']}")
                    st.write(item['snippet'])
                    st.write(f"링크: {item['link']}")
            else:
                st.write("관련된 검색 결과가 없습니다.")
        except Exception as e:
            st.write(f"오류 발생: {e}")
