import pandas as pd
from scripts.load_and_preprocess_data import load_and_preprocess_data
from scripts.analysis import analyze_data
from scripts.static_visualizations import create_and_save_visualizations
from scripts.dash_app import create_dash_app
import os
import matplotlib
matplotlib.use('Agg') # Use non-GUI backend for matplotlib

def main():
    """Main application entry point: Automates preprocessing, analysis, visualizations, and dashboard."""
    # Step 1: Ensure necessary directories exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('visualizations', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('logs', exist_ok=True)  # Directory for logs
    
    # Step 2: Preprocess data
    print("🚀 Step 1: Preprocessing data...")
    try:
        raw_df = load_and_preprocess_data('data/sales_data.csv')  # Load and preprocess raw data
        raw_df.to_csv('data/cleaned_sales_data.csv', index=False)  # Save cleaned data
        print("✅ Data preprocessing completed!")
    except Exception as e:
        print(f"❌ Error during preprocessing: {e}")
        return  # Exit if preprocessing fails

    # Step 3: Perform data analysis
    print("🔍 Step 2: Performing data analysis...")
    try:
        cleaned_df = pd.read_csv('data/cleaned_sales_data.csv', parse_dates=['Date'])  # Load preprocessed data
        analysis_results = analyze_data(cleaned_df)  # Perform analysis

        # Display key results from the analysis
        print("📊 Analysis Results:")
        print(f"Total Sales: ${analysis_results['total_sales']:,.2f}")
        print(f"Average Sales: ${analysis_results['average_sales']:,.2f}")
        print("Sales by Region:")
        print(analysis_results['sales_by_region'])
        print("Sales by Product Line:")
        print(analysis_results['sales_by_product'])
        print("Sales by Month:")
        print(analysis_results['sales_by_month'])
        print("Top Customer Types:")
        print(analysis_results['top_customers'])
        print("Payment Method Distribution:")
        print(analysis_results['payment_distribution'])
        print("✅ Analysis completed!")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return  # Exit if analysis fails

    # Step 4: Generate static visualizations
    print("📊 Step 3: Generating static visualizations...")
    try:
        create_and_save_visualizations(cleaned_df, 'visualizations')  # Generate static visualizations
        print(f"🎨 Visualizations saved to: visualizations/")
    except Exception as e:
        print(f"❌ Error during visualization generation: {e}")
        return  # Exit if visualization fails

    # Step 5: Launch interactive dashboard
    print("🌐 Step 4: Launching Dash application...")
    try:
        app = create_dash_app()  # Initialize the Dash app
        app.run_server(debug=True, port=8050)  # Run the app locally on port 8050
    except Exception as e:
        print(f"❌ Error during Dash app launch: {e}")
        return  # Exit if the Dash app fails

if __name__ == '__main__':
    main()
