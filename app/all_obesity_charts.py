import streamlit as st
import pandas as pd
import plotly.express as px

def chart_ob_pre():
    data = pd.read_csv("/mount/src/ilab_group_6_uts/chart_data/share-of-adults-defined-as-obese.csv")

    fig = px.choropleth(data,
                        locations="Code",
                        color="Percent",
                        hover_name="Entity",
                        title='Prevalence of Obesity in adults.<br><sup>Estimated prevalence of obesity, based on general population surveys and statistical modeling.</sup>',
                        animation_frame="Year",
                        range_color=[0, 40],
                        color_continuous_scale=px.colors.sequential.Sunsetdark,
                        projection="natural earth")

    fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular', bgcolor='rgba(0,0,0,0)'),
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0)',
                    coloraxis_colorbar=dict(tickvals=list(range(0, 45, 10))),
                    updatemenus=[dict(type='buttons', showactive=False,
                                        buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=75, redraw=True), fromcurrent=True)]),
                                                dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=True), mode='immediate')])])])

    return fig
#ds
def chart_ob_dea():
    data = pd.read_csv("/mount/src/ilab_group_6_uts/chart_data/death-rate-vs-share-obesity.csv").dropna()

    fig = px.scatter(data,
                    x='Percentage',
                    y='Deaths', color='Continent',
                    hover_data=['Country', 'Country_code', 'Year'],
                    title='Death rate from obesity vs. share of adults who are obese<br><sup>Premature deaths attributed to obesity per 100,000 individuals.</sup>',
                    animation_frame='Year')
    fig.update_layout(xaxis_title='Adult obesity',
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0)',
                    yaxis_title='Death rate from obesity',
                    updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=75, redraw=False), fromcurrent=True)]),
                                                dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])]
                                                )

    return fig

def chart_ob_age():
    data = pd.read_csv('/mount/src/ilab_group_6_uts/chart_data/deaths-from-obesity-by-age.csv')

    selected_country = st.selectbox('Select Country', ['World'] + data['Country'].unique().tolist())

    if selected_country == 'World':
        world_data = data.groupby('Year').sum().reset_index()
        fig = px.area(world_data,
                        x='Year',
                        y=['Age_70+', 'Age_50-69', 'Age_15-49', 'Age_5-14', 'Age_5-'],
                        title='Deaths from Obesity by Age in World from 1990 to 2019<br><sup>Total premature deaths due to obesity (high body-mass index) differentiated by age.</sup>',
                        labels={'value': 'Population', 'Year': 'Year', 'variable': 'Age Group'}
                        )
        fig.update_layout(
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)')
    else:
        filtered_data = data[data['Country'] == selected_country]
        fig = px.area(filtered_data,
                    x='Year',
                    y=['Age_70+', 'Age_50-69', 'Age_15-49', 'Age_5-14', 'Age_5-'],
                    title='Deaths from Obesity by Age in World from 1990 to 2019<br><sup>Total premature deaths due to obesity (high body-mass index) differentiated by age.</sup>',
                    labels={'value': 'Population', 'Year': 'Year', 'variable': 'Age Group'}
                    )
        fig.update_layout(
                                plot_bgcolor='rgba(0, 0, 0, 0)',
                                paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig

def chart_all():
    #with st.container(border=True):

        tab1, tab2, tab3 = st.tabs(['Prevalence of Obesity', 'Death Rate from Obesity', 'Deaths from Obesity by Age'])

        with tab1:
            st.plotly_chart(chart_ob_pre())

        with tab2:
            st.plotly_chart(chart_ob_dea())

        with tab3:
            st.plotly_chart(chart_ob_age())