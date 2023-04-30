import streamlit as st
import plotly.express as px

df = px.data.tips()
st.set_page_config(
    layout="wide", ## wide to take The largest area
    page_title="Dash board", ## title of the page
    page_icon='💰' ## icon of tab of page
)


page = st.sidebar.radio("Select Page",["DataSet Overview", "Describtive Statistics","Charts"])

if page == "DataSet Overview":
    st.write("<h1 style='text-align: center; color: GoldenRod'>Tips Dashboard.</h1>", unsafe_allow_html=True)
    space1, col, space2 = st.columns([3, 4, 3])
    col.dataframe(df, width=600, height=700)

elif page == "Describtive Statistics":
    st.write("<h2 style='text-align: center; color: GoldenRod'>Descriptive Statistics.</h2>", unsafe_allow_html=True)
    col1, space, col2 = st.columns([5,1,5])
    with col1:
        ## sun = df[df["day"]=="Sun"]["total_bill"].sum()
        ## sat = df[df["day"]=="Sat"]["total_bill"].sum()
        ## st.metric("total bill of sunday",round(sun,2),round(sun-sat,2))
        st.dataframe(df.describe(include="number"), width=450, height=315)
    with col2:
        st.dataframe(df.describe(include="O"), width=350,height=178)

elif page == "Charts":
    tab1, tab2 = st.tabs(["Univariate Plot", "Bivariate Plot"])
    with tab1:
        with st.container():
            space, col1, space2 = st.columns([3,4,3])
            col_name = st.selectbox("Select column to show its distribution".title(), df.columns)
            if col_name in df.select_dtypes(include="number"):
                col1, space, col2 = st.columns([5,2,5])
                fig1 = px.histogram(df, x=col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                    title=f"{col_name} hist distribution", width=520)
                fig2 = px.box(df, x=col_name , color_discrete_sequence=px.colors.qualitative.Bold,
                              title=f"{col_name} boxplot distribution", width=520)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig2)
            else:
                col1, space, col2 = st.columns([5,2,5])
                fig1 = px.histogram(df, x=col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                    title=f"{col_name} hist distribution", width=520)
                fig2 = px.pie(df, names=col_name , color_discrete_sequence=px.colors.qualitative.Bold, hole=0.3,
                              title=f"{col_name} boxplot distribution", width=520)
                col1.plotly_chart(fig1)
                col2.plotly_chart(fig2)
    with tab2:
        col1, space, col2 = st.columns([5,2,5])
        with col1 : 
            fig1 = px.histogram(data_frame=df, x="total_bill", color="sex",color_discrete_sequence=px.colors.qualitative.Antique,
                               title="total bill hist distribution seperated to each gender", width=550).update_layout(title_x=0.2)
            st.plotly_chart(fig1)
            fig2 = px.scatter(data_frame=df, x="total_bill", y="tip",color_discrete_sequence=px.colors.qualitative.Antique,
                             title="correlation between total bill and tips", width=550).update_layout(title_x=0.2)
            st.plotly_chart(fig2)
        with col2 :
            fig1 = px.sunburst(df, path=["day", "time", "sex"], color_discrete_sequence=px.colors.qualitative.Antique, width=550,
                              title="Sunburst Chart of ['day', 'time', 'sex']")
            st.plotly_chart(fig1)
            fig2 = px.histogram(df, x="day", y="total_bill", color='time', histfunc='sum', barmode="group", width=550,
                                color_discrete_sequence = px.colors.qualitative.Antique,
                                title="hist distribution of total bill by day and time")
            st.plotly_chart(fig2)
