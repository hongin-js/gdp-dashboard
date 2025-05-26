
import pandas as pd
import streamlit as st

# --- 사이드바 (슬라이더) ---
st.sidebar.title("슬라이더")
slider_val = st.sidebar.slider("값 선택", 0, 100, 50)

# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["탭 01", "탭 02", "탭 03"])

with tab1:
    st.write("탭 01 내용")
    users = [{"id": 1, "name": "홍길동"}, {"id": 2, "name": "이몽룡"}]
    selected_user = st.selectbox(
        "사용자 선택",
        users,
        format_func=lambda x: f"{x['name']} (ID: {x['id']})"
        )
    st.write("선택한 사용자 ID:", selected_user['id'])
    # 2x2 레이아웃 구성
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧱 레이아웃 01")
        st.info(f"슬라이더 값: {slider_val}")
        

    with col2:
        st.markdown("### 🧱 레이아웃 02")
        st.success("오른쪽 상단 영역")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🧱 레이아웃 03")
        st.warning("왼쪽 하단 영역")
    with col4:
        st.markdown("### 🧱 레이아웃 04")
        st.error("오른쪽 하단 영역")

with tab2:
    st.write("탭 02 내용")
    

    # 예시용 간단한 데이터프레임 생성
    data = {
        "행정구역": ["서울특별시", "부산광역시", "제주특별자치도", "서울특별시", "부산광역시"],
        "인구수": [9500000, 3400000, 670000, 9600000, 3450000],
        "연도": ["2024", "2024", "2024", "2025", "2025"]
    }
    df = pd.DataFrame(data)

    # 멀티셀렉트: 유저가 선택할 지역 목록
    행정구역목록 = sorted(df["행정구역"].unique())

    # 멀티셀렉트 위젯
    selected_regions = st.multiselect(
        "분석할 지역을 선택하세요", 
        options=행정구역목록, 
        default=["서울특별시"]
    )

    # 선택된 지역에 따라 필터링
    filtered_df = df[df["행정구역"].isin(selected_regions)]

    # 결과 출력
    st.write("선택된 지역 데이터:")
    st.dataframe(filtered_df)



with tab3:
    st.write("탭 03 내용")
    

    color = st.radio(
        "좋아하는 색을 고르세요",
        options=["빨강", "파랑", "초록"],
        index=1  # 기본 선택은 "파랑"
    )
    st.success(f"선택한 색상: {color}")



    age = st.slider("나이를 선택하세요", min_value=10, max_value=80, value=30, step=5)
    st.write("선택한 나이:", age)


