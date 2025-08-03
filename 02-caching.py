import streamlit as st
import pandas as pd
import numpy as np
from time import sleep
from transformers import pipeline

# to cache data
@st.cache_data
def load_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url)

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

@st.cache_resource
def load_model():
    return pipeline(":sentiment-analysis")

model = load_model()

text = st.text_input("Type some text: ")

if text:
    output = model(text)[0]
    st.write(output)

# # cache data for 10 seconds, then rerun the function again
# @st.cache_data(ttl=10)
# def get_data() -> int:
#     sleep(3)
#     return 5

# st.write(get_data())


# @st.cache_data(max_entries=3)
# def get_data(some_integer: int) -> int:
#     sleep(3)
#     return some_integer * np.random.randn(1000)

# some_integer = int(st.number_input("Enter some integer: "))
# st.write(get_data(some_integer))


# only mean will be used to cache the data
# if mean changes, the function will be rerun
# _std is not used for caching, so it can change without affecting the cache
@st.cache_data()
def get_data(mean: float, _std: float) -> np.ndarray:
    sleep(3)
    return mean + _std * np.random.randn(1000)

mean = float(st.number_input("Enter mean: "), value=0)
std = float(st.number_input("Enter std: "), value=1)
st.write(get_data(mean, std))


class SomeClass:
    def __init__(self, some_integer: int) -> None:
        self.some_integer = some_integer

def hash_func(obj: SomeClass) -> int:
    return obj.some_integer

# # this will get error as custom Class is not hashable
# @st.cache_data
@st.cache_data(hash_funcs={SomeClass: hash_func}) # Custom Class: Custom hash function
def multiply_with(obj: SomeClass, multiplier: int) -> int:
    return obj.some_integer * multiplier

some_integer = int(st.number_input("Enter some integer:", value=13))

my_class = SomeClass(some_integer)
multiplier = 3

st.write(multiply_with(my_class, multiplier))