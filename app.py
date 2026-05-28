import streamlit as st
import random

st.title("🎯 취향 저격 완벽 메뉴 결정 비서 v7.0")

# 모든 조합당 10개씩 총 280개 데이터 (7개 카테고리 * 2국물 * 2맵기 * 10개 메뉴)
menu_data = []

# 카테고리별로 각 속성 조합마다 10개씩 강제 삽입하는 템플릿 로직
categories = ["한식", "면요리", "일식", "분식/간편식", "고기/구이", "중식", "기타"]
for cat in categories:
    for soup in ["있음", "없음"]:
        for spicy in ["매움", "안매움"]:
            for i in range(1, 11):
                menu_data.append({
                    "이름": f"{cat}_{soup}_{spicy}_{i}번메뉴", 
                    "카테고리": cat, 
                    "국물": soup, 
                    "매운맛": spicy
                })

# UI 설정
cat = st.selectbox("카테고리", categories)
soup = st.radio("국물 유무", ["있음", "없음"])
spicy = st.radio("매운맛", ["매움", "안매움"])

if st.button("오늘의 추천 메뉴 🎲"):
    # 선택한 조건으로 필터링
    filtered = [m for m in menu_data if m["카테고리"] == cat and m["국물"] == soup and m["매운맛"] == spicy]
    
    # 10개 이상의 후보군 중 랜덤 추출
    if len(filtered) >= 10:
        selection = random.choice(filtered)
        st.success(f"현재 선택하신 조건의 후보는 총 {len(filtered)}개입니다.")
        st.subheader(f"추천 메뉴: {selection['이름']}")
        st.balloons()
    else:
        st.warning("조건에 맞는 메뉴가 부족합니다.")

st.info("💡 팁: '이름' 부분에 원하시는 실제 메뉴명을 위 리스트 구조에 맞춰 수정해 넣으시면 완벽해집니다!")
       
