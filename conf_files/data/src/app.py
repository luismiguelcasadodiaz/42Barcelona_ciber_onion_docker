import dash
import dash_bootstrap_components as dbc
import base64
import io
import param
import plotly.express as px
import pandas as pd
import sizes



myempresa, myfinca, myparcela, myfruta, myvariedad, mymindiacon, mybinsize = "Una empresa", "Una finca", "una parcela","Una fruta", "una variedad", 50, 5

mysizes = sizes.Sizes(pd.DataFrame({'diameter' : [1,2,3,4,5]}))
mysizes.set_comercial(param.default_comercial_dim)
mysizes.set_bin_width(param.default_bin_size)

app= dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

@app.callback(dash.Output('output-medidas', 'children'),
              dash.Input('medidas', 'filename'),
              dash.State('medidas', 'contents'))
              #dash.State('medidas', 'last_modified'))
def update_output(filename, contents):
    global mysizes
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            
                mysizes = sizes.Sizes(df)
                mysizes.set_comercial(param.default_comercial_dim)
                mysizes.set_bin_width(param.default_bin_size)
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
                mysizes = sizes.Sizes(df)
                mysizes.set_comercial(param.default_comercial_dim)
                mysizes.set_bin_width(param.default_bin_size)
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
  
    return filename

@app.callback(
    dash.Output("parametros", "children"),
    dash.Output("dashtitle", "children"),
    dash.Input("empresa", "value"),
    dash.Input("finca", "value"),
    dash.Input("parcela", "value"),
    dash.Input("fruta", "value"),
    dash.Input("variedad", "value"),
    dash.Input("mindiacom", "value"),
    dash.Input("binsize", "value"),
)
def parametros(empresa, finca, parcela, fruta, variedad, mindiacon, binsize):
    global myempresa
    global myfinca
    global myparcela
    global myfruta
    global myvariedad
    global mymindiacon
    global mybinsize
    myempresa, myfinca, myparcela, myfruta, myvariedad, mymindiacon, mybinsize = empresa, finca, parcela, fruta, variedad, mindiacon, binsize
    texto = "La parcela {2} de la finca {1} de la empresa {0} tiene {3} de la variedad {4}. Su calibre comercial es {5}. Clasificamos en cajones de tamaño {6}mm.".format(empresa, finca, parcela, fruta, variedad, mindiacon, binsize)
    return texto, texto

@app.callback(dash.Output('chart1','figure'),
              dash.Input('medidas','filename'),
              dash.Input('botonaceptar','n_clicks')
              )
def chart1(filename,n_clicks):
    fig=mysizes.chart_scatter()
    return fig
@app.callback(dash.Output('chart2','figure'),
              dash.Input('medidas','filename'),
              dash.Input('botonaceptar','n_clicks')
              )
def chart2(filename,n_clicks):
    fig=mysizes.chart_histogram()
    return fig
@app.callback(dash.Output('chart3','figure'),
              dash.Input('medidas','filename'),
              dash.Input('botonaceptar','n_clicks')
              )
def chart3(filename,n_clicks):
    fig=mysizes.chart_violin_bins('distance')
    return fig
"""
@app.callback(dash.Input('mindiacom','value'),
              dash.Input('botonaceptar','n_clicks')
            )
def change_com_dim(newdim,n_clicks):
    mysizes.set_comercial(newdim)
"""
selector = dash.html.Div([
    dbc.Row(
        [
        dash.html.H5(children="PARAMETROS",
                     style={'margin-top': '5px', 'margin-left': '2px'})
        ],className='bg-primary text-white font-italic'
    ),
    dbc.Row(
        [
        dash.html.Div(
            [
            dash.html.I(children="Empresa"),
            dash.html.Br(),
            dash.dcc.Input(id="empresa", type="text", placeholder="Nombre empresa",debounce=True,
                           style={'width':'100%'})
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Finca"),
            dash.html.Br(),
            dash.dcc.Input(id="finca", type="text", placeholder="Nombre finca",
                           style={'width':'100%'})
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Código parcela"),
            dash.html.Br(),
            dash.dcc.Input(id="parcela", type="text", placeholder="Código parcela",
                           style={'width':'100%'})
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Fruta"),
            dash.html.Br(),
            dash.dcc.Dropdown(id="fruta", options=param.frutas,optionHeight=15, placeholder="Fruta")
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Variedad"),
            dash.html.Br(),
            dash.dcc.Input(id="variedad", type="text", placeholder="Variedad",
                           style={'width':'100%'})
            ]
            ),

        dash.html.Div(
            [
            dash.html.I(children="Fichero de medidas"),
            dash.html.Br(),
            dash.dcc.Upload(id="medidas",
                            children=dash.html.Div(['Drag and drop ',dash.html.Br(),'or ', 
                                                    dash.html.A('Seleccionar Archivo')]
                                                ),
                            accept=".csv",
                            multiple=False,
                            style={ 'width': '130px',
                                    'height': '60px',
                                    'lineHeight': '2LO de los otros 0px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin': '0px',
                                    'font-size':'10px'}

                            ),
            dash.html.P(id='output-medidas',
                        style={'width':'100%','font-size':'10px','textAlign': 'center'})
            ]
        ),
        dash.html.Div(
            [
            dash.html.I(children="Diámetro comercial"),
            dash.html.Br(),
            dash.dcc.Slider(id="mindiacom", min=0, max=100, step = 1, value = param.default_comercial_dim, marks = None, tooltip={"placement":"left","always_visible": True})
            ]
            ),
        dash.html.Div(
            [
            dash.html.I(children="Tamaño Cajón"),
            dash.html.Br(),
            dash.dcc.Slider(id="binsize", min=2, max=15, step = 1, value =param.default_bin_size, marks = None, tooltip={"placement":"left","always_visible": True})
            ],
                           style={'width':'100%'}
            ),
        dash.html.Hr(),
        dash.html.P(id="parametros",children="vacio",
                           style={'width':'100%'})       
        ]
    ),
    dbc.Row(
        [
        dash.html.Hr(),
        dash.html.Button(id='botonaceptar',children='Analizar',n_clicks=0,
                         style={'width': '100%'})
        ]
    )
])

graficos = dash.html.Div(
    [
        dbc.Row(
            [
                dash.html.H5(id='dashtitle',
                             children=parametros(myempresa, myfinca, myparcela, myfruta, myvariedad, mymindiacon, mybinsize),
                             className='font-weight-bold')
            ],style={'height':'10%','text-align':'center'}),
        dbc.Row(
            [
                dbc.Col(
                    [

                        dash.dcc.Graph(id='chart1',
                                       figure=chart1('filename','n_clicks'),
                                       className='bg-Light')
                    ]),
                dbc.Col(
                    [

                        dash.dcc.Graph(id='chart2',
                                       figure=chart2('filename','n_clicks'),
                                       className='bg-Light')
    
                    ])
            ],style={'height':'45%'}),
        dbc.Row(
            [
                
                dash.dcc.Graph(id='chart3',
                                       figure=chart3('filename','n_clicks'),
                                       className='bg-Light')
            ],style={'height':'45%'})
])

app.layout = dbc.Container(
    [
    dbc.Row(
        [
        dbc.Col(selector, width=1),
        dbc.Col(graficos, width=11)
        ]
        )
    ],
    fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=True, port=1234)