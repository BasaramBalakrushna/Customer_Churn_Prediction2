<h1>📉 Customer Churn Prediction – Olist E-commerce</h1>

<p><strong>Author:</strong> Basaram Balakrushna</p>

---

<h2>🧠 Problem Statement</h2>
<p>
Customer churn directly impacts revenue and growth.  
This project builds a machine learning model to <strong>predict whether a customer is likely to churn</strong> based on their purchasing behavior, reviews, and payment history.  
The goal is to help businesses <strong>retain valuable customers</strong> by proactively identifying those at risk and enabling targeted interventions like loyalty programs, discounts, or personalized offers.  
</p>

---

<h2>📂 Project Structure</h2>
<ul>
  <li><strong>app.py</strong> – Streamlit app for interactive churn prediction</li>
  <li><strong>rf_model_compressed.pkl</strong> – Trained Random Forest model (add this file manually)</li>
  <li><em>notebooks/Churn_Prediction.ipynb</em> – Jupyter notebook for EDA, feature engineering, and model training</li>
  <li><em>assets/</em> – Visuals & plots (EDA graphs, cover image)</li>
  <li><strong>requirements.txt</strong> – Python dependencies</li>
</ul>

---

<h2>🔍 Key Features</h2>
<ul>
  <li>📊 Comprehensive Exploratory Data Analysis (EDA) on Olist e-commerce dataset</li>
  <li>🧹 Feature engineering: orders, spend, reviews, payments, tenure</li>
  <li>🤖 Machine Learning models – Logistic Regression, Random Forest, XGBoost</li>
  <li>🎯 Deployment-ready Streamlit web app for churn scoring</li>
  <li>📈 Actionable insights into customer behavior driving churn</li>
</ul>

---

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>🐍 Python 3</li>
  <li>📦 Pandas, NumPy</li>
  <li>📊 Matplotlib, Seaborn</li>
  <li>⚙️ scikit-learn</li>
  <li>🌲 Random Forest / XGBoost</li>
  <li>💻 Streamlit</li>
  <li>💾 Joblib</li>
</ul>

---

<h2>⚙️ How to Run the Project</h2>
<ol>
  <li>Clone this repository:
    <pre><code>git clone &lt;your-repo-url&gt;
cd &lt;your-repo-folder&gt;</code></pre>
  </li>
  <li>Create and activate a virtual environment:
    <pre><code>python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Add the trained model file <code>rf_model_compressed.pkl</code> at the project root</li>
  <li>Run the Streamlit app:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

---

<h2>📊 Dataset Overview</h2>
<ul>
  <li><strong>Source:</strong> Olist Brazilian E-commerce dataset (public Kaggle dataset)</li>
  <li><strong>Granularity:</strong> Orders aggregated at <em>customer level</em></li>
  <li><strong>Target Variable:</strong> <code>churn</code> (1 = churned, 0 = active)</li>
  <li><strong>Features include:</strong>
    <ul>
      <li>Total Orders</li>
      <li>Total Spend</li>
      <li>Average Spend per Order</li>
      <li>Average Review Score</li>
      <li>Number of Payment Methods</li>
      <li>Customer Tenure (days)</li>
    </ul>
  </li>
</ul>

---

<h2>📈 Insights from EDA</h2>
<ul>
  <li>🚨 Customers with <strong>low order frequency</strong> and <strong>short tenure</strong> are more likely to churn</li>
  <li>💳 Customers using <strong>multiple payment methods</strong> tend to stay longer</li>
  <li>⭐ Higher <strong>average review scores</strong> correlate with lower churn risk</li>
  <li>💵 Customers with <strong>high lifetime spend</strong> show better retention</li>
</ul>

---

<h2>🖥️ Streamlit App Demo</h2>
<p>
The interactive web app collects inputs:
</p>
<ul>
  <li>Total Orders</li>
  <li>Total Spend</li>
  <li>Average Spend per Order</li>
  <li>Average Review Score</li>
  <li>Number of Payment Methods</li>
  <li>Customer Tenure (days)</li>
</ul>
<p>
And outputs:
</p>
<ul>
  <li>🚨 <strong>Likely to Churn</strong> – with probability confidence</li>
  <li>✅ <strong>Not Likely to Churn</strong> – with probability confidence</li>
</ul>

---

<h2>📦 Requirements</h2>
<pre><code>streamlit
pandas
numpy
scikit-learn
xgboost
joblib
matplotlib
seaborn
</code></pre>

---

<h2>📊 Dataset Source</h2>
<p>
The dataset is publicly available via <a href="https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce" target="_blank">Kaggle – Olist Brazilian E-commerce Dataset</a>.
</p>
