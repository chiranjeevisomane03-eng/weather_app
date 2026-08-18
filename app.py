import streamlit as st
pg=st.navigation([st.Page("home.py",title="Home"),
                  st.Page("page1.py",title="Weather Forecast")
                 


                  ])
pg.run()

#python -m streamlit run app.py