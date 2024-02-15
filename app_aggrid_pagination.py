import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

st.set_page_config(layout="wide")

@st.cache_data()
def data_upload():
    df = pd.read_csv('./Superstore.csv')
    return df

df = data_upload()

# st.header("This is Streamlit Dataframe")
# st.dataframe(data=df)
# st.info(len(df))

_funct = st.sidebar.radio(label="Functions", options=['Display','Highlight'])

st.header("This is AgGrid Table with Pagination")

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_side_bar()    # SIDEBAR
gd.configure_default_column(editable=False,groupable=True)

if _funct=='Display':
    sel_mode=st.radio('Selection Type',options=['single','multiple'])
    gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
    gridoptions=gd.build()

    grid_table=AgGrid(df, gridOptions=gridoptions,
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            allow_unsafe_jscode=True,
            height=400,
            custom_css={
                    "#gridToolBar": {
                        "padding-bottom": "0px !important",
                    }
                },
            theme='balham', # streamlit | alpine | balham | material
    )
    st.info("Total Rows :" + str(len(grid_table['data'])))   
    
    sel_row = grid_table["selected_rows"]
    st.subheader("Output")
    st.write(sel_row)

