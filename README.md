# Stock Market Forecasting Tool with Streamlit

This project leverages Streamlit in Python to create a robust tool for forecasting stock market trends for top companies using real-time data. Users can customize the date range, select a specific company, and interactively choose various forecasting options. The application fetches and displays stock data within the specified range, offering both data visualizations and predictive insights.

## Features
- **Date Selection**: Users can select their desired start and end dates, with defaults set to `01-01-2023` and `31-12-2023`.
- **Company Selection**: Choose from a list of top companies to forecast stock trends.
- **Data Display**: Displays stock data fetched for the selected company within the chosen date range.
- **Column Selection for Forecasting**: Select a specific column (e.g., Close, Open, High, Low prices) to base the forecasting on.
- **Model Summary**: View a summary of the forecasting model used for predictions.
- **Forecasting Duration**: Specify the number of days to predict stock trends.
- **Visualizations**:
  - Display actual vs. predicted values in a combined plot.
  - Separate plots for actual and predicted values.

## Getting Started

### Prerequisites
Ensure the following are installed:
- Python 3.7+
- Streamlit
- Additional dependencies as listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-market-forecasting.git
   cd stock-market-forecasting
2. Clone the repository:
   ```bash
   pip install -r requirements.txt
3. Navigate to the project directory in your terminal and run the Streamlit app:
   ```bash
   streamlit run app.py

## Usage Instructions

1. **Select Date Range**: Choose the start and end dates for the stock data.
2. **Select Company**: Pick a company from the dropdown menu to view its stock data.
3. **Choose Forecasting Column**: Select the column you wish to forecast, such as `Close`, `Open`, `High`, or `Low`.
4. **View Model Summary**: Check the model summary to understand the forecasting details.
5. **Set Forecasting Days**: Specify the number of days you want to predict into the future.
6. **View Results**:
   - **Combined Plot**: View a plot with both actual and predicted stock values.
   - **Separate Plots**: View individual plots for actual and predicted values.

## Project Structure

- `Streamlit_Main.py`: Main Streamlit application file, handling UI and backend processing.
- `requirements.txt`: List of required Python packages for the project.
- `README.md`: Project documentation, setup instructions, and usage examples.

## Example Usage

1. Start by setting the date range for your analysis.
2. Select a company from the dropdown list, such as "Apple" or "Google."
3. Choose the `Close` column for forecasting and set the prediction period to 30 days.
4. View the combined plot of actual vs. predicted values, or check separate plots for detailed insights.

This tool offers a convenient, interactive way to analyze and forecast stock market trends, making it useful for financial analysts, investors, and enthusiasts.

