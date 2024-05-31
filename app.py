import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
gcp_service_account = {
    "type": "service_account",
    "project_id": "gform-app-424711",
    "private_key_id": "b9c0817cff63ed729516175fa64d910760e7272c",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCmXXma+l9jrBfG\n17mmB1OBloVtz74nrrH9+ei//Kh4dlL8e87BSlczB48X+9DysYZu1SnVmBl25sp2\nE++DldNxfQDqDC+IepEMU9LhOP6vFlTaD+WTlEZwVCLxyh9KCyQNLuqiV+1yg0Il\nzjMw8MoZWloVB7FKNmxmQr0UWSzwKVMWObxulHyrWh2kVAQ/waqScHuXiZVzEyo4\nUR+lFOXH780vpwN5eQxgET+BXRf+WXq+1RAlzv4ahSdeH/fJyCeUxU+3wZosBiMD\nxgZuhmd9OW68XvPNSwVnKfMQQa32rrmsX6wDDiGS4Or9xn0Olw6lR7TCtphxzgqN\nY/Rbi9arAgMBAAECggEAFFKfPCaGsuXUbRFwQnnATThxKetynBAJT/Bl6tdh+yk1\nKlZeI5rsZmBE2NYFqIgK1zeJ/zzagNMLpiX5oHY+g1gVCFefEjSAII84LRQpzy39\nWpAOPZt43q2ggS9C6D15Kh/Hljet2sscWwLtRPa9MXX/QsoS8cZj3TrHie36K9zQ\nUQH2ne30k6fM2OUPBQGcpNd2DdFreXosrVolZanKY+pgTsqrnXEFNVDoOdXIfx9r\nBGllB5mn8EiQO+tV6knyzkcFXWNh1GEwQ/Txq21Adm7BKfwGpQXa2Qj8WdaxlPxs\nfQG0EYvz8x4otY4lqCsmyaJG6JmhINOqbiNhxJHalQKBgQDqGXSLLfryo/n6LvMa\nWHQGPPyi9vm+xa/Y+swPSkeFRplBhgGFZKBzGAcjFVnS3LFbhI2KLX3Bafr/C7SJ\nIl9XSu5hx9zS9VFpWobAY+lyeptCY1HNJr4J7po7c6W5cO3yT0FqGQZjxhMStt2J\nca/J33hhZW8ZTqZzc7gceJuS5wKBgQC17dKpR76GfIwgr7DpU2xD9SKpJh0C+T90\ntPluAoTv+l84V5F+e57CQQyEwmnZ7sIGIaOLHk9zUYFBu7ow1srmKfbf+29HOVaP\nVzWpGqFv9cL5rbFiadfOeloiHvzEYZOaE4n+xAvs1eBsaaxX+6KW5qiURpBf9iH7\nE4mpyc5pnQKBgBYeMZS003D5bTTmGrHyiYPNX1FGZHJR2zt09rK7IebFtNUsBBjG\nWSKGsqXt7n6tu1QaQgU8JxWPHdfbE0Ohq8BjpAI5D/QemYKKuxCSYAwg6WpsV946\nOtpVYN0dIBtVQCYUtul/U8s5e7PY8zV5OFKqeoU5QDXz6GYgGNUX0BshAoGAfV8N\n3GA3mOA9hMzuQmyd4FsO7rf4KDNxmlCYz0nnKKVGd0JJXnt8VWuUX+zGG0wg4y7N\nUDKsF9EkHRNsZPmwS1rB6WqRLekCkLdNoGJcvBYFriAXbLV55a2FbZwjHoYLvJMY\ndrvNaAGfrbZI8TzUt97ub3gNSEQK+MZnCN2sZDUCgYBuajGd99hY4F9gHWRPSfe8\nCwJlOQfzbvgVDdu1LtnMN4AVIHlpIm19AEhypUpKD9K61ad7gR8ixR9ig855kjCC\ne7u0yLbok/A7l4STeDJJlloovvFub7QWYAOripfVjWXEMQdJ+eixjrZqw+BJewZq\np3NrzkWPcc9s+6FoNOz60g==\n-----END PRIVATE KEY-----\n",
    "client_email": "piyush-vedwal@gform-app-424711.iam.gserviceaccount.com",
    "client_id": "103470424737845469321",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/piyush-vedwal%40gform-app-424711.iam.gserviceaccount.com"
}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(gcp_service_account, scope)
client = gspread.authorize(credentials)

# Open Google Sheets
spreadsheet = client.open('python_form')

# List available worksheets
worksheet_names = [sheet.title for sheet in spreadsheet.worksheets()]

# Streamlit UI
st.markdown("""
    <style>
        .main-title, .sub-title {
            text-align: center;
        }
        .main-title {
            font-size: 3em;
            color: #FF4B4B;
            animation: fadeIn 2s;
        }
        .sub-title {
            font-size: 1.5em;
            color: #4B8AFF;
            animation: fadeIn 4s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .hover-pop:hover {
            transform: scale(1.1);
            transition: transform 0.2s;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title hover-pop">VENDOR MANAGEMENT SYSTEM</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-title hover-pop">Enter details of new vendors below</h2>', unsafe_allow_html=True)

# Select worksheet
worksheet_name = st.selectbox("Select Worksheet", options=worksheet_names)

# Access the selected worksheet
sheet = spreadsheet.worksheet(worksheet_name)

# Load existing data
existing_data = pd.DataFrame(sheet.get_all_records())

# Print column names to debug
st.write("Column Names:", existing_data.columns.tolist())

# Lists for dropdowns
Business_types = ["Manufacturer", "Distributor", "Wholesaler", "Retailer", "Service Provider"]
Products = ["Electronics", "Apparel", "Groceries", "Software", "Other"]

# Input form for vendor details
with st.form(key="vendor_form"):
    company_name = st.text_input(label="Company Name*")
    business_type = st.selectbox("Business Type*", options=Business_types)
    products_selected = st.multiselect("Products Type", options=Products)
    experience_in_business = st.slider("Experience (years)", 0, 50, 5)
    onboarding_date = st.date_input(label="Onboarding Date")
    additional_info = st.text_area(label="Additional Notes")
    submit_button = st.form_submit_button(label="Submit Form Details")

    if submit_button:
        new_vendor = {
            "company_name": company_name,
            "Business Type": business_type,
            "Products": ", ".join(products_selected),
            "Experience (years)": experience_in_business,
            "Onboarding Date": onboarding_date.strftime('%Y-%m-%d'),
            "Additional Notes": additional_info
        }
        # Ensure the column name is correct
        if 'company_name' in existing_data.columns:
            if existing_data["company_name"].str.contains(company_name).any():
                st.warning(f"Vendor '{company_name}' already exists.")
            else:
                sheet.append_row(list(new_vendor.values()))
                st.success(f"Vendor '{company_name}' has been added successfully.")
                new_vendor_df = pd.DataFrame([new_vendor])
                existing_data = pd.concat([existing_data, new_vendor_df], ignore_index=True)
        else:
            st.error("Column 'company_name' does not exist in the worksheet. Please check")

# Display existing vendor data
st.subheader("Existing Vendors")
st.dataframe(existing_data)

# Export to CSV
if st.button('Export to CSV'):
    csv = existing_data.to_csv(index=False).encode('utf-8')
    st.download_button(label='Download CSV', data=csv, file_name='vendors.csv', mime='text/csv')
