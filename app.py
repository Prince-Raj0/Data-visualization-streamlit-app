import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config
st.set_page_config(page_title='Data Visualizer', layout='centered', page_icon='📊')

# Title
st.title('📊  Data Visualizer')

# --- Data Source Selection ---
data_source = st.radio("Select Data Source:", ("Upload CSV", "Use Existing Data"))

df = None  # Initialize df

if data_source == "Upload CSV":
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Uploaded Data:")
            st.write(df.head())
        except pd.errors.ParserError as e:  # Catch CSV parsing errors
            st.error(f"Error parsing CSV: {e}")
        except Exception as e:  # Catch other potential errors
            st.error(f"An error occurred: {e}")

elif data_source == "Use Existing Data":
    working_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = f"{working_dir}/data"

    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        if files:
            selected_file = st.selectbox('Select a file', files, index=None)
            if selected_file:
                file_path = os.path.join(folder_path, selected_file)
                try:
                    df = pd.read_csv(file_path)
                    st.write("Selected Data:")
                    st.write(df.head())
                except pd.errors.ParserError as e:
                    st.error(f"Error parsing CSV: {e}")
                except FileNotFoundError:  # Handle file not found
                    st.error(f"File not found at: {file_path}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("No CSV files found in the 'data' directory. Please upload a file or add files to the directory.")
    else:
        st.warning("The 'data' directory does not exist. Please create it and add CSV files.")


if df is not None:  # Proceed only if a DataFrame is loaded
    try:
        col1, col2 = st.columns(2)
        columns = df.columns.tolist()

        with col1:
            x_axis = st.selectbox('Select the X-axis', options=columns + ["None"])
            y_axis = st.selectbox('Select the Y-axis', options=columns + ["None"])

            plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']
            plot_type = st.selectbox('Select the type of plot', options=plot_list)

        with col2:
            if st.checkbox("Show Descriptive Statistics"):
                st.write(df.describe())

            if st.checkbox("Show Missing Values"):
                st.write(df.isnull().sum())

            if st.checkbox("Handle Missing Values"):
                strategy = st.selectbox("Missing Value Strategy", ["Drop Rows", "Fill with Mean/Median"])
                if strategy == "Drop Rows":
                    df = df.dropna()
                    st.write("Missing values dropped.")
                elif strategy == "Fill with Mean/Median":
                    column_to_fill = st.selectbox("Select Column to fill", options=columns)
                    fill_value = st.selectbox("Fill with", ["Mean", "Median"])
                    try:  # Handle potential type errors during filling.
                        if fill_value == "Mean":
                            df[column_to_fill] = df[column_to_fill].fillna(df[column_to_fill].mean())
                        elif fill_value == "Median":
                            df[column_to_fill] = df[column_to_fill].fillna(df[column_to_fill].median())
                        st.write(f"Missing values in '{column_to_fill}' filled with {fill_value}.")
                    except TypeError as e:
                         st.error(f"Type error during missing value filling: {e}. Check if the selected column is numeric for Mean/Median filling.")

                st.write("Updated Data:")
                st.write(df.head())  # Display the updated DataFrame


        if st.button('Generate Plot'):
            try:
                fig, ax = plt.subplots(figsize=(6, 4))

                if plot_type == 'Line Plot':
                    sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
                elif plot_type == 'Bar Chart':
                    sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
                elif plot_type == 'Scatter Plot':
                    sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
                elif plot_type == 'Distribution Plot':
                    sns.histplot(df[x_axis], kde=True, ax=ax)
                    y_axis = 'Density'
                elif plot_type == 'Count Plot':
                    sns.countplot(x=df[x_axis], ax=ax)
                    y_axis = 'Count'

                ax.tick_params(axis='x', labelsize=10)
                ax.tick_params(axis='y', labelsize=10)

                plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)
                plt.xlabel(x_axis, fontsize=10)
                plt.ylabel(y_axis, fontsize=10)

                st.pyplot(fig)

            except KeyError as e:
                st.error(f"KeyError during plotting. Check if the selected columns exist: {e}")
            except TypeError as e:  # Catch potential type errors during plotting
                st.error(f"Type error during plotting: {e}. Ensure correct data types for the chosen plot type.")
            except Exception as e:
                st.error(f"An error occurred during plotting: {e}")

    except Exception as e:
        st.error(f"A general error occurred: {e}")


