import streamlit as st

# 1. Dán code ẩn giao diện vào đây (ngay dưới import)
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
    st.image("anh.jpg", caption="Nhìn quen lắm đk")
    st.image("ngoc_han_phongcanh.png",  caption="Nhìn quen lắm đk")
    st.video("https://www.youtube.com/watch?v=PWy4sxLpl58")
