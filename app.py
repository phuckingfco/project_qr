import streamlit as st

st.title("🎂 Chúc mừng ngày 1/6, người anh em!")

if st.button('Nhấn vào đây để nhận quà bất ngờ'):
    st.balloons() # Hiệu ứng bóng bay
    st.success("Cảm ơn vì đã luôn là một người bạn tuyệt vời! Chúc bạn mọi điều tốt đẹp nhất!")
    
    # Dòng này là chìa khóa để hiện video của bạn
    st.video("https://www.youtube.com/watch?v=PWy4sxLpl58")
