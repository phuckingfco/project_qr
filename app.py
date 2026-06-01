import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Ép chữ luôn hiển thị màu trắng sáng rõ nét trên mọi nền */
            .stApp, .stMarkdown, .stText, p, div {
                color: #FFFFFF !important; 
            }
            
            /* Đảm bảo tiêu đề cũng luôn sáng */
            h1, h2, h3 {
                color: #FFFFFF !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Đoạn mã CSS này tự động đổi màu chữ tùy theo chế độ nền
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Tự động điều chỉnh màu chữ theo nền */
            .stApp {
                color: var(--text-color);
            }
            </style>
            """
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fce4ec, #e3f2fd);
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
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
