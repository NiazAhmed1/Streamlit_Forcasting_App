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
