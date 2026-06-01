import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/username/ten-repo/main/background.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.title("🎂 Chúc em ngày Quốc tế thiếu nhi thật nhiều niềm vui. Dù lớn rồi nhưng vẫn luôn là một cô bé hạnh phúc nhé!")

if st.button('Nhấn vào đây để nhận quà bất ngờ'):
    st.balloons() # Hiệu ứng bóng bay
    st.success("Cảm ơn vì đã luôn là một người bạn tuyệt vời! Chúc em mọi điều tốt đẹp nhất!")    
    st.image("anh.jpg", caption="chắc e sẽ nhận ra người trong ảnh mà đk")
    st.image("ngoc_han_phongcanh.png",  caption="Nhìn quen lắm đk")
    st.image("ki_niem_ff.png",  caption="Kĩ niệm năm ngoái")
    st.image("tn_dautien.png",  caption="tn đầu tiên")
    st.image("loi_hua.png",  caption="Lời hứa hqua")
    st.video("https://www.youtube.com/watch?v=PWy4sxLpl58")
