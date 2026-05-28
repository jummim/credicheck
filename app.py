import streamlit as st
from googleapiclient.discovery import build

st.title("🔍 구글 팩트체크 분석기")

# 보안 설정(Secrets) 대신 키를 코드에 직접 넣습니다.
API_KEY = "AIzaSyDYX-It7NiJ-pRVEYY0J-R4KWsTHBb_5P4"
CX = "542df9d8f19064b62"

user_input = st.text_input("검증할 내용을 입력하세요:")

if st.button("검색"):
    if user_input:
        try:
            # 구글 검색 서비스 연결
            service = build("customsearch", "v1", developerKey=API_KEY)
            
            # 검색 결과 요청
            res = service.cse().list(q=user_input, cx=CX, lr="lang_ko", gl="kr").execute()
            
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
