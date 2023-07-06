import dash
from dash import Dash, html, dcc, callback, Output, Input ,Dash, dash_table, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

import plotly.graph_objects as go


# 讀檔區 
df = pd.read_csv('elden_ring_weapon.csv')
PLOTLY_LOGO = "./wendyCoin.png"

#主題選擇區
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])

#連結設定
nav_item = dbc.NavItem(
				dbc.NavLink("DATASET來源", 
							style={	'font-size': '2rem',
									'line-height': '1.2',
									'color': 'white',
									},
							href="https://www.kaggle.com/datasets/l3llff/-elden-ring-weapons"),
							)

#下拉選單
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("ELDEN RING STEAM",href="https://store.steampowered.com/app/1245620/_/"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("ELDEN RING WIKI",href="https://eldenring.wiki.fextralife.com/Elden+Ring+Wiki"),
		dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("ELDEN RING 哈啦 精華區",href="https://forum.gamer.com.tw/G1.php?bsn=36726"),
		dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("武器中英對照",href="https://home.gamer.com.tw/artwork.php?sn=5416196"),
	],
    nav=True,
    in_navbar=True,
    label="攻略",
	style={	'font-size': '2rem',
			'line-height': '1.2',
			'color': '#1d2951',
			"background": "#713cc8",
			},
)


#標題BAR & LOGO
logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                    dbc.Col(html.Img(src="assets/wendyCoin.png" ,height="60px")),
                    dbc.Col(
						dbc.NavbarBrand("Elden Ring Weapon - Data Analysis and Visualization",
										className="ms-2",
										style={	'font-size': '3rem',
												'line-height': '1.2',
												'letter-spacing': '-0.1rem',
												'margin-bottom': '2rem',
												},
										)),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="http://127.0.0.1:8888/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(	id="navbar-toggler2", 
								n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, dropdown],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="#624a89",
    dark=True,
    className="mb-5",
)

#武器表格設定
weaponDataTable = dmc.Grid([
		dmc.Col(
		[
			dash_table.DataTable(data=df.to_dict('records'), 
			page_size=15,
			style_table={'overflowX':'auto'},
			style_cell={'textAlign': 'left',
									  'min-width': '100px',
									  'backgroundColor': '#624a89',
									  'color': '#FEFEFE',
									  'border-bottom': '0.01rem solid #19AAE1',
									  },
			style_as_list_view = True,
			style_data = {'textOverflow': 'hidden','color': 'white'},
			),
		]),
])

#互動式選單	
chooseBarChart=dcc.RadioItems(	
							id = 'my-dmc-radio-item',
							labelStyle = {"display": "inline-block"},
							value = "Phy",
							options = ["Phy","Mag","Sta","Wgt"],
							style = {'text-align': 'center', 'color': 'white',},
							className = 'dcc_compon')


choosePieChart=dcc.RadioItems(	
							id = 'names',
							labelStyle = {"display": "inline-block"},
							value = "Type",
							options = ['Type', 'Upgrade'],
							style = {'text-align': 'center', 'color': 'white',},
							className = 'dcc_compon')

#長條圖繪圖設定		
drawBarChart=dmc.Grid(
		[dmc.Col([
			dcc.Graph(	figure={}, 
						id ='graph-placeholder',
						style={'height':'500px',},
						)
		]),
	])


#頁面組合區
app.layout = html.Div([
    
	#資料行表格
	html.Div([
		logo,
		html.Div(['WEAPONs',],
					style = {	'textAlign': 'center',
								'color': '#1d1724',
								'font-size': '2rem',
								'font-weight':'bold',
								},
				className="ms-2",
			),
		weaponDataTable,
	]),
	
	#第一列
	html.Div([
		
		#縮寫文字文字備註
		html.Div([
			html.Div(['縮寫備註',],
					style = {	'textAlign': 'center',
								'color': 'white',
								'font-size': '2rem',
								'font-family':'Microsoft JhengHei',
								'font-weight':'bold',
								},
				className="ms-2",
			),
			html.Div(
				children = ['Name - name of weapon'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Type - type of weapon'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Phy - physical damage'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Mag - magical damage'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Fir - fire damage'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Lit - light damage'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Hol - holy damage'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Cri - critical damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Sta - stamina usage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Str - strength scaling',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Dex - dexterity scaling'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Int - intelligence scaling',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Fai - faith scaling',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Arc - arcane scaling',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Any - special effect damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['PhyB - physical blocking damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['MagB - magical blocking damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['FirB - fire blocking damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['LitB - light blocking damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['HolB - holy blocking damage',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Bst - boost',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Wgt - wight of weapon',],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),
			html.Div(
				children = ['Upgrade - stone use to upgrade the weapon'],
				style = {	'textAlign': 'center',
							'color': 'white'}
			),

		], className = 'create_container2',
		style={'width':'19.5%'},
		),
		#長條圖(X:武器種類&Y:平均值)
		html.Div([
			html.Div(['長條圖',],
					style = {	'textAlign': 'center',
								'color': 'white',
								'font-size': '2rem',
								'font-family':'Microsoft JhengHei',
								'font-weight':'bold',
								},
				className="ms-2",
			),
			chooseBarChart,
			drawBarChart,
			],	className = 'create_container2',
				style={'width':'38.5%',
				},
		),
		#圓餅圖(武器種類/升級素材 百分比)
		html.Div([
			html.Div(['圓餅圖'],
					style = {	'textAlign': 'center',
								'color': 'white',
								'font-size': '2rem',
								'font-family':'Microsoft JhengHei',
								'font-weight':'bold',
								},
				className="ms-2",
			),
			choosePieChart,
			dcc.Graph(	id="graph",
					style={'height':'500px'}
				),
			],	className = 'create_container2',
				style={'width':'38.5%'},
		),

	],className="row flex-display"),
	
	#第二列
	html.Div([
		#泡泡圖(PHY)
		html.Div([
			html.Div(['各武器物理攻擊對應各類型武器重量分析',],
				style = {	'textAlign': 'center',
							'color': 'white',
							'font-size': '2rem',
							'font-family':'Microsoft JhengHei',
							'font-weight':'bold',
							},
			className="ms-2",
			),
			dcc.Graph(id = 'bubble_chart',
				  config = {'displayModeBar': 'hover'}),
		], 	className = 'create_container2',
			style={'width':'40%'}
		),
		#武器種類選擇
		html.Div([
			html.Div(['武器種類選擇',],
					style = {	'textAlign': 'center',
								'color': 'white',
								'font-size': '2rem',
								'font-family':'Microsoft JhengHei',
								'font-weight':'bold',
								},
				className="ms-2",
			),
			dcc.RadioItems(	id = 'radio_items',
					labelStyle = {"display": "inline-block"},
					value = 'Greatsword',
					options = [{'label': i,'value': i} for i in df['Type'].unique()],
					style = {'text-align': 'center', 'color': 'white','margin-top':'2rem'},
					className = 'dcc_compon',
					),
		],className = 'create_container2',
			style={'width':'16.5%'}
		),
		#泡泡圖MAG
		html.Div([
			html.Div(['各武器魔法攻擊對應各類型武器重量分析',],
				style = {	'textAlign': 'center',
							'color': 'white',
							'font-size': '2rem',
							'font-family':'Microsoft JhengHei',
							'font-weight':'bold',
							},
			className="ms-2",
			),
			dcc.Graph(id = 'bubble_chart2',
				  config = {'displayModeBar': 'hover'}),
		], 	className = 'create_container2',
			style={'width':'40%'}
		),
		
		],	
		className = 'row flex-display',
		
	),
	
],style={'background':"#decef2",})


#繪製長條圖
@callback(
	Output(	component_id = 'graph-placeholder', 
			component_property ='figure'),
	Input(	component_id ='my-dmc-radio-item', 
			component_property ='value')
	)
def update_graph(col_chosen):
	fig1= px.histogram(df ,	x='Type', 
							y=col_chosen , 
							histfunc ='avg'
							)
	# fig1.update_xaxes(nticks=33)

	return fig1
	
#繪製圓餅圖
@app.callback(
    Output("graph", "figure"), 
    Input("names", "value"))
def generate_chart(names): 
    fig2 = px.pie(df, names=names, hole=.3)
    return fig2
#泡泡圖(PHY)
@app.callback(Output('bubble_chart', 'figure'),
			[Input('radio_items', 'value')])
def update_graph(radio_items):
	Info = df.groupby(['Name', 'Type', 'Phy', 'Mag'])['Wgt'].sum().reset_index()
	bubble = Info[(Info['Type'] == radio_items)]

	return {
		'data': [go.Scatter(
			x = bubble['Wgt'],
			y = bubble['Phy'],
			mode = 'markers',
			marker = dict(
				size = bubble['Wgt']*8,
				color = bubble['Wgt'],
				colorscale = 'HSV',
				showscale = False,
				line = dict(
					color = 'MediumPurple',
					width = 2
				)),
			hoverinfo = 'text',
			hovertext =
			'<b>Name</b>: ' + bubble['Name'].astype(str) + '<br>' +
			'<b>Type</b>: ' + bubble['Type'].astype(str) + '<br>' +
			'<b>Phy</b>: ' + bubble['Phy'].astype(str) + '<br>' +
			'<b>Mag</b>: ' + bubble['Mag'].astype(str) + '<br>' +
			'<b>Wgt</b>: ' + bubble['Wgt'].astype(str) + '<br>'

		)],

		'layout': go.Layout(
			plot_bgcolor = '#efe6f9',
			paper_bgcolor = '#efe6f9',
			title = {
				'y': 0.99,
				'x': 0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			titlefont = {
				'color': 'white',
				'size': 15},
			margin = dict(t = 40, r = 0, l = 0),

			hovermode = 'closest',

			xaxis = dict(title = '<b>Wgt</b>',
						 color = '#966fd6',
						 gridcolor='white',
						 linewidth = 1,
						 ticks = '',
						 tickfont = dict(
							 family = 'Arial',
							 size = 12,
							 color = '#966fd6')
						 ),

			yaxis = dict(title = '<b>Phy</b>',
						 color = '#966fd6',
						 gridcolor='white',
						 linewidth = 1,
						 ticks = '',
						 tickfont = dict(
							 family = 'Arial',
							 size = 12,
							 color = '#966fd6')
						 ),

			legend = {
				'orientation': 'h',
				'bgcolor': 'white',
				'x': 0.5,
				'y': 0.7,
				'xanchor': 'center',
				'yanchor': 'top'},

			font = dict(
				family = "sans-serif",
				size = 12,
				color = 'white'),
		)
	}
#泡泡圖(MAG)
@app.callback(Output('bubble_chart2', 'figure'),
			[Input('radio_items', 'value')])
def update_graph(radio_items):
	Info = df.groupby(['Name', 'Type', 'Phy', 'Mag'])['Wgt'].sum().reset_index()
	bubble = Info[(Info['Type'] == radio_items)]

	return {
		'data': [go.Scatter(
			x = bubble['Wgt'],
			y = bubble['Mag'],
			mode = 'markers',
			marker = dict(
				size = bubble['Wgt']*8,
				color = bubble['Wgt'],
				colorscale = 'HSV',
				showscale = False,
				line = dict(
					color = 'MediumPurple',
					width = 2
				)),
			hoverinfo = 'text',
			hovertext =
			'<b>Name</b>: ' + bubble['Name'].astype(str) + '<br>' +
			'<b>Type</b>: ' + bubble['Type'].astype(str) + '<br>' +
			'<b>Phy</b>: ' + bubble['Phy'].astype(str) + '<br>' +
			'<b>Mag</b>: ' + bubble['Mag'].astype(str) + '<br>' +
			'<b>Wgt</b>: ' + bubble['Wgt'].astype(str) + '<br>'

		)],

		'layout': go.Layout(
			plot_bgcolor = '#efe6f9',
			paper_bgcolor = '#efe6f9',
			title = {
				'y': 0.99,
				'x': 0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			titlefont = {
				'color': 'white',
				'size': 15},
			margin = dict(t = 40, r = 0, l = 0),

			hovermode = 'closest',

			xaxis = dict(title = '<b>Wgt</b>',
						 color = '#966fd6',
						 gridcolor='white',
						 linewidth = 1,
						 ticks = '',
						 tickfont = dict(
							 family = 'Arial',
							 size = 12,
							 color = '#966fd6')
						 ),

			yaxis = dict(title = '<b>Mag</b>',
						 color = '#966fd6',
						 gridcolor='white',
						 linewidth = 1,
						 ticks = '',
						 tickfont = dict(
							 family = 'Arial',
							 size = 12,
							 color = '#966fd6')
						 ),

			legend = {
				'orientation': 'h',
				'bgcolor': 'white',
				'x': 0.5,
				'y': 0.7,
				'xanchor': 'center',
				'yanchor': 'top'},

			font = dict(
				family = "sans-serif",
				size = 12,
				color = 'white'),
		)
	}
if __name__ == "__main__":
	app.run_server(debug=True, port=8888)
