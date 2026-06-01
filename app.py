import streamlit as st

st.title("🎂 Chúc em ngày Quốc tế thiếu nhi thật nhiều niềm vui. Dù lớn rồi nhưng vẫn luôn là một cô bé hạnh phúc nhé!")

if st.button('Nhấn vào đây để nhận quà bất ngờ'):
    st.balloons() # Hiệu ứng bóng bay
    st.success("Cảm ơn vì đã luôn là một người bạn tuyệt vời! Chúc bạn mọi điều tốt đẹp nhất!")
    
    st.image("anh.jpg", caption="Nhìn quen hok, đẹp lắm đó, anh cũng xin lỗi vì tự ý xem ảnh em")
    st.video("https://www.youtube.com/watch?v=PWy4sxLpl58")
