import streamlit as st

st.title('Great Website for mental health~')

st.write("Hi dude wanna see a trick?")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiD7-vByJphuzYF8WNB5ocmAM3LoM5ZBYYlSZMmE7TTw&s")

st.button("Feel Better?", type="primary")
if st.button('Click Here ,He He~'):
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
else :
    st.write('come on trust me this white button is the best button ever!')
    st.image('https://pbs.twimg.com/profile_images/1113688388752826368/vWVuNBEW_400x400.jpg')

st.image('https://static.amarintv.com/images/upload/editor/source/SODA/29-8/493794.jpg')
st.write('Nothing here, just test my knowledge about github repo only.')

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://pbs.twimg.com/media/EVT8UFHU4AAg37r.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.text_input("", placeholder="Streamlit CSS ")

input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)