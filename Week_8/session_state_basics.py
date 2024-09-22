import streamlit as st

st.title("Session State Basics")

"st.session_state_object:", st.session_state

# if "a_counter" not in st.session_state:
#     st.session_state["a_counter"] =0
    
# if "boolean" not in st.session_state:
#     st.session_state["boolean"] = False
    
# st.write(st.session_state)

# #Accessing keys in session state object
# st.write("a_counter is", st.session_state["a_counter"])
# st.write("boolean is", st.session_state["boolean"])

# #To Access keys in session state object
# for the_key in st.session_state.keys():
#     st.write(the_key)

# # To access values in session state object
# for the_values in st.session_state.values():
#     st.write(the_values)
    
# # To access key-value pairs in session state object
# for items in st.session_state.items():
#     st.write(items)

# # Update session state by pressing button

# button = st.button("Update State")
# "before pressing button", st.session_state
# if button:
#     st.session_state["a_counter"] = 1
#     st.session_state.boolean = not st.session_state.boolean
#     "after pressing button", st.session_state
    
# # Ckear sessuib state by accessing key and deleting

# for key in st.session_state.keys():
#     del st.session_state[key]

# st.session_state

# Works with all widgets()
# number =st.slider("A number", 1, 10, key="slider")

# st.write(st.session_state)

# #Use value stored in state to update a widget

# col1, buff, col2 = st.columns([1,0.5,3])

# option_names =["a","b","c"]

# next = st.button("Next option")

# if next:
#     if st.session_state["radio_option"] == "a":
#         st.session_state.radio_option = "b"
#     elif st.session_state["radio_option"] == "b":
#         st.session_state.radio_option = "c"
#     else:
#         st.session_state.radio_option = "a"
               
# option = col1.radio("Pick an option", option_names, key = "radio_option")

# st.session_state

# if option == "a":
#     col2.write("You picked 'a' :smile:")
# elif option =="b":
#     col2.write("You picked 'b' :cry:")
# else:
#     col2.write("You picked 'c' :rocket:")


"""
    ## On change and on click
"""
col1, buff, col2 = st.columns([2,1,2])

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs * 0.453592

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg / 0.453592

with col1:
    pounds = st.number_input("Pounds:", key="lbs",
                             on_change= lbs_to_kg)
              
with col2:
    kilogram = st.number_input("Kilogram:", key="kg",
                               on_change = kg_to_lbs)
    