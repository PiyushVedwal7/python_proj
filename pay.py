import streamlit as st
 
from st_paywall import add_auth

# Load secrets
testing_mode = st.secrets["testing_mode"]
payment_provider = st.secrets["payment_provider"]
stripe_api_key_test = st.secrets["stripe_api_key_test"]
stripe_api_key = st.secrets["stripe_api_key"]
stripe_link = st.secrets["stripe_link"]
stripe_link_test = st.secrets["stripe_link_test"]
client_id = st.secrets["client_id"]
client_secret = st.secrets["client_secret"]
redirect_url_test = st.secrets["redirect_url_test"]
redirect_url = st.secrets["redirect_url"]
bmac_api_key = st.secrets["bmac_api_key"]
bmac_link = st.secrets["bmac_link"]

# Determine the redirect URI based on the testing mode
redirect_uri = redirect_url_test if testing_mode else redirect_url

# Configure Streamlit
st.set_page_config(layout='wide')
st.markdown("""
<style>
  .animated-title {
  animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>

<h1 class="animated-title">PAYMENT PORTAL</h1>
""", unsafe_allow_html=True)

# Add authentication with the correct redirect URI
add_auth(required=True)

# Display user subscription status
st.write(f"YOUR SUBSCRIPTION IS VALID: {st.session_state.get('user_subscribed', False)}")
st.write(f"You are: {st.session_state.get('email', 'Unknown')}")
st.write("Subscription")



#after payent

import webbrowser

# ... (payment processing code)

# Construct redirect URL with success_url and any parameters
#edirect_url = f"{success_url}?payment_successful=True&token={confirmation_token}"

# Open user's browser and redirect
webbrowser.open(redirect_url)

