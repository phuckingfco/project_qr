import streamlit as st
import time

st.title("🎂 Chúc mừng ngày 1/6, người anh em!")

if st.button('Nhấn vào đây để nhận quà bất ngờ'):
    st.balloons() # Hiệu ứng bóng bay
    st.success("Cảm ơn vì đã luôn là một người bạn tuyệt vời! Chúc bạn mọi điều tốt đẹp nhất!")
    st.video("https://youtube.com/shorts/PWy4sxLpl58?si=FGXBUhxSJgq9DxC3")
