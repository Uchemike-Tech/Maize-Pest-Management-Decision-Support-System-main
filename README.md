# Decision Support System for Integrated Pest and Disease Management in Maize

This project is a prototype Decision Support System (DSS) developed as part of the research paper, "Design and Development of Decision Support System for Integrated Pest and Disease Management in Maize".

The system is designed to assist smallholder maize farmers in Imo State, Nigeria, by providing quick diagnoses of common pests and diseases based on environmental data and observed symptoms. It then offers sustainable Integrated Pest Management (IPM) recommendations.

## ✨ Features

-   **User-Friendly Interface:** A simple web interface built with Streamlit for easy data entry.
-   **Hybrid Diagnosis Engine:**
    1.  A **Rule-Based System** provides immediate diagnoses for clear-cut, high-confidence scenarios.
    2.  A **Machine Learning Model** (Random Forest Classifier) predicts the most likely issue when rules do not apply.
-   **Actionable IPM Advice:** Provides tailored Cultural, Biological, and Chemical control recommendations for each diagnosis.

## 🛠️ Technology Stack

-   **Language:** Python
-   **Machine Learning:** Scikit-learn, Pandas, NumPy
-   **Web Framework:** Streamlit
-   **Model Persistence:** Joblib
-   **Development:** Google Colab (for model training), VS Code (for application development)

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Ensure you have **Python 3.8 or newer** installed on your system.

### Installation & Setup

1.  **Navigate to the Project Directory:**
    Open a terminal or command prompt and navigate to the folder containing this project's files.

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to keep project dependencies isolated.

    ```bash
    # Create the environment
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    -   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    -   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    _Your terminal prompt should now show `(venv)` at the beginning._

4.  **Install Required Libraries:**
    Install all the necessary Python packages using pip.

    ```bash
    pip install streamlit pandas scikit-learn joblib
    ```

### Running the Application

1.  **Start the Streamlit Server:**
    With your virtual environment still active, run the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

2.  **View the Application:**
    Your default web browser will automatically open a new tab with the application running. If it doesn't, the terminal will provide a local URL (usually `http://localhost:8501`) that you can visit.

##  Usage

1.  Use the sliders and checkboxes in the left sidebar to enter the current conditions and observed symptoms of your maize crop.
2.  Click the **"Diagnose Crop"** button at the bottom of the sidebar.
3.  The main page will display the diagnosis, its source (Rule-Based or ML Model), and the corresponding IPM management strategies.