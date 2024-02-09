"""
Created on Tue Jan 30 15:32:25 2024

@author: Athul Jose P
"""

# Importing Required Modules
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_daq as daq

# Importing User-Defined Modules
import MyDashApp_Module as AppFuncs

# Instantiate our App and incorporate BOOTSTRAP theme Stylesheet
# Themes - https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
# Themes - https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
# hackerthemes.com/bootstrap-cheatsheet/

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# App Layout using Dash Bootstrap

app.layout = dbc.Container([
    

    # Row 1
    dbc.Row([
        
        dbc.Col([
            
            html.H1("EP Generation", 
                    className = 'text-center text-primary mb-4')
            
            ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
        
        ], justify = "center", align = "center"),

    
    # Row 2
    dbc.Row([
        
        # Column 1
        dbc.Col([
            
            html.Br(),

            # Box 1 C1
            # Database selection
            dcc.RadioItems(
                id = 'database_selection',
                labelStyle = {'display': 'block'},
                options = [
                    {'label' : " Our Database", 'value' : 1},
                    {'label' : " Your Files", 'value' : 2}
                    ]  ,
                value = 1,
                className = 'ps-4 p-3',
                style = {
                    'width': '100%',
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    }
                ),
            
            html.Br(),

            # Box 2 C1
            html.Div([

                # Upload IDF file
                dcc.Upload(['Upload IDF file'],
                    className = 'center',
                    style = {
                        'width': '90%',
                        'height': '40px',
                        'lineHeight': '40px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin-left': '5%',
                        'margin-top': '5%'
                        }),

                # Upload EPW file
                dcc.Upload(['Upload EPW file'],
                    className = 'center',
                    style = {
                        'width': '90%',
                        'height': '40px',
                        'lineHeight': '40px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '5%',
                        }),

                
                # Version selection
                dbc.Stack([
                    html.Label("Energy Plus Version:",
                        className = 'text'),
                    dcc.Dropdown(['8.0.0','9.0.0','22.0.0','23.0.0'], '9.0.0',
                        id='version-selection',
                        style = {
                            'width':'60%',
                            'margin-left':'8%'
                        }),
                    ],direction="horizontal",
                    style = {
                        'width': '90%',
                        'margin': '5%',
                        }),

                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    }),

            html.Br(),

            # Box 3 C1
            html.Div([

                # Time-step selection
                dbc.Stack([
                    html.Label("Time Step:",
                        className = 'text'), 
                    daq.NumericInput(id = 'time-step', 
                        value = 5,
                        style = {
                            'margin-left':'28%'
                            }),
                    ],direction = "horizontal",
                    style = {
                        'margin': '5%',
                        }),
                
                # Simulation reporting frequency selection
                dbc.Stack([
                    html.Label("Simulation Reporting Frequency:",
                        className = 'text'), 
                    dcc.Dropdown(['timestep','hourly','detailed','daily','monthly','runperiod','environment','annual'], 'timestep',
                        id = 'simReportFreq-selection',
                        style = {
                            'width':'70%',
                            'margin':'2%'
                            }),
                    ],direction = "horizontal",
                    style = {
                        #'width': '90%',
                        'margin': '5%',
                        }), 

                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    },),

            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4), # width = 12
        

        # Column 2
        dbc.Col([

            html.Br(),

            # Box 1 C2
            html.Div([
                html.H3("Schedules",
                    className = 'text-center mt-1'),
                html.H6("People",
                    className = 'ms-2'),
                html.H6("Equipment",
                    className = 'ms-2'),
                html.H6("Light",
                    className = 'ms-2'),
                html.H6("Exterior Light",
                    className = 'ms-2'),
                html.H6("Heat/Cool Setpoint",
                    className = 'ms-2'),
                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    },),
            
            html.Br(),

            # Box 2 C2
            html.Div([
                html.Button('Generate Variables',
                    id = 'Button_1', 
                    className = "btn btn-secondary btn-lg col-12",
                    style = {
                        'width':'90%',
                        'margin':'5%'
                        },),

                dcc.Dropdown(['var 1','var 2','var 3'], '',
                    id = 'variable-selection',
                    style = {
                        'width':'95%',
                        'margin-left':'2.5%',
                        'margin-bottom':'5%'
                        }),
                
                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    },),

            html.Br(),

            # Box 3 C2
            html.Div([

                dcc.Checklist([' Simulation Variables',' EIO',' IDF Object Records'],
                    id = 'download-selection',
                    style = {
                        'width':'95%',
                        'margin':'5%',
                    }),
                
                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    },),

                    ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4,),


        # Column 3
        dbc.Col([
            
            html.Br(),

            # Box 1 C3
            html.Div([

                # Building type selection
                html.Label("Building Type",
                    className = 'text-left ms-4 mt-1'),
                dcc.Dropdown(['Commercial','Manufactured','Residential'], 'Commercial',
                    id='buildingType-selection',
                    style = {
                        'width': '95%',
                        'margin-left': '2.5%',   
                        }),

                # IDF type selection
                html.Label("IDF Type",
                    className = 'text-left ms-4'),
                dcc.Dropdown(['ASHRAE','IECC'], 'IECC',
                    id = 'idfType-selection',
                    style = {
                        'width': '95%',
                        'margin-left': '2.5%',   
                        }),

                # IDF year selection
                html.Label("IDF Year",
                    className = 'text-left ms-4'),
                dcc.Dropdown(['2012','2013','2015','2016','2018','2019'], '2013',
                    id='idfYear-selection',
                    style = {
                        'width': '95%',
                        'margin-left': '2.5%',   
                        }),

                # Building selection
                html.Label("Building",
                    className = 'text-left ms-4'),
                dcc.Dropdown(['ApartmentHighRise','Hospital','HotelLarge','HotelSmall','OfficeLarge','OfficeMedium','OfficeSmall'], 'OfficeSmall',         
                    id = 'building-selection',
                    style = {
                        'width': '95%',
                        'margin-left': '2.5%',   
                        }),

                # Location selection
                html.Label("Location",
                    className = 'text-left ms-4'),
                dcc.Dropdown(['Albuquerque','Atlanta','Buffalo','Denver','ElPaso','Fairbanks','GreatFalls','Honululu','InternationalFalls','NewYork','PortAngeles','Rochester','SanDiego','Seattle','Tampa','Tucson'], 'Seattle',
                    id = 'location-selection',
                    style = {
                        'width': '95%',
                        'margin-left': '2.5%',
                        'margin-bottom': '3%',   
                        },),

                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    }),

            html.Br(),
            
            # Box 2 C3
            html.Div([

                html.Button('Generate Data',
                    id = 'Button_2', 
                    className = "btn btn-secondary btn-lg col-12",
                    style = {
                        'width':'90%',
                        'margin':'5%'
                        },),

                html.Button('Download Files',
                    id = 'Button_3', 
                    className = "btn btn-primary btn-lg col-12",
                    style = {
                        'width':'90%',
                        'margin-left':'5%',
                        'margin-bottom':'5%'
                        },),
                
                ],style = {
                    'borderWidth': '1px',
                    'borderStyle': 'solid',
                    'borderRadius': '5px',
                    },),

            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4,),
        
        ], justify = "center", align = "center"),  
    
], fluid = False)


# App Callbacks - Providing Functionality

@app.callback(    
    Output(component_id = 'output', component_property = 'value'),
    Input(component_id = 'Button_1', component_property = 'n_clicks'),
    Input(component_id = 'Button_2', component_property = 'n_clicks'),
    Input(component_id = 'Button_3', component_property = 'n_clicks'),

    State(component_id = 'database-selection', component_property = 'value'),
    State(component_id = 'version-selection', component_property = 'value'),
    State(component_id = 'time-step', component_property = 'value'),
    State(component_id = 'buildingType-selection', component_property = 'value'),

    prevent_initial_call = False)

def CreateOutput():
    
    output = 1

    return output
    
# Running the App
 
if __name__ == '__main__': 
    app.run_server(port=4050)