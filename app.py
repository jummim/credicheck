import streamlit as st

# 페이지 설정
st.set_page_config(page_title="CrediCheck", page_icon="🔍")
st.title("🔍 CrediCheck: 온라인 정보 신뢰도 분석기")
st.subheader("정보의 링크나 텍스트를 입력하면 신뢰도를 분석해 드립니다.")

# 사용자 입력
user_input = st.text_area("분석할 텍스트나 기사 내용을 입력하세요:", height=200)

if st.button("분석 시작"):
    if user_input:
        with st.spinner("정보의 신뢰도를 분석 중입니다..."):
            # 분석 로직 (시연을 위한 예시 결과값)
            # 실제 서비스 시에는 여기에 AI 분석 로직이 들어갑니다.
            st.success("분석 결과")
            st.write("### [종합 신뢰도 점수: 78/100]")
            
            # 4대 지표 시각화
            col1, col2 = st.columns(2)
            with col1:
                st.write("- **출처 객관성:** 8/10")
                st.write("- **데이터 일관성:** 9/10")
            with col2:
                st.write("- **감정적 편향성:** 5/10")
                st.write("- **근거 최신성:** 7/10")
            
            st.write("---")
            st.write("**분석 요약:** 해당 정보는 공신력 있는 기관의 데이터를 인용하고 있어 논리적으로 안정적이나, 감정적인 단어가 일부 포함되어 있어 중립적 판단이 필요합니다.")
    else:
        st.warning("분석할 내용을 먼저 입력해주세요.")
