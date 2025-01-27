import os
import pandas as pd
from scripts.load_and_preprocess_data import load_and_preprocess_data
from scripts.analysis import analyze_data
import matplotlib.pyplot as plt
import seaborn as sns

def create_and_save_visualizations(df, output_dir):
    """
    Generate static visualizations and save them to the specified directory.
    Args:
        df (pd.DataFrame): Cleaned sales data.
        output_dir (str): Directory to save the visualizations.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Sales Trend Over Time
    sales_trend = df.groupby('Date')['Total'].sum()
    plt.figure(figsize=(12, 6))
    sales_trend.plot(title='Sales Trend Over Time', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.grid(True)
    sales_trend_path = os.path.join(output_dir, 'sales_trend_over_time.png')
    plt.savefig(sales_trend_path)
    print(f"Saved: {sales_trend_path}")
    plt.close()

    # Heatmap of Sales by Region and Product Line
    region_product_sales = df.pivot_table(index='City', columns='Product line', values='Total', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(region_product_sales, annot=True, fmt='.1f', cmap='YlGnBu', linewidths=0.5)
    plt.title('Sales Heatmap by Region and Product Line')
    plt.xlabel('Product Line')
    plt.ylabel('City')
    heatmap_path = os.path.join(output_dir, 'sales_heatmap_region_product.png')
    plt.savefig(heatmap_path)
    print(f"Saved: {heatmap_path}")
    plt.close()

    # Sales by Month
    sales_by_month = df.groupby('Month')['Total'].sum().sort_index()
    plt.figure(figsize=(12, 6))
    sales_by_month.plot(kind='bar', color='orange', title='Total Sales by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    sales_by_month_path = os.path.join(output_dir, 'sales_by_month.png')
    plt.savefig(sales_by_month_path)
    print(f"Saved: {sales_by_month_path}")
    plt.close()
