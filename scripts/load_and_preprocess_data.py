import pandas as pd
import numpy as np
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/sales.log"),
        logging.StreamHandler()
    ]
)

def load_and_preprocess_data(file_path):
    """Load and clean raw sales data."""
    try:
        logging.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        logging.info(" Preprocessing Started !!")
        # Check for missing values and log the result
        missing_values = df.isnull().sum()
        if missing_values.any():
            logging.info("Missing values found in the dataset:")
            logging.info(f"\n{missing_values}")
        else:
            logging.info("No missing values found in the dataset")

        # Handle missing values
        numeric_cols = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'cogs', 'gross income']
        for col in numeric_cols:
            if df[col].isnull().any():
                df[col].fillna(df[col].median(), inplace=True)
                logging.info(f"Filled missing values in numeric column: {col} with median")

        categorical_cols = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
        for col in categorical_cols:
            if df[col].isnull().any():
                mode_value = df[col].mode()[0] if df[col].notna().any() else 'Unknown'
                df[col].fillna(mode_value, inplace=True)
                logging.info(f"Filled missing values in categorical column: {col} with mode ('{mode_value}')")

        # Check for duplicates and log the result
        duplicates_count = df.duplicated(subset=['Invoice ID']).sum()
        if duplicates_count > 0:
            logging.info(f"Found {duplicates_count} duplicate rows based on 'Invoice ID'")
            df = df.drop_duplicates(subset=['Invoice ID'], keep='first')
            logging.info("Duplicates removed")
        else:
            logging.info("No duplicate rows found")

        # Standardize data
        logging.info("Standardizing categorical data")
        df['Customer type'] = df['Customer type'].str.title()
        df['Gender'] = df['Gender'].str.title()
        df['Product line'] = df['Product line'].str.strip().str.title()
        logging.info("Categorical data standardized")

        # Convert dates
        logging.info("Processing date and time columns")
        df['Date'] = pd.to_datetime(df['Date'])
        df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
        df['Hour'] = pd.to_datetime(df['Time'].astype(str)).dt.hour
        df['Day_of_week'] = df['Date'].dt.day_name()
        df['Month'] = df['Date'].dt.month_name()
        df['Quarter'] = df['Date'].dt.quarter
        logging.info("Date and time columns processed")

        logging.info("Data preprocessing completed successfully")
        return df

    except Exception as e:
        logging.error(f"Error during data processing: {e}")
        raise

