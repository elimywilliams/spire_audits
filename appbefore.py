# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#from dash.dependencies import Input, Output
import plotly.express as px
#import base64
import json
#from textwrap import dedent as d
import bs4 as bs
import dash_html_components as html
import requests 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/header2.css'  ,
                        'https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css'
                        ]
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')

allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allLeaks.csv')
allPoly = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allPoly.csv')
allGaps = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allGaps.csv')
allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allLeaksWin.csv')



import plotly.express as px
import plotly.io as pio

projOPTS = [
            {'label': 'ACLARA (NY)', 'value': 'Aclara'},
            {'label': 'Con Edison', 'value': 'ConEd'},
            #{'label': 'CPS (TX)', 'value': 'CPS_TX'},

            {'label': 'Dom Questar (UT)', 'value': 'DomQuest'},
            
            #{'label': 'Dominion (NC)', 'value': 'DominionNC'},
            #{'label': 'Dominion (SC)', 'value': 'DominionSC'},
            
            {'label': 'Duke IPI', 'value': 'DukeIPI'},
            {'label': 'Duke Ohio', 'value': 'DukeOH'},
            {'label': 'Norwhich Public Utilities', 'value': 'norwhich'},

            {'label': 'Peoples (IL)', 'value': 'PeoplesIL'},
            #{'label': 'Trussville (AL)', 'value': 'Trussville'},

            {'label': 'WEC Energy (WI)', 'value': 'WEC_WI'},
            {'label': 'WPS MMD (WI)', 'value': 'WPS_WI'}
        ]

whichAvgOPTS = [
        {'label': '7 Day Avg ', 'value': 'sevenday'},
        {'label': '3 Day Avg', 'value': 'threeday'},
        {'label': 'Daily ', 'value': 'daily'},
        {'label': 'Cumulative ','value':'total'}
    ]

popOPTS = [
    {'label':'Relative to Population','value':'relpop'},
    {'label':'Raw Cases', 'value':'nonrelpop'}
    
    
    ]

whichMapOPTS = [
    {'label':'Satellite Map','value':'sat'},
    {'label':'Street Map', 'value':'street'}
       
    ]

countryOPTS = [
            {'label': 'United States of America', 'value': 'US'},
            {'label': 'Italy', 'value': 'Italy'},

            {'label': 'Spain', 'value': 'Spain'},
            {'label': 'United Kingdom', 'value': 'United Kingdom'},

            {'label': 'Australia', 'value': 'Australia'},

            
            {'label': 'Sweden', 'value': 'Sweden'},
            {'label': 'Switzerland', 'value': 'Switzerland'},
            {'label': 'Austria', 'value': 'Austria'},
            {'label': 'France', 'value': 'France'},
            {'label': 'Germany', 'value': 'Germany'},
            {'label': 'Turkey', 'value': 'Turkey'},
            
            {'label': 'New Zealand', 'value': 'New Zealand'},
            ]

stateOPTS = [
    {'label':'Polygon 1','value':"P1"},
    {'label':'Polygon 2','value':"P2"},
    {'label':'Polygon 3','value':"P3"},
    {'label':'Polygon 4','value':"P4"}
    ]


fnameDict = {'P1': allLeaks.loc[allLeaks.POLYGON == "P1",].LEAKNUM.unique(), 'P2': allLeaks.loc[allLeaks.POLYGON == "P2",].LEAKNUM.unique(),
             'P3': allLeaks.loc[allLeaks.POLYGON == "P3",].LEAKNUM.unique(),'P4': allLeaks.loc[allLeaks.POLYGON == "P4",].LEAKNUM.unique()
                       
             }
names = list(fnameDict.keys())
nestedOptions = fnameDict[names[0]]


tab1=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Polygon:", className="control_label"),
                       dcc.Dropdown(
                            id="whichPoly",
                            #options=well_status_options,
                            options = stateOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'P1',
                            className="dcc_control",
                        ),
                        html.P("Choose Leak Number:", className="control_label"),
                        dcc.Dropdown(
                            id='opt-dropdown',
                            #options=[{'label':opt, 'value':opt} for opt in nestedOptions],
                            #value = nestedOptions[0]        
                            options = [],
                        ),
                        dcc.RadioItems(
                            id="whichMap",
                            options=whichMapOPTS,
                            value="sat",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ),
                        html.A(html.Button('Get Route'),
    #href='https://github.com/czbiohub/singlecell-dash/issues/new',
    id = 'map_dir',target='_blank',
    )

                       # dcc.RadioItems(
                       #     id="popratiostate",
                       #     options=popOPTS,
                       #     value="nonrelpop",
                       #     labelStyle={"display": "inline-block"},
                       #     className="dcc_control",
                       # ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options-state",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                 html.Div(
                                     [html.H6(id="well_text"), html.P("Polygon:")],
                                     id="polygon",
                                     className="mini_container",
                                 ),
                                 html.Div(
                                     [html.H6(id="gasText"), html.P("Status:")],
                                     id="polygonLks",
                                     className="mini_container",
                                 ),
                               
                                # html.Div(
                                #     [html.H6(id="oilText"), html.P("")],
                                #     id="oil",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="waterText"), html.P("")],
                                #     id="water",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-state",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="leakGraph")],
                    className="pretty_container seven columns",
                ),
                #html.Div(
                #    [dcc.Graph(id="statePredGraph")],
                #    className="pretty_container five columns",
                #),
                html.Div(
                    [dcc.Graph(id='hover-data-plot')],#,id="hover-data-plot")],
                    className="pretty_container five columns"),
            ],
            className="row flex-display",
        ),
        html.Div(
             [
                 html.Div(id='hover-data-info',
                     #[dcc.Markdown(id="hover-data-info")],
                     className="pretty_container seven columns",
                 ),
        #         html.Div(
        #             [dcc.Graph(id="aggregate_graph")],
        #             className="pretty_container five columns",
        #         ),
             ],
             className="row flex-display",
         )
        ])

tab2=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Polygon:", className="control_label"),
                       dcc.Dropdown(
                            id="whichPolyGap",
                            #options=well_status_options,
                            options = stateOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'P1',
                            className="dcc_control",
                        ),
                        #html.P("Choose Related City:", className="control_label"),
                        #dcc.Dropdown(
                        #    id="whichCity",
                            #options=[{'label':opt, 'value':opt} for opt in stat_nestedOptions],
                            #value = stat_nestedOptions[0],
                            #options=well_type_options,
                            #multi=True,
                            #value=list(WELL_TYPES.keys()),
                         #   className="dcc_control",
                        #),
                        dcc.RadioItems(
                            id="whichMapGap",
                            options=whichMapOPTS,
                            value="sat",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ),
                        # dcc.RadioItems(
                        #     id="popratiostate",
                        #     options=popOPTS,
                        #     value="nonrelpop",
                        #     labelStyle={"display": "inline-block"},
                        #     className="dcc_control",
                        # ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options-state",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                # html.Div(
                                #     [html.H6(id="well_text"), html.P("State:")],
                                #     id="stateName",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="gasText"), html.P("Status:")],
                                #     id="stateStatus",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="oilText"), html.P("")],
                                #     id="oil",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="waterText"), html.P("")],
                                #     id="water",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-state",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="gapGraph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id='hover-data-plot')],#,id="hover-data-plot")],
                    className="pretty_container five columns"
                ),
            ],
            className="row flex-display",
        ),
        # html.Div(
        #     [
        #         html.Div(
        #             [dcc.Graph(id="pie_graph2")],
        #             className="pretty_container seven columns",
        #         ),
        #         html.Div(
        #             [dcc.Graph(id="aggregate_graph")],
        #             className="pretty_container five columns",
        #         ),
        #     ],
        #     className="row flex-display",
        # )
        ])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True,
                 meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server = app.server
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        #html.Img(
                        #    src = img,
                            #src='data:image/png;base64,{}'.format(encoded_image.decode()),
                         #   id="plotly-image",
                         #   style={
                         #       "height": "60px",
                         #       "width": "auto",
                         #       "margin-bottom": "25px",
                         #   },
                       # )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Southern Cross Gap and Leak Indication",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Trussville, AL", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Last Updated",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    '6.23.20', style={"margin-top": "0px"}
                                ),
                              dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
                                  dcc.Tab(id="tab-1", label='Leak Indications', value='tab-1-example'),
                                  dcc.Tab(id="tab-2", label='Gaps', value='tab-2-example'),
                                 # dcc.Tab(id= 'tab-4',label = 'Weekly Info',value = 'tab-4-example')
                                  ])

                            ]
                        )
                    ],
                    className="one-fourth row",
                    id="title2",
                ),

                
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(id='tabs-content-example',
             children = tab1),
       
        
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column",'backgroundColor':'white'},
)





@app.callback(dash.dependencies.Output('tabs-content-example', 'children'),
             [dash.dependencies.Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1
    elif tab == 'tab-2-example':
        return tab2
    #elif tab == 'tab-4-example':
    #    return tab4

@app.callback(dash.dependencies.Output('leakGraph', 'figure'),
              [dash.dependencies.Input('whichPoly', 'value'),
               dash.dependencies.Input('whichMap', 'value')
               
               ]
              )
def update_polyLeak(whichPolygon,whichMap):
    usedat = allLeaks.loc[allLeaks.POLYGON == whichPolygon,:]
    color_discrete_map = {'P1': 'rgb(255,0,0)', 'P2': 'rgb(255,0,0)', 'P3': 'rgb(255,0,0)',
                          'P4': 'rgb(255,0,0)'}
    color_discrete_lks= {'P1': 'rgb(255,255,255)', 'P2': 'rgb(255,255,255)', 'P3': 'rgb(255,255,255)',
                          'P4': 'rgb(255,255,255)'}
    color_discrete_lks_ns= {'P1': 'rgb(0, 0, 99)', 'P2': 'rgb(0, 0, 99)', 'P3': 'rgb(0, 0, 99)',
                          'P4': 'rgb(0, 0, 99)'}
    
    usepoly = allPoly.loc[allPoly.POLYGON == whichPolygon,:]
    usepoly2 = usepoly.loc[usepoly.portion == 3,:]
    if whichMap == 'sat':
        fig = px.line_mapbox(
            usepoly2,
            lon = 'lat',
            lat = 'lon',
            zoom = 12,
            color = 'POLYGON',
            color_discrete_map=color_discrete_map
    
            )
        if usedat.shape[0]!=0:
            fig2 = px.scatter_mapbox(usedat, lat="Latitude", lon="Longitude",  
                          color = 'POLYGON', color_discrete_map = color_discrete_lks, size_max=15, zoom=11,
                          hover_data = {'PolyLK'})
            fig.add_trace(fig2.data[0])
    elif whichMap != 'sat':
        fig = px.line_mapbox(
            usepoly2,
            lon = 'lat',
            lat = 'lon',
            zoom = 12,
            color = 'POLYGON',
            color_discrete_map=color_discrete_map
    
            )
        if usedat.shape[0]!=0:
            fig2 = px.scatter_mapbox(usedat, lat="Latitude", lon="Longitude",  
                          color = 'POLYGON', color_discrete_map = color_discrete_lks_ns, size_max=15, zoom=11,
                          hover_data = {'PolyLK'})
            fig.add_trace(fig2.data[0])
            

        
    fig.update_layout(
        autosize=True,
        width = 800,
        height = 800,
        showlegend = False
        )

    fig.update()
    if whichMap == "sat":
        fig.update_layout(
            mapbox_style="satellite-streets",
 )
    
    
    return fig

@app.callback(
    dash.dependencies.Output('opt-dropdown', 'options'),
    [dash.dependencies.Input('whichPoly', 'value')]
)
def update_date_dropdown(name):
    options=[{'label':i, 'value':i} for i in fnameDict[name]]
    return options
    #return ('options':[{'label': 1, 'value': 1},{'label': 2, 'value': 2},{'label': 3, 'value': 3},{'label': 4, 'value': 4}])


@app.callback(dash.dependencies.Output('gapGraph', 'figure'),
              [dash.dependencies.Input('whichPolyGap', 'value'),
               dash.dependencies.Input('whichMapGap', 'value')
               
               ]
              )
def update_gapLeak(whichPolygon,whichMap):
    usedat = allLeaks.loc[allLeaks.POLYGON == whichPolygon,:]    
    usepoly = allPoly.loc[allPoly.POLYGON == whichPolygon,:]
    usegap = allGaps.loc[allGaps.POLYGON == whichPolygon,:]
    usepoly2 = usepoly.loc[usepoly.portion == 3,:]
    #howmany = usegap.portion.drop_duplicates().size
    if whichPolygon == 'P1':
      #howmany =129
      howmany = 50
    elif whichPolygon == "P2":
      #howmany = 72
      howmany = 50
    elif whichPolygon == "P3":
      #howmany = 141
      howmany = 50
    elif whichPolygon == 'P4':
      howmany = 31
    
    if whichMap == 'sat':
        color_discrete_map = {'P1': 'rgb(255,0,0)', 'P2': 'rgb(255,0,0)', 'P3': 'rgb(255,0,0)',
                              'P4': 'rgb(255,0,0)'}
        color_discrete_lks= {'P1': 'rgb(255,255,255)', 'P2': 'rgb(255,255,255)', 'P3': 'rgb(255,255,255)',
                              'P4': 'rgb(255,255,255)'}
    elif whichMap != 'sat':
        color_discrete_lks= {'P1': 'rgb(0, 0, 99)', 'P2': 'rgb(0, 0, 99)', 'P3': 'rgb(0, 0, 99)',
                              'P4': 'rgb(0, 0, 99)'}
        color_discrete_map = {'P1': 'rgb(255,0,0)', 'P2': 'rgb(255,0,0)', 'P3': 'rgb(255,0,0)',
                              'P4': 'rgb(255,0,0)'}
    
    fig = px.line_mapbox(
        usepoly2,
        lon = 'lat',
        lat = 'lon',
        zoom = 12,
        color = 'POLYGON',
        color_discrete_map=color_discrete_map
            )
    
    fig.update_layout(
        autosize=True,
        width = 800,
        height = 800,
        showlegend = False,
        
        )
    for x in range(howmany):
    #for x in range(32):
        i = x+1
        use = usegap.loc[usegap.portion == i,]
        fig.add_trace(
            px.line_mapbox(use,
                lon = 'lon',
                lat = 'lat',
                zoom = 10,
                color = 'POLYGON',
                color_discrete_map=color_discrete_lks,
                width = 10,
                ).data[0],
                
            
            )    
    if whichMap == "sat":
        fig.update_layout(
            mapbox_style="satellite-streets",
 )
    return fig






# =============================================================================
# @app.callback(
#     dash.dependencies.Output('hover-data-plot', 'figure'),
#     [dash.dependencies.Input('leakGraph', 'hoverData'),
#      dash.dependencies.Input('whichMap', 'value')])
# def updatePlot(hoverData,whichMap):
#      plk = hoverData['points'][0]['customdata'][0]
#      dat = allLeaks[allLeaks.PolyLK==str(plk)]
#      #dat=allLeaks
#      title = "Leak " + str(int(dat.reset_index().LEAKNUM)) + '. '+ " Location: " + str(float(dat.reset_index().loc[0,['Longitude']])) + ',' + str(float(dat.reset_index().loc[0,['Latitude']]))
#      fig = px.scatter_mapbox(dat, lat="Latitude", lon="Longitude", 
#                    size_max=25, zoom=15,
#                   hover_data = {'PolyLK'})
#                                                   
#      fig.update_layout(
#         autosize=True,
#         width = 800,
#         height = 800,
#         title =title
#         )
#      fig.update_traces(marker = dict(size = 20))
#      
#      if whichMap == "sat":
#         fig.update_layout(
#             mapbox_style="satellite-streets",
#             )
#      fig.update()
#      return fig
# =============================================================================
 
@app.callback(
    dash.dependencies.Output('hover-data-plot', 'figure'),
    [dash.dependencies.Input('whichPoly', 'value'),
     dash.dependencies.Input('opt-dropdown', 'value'),
     dash.dependencies.Input('whichMap', 'value')
     ])
def updatePlot(whichPoly,whichLeak,whichMap):
     #plk = hoverData['points'][0]['customdata'][0]
     dat2 = allLeaks.loc[allLeaks.POLYGON == whichPoly,]
     dat = dat2.loc[dat2.LEAKNUM == whichLeak,]
     if whichMap == 'sat':
        color_discrete_map = {'P1': 'rgb(255,0,0)', 'P2': 'rgb(255,0,0)', 'P3': 'rgb(255,0,0)',
                              'P4': 'rgb(255,0,0)'}
        color_discrete_lks= {'P1': 'rgb(255,255,255)', 'P2': 'rgb(255,255,255)', 'P3': 'rgb(255,255,255)',
                              'P4': 'rgb(255,255,255)'}
     elif whichMap != 'sat':
         color_discrete_lks= {'P1': 'rgb(0, 0, 99)', 'P2': 'rgb(0, 0, 99)', 'P3': 'rgb(0, 0, 99)',
                              'P4': 'rgb(0, 0, 99)'}
         color_discrete_map = {'P1': 'rgb(255,0,0)', 'P2': 'rgb(255,0,0)', 'P3': 'rgb(255,0,0)',
                              'P4': 'rgb(255,0,0)'}
     #dat = allLeaks[allLeaks.PolyLK==str(plk)]
     #dat=allLeaks
     title = "Leak " + str(whichLeak) + '. '+ " Location: " + str(float(dat.reset_index().loc[0,['Latitude']])) + ',' + str(float(dat.reset_index().loc[0,['Longitude']]))
     fig = px.scatter_mapbox(dat, lat="Latitude", lon="Longitude", 
                   size_max=25, zoom=15,
                  hover_data = {'PolyLK'},
                  color = 'POLYGON',
                  color_discrete_map=color_discrete_lks

                  
                  
                  )
                                                  
     fig.update_layout(
        autosize=True,
        width = 800,
        height = 800,
        title =title
        )
     fig.update_traces(marker = dict(size = 20))
     
     if whichMap == "sat":
        fig.update_layout(
            mapbox_style="satellite-streets",
            )
     fig.update()
     return fig
 
@app.callback(
    dash.dependencies.Output('map_dir', 'href'),
    [dash.dependencies.Input('whichPoly', 'value'),
     dash.dependencies.Input('opt-dropdown', 'value'),
     ])
def giveURL(whichPoly,whichLeak):
    dat2 = allLeaks.loc[allLeaks.POLYGON == whichPoly,]
    dat = dat2.loc[dat2.LEAKNUM == whichLeak,]
    
    lon = str(float(dat.Longitude))
    lat = str(float(dat.Latitude))
    
    url = 'https://www.google.com/maps/dir//' + lat + ',' + lon + '/@' + lat + ',' + lon + ',13z/data=!4m7!4m6!1m0!1m3!2m2!1d-86.5940475!2d33.7491112!3e0'
    return(url)



@app.callback(
    dash.dependencies.Output('hover-data-info', 'children'),
    [dash.dependencies.Input('leakGraph', 'hoverData')])
def updatename(hoverData):
     plk = hoverData['points'][0]['customdata']
     title = plk
     return title
 
@app.callback(dash.dependencies.Output('polygon', 'children'),
              [dash.dependencies.Input('whichPoly', 'value')]
              )
def updateText(whichPolygon):
    return "Polygon " + str(whichPolygon[1:])

@app.callback(dash.dependencies.Output('polygonLks', 'children'),
              [dash.dependencies.Input('whichPoly', 'value')]
              )
def updatePolyLk(whichPolygon):
    dat = allLeaks[allLeaks.POLYGON==str(whichPolygon)]
    return "Number of Leaks: " + str(dat.shape[0])

    
if __name__ == '__main__':
    app.run_server(debug=False)



                
