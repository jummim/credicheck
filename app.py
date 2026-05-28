import streamlit as st

st.set_page_config(page_title="CrediCheck", page_icon="🔍")
st.title("🔍 CrediCheck: 온라인 정보 신뢰도 분석기")

user_input = st.text_area("분석할 내용을 입력하세요:", height=200)

if st.button("분석 시작"):
    if user_input:
        with st.spinner("정보의 신뢰도를 분석 중입니다..."):
            bad_words = ["기적", "100%", "무조건", "절대", "즉시"]
            score = 85
            
            for word in bad_words:
                if word in user_input:
                    score -= 10
            
            st.success("분석 완료!")
            st.write(f"### [종합 신뢰도 점수: {score}/100]")
            
            if score >= 80:
                st.info("✅ 매우 신뢰할 수 있는 정보입니다.")
            elif score >= 60:
                st.warning("⚠️ 중립적인 정보입니다. 출처를 한 번 더 확인하세요.")
            else:
                st.error("❌ 신뢰도가 매우 낮습니다. 과장된 광고성 정보일 수 있습니다.")
    else:
        st.warning("분석할 내용을 먼저 입력해주세요.")
