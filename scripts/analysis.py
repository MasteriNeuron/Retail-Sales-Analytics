import pandas as pd
import logging


def analyze_data(df):
    """Perform sales data analysis with logging."""
    try:
        logging.info("Starting data analysis...")

        # Calculate total sales
        total_sales = df['Total'].sum()
        logging.info(f"Total sales calculated: ${total_sales:,.2f}")

        # Calculate average sales
        average_sales = df['Total'].mean()
        logging.info(f"Average sales calculated: ${average_sales:,.2f}")

        # Sales by region
        sales_by_region = df.groupby('City')['Total'].sum()
        logging.info(f"Sales by region calculated: {sales_by_region.to_dict()}")

        # Sales by product
        sales_by_product = df.groupby('Product line')['Total'].sum()
        logging.info(f"Sales by product line calculated: {sales_by_product.to_dict()}")

        # Sales by month
        sales_by_month = df.groupby('Month')['Total'].sum()
        logging.info(f"Sales by month calculated: {sales_by_month.to_dict()}")

        # Top customers by frequency
        top_customers = df['Customer type'].value_counts().head(5)
        logging.info(f"Top customer types identified: {top_customers.to_dict()}")

        # Payment method distribution
        payment_distribution = df['Payment'].value_counts(normalize=True)
        logging.info(f"Payment method distribution calculated: {payment_distribution.to_dict()}")

        # Consolidate analysis results
        analysis = {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'sales_by_region': sales_by_region,
            'sales_by_product': sales_by_product,
            'sales_by_month': sales_by_month,
            'top_customers': top_customers,
            'payment_distribution': payment_distribution
        }

        logging.info("Data analysis completed successfully.")
        return analysis

    except Exception as e:
        logging.error(f"Error during data analysis: {e}")
        raise
