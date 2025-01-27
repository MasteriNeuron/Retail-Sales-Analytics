---

# **🌟 Retail Sales Analytics Dashboard**
![Dashboard Screenshot](https://github.com/user-attachments/assets/1f4d02ef-57fb-4f30-880c-545dc567f415)

---

## **📋 Overview**
The **Retail Sales Analytics Dashboard** is a comprehensive data analytics application designed to **preprocess**, **analyze**, and **visualize** retail sales data. It includes an **interactive dashboard** for exploring sales trends, customer behavior, and product performance.

> 🎨 The dashboard is styled with the **Indian tricolor theme** (saffron, white, and green) to celebrate its identity.

---

## **✨ Features**
1. 🔧 **Data Preprocessing**:
   - Handles missing values, duplicates, and standardizes the dataset.
   - Adds time-based features for granular insights (e.g., Hour, Day, Month).

2. 📊 **Data Analysis**:
   - Computes key metrics: total sales, average sales, sales by region, and sales by product.
   - Provides insights into customer behavior and payment distribution.

3. 🖼️ **Static Visualizations**:
   - Line charts, bar plots, and heatmaps to summarize sales trends.
   - Saves visualizations as static images.

4. 🌐 **Interactive Dashboard**:
   - Filters data by date, city, product line, and gender.
   - Dynamic charts: sales trends, product performance, payment distribution, and hourly sales patterns.
   - Export filtered data as a CSV file.

---

## **📂 Project Structure**
```
Retail_Sales_Analytics/
├── data/
│   ├── sales_data.csv             # Raw sales data (input)
│   └── cleaned_sales_data.csv     # Cleaned data after preprocessing
├── visualizations/                # Static visualizations
├── outputs/                       # Exported filtered data
├── logs/                          # Log files
├── scripts/
│   ├── load_and_preprocess_data.py # Data preprocessing module
│   ├── analysis.py                 # Data analysis module
│   ├── static_visualizations.py    # Static visualization module
│   └── dash_app.py                 # Interactive dashboard module
├── app.py                         # Main application entry point
├── requirements.txt               # Python dependencies
├── README.md                      # Documentation
```

---

## **🛠️ Technologies Used**
1. **Language**: Python 3.8 or higher
2. **Libraries**:
   - 📂 **Data Manipulation**: `pandas`, `numpy`
   - 📈 **Visualizations**: `matplotlib`, `seaborn`, `plotly`
   - 🌐 **Dashboard**: `Dash`, `dash-bootstrap-components`
   - 📝 **Logging**: `logging`
3. **Styling**: Indian tricolor theme (saffron, white, green)

---

## **🚀 How to Run the Code**

### **1. Clone the Repository**
```bash
git clone https://github.com/MasteriNeuron/Retail-Sales-Analytics.git
cd retail-sales-analytics
```

### **2. Create & Activate a Virtual Environment**
```bash
conda create -n venv python=3.11 -y
conda activate venv/
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add Your Data**
- Place the raw sales data file (`sales_data.csv`) in the `data/` directory.
- Ensure the file includes columns like `Date`, `City`, `Product line`, `Total`, `Quantity`, `Payment`, `Gender`, etc.

---

### **💻 Steps to Run the Application**

#### **1. Preprocessing**
Automatically cleans and preprocesses raw data.
```bash
python app.py
```

#### **2. Automated Workflow**
Running `app.py` performs:
1. Cleans and saves the processed data to `data/cleaned_sales_data.csv`.
2. Outputs key analysis metrics in the console.
3. Saves static visualizations in the `visualizations/` directory.
4. Launches an interactive dashboard on `http://localhost:8050`.

#### **3. Access the Dashboard**
- Navigate to [http://localhost:8050](http://localhost:8050) to interact with the dashboard.

---

## **🎯 Key Dashboard Features**
1. **Filters**:
   - 📅 Date Range
   - 🌆 City
   - 🛍️ Product Line
   - 👥 Gender

2. **Key Metrics**:
   - 💰 Total Sales
   - 📈 Gross Income
   - 📦 Total Quantity Sold
   - ⭐ Average Rating

3. **Dynamic Visualizations**:
   - 📊 Sales Trend Over Time
   - 📦 Product Performance
   - 💳 Payment Method Distribution
   - 👤 Customer Type Analysis
   - ⏰ Hourly Sales Patterns

4. **Export Data**:
   - Save filtered data as a CSV file.

---

## **📦 Outputs**

### **1. Static Visualizations**
Generated visualizations include:
- 📈 **Sales Trend Over Time** (Line Chart)
- 🌆 **Sales Heatmap by Region and Product Line** (Heatmap)
- 📊 **Sales by Month** (Bar Chart)

![Visualization Screenshot](https://github.com/user-attachments/assets/7efb8298-3534-4ee2-afc8-67ed17cbcb82)

---

### **2. Interactive Dashboard**
- 💡 Interactive filtering.
- 🔄 Real-time chart updates.
- 📤 Export functionality.

![Dashboard Screenshot 1](https://github.com/user-attachments/assets/7e56ed83-6f7a-4b5c-9465-a1bb224a6852)
![Dashboard Screenshot 2](https://github.com/user-attachments/assets/d0cae10f-5dcc-4249-a097-cfc3d4b800b5)

---

## **🛡️ Error Handling**
- 📝 Logs are stored in the `logs/` directory for debugging.
- All errors during preprocessing, analysis, or dashboard runtime are logged.

---

## **⚠️ Known Issues**
- Ensure the raw data file (`sales_data.csv`) includes all required columns to prevent preprocessing errors.
- For port conflicts on `8050`, modify `app.run_server` in `app.py`:
   ```python
   app.run_server(debug=True, port=8051)
   ```

---

## **🌟 Future Enhancements**
1. 🔒 **Add User Authentication**: Restrict access and personalize dashboards.
2. 📊 **Enhance Visualizations**: Add advanced plots (e.g., maps, trend forecasts).
3. 📂 **Support Multi-File Preprocessing**: Merge and process multiple datasets seamlessly.
4. ☁️ **Deploy on Cloud**: Host on AWS, Render, or Azure for global access.

---

## **📄 License**
This project is licensed under the MIT License.

---
