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
import dash_html_components as htmllast
import requests 
import plotly.io as pio
#from datetime import date
#today = date.today()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/header2.css'  ,
                        'https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css'
                        ]
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')

allPoly = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/spire_audits/master/allPoly.csv')
allGaps = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/spire_audits/master/allGaps.csv')
allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/spire_audits/master/allLeaksWin.csv')
#allLeaks = pd.read_csv('https://raw.githubusercontent.com/elimywilliams/spire_audits/master/polygon3_h/allLeaksWin.csv')

#### CREATING A LIST OF THE POLYGONS THAT HAVE BEEN CHECKED
checked = []
for x in range(0,len(allGaps.POLYGON.unique())):
    checked.append(allGaps.POLYGON.unique()[x])

whichMapOPTS = [
    {'label':'Satellite Map','value':'sat'},
    {'label':'Street Map', 'value':'street'}
       
    ]

polyLkOPTS = [
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
    {'label':'Polygon 18','value':"P18"}
    ]

polyOPTS = [{'label':str('Polygon ') + str(x),'value':str('P')+str(x)} for x in list(range(3,18+1))]


fnameDict = {
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
             'P18': allLeaks.loc[allLeaks.POLYGON == "P18",].LEAKNUM.unique()

             }

gsizeDict = {}
for x in checked:
    gsizeDict[x] = allGaps.loc[allGaps.POLYGON==x,].portion.unique().size

color_discrete_map_st = {}
for x in list(range(3,18+1)):
    color_discrete_map_st[str("P") + str(x)] = 'rgb(255,0,0)'

color_discrete_lks_st = {}
for x in list(range(3,18+1)):
    color_discrete_lks_st[str("P") + str(x)] = 'rgb(255,255,255)'

color_discrete_lks_ns = {}
for x in list(range(3,18+1)):
    color_discrete_lks_ns[str("P") + str(x)] = 'rgb(0, 0, 99)'
 

tab1=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Polygon:", className="control_label"),
                       dcc.Dropdown(
                            id="whichPoly",
                            options = polyOPTS,
                            value = 'P3',
                            className="dcc_control",
                        ),
                        html.P("Choose Leak Number:", className="control_label"),
                        dcc.Dropdown(
                            id='opt-dropdown',
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
                html.Div(
                    [dcc.Graph(id='hover-data-plot')],
                    className="pretty_container five columns"),
            ],
            className="row flex-display",
        ),
        html.Div(
             [
                 html.Div(id='hover-data-info',
                     className="pretty_container seven columns",
                 ),

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
                            options = polyLkOPTS,
                            value = 'P3',
                            className="dcc_control",
                        ),
                        html.P("Choose Which Gap:", className="control_label"),
                        dcc.Dropdown(
                            id="whichGapPack",
                            options=[],
                            className="dcc_control",
                        ),
                        dcc.RadioItems(
                            id="whichMapGap",
                            options=whichMapOPTS,
                            value="sat",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ), html.A(html.Button('Get Route'),
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

                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Southern Cross Audits",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Spire, AL", style={"margin-top": "0px"}
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
                                    '1.28.21', style={"margin-top": "0px"}
                                ),
                              dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
                                  dcc.Tab(id="tab-1", label='Leak Indications', value='tab-1-example'),
                                  dcc.Tab(id="tab-2", label='Gaps', value='tab-2-example')
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
    #if whichPolygon == 'P2':
    #    usepoly2 = usepoly.loc[usepoly.portion == 1,:]

    #if whichPolygon == "P5" or whichPolygon == "P58" or whichPolygon == "P59" or whichPolygon == "P8" or whichPolygon == "P7" or whichPolygon == "P10" or whichPolygon == "P11":
    #    usepoly2 = usepoly.loc[usepoly.portion == 1,:]
    #if whichPolygon == "P23":
    #    usepoly2 = usepoly.loc[usepoly.portion == 3,:]

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
    return options


@app.callback(dash.dependencies.Output('gapGraph', 'figure'),
              [dash.dependencies.Input('whichPolyGap', 'value'),
               dash.dependencies.Input('whichMapGap', 'value'),
               dash.dependencies.Input('whichGapPack','value')
               
               ]
              )
def newGapGraph(whichPolygon,whichMap,whichGapPack):
    usegap = allGaps.loc[allGaps.POLYGON == whichPolygon,:]
    usegapsmall = usegap.loc[usegap['portion']== whichGapPack,:]
    
    if usegapsmall.loc[:,'multiple'].reset_index(drop=True)[0] == True:
        firstgapsmall = usegapsmall.loc[usegapsmall.subportion == 1,]
        secgapsmall = usegapsmall.loc[usegapsmall.subportion == 2,]

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
     
     if whichLeak == []:
        return []
     
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



                
