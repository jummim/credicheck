import streamlit as st
from googleapiclient.discovery import build

# 페이지 제목 설정
st.title("🔍 구글 팩트체크 분석기")

# 본인의 API KEY와 CX(검색 엔진 ID)를 직접 입력합니다.
API_KEY = "AIzaSyDYX-It7NiJ-pRVEYY0J-R4KWsTHBb_5P4"
CX = "542df9d8f19064b62"

# 사용자 입력 받기
user_input = st.text_input("검증할 내용을 입력하세요:")

# 검색 버튼 클릭 시 동작
if st.button("검색"):
    if user_input:
        try:
            # 구글 검색 서비스 연결
            service = build("customsearch", "v1", developerKey=API_KEY)
            
            # 검색 결과 요청
            res = service.cse().list(q=user_input, cx=CX, lr="lang_ko", gl="kr").execute()
            
            # 검색 결과 출력
            if 'items' in res:
                st.success(f"'{user_input}'에 대한 검색 결과입니다:")
                for item in res['items'][:3]:
                    st.write(f"### {item['title']}")
                    st.write(item['snippet'])
                    st.write(f"링크: {item['link']}")
                    st.divider()
            else:
                st.write("관련된 검색 결과가 없습니다.")
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("검색어를 입력해주세요!")
