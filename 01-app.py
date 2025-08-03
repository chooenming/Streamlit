import streamlit as st
import pandas as pd
import numpy as np
import time

"""
### Block Comments

You can use block comments to put text on apps using markdown

* Bullet point 1
* Bullet point 2
* Bullet point 3

1. Enumerate 1
2. Enumerate 2
3. Enumerate 3
"""

df = pd.DataFrame({
    "first": [1, 2, 3, 4],
    "second": [10, 20, 30, 40]
})

# Display in the app
df

st.write("A magical method to write many different types on screen")
st.write(df) # Display in the app again
st.table(df) # Display the df as table -> cant be sorted

st.write("### You can use streamlit to draw charts and maps:")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

mpat_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [36.76, -122.4],
    columns=["lat", "lon"]
)
st.map(mpat_data)

st.write("### Streamlit Widgets: ")
st.write("#### Slider")
slider = st.slider(
    label="Number x",
    min_value=1,
    max_value=100,
    value=3,
    step=1
)
st.write(slider, "squared is", slider ** 2)

st.write("#### Button")
button = st.button(label="A button")
if button:
    st.write("Button was clicked!")


st.write("#### Selectbox")
selectbox = st.selectbox(
    label = "A selectox",
    options = ["Option 1", "Option 2", "Option 3"]
)
if selectbox == "Option 1":
    st.write("Option 1 was selected")
elif selectbox == "Option 2":
    st.write("Option 2 was selected")
elif selectbox == "Option 3":
    st.write("Option 3 was selected")

# st.write("You can also assign keys to widgets to select them:")

# st.text_input("Please enter your name:", key="name")
# st.session_state.name

st.write("#### Using checkboxes to show/hide data:")
if st.checkbox("Show chart data"):
    st.line_chart(chart_data)

st.write("#### Layout the application:")
st.write("You can use `st.sidebar.<st component>` to add streamlit components to the sidebar.")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be connected?",
    ("Email", "Phone", "Social Media")
)

add_slider = st.sidebar.slider(
    label = "Select a range of values",
    min_value = 0.0, max_value = 100.0, value=(25.0, 75.0)
)

st.write("You can also use `st.columns` to layout the app")

# 2 indicates number of columns
left_column, right_column = st.columns(2)
left_column.button("Press me!")

with right_column:
    chosen = st.radio(
        label = "Sorting hat",
        options = ("Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")

st.write("#### Showing progress in the app:")

"Starting a long computation..."

latest_iteration = st.empty() # this as a placeholder
# progress bar from 0 to 100
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"... long computation finished!"