import streamlit as st
import datetime
img_path = "Assets/QCImage.png"
# read the image
image = plt.imread(image_path)
# Function to initialize session state
def init_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 1

# Navigation function to increment the step
def next_step():
    st.session_state.step += 1

# Navigation function to decrement the step
def prev_step():
    st.session_state.step -= 1

# Function to create a navigation menu
def navigation():
    steps = ["Household Information", "Water Source Access", 
             "Water Treatment Practices", "Hygiene Practices", 
             "Health History", "Additional Information"]
    return steps[st.session_state.step - 1]

# Household Information section
def household_information():
    st.title("Household Information")
    st.session_state.household_info = {
        "district": st.text_input("District"),
        "rural_urban": st.selectbox("Rural or Urban Residence", ["Rural", "Urban"]),
        "num_household_members": st.number_input("Number of Household Members", min_value=0, step=1),
        "residential_area": st.text_input("Residential Area"),
        "house_number": st.text_input("House Number"),
        "street": st.text_input("Street"),
        "city": st.text_input("City", value="Harare"),
        "country": st.text_input("Country", value="Zimbabwe")
    }

# Water Source Access section
def water_source_access():
    st.title("Water Source Access")
    st.session_state.water_source_info = {
        "water_source_type": st.text_input("Water Source Type"),
        "water_source_description": st.text_area("Water Source Description"),
        "water_source_quality": st.selectbox("Water Source Quality", ["Clean", "Contaminated"]),
        "tap_water_access": st.checkbox("Tap Water Access"),
        "frequency_of_access": st.number_input("Frequency of Tap Water Access (days per week)", min_value=0, step=1, max_value=7)
    }

# Water Treatment Practices section
def water_treatment_practices():
    st.title("Water Treatment Practices")
    st.session_state.water_treatment_info = {
        "water_treatment_methods": st.text_input("Water Treatment Methods"),
        "treatment_consistency": st.selectbox("Treatment Consistency", ["Always", "Sometimes", "Never"])
    }

# Hygiene Practices section
def hygiene_practices():
    st.title("Hygiene Practices")
    st.session_state.hygiene_info = {
        "handwashing_frequency": st.text_input("Handwashing Frequency (times per day)"),
        "sanitation_facilities": st.text_input("Sanitation Facilities"),
        "wastewater_disposal": st.text_input("Wastewater Disposal"),
        "solid_waste_disposal": st.text_input("Solid Waste Disposal")
    }

# Health History section
def health_history():
    st.title("Health History")
    st.session_state.health_history_info = {
        "cholera_history": st.checkbox("Cholera History"),
        "recent_waterborne_illness": st.checkbox("Recent Waterborne Illness")
    }

# Additional Information section
def additional_information():
    st.title("Additional Information")
    st.session_state.additional_info = {
        "water_access_challenges": st.text_area("Water Access Challenges")
    }

# Main function
def main():
    init_session_state()
    st.image(image, caption='My Image', use_column_width=True)
    st.sidebar.markdown(
        f"""
        <div style="padding: 10px 0;">
            <img src="data:image/png;base64,{img_path}" alt="" style="width:50px;">
            <h1 style="margin-top: 10px; font-size: 1.5rem;">Quantacrusaders</h1>
        </div>
        """,
        unsafe_allow_html=True
        
    )
    st.sidebar.info("DWAHS Water Access Survey")

    step_name = navigation()
    st.write(f"Step {st.session_state.step}: {step_name}")

    if step_name == "Household Information":
        household_information()
    elif step_name == "Water Source Access":
        water_source_access()
    elif step_name == "Water Treatment Practices":
        water_treatment_practices()
    elif step_name == "Hygiene Practices":
        hygiene_practices()
    elif step_name == "Health History":
        health_history()
    elif step_name == "Additional Information":
        additional_information()

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.session_state.step > 1:
            if st.button("Previous"):
                prev_step()
                
    with col3:
        if st.session_state.step < 6:
            if st.button("Next"):
                next_step()
        elif st.session_state.step == 6:
            if st.button("Submit"):
                st.success("All Information Submitted")
                st.session_state.completed = True

if __name__ == "__main__":
    main()
    
