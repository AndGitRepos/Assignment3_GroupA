import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.express as px 
import pandas as pd 
import plotly.graph_objects as go 
 
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
 
app.layout = html.Div(style={'backgroundColor': '#003366', 'color': 'white', 'padding': '20px'}, children=[ 
html.H1("Ofsted Ratings & Crime Data Dashboards", style={'textAlign': 'center', 'color': 'white'}), 
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
]) 
 
if __name__ == "__main__": 
app.run_server(debug=True) 
