"""
Created on Tue Jan 30 15:32:25 2024

@author: Athul Jose P
"""

# Importing Required Modules
from dash import Dash, dcc, html, Input, Output, State, ctx, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_daq as daq
import os
import base64
from datetime import date

# Importing User-Defined Modules
import MyDashApp_Module as AppFuncs

UPLOAD_DIRECTORY = os.path.join(os.getcwd(), "EP_APP_Uploads")
WORKSPACE_DIRECTORY = os.path.join(os.getcwd(), "EP_APP_Workspace")

# Instantiate our App and incorporate BOOTSTRAP theme Stylesheet
# Themes - https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
# Themes - https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
# hackerthemes.com/bootstrap-cheatsheet/

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# App Layout using Dash Bootstrap

app.layout = dbc.Container([

    dbc.Row([
        html.H1("Buildings Data Analysis", className = 'text-center text-primary mb-4')
    ]),

    dcc.Tabs([

#################################################################################################
        
# # # # # #  EP Generation Tab # # # # # # # # #

#################################################################################################
        
        # EP Generation Tab
        dcc.Tab(label='EP Generation', className = 'text-center text-primary mb-4', children=[
           
            # Row 1
            dbc.Row([
                
                # Column 1
                dbc.Col([
                    
                    html.Br(),

                    # Box 11 C1
                    html.Div([
                        dcc.Input(
                            id='folder_name',
                            type='text',
                            value='',
                            placeholder='Enter simulation name',
                            className="center-placeholder center-input",
                            style={
                                'width':'100%',
                                'margin':'0%',
                                'text-align': 'center'
                                },),

                        # html.Button('Create Folder',
                        #     id = 'Button_create_directory', 
                        #     className = "btn btn-secondary btn-lg col-12",
                        #     style = {
                        #         'width':'90%',
                        #         'margin-left':'5%',
                        #         'margin-bottom':'5%'
                        #         },),
                     
                        ],id = 'create_directory',
                        style = {
                            # 'borderWidth': '1px',
                            # 'borderStyle': 'solid',
                            # 'borderRadius': '5px',
                            },),

                    html.Br(),

                    # Box 1 C1
                    # Database selection
                    dcc.RadioItems(
                        id = 'database_selection',
                        labelStyle = {'display': 'block'},
                        value = '1',
                        options = [
                            {'label' : " Our Database", 'value' : 1},
                            {'label' : " Your Files", 'value' : 2}
                            ]  ,
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
                            id = 'upload_idf',
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
                            id = 'upload_epw',
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
                            dcc.Dropdown(['8.0.0','9.0.0','22.0.0','23.0.0'], '',
                                id='version_selection',
                                style = {
                                    'width':'60%',
                                    'margin-left':'8%'
                                }),
                            ],direction="horizontal",
                            style = {
                                'width': '90%',
                                'margin': '5%',
                                }),

                        ],id = 'upload_files',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            #'display':'none'
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
                        
                        # Simulation run period
                        html.Label("Simulation Run Period:",
                                className = 'text', style={'margin-left': '5%'}),
                        dcc.DatePickerRange(
                            id='sim-run-period',
                            min_date_allowed=date(2000, 1, 1),
                            max_date_allowed=date(2021, 12, 31),
                            #initial_visible_month=date(2020, 1, 1),
                            start_date=date(2020, 1, 1),
                            end_date=date(2020, 12, 31),
                            display_format='M/D',
                            style = {
                                'width': '100%',
                                'margin': '5%',
                                'display': 'block'
                                },
                        ),
                        # html.Div(id='sim-run-period2'),


                        # Simulation reporting frequency selection
                        dbc.Stack([
                            html.Label("Simulation Reporting Frequency:",
                                className = 'text'), 
                            dcc.Dropdown(['timestep','hourly','detailed','daily','monthly','runperiod','environment','annual'], '',
                                id = 'simReportFreq_selection',
                                style = {
                                    'width':'70%',
                                    'margin':'2%'
                                    }),
                            ],direction = "horizontal",
                            style = {
                                #'width': '90%',
                                'margin': '5%',
                                }), 

                        ],id = 'simulation_details',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),
                    
                    html.Br(),

                    ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4), # width = 12
                

                # Column 2
                dbc.Col([

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
                        ],id = 'schedules',
                        hidden = True,
                        style = {
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
                            id = 'variable_selection',
                            style = {
                                'width':'95%',
                                'margin-left':'2.5%',
                                'margin-bottom':'5%'
                                }),
                        
                        ],id = 'generate_variables',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                    html.Br(),

                    # Box 3 C2
                    html.Div([

                        dcc.Checklist([' Simulation Variables',' EIO',' IDF Object Records'],'',
                            id = 'download_selection',
                            style = {
                                'width':'95%',
                                'margin':'5%',
                            }),
                        
                        ],id = 'download_variables',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                    html.Br(),

                            ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4,),


                # Column 3
                dbc.Col([
                    
                    html.Br(),

                    # Box 1 C3
                    html.Div([

                        # Building type selection
                        html.Label("Building Type",
                            className = 'text-left ms-4 mt-1'),
                        dcc.Dropdown(['Commercial_Prototypes','Manufactured_Prototypes','Residential_Prototypes'], '',
                            id='buildingType_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # Sub Level 1
                        html.Label("Sub Level 1",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(options = [],
                            value = '',
                            id = 'level_1',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # Sub Level 2
                        html.Label("Sub Level 2",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(options = [],
                            value = '',
                            id='level_2',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # Sub Level 3
                        html.Label("Sub Level 3",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(options = [],
                            value = '',         
                            id = 'level_3',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        # Location selection
                        html.Label("Location",
                            className = 'text-left ms-4'),
                        dcc.Dropdown(['Albuquerque','Atlanta','Buffalo','Denver','ElPaso','Fairbanks','GreatFalls','Honululu','InternationalFalls','NewYork','PortAngeles','Rochester','SanDiego','Seattle','Tampa','Tucson'], '',
                            id = 'location_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',
                                'margin-bottom': '3%',   
                                },),

                        ],id = 'building_details',
                        hidden = True,
                        style = {
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
                        
                        ],id = 'final_download',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },),

                    ], xs = 12, sm = 12, md = 4, lg = 4, xl = 4,),
                
                

                html.Button('End Session',
                    id = 'Button_es_generation', 
                    className = "btn btn-primary btn-lg col-12",
                    style = {
                        'width':'98%',
                        },),

                ], justify = "center", align = "center"),  
            
        ]),
        
#################################################################################################
        
# # # # # #  Aggregation Tab # # # # # # # # #

#################################################################################################
        
        
        dcc.Tab(label = 'Aggregation', className = 'text-center text-primary mb-4', children = [

            dbc.Row([
                
                # First Column
                dbc.Col([
                    
                    # Input selection
                    dcc.RadioItems(
                    id = 'input_selection',
                    labelStyle = {'display': 'block'},
                    options = [
                        {'label' : " Continue Session", 'value' : 1},
                        {'label' : " Upload Files", 'value' : 2}
                        ]  ,
                    value = '',
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

                        # Upload Pickled Variable file
                        dcc.Upload(['Upload Pickled Variable file'],
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

                        # Upload EIO file
                        dcc.Upload(['Upload EIO file'],
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


                        ],id = 'upload_aggr_files',
                        hidden = True,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            #'display':'none'
                            }),

                    html.Br(),

                    # Aggregation Variables
                    html.Div([
                        dcc.RadioItems(
                            id = 'aggr_variable_selection',
                            labelStyle = {'display': 'block'},
                            options = [
                                {'label' : " Preselected Variables", 'value' : 1},
                                {'label' : " Custom Variables", 'value' : 2}
                                ]  ,
                            value = '',
                            className = 'ps-4 p-3',
                        ),

                        dcc.Dropdown(['Var1','Var2','Var3'], '',
                            id='aggr_variables',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',
                                'margin-bottom': '2.5%'
                                }),

                    ],id = 'aggr_variable_details',
                    hidden = True,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        },)

                ], xs = 12, sm = 12, md = 6, lg = 6, xl = 6,),

                # Second Column
                dbc.Col([
                    
                    # Box 1 C2
                    html.Div([

                        # Zone selection
                        html.Label("Zone Lists",
                            className = 'text-left ms-4 mt-1'),
                        dcc.Dropdown(['Zone list 1','Zone list 2','Zone list 3'], '',
                            id='zone_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',   
                                }),

                        dcc.RadioItems(
                            id = 'aggregate_to',
                            labelStyle = {'display': 'block'},
                            options = [
                                {'label' : " Aggregate to one", 'value' : 1},
                                {'label' : " Custom Aggregation", 'value' : 2}
                                ]  ,
                            value = '',
                            className = 'ps-4 p-3',
                        ),

                        dcc.Dropdown(['Set 1','Set 2','Set 3'], '',
                            id='custom_aggr_variables',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%',
                                #'margin-bottom': '2.5%'
                                }),

                        # Zone selection
                        html.Label("Type of Aggregation",
                            className = 'text-left ms-4 mt-1'),
                        dcc.Dropdown(['Average','Weighted Floor Area Average','Weighted Volume Average'], '',
                            id='type_selection',
                            style = {
                                'width': '95%',
                                'margin-left': '2.5%', 
                                'margin-bottom': '2.5%'  
                                }),

                    ],id = 'aggr_details',
                    hidden = True,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        },),


                    html.Br(),

                    # Box 2 C2
                    html.Div([


                        html.Button('Aggregate',
                            id = 'Button_4', 
                            className = "btn btn-secondary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin':'5%'
                                },),

                        html.Button('Download',
                            id = 'Button_5', 
                            className = "btn btn-primary btn-lg col-12",
                            style = {
                                'width':'90%',
                                'margin-left':'5%',
                                'margin-bottom':'5%'
                                },),

                    ],id = 'aggr_download',
                    hidden = True,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        },)

                ], xs = 12, sm = 12, md = 6, lg = 6, xl = 6,),

                html.Button('End Session',
                    id = 'Button_es_aggregation', 
                    className = "btn btn-primary btn-lg col-12",
                    style = {
                        'width':'98%',
                        'margin-left':'1%'
                        },),

                ])
            ]), 

#################################################################################################
        
# # # # # #  Visualization & Analysis Tab # # # # # # # # #

#################################################################################################
        
        
        dcc.Tab(label = 'Visualization & Analysis', className = 'text-center text-primary mb-4', children = [

                    
            
            # Row 3
            dbc.Row([
                
                dbc.Col([
                    
                    dcc.RadioItems(
                            id = 'RadioItem1',
                            labelStyle = {'display': 'block'},
                            options = [
                                {'label' : " Continue Session", 'value' : 1},
                                {'label' : " Upload Files", 'value' : 2},
                                {'label' : " Buildings Database", 'value' : 3}
                                ]  ,
                            value = '',
                            className = 'ps-4 p-3',
                            style = {
                                'width': '100%',
                                'borderWidth': '1px',
                                'borderStyle': 'solid',
                                'borderRadius': '5px',
                                }
                        ),
                    
                    ], xs = 12, sm = 12, md = 6, lg = 6, xl = 6), # width = 12

                dbc.Col([
                    
                    dcc.RadioItems(
                            id = 'RadioItem2',
                            labelStyle = {'display': 'block'},
                            options = [
                                {'label' : " Raw Data", 'value' : 1},
                                {'label' : " Aggregated Data", 'value' : 2},
                                {'label' : " Both", 'value' : 3}
                                ]  ,
                            value = '',
                            className = 'ps-4 p-3',
                            style = {
                                'width': '100%',
                                'borderWidth': '1px',
                                'borderStyle': 'solid',
                                'borderRadius': '5px',
                                }
                        ),
                    
                    ], xs = 12, sm = 12, md = 6, lg = 6, xl = 6), # width = 12
                
                ], justify = "center", align = "center"),
            
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
          
            
            # Row 5, upload files
                html.Div([

                    # Upload Raw data
                    dcc.Upload(
                        id='upload-data1',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select Files for Raw Data')
                        ]),
                        style={
                            'width': '98.5%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                        # Allow multiple files to be uploaded
                        multiple=True
                    ),
                    html.Div(id='output-data-upload1'),
                    
                    # Break Row
                    dbc.Row([
                        
                        dbc.Col([
                            
                            html.Br()
                            
                            ], width = 12),
                        
                        ]),  
                    
                    # Upload Aggregated data
                    dcc.Upload(
                        id='upload-data2',
                        children=html.Div([
                            'Drag and Drop or ',
                            html.A('Select Files for Aggregated Data')
                        ]),
                        style={
                            'width': '98.5%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                        # Allow multiple files to be uploaded
                        multiple=True
                    ),
                    html.Div(id='output-data-upload2'),
            
                    ],id = 'upload_vis_files',
                    hidden = False,
                    style = {
                        'borderWidth': '1px',
                        'borderStyle': 'solid',
                        'borderRadius': '5px',
                        #'display':'none'
                        }),

            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),
            
            # Row 7
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Date Range from Uploaded File:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 8
            dcc.DatePickerRange(
                id='my-date-picker-range1',
                min_date_allowed=date(2000, 1, 1),
                max_date_allowed=date(2021, 12, 31),
                initial_visible_month=date(2020, 1, 1),
                end_date=date(2020, 12, 31)
            ),
            html.Div(id='output-container-date-picker-range1'),
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]), 
            
            # Row 9
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Select Date Range for Visualization:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 10
            dcc.DatePickerRange(
                id='my-date-picker-range2',
                min_date_allowed=date(2000, 1, 1),
                max_date_allowed=date(2021, 12, 31),
                initial_visible_month=date(2020, 1, 1),
                end_date=date(2020, 12, 31)
            ),
            html.Div(id='output-container-date-picker-range2'),
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),
            

            dbc.Row([
                        
                        dbc.Col([
                            
                            html.H4('Mean:')
                            
                            ], width = 3),
                         

                        dbc.Col([
                            
                            html.H4('Variance:')
                            
                            ], width = 3),
                         

                        dbc.Col([
                            
                            html.H4('Standard Deviation:')
                            
                            ], width = 3),
                         

                        dbc.Col([
                            
                            html.H4('Range:')
                            
                            ], width = 3),
                        
                        ],id = 'vis_details',
                        #hidden = False,
                        style = {
                            'borderWidth': '1px',
                            'borderStyle': 'solid',
                            'borderRadius': '5px',
                            },), 
            
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),
            
            # Row 11
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Distribution Plot:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 12
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Select Variable:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
        
            # Row 13
            dcc.Dropdown(
                ['Heating', 'Cooling', 'Humidification'],
                ['Heating', 'Cooling'],
                multi=True
                ),
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 14
            dbc.Row([
                
                dbc.Col([
                    
                    html.Button('Plot', id = 'Button_6', 
                                className = "btn btn-primary btn-lg col-12") ,
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
                
                ], justify = "center", align = "center"),   

            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]), 
            
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),       
            
            # Row 15
            dbc.Row([
                
                dbc.Col([
                    
                    dcc.Graph(id = 'Graph1', figure ={}),
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
                
                ], justify = "center", align = "center"),
                
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]), 
            
            # Row 11
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Raw Data Plot:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 12
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Select Variable:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
        
            # Row 13
            dcc.Dropdown(
                ['Heating', 'Cooling', 'Humidification'],
                ['Heating', 'Cooling'],
                multi=True
                ),
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 14
            dbc.Row([
                
                dbc.Col([
                    
                    html.Button('Plot', id = 'Button_7', 
                                className = "btn btn-primary btn-lg col-12") ,
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
                
                ], justify = "center", align = "center"),   

            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),       
            
            # Row 15
            dbc.Row([
                
                dbc.Col([
                    
                    dcc.Graph(id = 'Graph2', figure ={}),
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
                
                ], justify = "center", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 16
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Aggregated Data Plot:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 12
            dbc.Row([
                
                dbc.Col([
                    
                    html.H3("Select Variable:",
                            className = 'text-left text-secondary mb-4')
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12      
                
                ], justify = "left", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
        
            # Row 13
            dcc.Dropdown(
                ['Heating', 'Cooling', 'Humidification'],
                ['Heating', 'Cooling'],
                multi=True
                ),
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),  
            
            # Row 14
            dbc.Row([
                
                dbc.Col([
                    
                    html.Button('Plot', id = 'Button_8', 
                                className = "btn btn-primary btn-lg col-12") ,
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
                
                ], justify = "center", align = "center"),   

            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br()
                    
                    ], width = 12),
                
                ]),       
            
            # Row 15
            dbc.Row([
                
                dbc.Col([
                    
                    dcc.Graph(id = 'Graph3', figure ={}),
                    
                    ], xs = 12, sm = 12, md = 12, lg = 12, xl = 12), # width = 12
                
                ], justify = "center", align = "center"), 
            
            # Break Row
            dbc.Row([
                
                dbc.Col([
                    
                    html.Br(),
                    html.Button('End Session',
                    id = 'Button_es_visualization', 
                    className = "btn btn-primary btn-lg col-12",
                    ),
                    
                    ], width = 12),
                
                ]), 

            
            ]) 
        
    ])

], fluid = False)

# App Callbacks - Providing Functionality

@app.callback(
    Output(component_id = 'building_details', component_property = 'hidden'),
    Output(component_id = 'upload_files', component_property = 'hidden'),
    Output(component_id = 'simulation_details', component_property = 'hidden', allow_duplicate = True),
    Output(component_id = 'schedules', component_property = 'hidden', allow_duplicate = True),
    Output(component_id = 'generate_variables', component_property = 'hidden', allow_duplicate = True),
    Output(component_id = 'download_variables', component_property = 'hidden', allow_duplicate = True),
    Output(component_id = 'final_download', component_property = 'hidden', allow_duplicate = True),
    Input(component_id = 'database_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Radiobutton_DatabaseSelection_Interaction(database_selection):
    
    if database_selection == 1:
        building_details = False
        upload_files = True
        simulation_details = True
        schedules = True
        generate_variables = True
        download_variables = True
        final_download = True

    elif database_selection == 2:
        building_details = True
        upload_files = False
        simulation_details = True
        schedules = True
        generate_variables = True
        download_variables = True
        final_download = True

    else:
        building_details = True
        upload_files = True
        simulation_details = True
        schedules = True
        generate_variables = True
        download_variables = True
        final_download = True

    return building_details, upload_files, simulation_details , schedules, generate_variables, download_variables, final_download

@app.callback(
    Output(component_id = 'upload_idf', component_property = 'children'),
    Input(component_id = 'upload_idf', component_property = 'filename'),
    State(component_id = 'upload_idf', component_property = 'contents'),
    prevent_initial_call = False)
def EPGen_Upload_IDF_Interaction(filename, content):
    if filename is not None and content is not None:
        AppFuncs.save_file(filename, content, UPLOAD_DIRECTORY)
        message = 'File Uploaded'
    
    else:
        message = 'Upload IDF file'

    return message

@app.callback(
    Output(component_id = 'upload_epw', component_property = 'children'),
    Input(component_id = 'upload_epw', component_property = 'filename'),
    State(component_id = 'upload_epw', component_property = 'contents'),
    prevent_initial_call = False)
def EPGen_Upload_EPW_Interaction(filename, content):
    if filename is not None and content is not None:
        AppFuncs.save_file(filename, content, UPLOAD_DIRECTORY)
        message = 'File Uploaded'
    
    else:
        message = 'Upload EPW file'

    return message

@app.callback(
    Output(component_id = 'simulation_details', component_property = 'hidden', allow_duplicate = True),
    Input(component_id = 'version_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_EPVersion_Interaction(version_selection):
    if version_selection != '' :
        simulation_details = False
    else:
        simulation_details = True
    return simulation_details

@app.callback(
    Output(component_id = 'simulation_details', component_property = 'hidden', allow_duplicate = True),
    Input(component_id = 'location_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_Location_Interaction(location_selection):
    if location_selection != '' :
        simulation_details = False
    else:
        simulation_details = True
    return simulation_details

@app.callback(
    Output(component_id = 'schedules', component_property = 'hidden', allow_duplicate = True),
    Output(component_id = 'generate_variables', component_property = 'hidden', allow_duplicate = True),
    Input(component_id = 'simReportFreq_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_SimReportFreq_Interaction(simReportFreq_selection):
    if simReportFreq_selection != '':
        schedules = False
        generate_variables = False
    else:
        schedules = True
        generate_variables = True
    return schedules, generate_variables

@app.callback(
    Output(component_id = 'download_variables', component_property = 'hidden', allow_duplicate = True),
    Input(component_id = 'variable_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_GeneratedVariables_Interaction(version_selection):
    if version_selection != '' :
        download_variables = False
    else:
        download_variables = True
    return download_variables

@app.callback(
    Output(component_id = 'final_download', component_property = 'hidden', allow_duplicate = True),
    Input(component_id = 'download_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_DownloadSelection_Interaction(download_selection):
    if download_selection != '' :
        final_download = False
    else:
        final_download = True
    return final_download


# Level 1 list
@app.callback(
    Output(component_id = 'level_1', component_property = 'options'),
    Output(component_id = 'level_2', component_property = 'options', allow_duplicate = True),
    Output(component_id = 'level_3', component_property = 'options', allow_duplicate = True),
    Output(component_id = 'level_1', component_property = 'value'),
    Output(component_id = 'level_2', component_property = 'value', allow_duplicate = True),
    Output(component_id = 'level_3', component_property = 'value', allow_duplicate = True),
    Input(component_id = 'buildingType_selection', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_BuildingType_Interaction(buildingType_selection):
    # Listing next sub level of folders
    if buildingType_selection is not None:
        FilePath = os.path.join(os.getcwd(), "../../Data/", buildingType_selection)
        level_1_list = AppFuncs.list_contents(FilePath)
        level_2_list = []
        level_3_list = []

    else:
        level_1_list = []
        level_2_list = []
        level_3_list = []

    level_1_value = ''
    level_2_value = ''
    level_3_value = ''

    return level_1_list, level_2_list, level_3_list, level_1_value, level_2_value, level_3_value


# Level 2 list
@app.callback(
    Output(component_id = 'level_2', component_property = 'options', allow_duplicate = True),
    Output(component_id = 'level_3', component_property = 'options', allow_duplicate = True),
    Output(component_id = 'level_2', component_property = 'value', allow_duplicate = True),
    Output(component_id = 'level_3', component_property = 'value', allow_duplicate = True),
    State(component_id = 'buildingType_selection', component_property = 'value'),
    Input(component_id = 'level_1', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_SubLevel1_Interaction(buildingType_selection, level_1):
    # Listing next sub level of folders
    if level_1 is not None:
        FilePath = os.path.join(os.getcwd(), "../../Data/", buildingType_selection, level_1)
        level_2_list = AppFuncs.list_contents(FilePath)
        level_3_list = []

    else:
        level_2_list = []
        level_3_list = []

    level_2_value = ''
    level_3_value = ''

    return level_2_list, level_3_list, level_2_value, level_3_value


# Level 3 list
@app.callback(
    Output(component_id = 'level_3', component_property = 'options', allow_duplicate = True),
    Output(component_id = 'level_3', component_property = 'value', allow_duplicate = True),
    State(component_id = 'buildingType_selection', component_property = 'value'),
    State(component_id = 'level_1', component_property = 'value'),
    Input(component_id = 'level_2', component_property = 'value'),
    prevent_initial_call = True)
def EPGen_Dropdown_SubLevel2_Interaction(buildingType_selection, level_1, level_2):     
    # Listing next sub level of folders
    if level_2 is not None:
        FilePath = os.path.join(os.getcwd(), "../../Data/", buildingType_selection, level_1, level_2)
        level_3_list = AppFuncs.list_contents(FilePath)
    
    else:
        level_3_list = []

    level_3_value = ''

    return level_3_list, level_3_value



# Running the App
if __name__ == '__main__': 
    app.run_server(port=4050)