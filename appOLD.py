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
import plotly.io as pio



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/header2.css'  ,
                        'https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css'
                        ]
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')

#allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allLeaks.csv')
allPoly = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allPoly.csv')
allGaps = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allGaps.csv')
allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allLeaksWin.csv')

#### CREATING A LIST OF THE POLYGONS THAT HAVE BEEN CHECKED
checked = []
for x in range(0,len(allGaps.POLYGON.unique())):
    checked.append(allGaps.POLYGON.unique()[x])

#### CREATING GROUPS OF GAPS
gaps2a = list(range(42,57+1)) + list(range(74,75))
gaps2b = list(range(29,41+1)) 
gaps2c = list(range(60,69+1)) 
gaps2d = list(range(9,12+1)) + list(range(14,28+1))
gaps2e = list(range(5,8+1)) + list(range(58,59+1)) + list(range(70,73+1))
gaps2f = list(range(42,57+1)) + list(range(74,75))

gaps1a = list(range(1,4+1)) + list(range(7,9+1))+ list(range(108,131+1)) 
gaps1b = list(range(5,6+1)) + list(range(10,17+1))+ list(range(50,54+1)) + list(range(107,108))
gaps1c = list(range(29,49+1)) 
gaps1d = list(range(18,28+1))
gaps1e = list(range(105,106+1))
gaps1f = list(range(67,100+1))
gaps1g = list(range(55,66+1))

gaps3a = list(range(76,92+1))
gaps3b = list(range(72,75)) + list(range(102,105+1))
gaps3c = list(range(68,71+1))
gaps3d = list(range(93,101+1))
gaps3e = list(range(59,67+1))+list(range(106,107))
gaps3f = list(range(107,123))
gaps3g = list(range(18,29)) + list(range(37,46+1))+ list(range(138,142+1))
gaps3h = list(range(47,58+1)) + list(range(136,137+1))
gaps3i = list(range(26,36+1)) + list(range(143,144))
gaps3l = list(range(1,7+1)) + list(range(127,135+1))
gaps3j = list(range(8,17+1)) + list(range(124,126+1))
gaps3k = list(range(19,25+1)) 

gaps4a = list(range(18,22+1)) 
gaps4b = list(range(6,17+1)) 
gaps4c = list(range(1,5+1)) +list(range(23,33+1))

gaps5a = list(range(93,105+1))
gaps5b = list(range(108,109+1)) +list(range(135,142+1))
gaps5c = list(range(110,135+1)) 
gaps5d = list(range(89,92+1)) +list(range(106,107+1))
gaps5e = list(range(7,8+1)) +list(range(83,88+1))+list(range(143,144+1))+list(range(147,148))
gaps5f = list(range(74,82+1))
gaps5g = list(range(3,6+1)) +list(range(9,10+1))+list(range(47,48+1))
gaps5h = list(range(49,56+1)) +list(range(72,73+1))
gaps5i = list(range(57,71+1))
gaps5j = list(range(1,2+1)) + list(range(11,22+1))
gaps5k = list(range(37,46+1))
gaps5l = list(range(23,36+1))


gaps58a = list(range(69,73+1)) + list(range(97,123+1))
gaps58b = list(range(56,68+1)) 
gaps58c = list(range(50,55+1)) +list(range(78,88+1))+list(range(92,96+1))
gaps58d = list(range(39,47+1))
gaps58e = list(range(74,76+1)) 
gaps58f = list(range(1,5+1)) + list(range(77,78)) + list(range(89,91+1))
gaps58g = list(range(6,12+1)) +list(range(34,38+1))
gaps58h = list(range(13,33+1)) 


gaps59a = list(range(80,85+1))
gaps59b = list(range(86,111+1)) 
gaps59c = list(range(71,79+1)) +list(range(113,114+1))
gaps59d = list(range(57,70+1)) +list(range(115,117+1))
gaps59e = list(range(43,56+1)) +list(range(130,132+1))+list(range(146,148+1))
gaps59f = list(range(38,42+1)) +list(range(120,129+1))+list(range(133,145+1))
gaps59g = list(range(28,37+1)) +list(range(121,124+1))
gaps59h = list(range(1,5+1)) +list(range(125,128+1))
gaps59i = list(range(13,16+1))+ list(range(21,27+1))
gaps59j = list(range(5,12+1)) + list(range(17,20+1)) + list(range(149,151+1))


gaps1Dict = {'1':gaps1a,
             '2':gaps1b,
             '3':gaps1c,
             '4':gaps1d,
             '5':gaps1e,
             '6':gaps1f,
             '7':gaps1g,
             }
gaps2Dict = {'1':gaps2a,
             '2':gaps2b,
             '3':gaps2c,
             '4':gaps2d,
             '5':gaps2e,
             '6':gaps2f,
             }
gaps3Dict = {'1':gaps3a,
             '2':gaps3b,
             '3':gaps3c,
             '4':gaps3d,
             '5':gaps3e,
             '6':gaps3f,
             '7':gaps3g,
             '8':gaps3h,
             '9':gaps3i,
             '10':gaps3j,
             '11':gaps3k,
             '12':gaps3l,
             }
gaps4Dict = {'1':gaps4a,
             '2':gaps4b,
             '3':gaps4c,
             }
gaps5Dict = {'1':gaps5a,
             '2':gaps5b,
             '3':gaps5c,
             '4':gaps5d,
             '5':gaps5e,
             '6':gaps5f,
             '7':gaps5g,
             '8':gaps5h,
             '9':gaps5i,
             '10':gaps5j,
             '11':gaps5k,
             '12':gaps5l,
             }

gaps58Dict = {'1':gaps58a,
             '2':gaps58b,
             '3':gaps58c,
             '4':gaps58d,
             '5':gaps58e,
             '6':gaps58f,
             '7':gaps58g,
             '8':gaps58h,
    
             }

gaps59Dict = {'1':gaps59a,
             '2':gaps59b,
             '3':gaps59c,
             '4':gaps59d,
             '5':gaps59e,
             '6':gaps59f,
             '7':gaps59g,
             '8':gaps59h,
             '9':gaps59i,
             '10':gaps59j,
             }

gapsDict = {'P1': gaps1Dict,
            'P2': gaps2Dict,
            'P3': gaps3Dict,
            'P4': gaps4Dict,
            'P5': gaps5Dict,
            'P58': gaps58Dict,
            'P59': gaps59Dict

    }




projOPTS = [        ]

whichAvgOPTS = []

popOPTS = [ ]

whichMapOPTS = [
    {'label':'Satellite Map','value':'sat'},
    {'label':'Street Map', 'value':'street'}
       
    ]

countryOPTS = [  ]

stateOPTS = [
    {'label':'Polygon 1','value':"P1"},
    {'label':'Polygon 2','value':"P2"},
    {'label':'Polygon 3','value':"P3"},
    {'label':'Polygon 4','value':"P4"},
    {'label':'Polygon 5','value':"P5"},
    {'label':'Polygon 58','value':"P58"},
    {'label':'Polygon 59','value':"P59"}

    ]
                            #options=[{'label':opt, 'value':opt} for opt in nestedOptions],

polyOPTS = [{'label':str('Polygon ') + str(x),'value':str('P')+str(x)} for x in list(range(1,22+1))+list(range(24,60+1))]


fnameDict = {'P1': allLeaks.loc[allLeaks.POLYGON == "P1",].LEAKNUM.unique(), 'P2': allLeaks.loc[allLeaks.POLYGON == "P2",].LEAKNUM.unique(),
             'P3': allLeaks.loc[allLeaks.POLYGON == "P3",].LEAKNUM.unique(),'P4': allLeaks.loc[allLeaks.POLYGON == "P4",].LEAKNUM.unique(),
             'P5': allLeaks.loc[allLeaks.POLYGON == "P5",].LEAKNUM.unique(),'P58': allLeaks.loc[allLeaks.POLYGON == "P58",].LEAKNUM.unique(),
             'P59': allLeaks.loc[allLeaks.POLYGON == "P59",].LEAKNUM.unique()
                       
             }

#fnameDict2 = [{x:allLeaks.loc[allLeaks.POLYGON == x].LEAKNUM.unique()} for x in checked]


gapSize = 10
gnameDict = {'P1':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P1',].portion.unique().size/gapSize)+1)),
             'P2':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P2',].portion.unique().size/gapSize)+1)),
             'P3':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P3',].portion.unique().size/gapSize)+1)),
             'P4':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P4',].portion.unique().size/gapSize)+1))             
             }
# gsizeDict = {'P1':allGaps.loc[allGaps.POLYGON=='P1',].portion.unique().size,
#              'P2':allGaps.loc[allGaps.POLYGON=='P2',].portion.unique().size,
#              'P3':allGaps.loc[allGaps.POLYGON=='P3',].portion.unique().size,
#              'P4':allGaps.loc[allGaps.POLYGON=='P4',].portion.unique().size,    
#              'P5':allGaps.loc[allGaps.POLYGON=='P5',].portion.unique().size,
#              'P58':allGaps.loc[allGaps.POLYGON=='P58',].portion.unique().size,
#              'P59':allGaps.loc[allGaps.POLYGON=='P59',].portion.unique().size
#              }

gsizeDict = {}
for x in checked:
    gsizeDict[x] = allGaps.loc[allGaps.POLYGON==x,].portion.unique().size

color_discrete_map_st = {}
for x in list(range(1,60+1)):
    color_discrete_map_st[str("P") + str(x)] = 'rgb(255,0,0)'

color_discrete_lks_st = {}
for x in list(range(1,60+1)):
    color_discrete_lks_st[str("P") + str(x)] = 'rgb(255,255,255)'

color_discrete_lks_ns = {}
for x in list(range(1,60+1)):
    color_discrete_lks_ns[str("P") + str(x)] = 'rgb(0, 0, 99)'
 

tab1=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Polygon:", className="control_label"),
                       dcc.Dropdown(
                            id="whichPoly",
                            #options=well_status_options,
                            options = polyOPTS,
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
                        html.P("Choose Which Group of Gaps:", className="control_label"),
                        dcc.Dropdown(
                            id="whichGapPack",
                            #options=[{'label':opt, 'value':opt} for opt in stat_nestedOptions],
                            #value = stat_nestedOptions[0],
                            options=[],
                            #multi=True,
                            #value=list(WELL_TYPES.keys()),
                            className="dcc_control",
                        ),
                        dcc.RadioItems(
                            id="whichMapGap",
                            options=whichMapOPTS,
                            value="sat",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ), html.A(html.Button('Get Route'),
    #href='https://github.com/czbiohub/singlecell-dash/issues/new',
    id = 'gap_dir',target='_blank',
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
                                     id="polyname",
                                     className="mini_container",
                                 ),
                                 html.Div(
                                     [html.H6(id="gasText"), html.P("Groups of Gaps:")],
                                     id="gapStatus",
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
                    [dcc.Graph(id="gapGraph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id='hoverGapPlot')],#,id="hover-data-plot")],
                    className="pretty_container five columns"
                ),
            ],
            className="row flex-display",
        ),
         html.Div(
             [
            html.Div(id='hover-gap-info',
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
                                    '6.25.20', style={"margin-top": "0px"}
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
    
    if whichMap == "sat":
        color_discrete_lks = color_discrete_lks_st
    elif whichMap != 'sat':
        color_discrete_lks = color_discrete_lks_ns
        
        
    usepoly = allPoly.loc[allPoly.POLYGON == whichPolygon,:]
    usepoly2 = usepoly.loc[usepoly.portion == 3,:]
    if whichPolygon == "P5" or whichPolygon == "P58" or whichPolygon == "P59":
            usepoly2 = usepoly.loc[usepoly.portion == 1,:]

    fig = px.line_mapbox(
        usepoly2,
        lon = 'lat',
        lat = 'lon',
        zoom = 12,
        color = 'POLYGON',
        color_discrete_map=color_discrete_map_st

        )
    if usedat.shape[0]!=0:
        fig2 = px.scatter_mapbox(usedat, lat="Latitude", lon="Longitude",  
                      color = 'POLYGON', color_discrete_map = color_discrete_lks, size_max=15, zoom=11,
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



@app.callback(dash.dependencies.Output('whichGapPack', 'options'),
              [dash.dependencies.Input('whichPolyGap', 'value')]
              )
def updateGapOpts(whichPoly):
        
    options = [{'label':i, 'value':i} for i in allGaps.loc[allGaps.POLYGON == whichPoly,'portion'].unique()]
    #relDict = gapsDict[whichPoly]
    #options=[{'label':i, 'value':i} for i in range(1,len(relDict)+1)]
    return options


@app.callback(dash.dependencies.Output('gapGraph', 'figure'),
              [dash.dependencies.Input('whichPolyGap', 'value'),
               dash.dependencies.Input('whichMapGap', 'value'),
               dash.dependencies.Input('whichGapPack','value')
               
               ]
              )
def newGapGraph(whichPolygon,whichMap,whichGapPack):
    #gapwoo = gapsDict[whichPolygon][str(whichGapPack)]
    usegap = allGaps.loc[allGaps.POLYGON == whichPolygon,:]
    #usegapsmall = usegap[usegap['portion'].isin(gapwoo)]
    usegapsmall = usegap.loc[usegap['portion']== whichGapPack,:]

    #usepoly = allPoly.loc[allPoly.POLYGON == whichPolygon,:]
    #usepoly2 = usepoly.loc[usepoly.portion == 3,:]
    if whichMap == "sat":
        color_discrete_lks = color_discrete_map_st
    elif whichMap != 'sat':
        color_discrete_lks = color_discrete_map_st
    fig = px.line_mapbox(usegapsmall,
                lon = 'lon',
                lat = 'lat',
                zoom = 16,
                color = 'POLYGON',
                color_discrete_map=color_discrete_lks,
                width = 50,
                hover_data = {'portion'}
                )
    fig.update_layout(
             #autosize=True,
             width = 800,
             height = 800,
             showlegend = False,
                 
       
            )    
    fig.update_traces(line=dict(width=6))

        
    # for x in usegapsmall.portion.unique():   
    #     use = usegapsmall.loc[usegap.portion == x,]
    #     if x==usegapsmall.portion.unique().min():
    #         fig = px.line_mapbox(use,
    #             lon = 'lon',
    #             lat = 'lat',
    #             zoom = 14,
    #             color = 'POLYGON',
    #             color_discrete_map=color_discrete_lks,
    #             width = 50,
    #             hover_data = {'portion'}
    #             )
    #         fig.update_layout(
    #          #autosize=True,
    #          width = 800,
    #          height = 800,
    #          showlegend = False,
       
    #         )
            
    #     elif x != usegapsmall.portion.unique().min():
    #         fig.add_trace(
    #             px.line_mapbox(use,
    #                 lon = 'lon',
    #                 lat = 'lat',
    #                 zoom = 14,
    #                 color = 'POLYGON',
    #                 color_discrete_map=color_discrete_lks,
    #                 width = 50,
    #                 hover_data = {'portion'}

    #                 ).data[0],
    #             )    
    if whichMap == "sat":
       fig.update_layout(
           mapbox_style="satellite-streets",
           )

    return(fig)

@app.callback(
    dash.dependencies.Output('hoverGapPlot', 'figure'),
    [dash.dependencies.Input('gapGraph', 'hoverData'),
      dash.dependencies.Input('whichPolyGap', 'value'),
      dash.dependencies.Input('whichMapGap', 'value')])
    
def updateGapHover(hoverData,whichGap,whichMap):
    plk = int(hoverData['points'][0]['customdata'][0])
    usegap = allGaps.loc[allGaps.POLYGON == whichGap,:]
    usegapsmall = usegap.loc[usegap.portion==plk,:]
    
    if whichMap == "sat":
        color_discrete_lks = color_discrete_lks_st
    elif whichMap != 'sat':
        color_discrete_lks = color_discrete_lks_ns
        
    
    fig = px.line_mapbox(usegapsmall,
        lon = 'lon',
        lat = 'lat',
        zoom = 18,
        color = 'POLYGON',
        color_discrete_map=color_discrete_lks,
        width = 50,

        #hover_data = {'portion'}
        )
    fig.update_layout(
     #autosize=True,
     width = 800,
     height = 800,
     showlegend = False,
   
    )
    fig.update_traces(line=dict(width=4))
            
      
    if whichMap == "sat":
       fig.update_layout(
           mapbox_style="satellite-streets",
           )

    return(fig)

 
 
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
     if whichMap == "sat":
        color_discrete_lks = color_discrete_lks_st
     elif whichMap != 'sat':
        color_discrete_lks = color_discrete_lks_ns
        
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
    dash.dependencies.Output('hover-gap-info', 'children'),
    [dash.dependencies.Input('gapGraph', 'hoverData')])
def updateHoverInfo(hoverData):
     plk = hoverData['points'][0]['customdata']
     title = plk
     return title
 

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

@app.callback(dash.dependencies.Output('polyname', 'children'),
              [dash.dependencies.Input('whichPolyGap', 'value')]
              )
def updateGapText(whichPolygon):
    return "Polygon " + str(whichPolygon[1:])

@app.callback(dash.dependencies.Output('gapStatus', 'children'),
              [dash.dependencies.Input('whichPolyGap', 'value')]
              )
def updateGapText2(whichPolygon):
    num = len(gapsDict[whichPolygon])
    return "Number of Gap Groups: " + str(num)



@app.callback(
    dash.dependencies.Output('gap_dir', 'href'),
    [dash.dependencies.Input('whichPolyGap', 'value'),
     dash.dependencies.Input('whichGapPack','value')
     ])
                  
def giveGAPURL(whichPoly,whichGap):
    usegap = allGaps.loc[allGaps.POLYGON == whichPoly,:]
    #usegapsmall = usegap[usegap['portion'].isin(gapwoo)]
    usegapsmall = usegap.loc[usegap['portion']== whichGap,:]

    #plk = int(whichGap['points'][0]['customdata'][0])
    #usegap = allGaps.loc[allGaps.POLYGON == whichPoly,:]
    #usegapsmall = usegap.loc[usegap.portion==plk,:]
    
    usegapsmall.reset_index().lon[0]
    
    lon = str(usegapsmall.reset_index().lon[0])

    lat =  str(usegapsmall.reset_index().lat[0])
    
    url = 'https://www.google.com/maps/dir//' + lat + ',' + lon + '/@' + lat + ',' + lon + ',13z/data=!4m7!4m6!1m0!1m3!2m2!1d-86.5940475!2d33.7491112!3e0'
    return(url)
    


if __name__ == '__main__':
    app.run_server(debug=False)



                
