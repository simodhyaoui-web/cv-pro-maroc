import streamlit as st
from google import genai
import os

st.set_page_config(page_title="CV PRO MAROC")

# المفتاح الجديد
api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("API_KEY") or os.getenv("API_KEY")

if not api_key:
    st.error("المفتاح ما كاينش ف Secrets")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("CV PRO MAROC 🇲🇦")
st.subheader("المعلم رشيد - خبير ANAPEC")
st.markdown("---")

uploaded_file = st.file_uploader("حط السيفي ديالك", type=["pdf","txt","docx"])

if uploaded_file:
    text = uploaded_file.read().decode('utf-8', errors='ignore')[:8000]
    if st.button("صاوب ليا الموقع"):
        with st.spinner("كنصاوب..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=f"حلل هاد CV وصاوب موقع: {text}"
                )
                st.success("تم!")
                st.write(response.text)
            except Exception as e:
                st.error(f"خطأ: {e}")
