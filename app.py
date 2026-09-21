import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="CV PRO MAROC", page_icon="🇲🇦", layout="centered")

api_key = st.secrets.get("API_KEY", os.getenv("API_KEY", ""))

if api_key:
    genai.configure(api_key=api_key)

st.title("CV PRO MAROC 🇲🇦")
st.subheader("المعلم رشيد - خبير ANAPEC")
st.markdown("---")
cv_text = st.text_area("حط النص ديال السيفي هنا", height=250, placeholder="كتب السيفي ديالك هنا...")

if st.button("🔥 حلل ليا السيفي", use_container_width=True, type="primary"):
    if not cv_text.strip():
        st.error("عافاك دخل السيفي بعدا")
    elif not api_key:
        st.error("API_KEY ما كاينش")
    else:
        try:
            with st.spinner("⏳ كنحلل..."):
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"أنت خبير ANAPEC مغربي. حلل هذا السيفي: {cv_text}"
                response = model.generate_content(prompt)
                st.success("✅ كمل!")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"مشكل: {e}")

st.markdown("---")
st.caption("صنع بـ ❤️ في الجديدة")
