import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Màu nền xám xanh */
            .stApp {
                background-color: #2C3E50 !important;
            }
            
            /* Chữ trắng, to, rõ */
            .stApp, .stMarkdown, .stText, p, div, h1, h2, h3 {
                color: #ECF0F1 !important; 
                font-size: 20px !important;
            }

            /* ĐIỀU CHỈNH NÚT BẤM */
            div.stButton > button {
                background-color: #E74C3C !important; /* Màu đỏ cam nổi bật */
                color: white !important;              /* Chữ màu trắng */
                font-weight: bold !important;         /* Chữ đậm */
                border: none !important;              /* Bỏ viền */
                border-radius: 10px !important;       /* Bo tròn góc */
                padding: 10px 20px !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("🎂 Chúc em ngày Quốc tế thiếu nhi thật nhiều niềm vui. Dù lớn rồi nhưng vẫn luôn là một cô bé hạnh phúc nhé!")

if st.button('Nhấn vào đây, có bất ngờ dành cho em á'):
    st.balloons() # Hiệu ứng bóng bay
    st.success("Cảm ơn vì đã luôn là một người bạn tuyệt vời! Chúc em mọi điều tốt đẹp nhất!")    
    st.image("anh.jpg", caption="chắc e sẽ nhận ra người trong ảnh mà đk (phong cảnh chỉ là minh họa)")
    st.image("ngoc_han_phongcanh.png",  caption="Nhìn quen lắm đk")
    st.image("ki_niem_ff.png",  caption="Kĩ niệm năm ngoái")
    st.image("tn_dautien.png",  caption="tn đầu tiên")
    st.image("loi_hua.png",  caption="Lời hứa hqua")
    st.video("https://www.youtube.com/watch?v=PWy4sxLpl58")
