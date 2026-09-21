import streamlit as st
import google.generativeai as genai
import os

api_key = st.secrets.get("API_KEY", os.environ.get("API_KEY", ""))

if api_key:
    genai.configure(api_key=api_key)

st.set_page_config(page_title="CV PRO MAROC", page_icon="🇲🇦")
st.title("CV PRO MAROC 🇲🇦")
st.subheader("المعلم رشيد - خبير ANAPEC")
cv_text = st.text_area("لصق النص ديال السيفي هنا:", height=250)
if st.button("🔥 حلل ليا السيفي"):
    if not cv_text:
        st.error("حط السيفي عافاك")
    else:
        with st.spinner("المعلم رشيد كيحلل..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"انت المعلم رشيد خبير ANAPEC 20 سنة، حلل هذا CV بنقطة صادمة /10 و 3 اخطاء قاتلة واعطي نسخة محسنة ATS فرنسية احترافية ونصيحة ذهبية. جاوب بالدارجة ممزوجة بالفرنسية: {cv_text}"
            response = model.generate_content(prompt)
            st.success("كمل!")
            st.markdown(response.text)
