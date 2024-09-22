import streamlit as st
import pandas as pd
import numpy as np


st.title('Uber pickups in NYC')

  
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)


"""
# My first app using magic command!
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

"""
# My first app using st.write to create a table
Here's our first attempt at using data to create a table:
"""
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [88, 88, 88, 88]
}))

"""
# use Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table.
"""
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

"""
## use style to highlight 
"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

"""
## st.table method to draw static table 
"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

"""
# Draw Line  Chart st.line_chart() method and maps wih st.map()
"""


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""
# Widgets 

When you've got the data or model into the state that you want to explore, you can add in widgets like 
st.slider(), st.button() or st.selectbox(). It

Every time a user interacts with a widget, Streamlit simply reruns your script from top to bottom, 
assigning the current state of the widget to your variable in the process.
"""
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

"""
## Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget:
"""

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

""" 
# Use checkboxes to show/hide data

One use case for checkboxes is to hide or show a specific chart or section in an app. 
st.checkbox() takes a single argument, which is the widget label. 
In this sample, the checkbox is used to toggle a conditional statement.
"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
"""
# Use a selectbox for options (Dropdown box)
Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.

Let's use the df data frame we created earlier.
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

"""
#Layout
 Streamlit makes it easy to organize your widgets in a left panel sidebar with st.sidebar. 
Each element that's passed to st.sidebar is pinned to the left, 
allowing users to focus on the content in your app while still having access to UI controls.
"""

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

"""
## Oeveral other ways to control the layout of your app. 
st.columns lets you place widgets side-by-side, and 
st.expander lets you conserve space by hiding away large content.
"""
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
"""
# Show progress bar
When adding long running computations to an app, you can use st.progress() to display status in real time.

First, let's import time. We're going to use the time.sleep() method to simulate a long running computation:
"""

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(50):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

"""
# Streamlit Reference
"""

st.write("Hello, world")

st.markdown("Hello, world")
st.title("Title of Application")
st.header("This is header")
st.subheader("This is subheader")
st.caption("This is caption")
st.text("This is text")
st.code("a = 1234") # Code bloc
st.latex("x^2 = 1234") #

"""
# Connections

As hinted above, you can use @st.cache_resource to cache connections. 
This is the most general solution which allows you to use almost any connection from any Python library. However, Streamlit also offers a convenient way to handle some of the most popular connections, like SQL! st.connection takes care of the caching for you so you can enjoy fewer lines of code. 
Getting data from your database can be as easy as:
"""
conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)

"""
# Secrets management 
#For now, let's just see how st.connection works very nicely with secrets. 
In your local project directory, you can save a .streamlit/secrets.toml file. 
You save your secrets in the toml file and st.connection just uses them! 
For example, if you have an app file streamlit_app.py your project directory may look like this:
"""

"""
# Themes

Streamlit will first check if the user viewing an app has a Light or Dark mode preference set 
by their operating system and browser. 
If so, then that preference will be used. Otherwise, the Light theme is applied by default.

You can also change the active theme from "⋮" → "Settings".

Want to add your own theme to an app?   
"Settings" menu has a theme editor accessible by clicking on "Edit active theme

"""

"""
# Pages

As apps grow large, it becomes useful to organize them into multiple pages. 
This makes the app easier to manage as a developer and easier to navigate as a user. 
"""