import dash 
from dash import dcc
from dash import html
import plotly.express as px 
import pandas as pd 
import plotly.graph_objects as go 
import plotly.io as pio
from plotly.subplots import make_subplots
import numpy as np
 
app = dash.Dash(__name__) 
 
ratings_kensington = ["Outstanding", "Good", "Requires Improvement", "Unknown"] 
percentages_kensington = [35, 50, 10, 5] 
 
df_kensington = pd.DataFrame({ 
"Rating": ratings_kensington, 
"Percentage": percentages_kensington 
}) 
 
ratings_havering = ["Outstanding", "Good", "Requires Improvement", "Inadequate", "No Rating/Unknown"] 
percentages_havering = [7, 22, 3, 1, 4] 
 
df_havering = pd.DataFrame({ 
"Rating": ratings_havering, 
"Percentage": percentages_havering 
}) 
 
fig_kensington = px.pie( 
df_kensington, 
names="Rating", 
values="Percentage", 
title="Ofsted Ratings Distribution - Kensington and Chelsea Primary Schools", 
color="Rating", 
color_discrete_map={ 
"Outstanding": "#003366", 
"Good": "#0066cc", 
"Requires Improvement": "#ff6600", 
"Unknown": "#999999"  
}, 
hole=0.3 
) 
 
fig_havering = px.pie( 
df_havering, 
names="Rating", 
values="Percentage", 
title="Ofsted Ratings Distribution - Havering Primary Schools", 
color="Rating", 
color_discrete_map={ 
"Outstanding": "#003366", 
"Good": "#0066cc", 
"Requires Improvement": "#ff6600", 
"Inadequate": "#cc3333", 
"No Rating/Unknown": "#999999"  
}, 
hole=0.3 
) 
 
crime_data_kensington = { 
"Crime Type": [ 
"Anti-social behaviour", "Burglary", "Robbery", "Vehicle crime",  
"Violent crime", "Criminal damage and arson", "Shoplifting",  
"Drug offences", "Theft", "Public disorder" 
], 
"Crime Count": [42.6, 17.6, 10.2, 28.7, 31.5, 7.41, 16.7, 3.7, 83.3, 13.9] 
} 
df_crime_kensington = pd.DataFrame(crime_data_kensington) 
 
fig_crime_kensington = px.bar( 
df_crime_kensington, 
x="Crime Type", 
y="Crime Count", 
title="Crime Types Description - South Kensington", 
labels={"Crime Type": "Type of Crime", "Crime Count": "Number of Incidents"}, 
hover_data={"Crime Count": True}, 
color="Crime Type", 
height=600 
) 
 
crime_data_havering = { 
"Crime Type": [ 
"Bicycle theft", "Burglary", "Criminal damage and arson", "Drugs",  
"Possession of weapons", "Public order", "Robbery", "Shoplifting",  
"Theft from person", "Vehicle crime", "Violence and sexual offences" 
], 
"Crime Count": [121, 1339, 1700, 828, 123, 1405, 572, 2370, 510, 2742, 6873] 
} 
df_crime_havering = pd.DataFrame(crime_data_havering) 
 
fig_crime_havering = go.Figure( 
data=[go.Bar( 
x=df_crime_havering["Crime Type"], 
y=df_crime_havering["Crime Count"], 
marker=dict(color='royalblue') 
)] 
) 
 
fig_crime_kensington.update_layout( 
xaxis_title="Type of Crime", 
yaxis_title="Number of Incidents Per 1000 Population", 
showlegend=False, 
hovermode="x unified", 
template="plotly_dark", 
title_x=0.5, 
height=600 
) 
 
fig_crime_havering.update_layout( 
title="Crime Count by Type in Havering (Oct-23 to Sep-24)", 
xaxis=dict(title="Crime Type", tickangle=-45), 
yaxis=dict(title="Crime Count"), 
template="plotly_dark", 
height=500, 
width=800 
) 
 
# New code for the heatmap
# Dictionary of London boroughs and their approximate coordinates
london_boroughs = {
    'City of London': (51.5155, -0.0922),
    'Barking and Dagenham': (51.5387, 0.1309),
    'Barnet': (51.6252, -0.1517),
    'Bexley': (51.4549, 0.1505),
    'Brent': (51.5588, -0.2817),
    'Bromley': (51.4039, 0.0198),
    'Camden': (51.5290, -0.1255),
    'Croydon': (51.3762, -0.0982),
    'Ealing': (51.5130, -0.3089),
    'Enfield': (51.6538, -0.0799),
    'Greenwich': (51.4892, 0.0648),
    'Hackney': (51.5450, -0.0553),
    'Hammersmith and Fulham': (51.4927, -0.2339),
    'Haringey': (51.5906, -0.1110),
    'Harrow': (51.5898, -0.3346),
    'Havering': (51.5812, 0.1837),
    'Hillingdon': (51.5441, -0.4760),
    'Hounslow': (51.4746, -0.3680),
    'Islington': (51.5465, -0.1058),
    'Kensington and Chelsea': (51.5020, -0.1947),
    'Kingston upon Thames': (51.4085, -0.3064),
    'Lambeth': (51.4571, -0.1231),
    'Lewisham': (51.4452, -0.0209),
    'Merton': (51.4014, -0.1958),
    'Newham': (51.5255, 0.0352),
    'Redbridge': (51.5590, 0.0741),
    'Richmond upon Thames': (51.4479, -0.3260),
    'Southwark': (51.5035, -0.0804),
    'Sutton': (51.3618, -0.1945),
    'Tower Hamlets': (51.5099, -0.0059),
    'Waltham Forest': (51.5908, -0.0134),
    'Wandsworth': (51.4567, -0.1910),
    'Westminster': (51.4973, -0.1372)
}

# Read the CSV file
df = pd.read_csv('dataset.csv', encoding='utf-8')

# Add latitude and longitude to the DataFrame
df['Latitude'] = df['Local Authority District name (2019)'].map(lambda x: london_boroughs.get(x, (None, None))[0])
df['Longitude'] = df['Local Authority District name (2019)'].map(lambda x: london_boroughs.get(x, (None, None))[1])

# Remove rows with missing coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# Calculate the correlation between Education and Crime scores
df['Correlation'] = (df['Education, Skills and Training Score'] - df['Education, Skills and Training Score'].mean()) * \
                    (df['Crime Score'] - df['Crime Score'].mean())

# Normalize the Correlation for color scaling
df['Normalized Correlation'] = (df['Correlation'] - df['Correlation'].min()) / (df['Correlation'].max() - df['Correlation'].min())

# Use absolute value of Crime Score for marker size
df['Abs Crime Score'] = np.abs(df['Crime Score'])

# Create the map
fig_heatmap = px.scatter_mapbox(df, 
                        lat="Latitude", 
                        lon="Longitude", 
                        color="Normalized Correlation",
                        size="Abs Crime Score",
                        hover_name="Local Authority District name (2019)",
                        hover_data=["Education, Skills and Training Score", "Crime Score", "Correlation"],
                        color_continuous_scale="RdYlBu_r",
                        size_max=30,
                        zoom=9, 
                        height=600)

fig_heatmap.update_layout(mapbox_style="open-street-map")
fig_heatmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Read the CSV file
df = pd.read_csv('dataset.csv')

# Convert scores to numeric, replacing any non-numeric values with NaN
df['Crime Score'] = pd.to_numeric(df['Crime Score'], errors='coerce')
df['Education, Skills and Training Score'] = pd.to_numeric(df['Education, Skills and Training Score'], errors='coerce')

# Group by Local Authority District and calculate mean scores
grouped = df.groupby('Local Authority District name (2019)').agg({
    'Crime Score': 'mean',
    'Education, Skills and Training Score': 'mean'
}).reset_index()

# 1. Scatter plot of Crime Score vs Education Score for all London Boroughs
fig1 = px.scatter(grouped, x='Education, Skills and Training Score', y='Crime Score', 
                  text='Local Authority District name (2019)',
                  title='Crime Score vs Education Score in London Boroughs',
                  labels={'Education, Skills and Training Score': 'Education Score',
                          'Crime Score': 'Crime Score'},
                  trendline='ols')

fig1.update_traces(textposition='top center')
fig1.update_layout(height=600, width=800)

# 2. Dual-axis bar chart comparing Crime and Education scores for all boroughs
grouped_sorted = grouped.sort_values('Crime Score', ascending=False)

fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(
    go.Scatter(x=grouped_sorted['Local Authority District name (2019)'], 
               y=grouped_sorted['Crime Score'], 
               name="Crime Score",
               mode='lines+markers'),
    secondary_y=False,
)

fig2.add_trace(
    go.Scatter(x=grouped_sorted['Local Authority District name (2019)'], 
               y=grouped_sorted['Education, Skills and Training Score'], 
               name="Education Score",
               mode='lines+markers'),
    secondary_y=True,
)

fig2.update_layout(
    title_text="Crime and Education Scores by London Borough",
    xaxis_title="Borough",
    xaxis_tickangle=-45,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    height=800,
    width=1200,
    margin=dict(b=100)
)

fig2.update_yaxes(title_text="Crime Score", secondary_y=False, range=[-1, 1])
fig2.update_yaxes(title_text="Education Score", secondary_y=True)

for i in range(5, len(grouped_sorted), 5):
    fig2.add_vline(x=i-0.5, line_width=1, line_dash="dash", line_color="gray")

# 3. Heatmap of Crime and Education scores (normalized)
normalized_data = grouped.copy()
normalized_data['Crime Score Normalized'] = (normalized_data['Crime Score'] - normalized_data['Crime Score'].min()) / (normalized_data['Crime Score'].max() - normalized_data['Crime Score'].min())
normalized_data['Education Score Normalized'] = 1 - (normalized_data['Education, Skills and Training Score'] - normalized_data['Education, Skills and Training Score'].min()) / (normalized_data['Education, Skills and Training Score'].max() - normalized_data['Education, Skills and Training Score'].min())

heatmap_data = normalized_data[['Crime Score Normalized', 'Education Score Normalized']].T

fig3 = go.Figure(data=go.Heatmap(
                   z=heatmap_data,
                   x=normalized_data['Local Authority District name (2019)'],
                   y=['Crime Score', 'Education Score'],
                   colorscale='RdYlGn_r',
                   zmin=0, zmax=1
                  ))

fig3.update_layout(
    title='Heatmap of Normalized Crime and Education Scores in London Boroughs',
    xaxis_title='Borough',
    yaxis_title='Score Type',
    height=600,
    width=1000
)

for i, col in enumerate(['Crime Score', 'Education, Skills and Training Score']):
    for j, borough in enumerate(normalized_data['Local Authority District name (2019)']):
        value = normalized_data.loc[normalized_data['Local Authority District name (2019)'] == borough, col].values[0]
        fig3.add_annotation(
            x=borough,
            y=i,
            text=f"{value:.2f}",
            showarrow=False,
            font=dict(size=8, color='black')
        )

# 4. Focus on Havering - Comparison with London average (dual-axis)
havering = grouped[grouped['Local Authority District name (2019)'] == 'Havering'].iloc[0]
london_avg = grouped[['Crime Score', 'Education, Skills and Training Score']].mean()

fig4 = make_subplots(specs=[[{"secondary_y": True}]])

fig4.add_trace(
    go.Bar(
        x=['Havering', 'London Average'],
        y=[havering['Crime Score'], london_avg['Crime Score']],
        name='Crime Score',
        offsetgroup=0
    ),
    secondary_y=False,
)

fig4.add_trace(
    go.Bar(
        x=['Havering', 'London Average'],
        y=[havering['Education, Skills and Training Score'], london_avg['Education, Skills and Training Score']],
        name='Education Score',
        offsetgroup=1
    ),
    secondary_y=True,
)

fig4.update_layout(
    title_text='Havering vs London Average: Crime and Education Scores',
    xaxis_title='Area',
    barmode='group',
    height=500,
    width=700
)

fig4.update_yaxes(title_text="Crime Score", secondary_y=False, range=[0, 1])
fig4.update_yaxes(title_text="Education Score", secondary_y=True)

for i, area in enumerate(['Havering', 'London Average']):
    fig4.add_annotation(
        x=area,
        y=havering['Crime Score'] if i == 0 else london_avg['Crime Score'],
        text=f"{havering['Crime Score']:.2f}" if i == 0 else f"{london_avg['Crime Score']:.2f}",
        showarrow=False,
        yshift=10,
        xshift=-20
    )
    fig4.add_annotation(
        x=area,
        y=havering['Education, Skills and Training Score'] if i == 0 else london_avg['Education, Skills and Training Score'],
        text=f"{havering['Education, Skills and Training Score']:.2f}" if i == 0 else f"{london_avg['Education, Skills and Training Score']:.2f}",
        showarrow=False,
        yshift=10,
        xshift=20
    )

# 5. Comparison of Havering with Neighboring Boroughs using a Radial Plot
neighbors = ['Havering', 'Barking and Dagenham', 'Redbridge', 'Bexley']
neighbor_data = grouped[grouped['Local Authority District name (2019)'].isin(neighbors)].reset_index(drop=True)

max_crime = neighbor_data['Crime Score'].max()
min_crime = neighbor_data['Crime Score'].min()
neighbor_data['Normalized Crime Score'] = (neighbor_data['Crime Score'] - min_crime) / (max_crime - min_crime)

max_education = neighbor_data['Education, Skills and Training Score'].max()
neighbor_data['Scaled Crime Score'] = neighbor_data['Normalized Crime Score'] * max_education

fig5 = go.Figure()

fig5.add_trace(go.Scatterpolar(
    r=neighbor_data['Education, Skills and Training Score'],
    theta=neighbor_data['Local Authority District name (2019)'],
    fill='toself',
    name='Education Score',
    fillcolor='rgba(0, 0, 255, 0.3)',
    line=dict(color='blue')
))

fig5.add_trace(go.Scatterpolar(
    r=neighbor_data['Scaled Crime Score'],
    theta=neighbor_data['Local Authority District name (2019)'],
    fill='toself',
    name='Crime Score (0-1 scale, scaled)',
    fillcolor='rgba(255, 0, 0, 0.3)',
    line=dict(color='red')
))

fig5.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, max_education * 1.1],
            tickmode='array',
            tickvals=np.linspace(0, max_education, 6),
            ticktext=[f'{x:.1f} / {x/max_education:.1f}' for x in np.linspace(0, max_education, 6)],
        ),
    ),
    showlegend=True,
    title={
        'text': 'Comparison of Havering with Neighboring Boroughs',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    height=700,
    width=800,
    margin=dict(t=100, b=100, l=100, r=100)
)

for i, row in neighbor_data.iterrows():
    borough = row['Local Authority District name (2019)']
    crime_score = row['Crime Score']
    normalized_crime_score = row['Normalized Crime Score']
    education_score = row['Education, Skills and Training Score']
    angle = (i / len(neighbor_data)) * 2 * np.pi
    
    fig5.add_annotation(
        x=1.3*np.cos(angle),
        y=1.3*np.sin(angle),
        text=f"{borough}<br>Crime: {crime_score:.2f} ({normalized_crime_score:.2f})<br>Education: {education_score:.2f}",
        showarrow=False,
        font=dict(size=10),
        align='center',
        bgcolor='rgba(255, 255, 255, 0.8)'
    )

# New code for the additional plots
data = pd.read_csv('SharedDataSet.csv', usecols=['Local Authority District name (2019)', 'Income - Average rank', 'Employment - Average rank', 'Education, Skills and Training - Average rank', 'Crime - Average rank', 'Barriers to Housing and Services - Average rank', 'Living Environment - Average rank'])

income_average_rank = np.array(data['Income - Average rank'])
employment_average_rank = np.array(data['Employment - Average rank'])
living_environment_average_rank = np.array(data['Living Environment - Average rank'])
crime_average_rank = np.array(data['Crime - Average rank'])

income_coef = np.corrcoef(income_average_rank, crime_average_rank)
employment_coef = np.corrcoef(employment_average_rank, crime_average_rank)
living_environment_coef = np.corrcoef(living_environment_average_rank, crime_average_rank)

fig_income = go.Figure()
fig_income.add_trace(go.Scatter(x=income_average_rank, y=crime_average_rank, mode='markers', name='Data'))
fig_income.add_trace(go.Scatter(x=income_average_rank, y=0.7176 * income_average_rank + 6559, mode='lines', name='Best Fit'))
fig_income.update_layout(
    title='Income vs Crime',
    xaxis_title='Average Income Rank',
    yaxis_title='Average Crime Rank',
    annotations=[dict(
        x=0.05, y=0.95, 
        xref="paper", yref="paper",
        text=f'Pearson Coefficient = {round(income_coef[0][1], 3)}',
        showarrow=False
    )]
)

fig_employment = go.Figure()
fig_employment.add_trace(go.Scatter(x=employment_average_rank, y=crime_average_rank, mode='markers', name='Data'))
fig_employment.add_trace(go.Scatter(x=employment_average_rank, y=0.84 * employment_average_rank + 6813, mode='lines', name='Best Fit'))
fig_employment.update_layout(
    title='Employment vs Crime',
    xaxis_title='Average Employment Rank',
    yaxis_title='Average Crime Rank',
    annotations=[dict(
        x=0.05, y=0.95, 
        xref="paper", yref="paper",
        text=f'Pearson Coefficient = {round(employment_coef[0][1], 3)}',
        showarrow=False
    )]
)

fig_living_env = go.Figure()
fig_living_env.add_trace(go.Scatter(x=living_environment_average_rank, y=crime_average_rank, mode='markers', name='Data'))
fig_living_env.add_trace(go.Scatter(x=living_environment_average_rank, y=0.5558 * living_environment_average_rank + 7156, mode='lines', name='Best Fit'))
fig_living_env.update_layout(
    title='Living Environment vs Crime',
    xaxis_title='Average Living Environment Rank',
    yaxis_title='Average Crime Rank',
    annotations=[dict(
        x=0.05, y=0.95, 
        xref="paper", yref="paper",
        text=f'Pearson Coefficient = {round(living_environment_coef[0][1], 3)}',
        showarrow=False
    )]
)

# New code for the correlation matrix
rank_df = pd.read_csv("PandasData.csv")
corr = rank_df.select_dtypes('number').corr()

fig_corr = go.Figure(data=go.Heatmap(
                z=corr.values,
                x=corr.columns,
                y=corr.columns,
                colorscale='RdBu',
                zmin=-1, zmax=1
            ))

fig_corr.update_layout(
    title='Correlation Matrix',
    xaxis_title='Features',
    yaxis_title='Features',
    width=800,
    height=800
)

for i, row in enumerate(corr.values):
    for j, val in enumerate(row):
        fig_corr.add_annotation(
            x=corr.columns[j],
            y=corr.columns[i],
            text=f"{val:.2f}",
            showarrow=False,
            font=dict(color='black' if abs(val) < 0.5 else 'white')
        )

# Update the app layout to include all visualizations
app.layout = html.Div(style={'backgroundColor': '#003366', 'color': 'white', 'padding': '20px'}, children=[
    html.H1("London Boroughs Education, Crime, and Ofsted Ratings Dashboard", style={'textAlign': 'center', 'color': 'white'}),
    
    html.Div([
        dcc.Graph(figure=fig_heatmap),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    html.Div([
        dcc.Graph(figure=fig1),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    html.Div([
        dcc.Graph(figure=fig2),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    html.Div([
        dcc.Graph(figure=fig3),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    html.Div([
        dcc.Graph(figure=fig4),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    html.Div([
        dcc.Graph(figure=fig5),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    html.Div([
        html.Div([
            dcc.Graph(figure=fig_kensington),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(figure=fig_havering),
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    html.Br(),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_crime_kensington),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(figure=fig_crime_havering),
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'display': 'flex', 'justify-content': 'space-between'}),

    # Income vs Crime plot
    html.Div([
        dcc.Graph(figure=fig_income),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    # Employment vs Crime plot
    html.Div([
        dcc.Graph(figure=fig_employment),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    # Living Environment vs Crime plot
    html.Div([
        dcc.Graph(figure=fig_living_env),
    ], style={'width': '100%', 'marginBottom': '20px'}),

    # Correlation Matrix
    html.Div([
        dcc.Graph(figure=fig_corr),
    ], style={'width': '100%', 'marginBottom': '20px'}),
])

if __name__ == "__main__":
    app.run_server(debug=True)
