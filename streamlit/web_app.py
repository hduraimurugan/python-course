import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to the Demo App")
st.write("This is a simple app built with Streamlit!")

# Interactive element
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}!          ")

# Slider example
age = st.slider("Select your age", 1, 100, 25)
st.write("You selected :", age)




# import streamlit as st
#
# animal_shelter = ['cat', 'dog', 'rabbit', 'bird']
#
# animal = st.text_input('Type an animal')
#
# if st.button('Check availability'):
#     have_it = animal.lower() in animal_shelter
#     'We have that animal!' if have_it else 'We don\'t have that animal.'

