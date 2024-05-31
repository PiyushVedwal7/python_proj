import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
gcp_service_account = st.secrets["gcp_service_account"]
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
