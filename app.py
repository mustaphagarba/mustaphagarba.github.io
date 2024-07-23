import streamlit as st
from PIL import Image

with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''
# Mustapha Garba
##### *Resume*
         ''')

image = Image.open("dp.jpg")
st.image(image, width=150)

st.markdown("## Summary", unsafe_allow_html=True)
st.info('''
- Multifaceted data professional with a focus         
''')