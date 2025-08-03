# To Run Streamlit
```bash
streamlit run ./01-app.py
```

# Caching
| `st.cache_data` | `st.cache_resource` |
| --- | --- |
| Used when a computation returns data, anything that can be stored in a database | Used for global resources (i.e. ML models / database connections), anything that cannot be stored in a database |
|  | does not create a copy of the return value, but stores the object itself in the cache |
|  | return values of the functions do not need to be serializable |

# Notes
Whenever users interact with streamlit, everything is refreshed, code is rerun