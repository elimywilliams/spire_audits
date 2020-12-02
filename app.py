# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import json
import bs4 as bs
import dash_html_components as html
import requests 
import plotly.io as pio



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/header2.css'  ,
                        'https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css'
                        ]
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')

allPoly = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allPoly.csv')
allGaps = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allGaps.csv')
allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/allLeaksWin.csv')

#### CREATING A LIST OF THE POLYGONS THAT HAVE BEEN CHECKED
checked = []
for x in range(0,len(allGaps.POLYGON.unique())):
    checked.append(allGaps.POLYGON.unique()[x])

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
    {'label':'Polygon 6','value':"P6"},

    {'label':'Polygon 7','value':"P7"},
    {'label':'Polygon 8','value':"P8"},
    {'label':'Polygon 9','value':"P9"},

    {'label':'Polygon 10','value':"P10"},
    {'label':'Polygon 11','value':"P11"},
    {'label':'Polygon 12','value':"P12"},
    {'label':'Polygon 13','value':"P13"},

    {'label':'Polygon 14','value':"P14"},
    {'label':'Polygon 15','value':"P15"},

    {'label':'Polygon 16','value':"P16"},
    {'label':'Polygon 17','value':"P17"},
    {'label':'Polygon 18','value':"P18"},

    {'label':'Polygon 19','value':"P19"},
    {'label':'Polygon 20','value':"P20"},
    {'label':'Polygon 21','value':"P21"},

    {'label':'Polygon 22','value':"P22"},
    {'label':'Polygon 23','value':"P23"},
    
    {'label':'Polygon 24','value':"P24"},
    {'label':'Polygon 25','value':"P25"},
    {'label':'Polygon 26','value':"P26"},
    {'label':'Polygon 27','value':"P27"},
    {'label':'Polygon 28','value':"P28"},
    {'label':'Polygon 29','value':"P29"},
    {'label':'Polygon 30','value':"P30"},
    {'label':'Polygon 31','value':"P31"},
  
    {'label':'Polygon 32','value':"P32"},
    {'label':'Polygon 33','value':"P33"},
    {'label':'Polygon 34','value':"P34"},
    {'label':'Polygon 35','value':"P35"},
    {'label':'Polygon 36','value':"P36"},
    {'label':'Polygon 37','value':"P37"},

    {'label':'Polygon 38','value':"P38"},
    {'label':'Polygon 39','value':"P39"},
    {'label':'Polygon 40','value':"P40"},
    {'label':'Polygon 41','value':"P41"},
    {'label':'Polygon 42','value':"P42"},
    {'label':'Polygon 43','value':"P43"},
    {'label':'Polygon 44','value':"P44"},
    {'label':'Polygon 45','value':"P45"},
    {'label':'Polygon 46','value':"P46"},
  
    {'label':'Polygon 47','value':"P47"},
    {'label':'Polygon 48','value':"P48"},
    {'label':'Polygon 49','value':"P49"},
    {'label':'Polygon 50','value':"P50"},
  
    {'label':'Polygon 51','value':"P51"},
    {'label':'Polygon 52','value':"P52"},
    {'label':'Polygon 53','value':"P53"},
    {'label':'Polygon 54','value':"P54"},
    {'label':'Polygon 55','value':"P55"},
    {'label':'Polygon 56','value':"P56"},
    {'label':'Polygon 57','value':"P57"},

    {'label':'Polygon 58','value':"P58"},
    {'label':'Polygon 59','value':"P59"},
    {'label':'Polygon 60','value':"P60"}


    ]
                            #options=[{'label':opt, 'value':opt} for opt in nestedOptions],

polyOPTS = [{'label':str('Polygon ') + str(x),'value':str('P')+str(x)} for x in list(range(1,60+1))]


fnameDict = {'P1': allLeaks.loc[allLeaks.POLYGON == "P1",].LEAKNUM.unique(), 
             'P2': allLeaks.loc[allLeaks.POLYGON == "P2",].LEAKNUM.unique(),
             'P3': allLeaks.loc[allLeaks.POLYGON == "P3",].LEAKNUM.unique(),
             'P4': allLeaks.loc[allLeaks.POLYGON == "P4",].LEAKNUM.unique(),
             'P5': allLeaks.loc[allLeaks.POLYGON == "P5",].LEAKNUM.unique(),
             'P6': allLeaks.loc[allLeaks.POLYGON == "P6",].LEAKNUM.unique(),

             'P7': allLeaks.loc[allLeaks.POLYGON == "P7",].LEAKNUM.unique(),
             'P8': allLeaks.loc[allLeaks.POLYGON == "P8",].LEAKNUM.unique(),
             'P9': allLeaks.loc[allLeaks.POLYGON == "P9",].LEAKNUM.unique(),
             'P10': allLeaks.loc[allLeaks.POLYGON == "P10",].LEAKNUM.unique(),
             'P11': allLeaks.loc[allLeaks.POLYGON == "P11",].LEAKNUM.unique(),
             'P12': allLeaks.loc[allLeaks.POLYGON == "P12",].LEAKNUM.unique(),
             'P13': allLeaks.loc[allLeaks.POLYGON == "P13",].LEAKNUM.unique(),
             'P14': allLeaks.loc[allLeaks.POLYGON == "P14",].LEAKNUM.unique(),
             'P15': allLeaks.loc[allLeaks.POLYGON == "P15",].LEAKNUM.unique(),

             'P16': allLeaks.loc[allLeaks.POLYGON == "P16",].LEAKNUM.unique(),
             'P17': allLeaks.loc[allLeaks.POLYGON == "P17",].LEAKNUM.unique(),
             'P18': allLeaks.loc[allLeaks.POLYGON == "P18",].LEAKNUM.unique(),

             'P19': allLeaks.loc[allLeaks.POLYGON == "P19",].LEAKNUM.unique(),
             'P20': allLeaks.loc[allLeaks.POLYGON == "P20",].LEAKNUM.unique(),
             'P21': allLeaks.loc[allLeaks.POLYGON == "P21",].LEAKNUM.unique(),
             'P22': allLeaks.loc[allLeaks.POLYGON == "P22",].LEAKNUM.unique(),
             'P23': allLeaks.loc[allLeaks.POLYGON == "P23",].LEAKNUM.unique(),
             'P24': allLeaks.loc[allLeaks.POLYGON == "P24",].LEAKNUM.unique(),
             'P25': allLeaks.loc[allLeaks.POLYGON == "P25",].LEAKNUM.unique(),
             'P26': allLeaks.loc[allLeaks.POLYGON == "P26",].LEAKNUM.unique(),
             'P27': allLeaks.loc[allLeaks.POLYGON == "P27",].LEAKNUM.unique(),
             'P28': allLeaks.loc[allLeaks.POLYGON == "P28",].LEAKNUM.unique(),
             'P29': allLeaks.loc[allLeaks.POLYGON == "P29",].LEAKNUM.unique(),
             'P30': allLeaks.loc[allLeaks.POLYGON == "P30",].LEAKNUM.unique(),
             'P31': allLeaks.loc[allLeaks.POLYGON == "P31",].LEAKNUM.unique(),
             'P32': allLeaks.loc[allLeaks.POLYGON == "P32",].LEAKNUM.unique(),
             'P33': allLeaks.loc[allLeaks.POLYGON == "P33",].LEAKNUM.unique(),
             'P34': allLeaks.loc[allLeaks.POLYGON == "P34",].LEAKNUM.unique(),
             'P35': allLeaks.loc[allLeaks.POLYGON == "P35",].LEAKNUM.unique(),
             'P36': allLeaks.loc[allLeaks.POLYGON == "P36",].LEAKNUM.unique(),
             'P37': allLeaks.loc[allLeaks.POLYGON == "P37",].LEAKNUM.unique(),

             'P38': allLeaks.loc[allLeaks.POLYGON == "P38",].LEAKNUM.unique(),
             'P39': allLeaks.loc[allLeaks.POLYGON == "P39",].LEAKNUM.unique(),
             'P40': allLeaks.loc[allLeaks.POLYGON == "P40",].LEAKNUM.unique(),
             'P41': allLeaks.loc[allLeaks.POLYGON == "P41",].LEAKNUM.unique(),
             'P42': allLeaks.loc[allLeaks.POLYGON == "P42",].LEAKNUM.unique(),
             'P43': allLeaks.loc[allLeaks.POLYGON == "P43",].LEAKNUM.unique(),
             'P44': allLeaks.loc[allLeaks.POLYGON == "P44",].LEAKNUM.unique(),
             'P45': allLeaks.loc[allLeaks.POLYGON == "P45",].LEAKNUM.unique(),
             'P46': allLeaks.loc[allLeaks.POLYGON == "P46",].LEAKNUM.unique(),
             
             'P47': allLeaks.loc[allLeaks.POLYGON == "P47",].LEAKNUM.unique(),
             'P48': allLeaks.loc[allLeaks.POLYGON == "P48",].LEAKNUM.unique(),
             'P49': allLeaks.loc[allLeaks.POLYGON == "P49",].LEAKNUM.unique(),
             'P50': allLeaks.loc[allLeaks.POLYGON == "P50",].LEAKNUM.unique(),
             
             'P51': allLeaks.loc[allLeaks.POLYGON == "P51",].LEAKNUM.unique(),
             'P52': allLeaks.loc[allLeaks.POLYGON == "P52",].LEAKNUM.unique(),
             'P53': allLeaks.loc[allLeaks.POLYGON == "P53",].LEAKNUM.unique(),
             'P54': allLeaks.loc[allLeaks.POLYGON == "P54",].LEAKNUM.unique(),
             'P55': allLeaks.loc[allLeaks.POLYGON == "P55",].LEAKNUM.unique(),
             'P56': allLeaks.loc[allLeaks.POLYGON == "P56",].LEAKNUM.unique(),

             'P57': allLeaks.loc[allLeaks.POLYGON == "P57",].LEAKNUM.unique(),

             'P58': allLeaks.loc[allLeaks.POLYGON == "P58",].LEAKNUM.unique(),
             'P59': allLeaks.loc[allLeaks.POLYGON == "P59",].LEAKNUM.unique(),
             'P60': allLeaks.loc[allLeaks.POLYGON == "P60",].LEAKNUM.unique()

             }


gapSize = 10
gnameDict = {'P1':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P1',].portion.unique().size/gapSize)+1)),
             'P2':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P2',].portion.unique().size/gapSize)+1)),
             'P3':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P3',].portion.unique().size/gapSize)+1)),
             'P4':list(range(1,int(allGaps.loc[allGaps.POLYGON == 'P4',].portion.unique().size/gapSize)+1))             
             }


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
    ),
                        html.Div( [
    dcc.ConfirmDialogProvider(
        children=html.Button(
            'Confirm: Leak Checked',
            id = 'submit_button',
        ),
        id='danger-provider',
        message='Danger danger! Are you sure you want to continue?'
    ),
    html.Div(id='output-provider')
],className = 'dcc_control')

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
                        html.P("Choose Which Gap:", className="control_label"),
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
    ),
                                   html.Div( [
    dcc.ConfirmDialogProvider(
        children=html.Button(
            'Confirm: Gap Checked',
            id = 'submit_button2',
        ),
        id='danger-provider2',
        message='Danger danger! Are you sure you want to continue?'
    ),
    html.Div(id='output-provider2')
],className = 'dcc_control')


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
                                    '10.26.20', style={"margin-top": "0px"}
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
    usepoly2 = usepoly.loc[usepoly.portion == 1,:]
    if whichPolygon == 'P2':
        usepoly2 = usepoly.loc[usepoly.portion == 1,:]

    if whichPolygon == "P5" or whichPolygon == "P58" or whichPolygon == "P59" or whichPolygon == "P8" or whichPolygon == "P7" or whichPolygon == "P10" or whichPolygon == "P11":
        usepoly2 = usepoly.loc[usepoly.portion == 1,:]
    if whichPolygon == "P23":
        usepoly2 = usepoly.loc[usepoly.portion == 3,:]

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
    
    if usegapsmall.loc[:,'multiple'].reset_index(drop=True)[0] == True:
        firstgapsmall = usegapsmall.loc[usegapsmall.subportion == 1,]
        secgapsmall = usegapsmall.loc[usegapsmall.subportion == 2,]

        #usepoly = allPoly.loc[allPoly.POLYGON == whichPolygon,:]
        #usepoly2 = usepoly.loc[usepoly.portion == 3,:]
        if whichMap == "sat":
            color_discrete_lks = color_discrete_map_st
        elif whichMap != 'sat':
            color_discrete_lks = color_discrete_map_st
        fig = px.line_mapbox(firstgapsmall,
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
        fig.add_trace(
                 px.line_mapbox(secgapsmall,
                     lon = 'lon',
                     lat = 'lat',
                     zoom = 14,
                     color = 'POLYGON',
                     color_discrete_map=color_discrete_lks,
                     width = 50,
                     hover_data = {'portion'}

                     ).data[0],
                 ) 
        fig.update_traces(line=dict(width=6))
        
    elif usegapsmall.loc[:,'multiple'].reset_index(drop=True)[0] == False:    
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
    dat = allLeaks.loc[allLeaks.POLYGON==str(whichPolygon),]
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
    #num = len(gapsDict[whichPolygon])
    num = allGaps.loc[allGaps.POLYGON == whichPolygon,:].portion.drop_duplicates().shape[0]
    return "Number of Gaps: " + str(num)

    

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


    
@app.callback(
    dash.dependencies.Output('danger-provider', 'message'),
    [dash.dependencies.Input('whichPoly', 'value'),
     dash.dependencies.Input('opt-dropdown', 'value')
     ]
    )
def whichDanger(polygon,leak):
    if not polygon or not leak:
        return (str("Please Choose a Polygon and Leak"))
    return(str("Confirm: I checked Leak Number: " + str(leak) + ' in Polygon ' + str(polygon[1:])))
    #return('hi')
    #return({'message':'hi'})
    
@app.callback(
    dash.dependencies.Output('danger-provider2', 'message'),
    [dash.dependencies.Input('whichPolyGap', 'value'),
     dash.dependencies.Input('whichGapPack', 'value')
     ]
    )
def whichDanger2(polygon,gap):
    if not polygon or not gap:
        return (str("Please Choose a Polygon and Gap"))
    
    return(str("Confirm: I checked Gap Number: " + str(gap) + ' in Polygon ' + str(polygon[1:])))
    #return('hi')
    #return({'message':'hi'})
    
    
@app.callback(dash.dependencies.Output('output-provider', 'children'),
              [dash.dependencies.Input('danger-provider', 'submit_n_clicks'),
                dash.dependencies.Input('whichPoly', 'value'),
                dash.dependencies.Input('opt-dropdown', 'value')])
def update_output(submit_n_clicks,whichPoly,whichLeak):
     if not submit_n_clicks:
         return ''
#     whichDone = allLeaks.loc[(allLeaks.LEAKNUM == whichLeak )& (allLeaks.POLYGON == whichPoly),:]
#     whichDonePull = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/leakLog.csv')
#     curdate = datetime.utcnow().strftime("%m-%d-%y")
#     curtime = datetime.utcnow().strftime("%H:%M:%S")
#     d = {'Date': [curdate],'Time': [curtime], 'Polygon':[whichDone.POLYGON[0]], 'LeakNumber':[whichDone.LEAKNUM[0]], 'LeakID':[whichDone.PolyLK[0]], 'geometry': [whichDone.geometry[0]]}
#     df = pd.DataFrame(data=d)
#     whichDonePush = whichDonePull.append(df).reset_index().loc[:,['Date','Time','Polygon','LeakNumber','LeakID','geometry']]
#     whichDonePush.to_csv()

     return """
         Leak Check Confirmed 
     """.format(submit_n_clicks)
     
@app.callback(dash.dependencies.Output('output-provider2', 'children'),
              [dash.dependencies.Input('danger-provider2', 'submit_n_clicks'),
                dash.dependencies.Input('whichPolyGap', 'value'),
                dash.dependencies.Input('whichGapPack', 'value')])
def update_output2(submit_n_clicks,whichPoly,whichLeak):
     if not submit_n_clicks:
         return ''
#     whichDone = allLeaks.loc[(allLeaks.LEAKNUM == whichLeak )& (allLeaks.POLYGON == whichPoly),:]
#     whichDonePull = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/Trussville/master/leakLog.csv')
#     curdate = datetime.utcnow().strftime("%m-%d-%y")
#     curtime = datetime.utcnow().strftime("%H:%M:%S")
#     d = {'Date': [curdate],'Time': [curtime], 'Polygon':[whichDone.POLYGON[0]], 'LeakNumber':[whichDone.LEAKNUM[0]], 'LeakID':[whichDone.PolyLK[0]], 'geometry': [whichDone.geometry[0]]}
#     df = pd.DataFrame(data=d)
#     whichDonePush = whichDonePull.append(df).reset_index().loc[:,['Date','Time','Polygon','LeakNumber','LeakID','geometry']]
#     whichDonePush.to_csv()

     return """
         Gap Check Confirmed 
     """.format(submit_n_clicks)
     
@app.callback(dash.dependencies.Output('danger-provider', 'submit_n_clicks'),
              [dash.dependencies.Input('whichPoly', 'value'),
                dash.dependencies.Input('opt-dropdown', 'value')])
def updateSubmit(whichPoly,whichLeak):
     return 0 
     
@app.callback(dash.dependencies.Output('danger-provider2', 'submit_n_clicks'),
              [dash.dependencies.Input('whichPolyGap', 'value'),
                dash.dependencies.Input('whichGapPack', 'value')])
def updateSubmit2(whichPoly,whichGap):
     return 0 

if __name__ == '__main__':
    app.run_server(debug=False)



                
