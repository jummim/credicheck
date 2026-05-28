import streamlit as st
from googleapiclient.discovery import build

# 페이지 설정
st.set_page_config(page_title="우리 동네 축제 찾기")
st.title("🎉 우리 동네 축제 찾기")

# 본인의 API KEY와 CX(검색 엔진 ID)를 입력하세요
API_KEY = "AIzaSyDYX-It7NiJ-pRVEYY0J-R4KWsTHBb_5P4"
CX = "cx=542df9d8f19064b62"

# 사용자 입력
region = st.text_input("축제를 찾고 싶은 지역을 입력하세요 (예: 서울, 제주, 부산):")

# 검색 버튼
if st.button("축제 검색"):
    if region:
        try:
            # 구글 커스텀 검색 서비스 연결
            service = build("customsearch", "v1", developerKey=API_KEY)
            
            # 검색어 설정 (지역 + 축제 키워드)
            query = f"{region} 지역 축제 행사 일정"
            
            # 검색 실행 (한국어, 한국 지역 결과)
            res = service.cse().list(q=query, cx=CX, lr="lang_ko", gl="kr").execute()
            
            # 결과 출력
            if 'items' in res:
                st.subheader(f"'{region}' 지역 축제 검색 결과")
                for item in res['items'][:5]: # 상위 5개만 출력
                    st.write(f"### {item['title']}")
                    st.write(item['snippet'])
                    st.link_button("상세 정보 보기", item['link'])
                    st.divider()
            else:
                st.info("해당 지역의 축제 정보를 찾을 수 없습니다. 지역명을 다시 확인해 보세요!")
        
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
            st.write("Tip: API 키나 CX가 정확한지, 혹은 할당량이 남았는지 확인해 주세요.")
    else:
        st.warning("지역명을 입력해주세요!")
