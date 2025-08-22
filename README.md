# 📊 Data Visualizer

A Streamlit web application for interactive data visualization. Users can upload their own CSV files or select from existing datasets to generate various plots and explore data insights.

🔗 **Live App**: [https://data-visualization-webapp.streamlit.app/](https://data-visualization-webapp.streamlit.app/)

---

## Features

- Upload CSV files or use preloaded datasets from the `data/` directory
- View data previews and descriptive statistics
- Detect and handle missing values (drop or fill with mean/median)
- Choose plot types: Line Plot, Bar Chart, Scatter Plot, Distribution Plot, Count Plot
- Interactive selection of X and Y axes
- Real-time plot generation using Matplotlib and Seaborn

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/data-visualizer.git
   cd data-visualizer
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## Requirements

```
streamlit==1.31.0
numpy==1.26.4
pandas==2.2.0
matplotlib==3.8.2
seaborn==0.13.2
```

---

## Usage

1. **Run the app**  
   ```bash
   streamlit run app.py
   ```

2. **Upload your CSV file** or place CSV files in the `data/` directory.

3. **Interact with the UI** to select axes, plot types, and view insights.

---

## Folder Structure

```
data-visualizer/
│
├── app.py               # Main Streamlit application
├── data/                # Folder for existing CSV files
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
