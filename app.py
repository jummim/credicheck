import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="CrediCheck", page_icon="🔍")
st.title("🔍 CrediCheck: 실시간 팩트체크 분석기")

user_input = st.text_area("검증할 내용을 입력하세요:", height=200)

if st.button("실시간 검증 시작"):
    if user_input:
        with st.spinner("웹에서 관련 자료를 검색하고 분석 중입니다..."):
            # DuckDuckGo를 사용해 실시간 웹 검색
            with DDGS() as ddgs:
                results = list(ddgs.text(user_input, max_results=3))
            
            st.success("검색 완료! 관련 정보입니다:")
            
            if results:
                for i, res in enumerate(results):
                    st.write(f"**[참고 자료 {i+1}]** {res['title']}")
                    st.write(f"내용: {res['body']}")
                    st.write(f"링크: {res['href']}")
                st.info("위 검색 결과와 입력 내용을 비교하여 신뢰도를 판단해 보세요.")
            else:
                st.write("관련 자료를 찾을 수 없습니다.")
    else:
        st.warning("내용을 입력해주세요.")
