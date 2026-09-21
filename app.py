import streamlit as st
from google import genai

st.title("CV Pro Maroc 🇲🇦")

key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=key)

nom = st.text_input("الاسم")
job = st.text_input("المجال")
exp = st.text_area("خبرتك بالدارجة")

if st.button("صاوب ليا CV"):
    r = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"صاوب CV مغربي احترافي ل {nom} مجال {job} خبرة {exp}"
    )
    st.success("CV واجد!")
    st.write(r.text)
