from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import os

def create_dash_app():
    """Create and configure Dash application."""
    app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
    
    # Load cleaned data
    df = pd.read_csv('data/cleaned_sales_data.csv', parse_dates=['Date'])
    
    # Define custom styles for the tricolor theme
    header_style = {"backgroundColor": "#FF9933", "color": "white", "padding": "10px"}
    white_style = {"backgroundColor": "white", "color": "black", "padding": "10px"}
    green_style = {"backgroundColor": "#138808", "color": "white", "padding": "10px"}

    app.layout = dbc.Container([
        # Header: Saffron background
        dbc.Row([
            dbc.Col(html.H1("Retail Sales Analytics Dashboard", 
                            className="text-center mb-4", 
                            style={"color": "white"}), 
                    width=12, 
                    style=header_style)
        ]),
        
        # Filters: White background
        dbc.Row([
            dbc.Col([
                dcc.DatePickerRange(
                    id='date-range',
                    start_date=df['Date'].min(),
                    end_date=df['Date'].max(),
                    display_format='YYYY-MM-DD'
                )
            ], width=3),
            dbc.Col([
                dcc.Dropdown(
                    id='city-select',
                    options=[{'label': city, 'value': city} for city in df['City'].unique()],
                    multi=True,
                    placeholder='Select Cities'
                )
            ], width=3),
            dbc.Col([
                dcc.Dropdown(
                    id='product-select',
                    options=[{'label': product, 'value': product} for product in df['Product line'].unique()],
                    multi=True,
                    placeholder='Select Product Lines'
                )
            ], width=3),
            dbc.Col([
                dcc.Dropdown(
                    id='gender-select',
                    options=[{'label': gender, 'value': gender} for gender in df['Gender'].unique()],
                    multi=True,
                    placeholder='Select Genders'
                )
            ], width=3)
        ], className="mb-4", style=white_style),
        
        # Key Metrics: Green background
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Total Sales", className="card-title"),
                        html.H4(id='total-sales', className="card-text")
                    ])
                ], style=green_style)
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Gross Income", className="card-title"),
                        html.H4(id='gross-income', className="card-text")
                    ])
                ], style=green_style)
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Total Quantity", className="card-title"),
                        html.H4(id='total-quantity', className="card-text")
                    ])
                ], style=green_style)
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Avg Rating", className="card-title"),
                        html.H4(id='avg-rating', className="card-text")
                    ])
                ], style=green_style)
            ], width=3)
        ], className="mb-4"),
        
        # Visualizations
        dbc.Row([
            dbc.Col(dcc.Graph(id='sales-trend'), width=6),
            dbc.Col(dcc.Graph(id='product-performance'), width=6)
        ], className="mb-4", style=white_style),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='payment-method'), width=4),
            dbc.Col(dcc.Graph(id='customer-type'), width=4),
            dbc.Col(dcc.Graph(id='hourly-sales'), width=4)
        ], className="mb-4", style=white_style),
        
        # Export Section: Green background
        dbc.Row([
            dbc.Col([
                html.Button("Export Filtered Data", id='export-btn', className="btn btn-primary"),
                html.Div(id='export-status', className="mt-2")
            ], width=12, style=green_style)
        ]),
        
        dcc.Store(id='filtered-data')
    ], fluid=True)

    @app.callback(
        [Output('total-sales', 'children'),
        Output('gross-income', 'children'),
        Output('total-quantity', 'children'),
        Output('avg-rating', 'children'),
        Output('filtered-data', 'data')],
        [Input('date-range', 'start_date'),
        Input('date-range', 'end_date'),
        Input('city-select', 'value'),
        Input('product-select', 'value'),
        Input('gender-select', 'value')]
    )
    def update_metrics(start_date, end_date, cities, products, genders):
        filtered_df = df.copy()
        
        # Apply filters
        filtered_df = filtered_df[(filtered_df['Date'] >= start_date) & 
                                (filtered_df['Date'] <= end_date)]
        if cities:
            filtered_df = filtered_df[filtered_df['City'].isin(cities)]
        if products:
            filtered_df = filtered_df[filtered_df['Product line'].isin(products)]
        if genders:
            filtered_df = filtered_df[filtered_df['Gender'].isin(genders)]
        
        # Calculate metrics
        total_sales = filtered_df['Total'].sum()
        gross_income = filtered_df['gross income'].sum()
        total_quantity = filtered_df['Quantity'].sum()
        avg_rating = filtered_df['Rating'].mean()
        
        return (
            f"${total_sales:,.2f}",
            f"${gross_income:,.2f}",
            f"{total_quantity:,}",
            f"{avg_rating:.1f}/10",
            filtered_df.to_json(date_format='iso', orient='split')
        )

    @app.callback(
        [Output('sales-trend', 'figure'),
        Output('product-performance', 'figure'),
        Output('payment-method', 'figure'),
        Output('customer-type', 'figure'),
        Output('hourly-sales', 'figure')],
        [Input('filtered-data', 'data')]
    )
    def update_visualizations(data):
        filtered_df = pd.read_json(data, orient='split')
        
        # Sales Trend
        sales_trend = filtered_df.groupby('Date')['Total'].sum().reset_index()
        trend_fig = px.line(sales_trend, x='Date', y='Total', 
                        title='Daily Sales Trend', 
                        labels={'Total': 'Total Sales ($)'})
        
        # Product Performance
        product_perf = filtered_df.groupby('Product line')['Total'].sum().reset_index()
        product_fig = px.bar(product_perf, x='Product line', y='Total', 
                            title='Sales by Product Line',
                            labels={'Total': 'Total Sales ($)'})
        
        # Payment Method Distribution
        payment_fig = px.pie(filtered_df, names='Payment', 
                            title='Payment Method Distribution',
                            hole=0.4)
        
        # Customer Type Analysis
        customer_fig = px.histogram(filtered_df, x='Customer type', color='Gender',
                                title='Customer Type Distribution by Gender',
                                barmode='group')
        
        # Hourly Sales Pattern
        hourly_sales = filtered_df.groupby('Hour')['Total'].sum().reset_index()
        hourly_fig = px.area(hourly_sales, x='Hour', y='Total',
                            title='Hourly Sales Pattern',
                            labels={'Total': 'Total Sales ($)'})
        
        return trend_fig, product_fig, payment_fig, customer_fig, hourly_fig

    @app.callback(
        Output('export-status', 'children'),
        [Input('export-btn', 'n_clicks')],
        [State('filtered-data', 'data')]
    )
    def export_data(n_clicks, data):
        if n_clicks:
            filtered_df = pd.read_json(data, orient='split')
            filtered_df.to_csv('outputs/exported_data.csv', index=False)
            return "Data exported to outputs/exported_data.csv"
        return ""

    return app
