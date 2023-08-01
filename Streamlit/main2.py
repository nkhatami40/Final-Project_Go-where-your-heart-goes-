import streamlit as st
import pandas as pd
import os
from PIL import Image


# Get the current working directory of the Streamlit app
streamlit_dir = os.getcwd()

# read csv
csv_file_path = os.path.join(streamlit_dir, 'food_df.csv')

# load data
food_df = pd.read_csv(csv_file_path)

nutrition_limit_dict = {
    'alpha_carotene': 21.6, 'beta_carotene': 100,
    'beta_cryptoxanthin': 180, 'carbohydrate': 100, 'cholesterol': 300, 'choline': 3500, 'fiber': 30, 'lutein_and_zeaxanthin': 6,
    'lycopene': 5, 'niacin': 1.5, 'protein': 58000, 'retinol': 1.5, 'riboflavin': 4.5, 'selenium': 0.055, 'sugar_total': 25000, 'thiamin':1.1, 'water': 1500000, 'monosaturated_fat': 13000, 'polysaturated_fat': 15000, 'total_lipid': 55000, 'calcium': 1000, 'copper': 5, 'iron': 10, 'magnesium': 300, 'phosphorus': 1189, 'sodium': 2000, 'zinc': 300, 'vitamin_a': 700, 'vitamin_b12':2.4, 'vitamin_b6': 1.5, 'vitamin_c': 500, 'vitamin_e': 500, 'vitamin_k': 0.12
}


nutrition_limit_df = pd.DataFrame(nutrition_limit_dict, index=[0])

food_beneficial = ['alpha_carotene', 'fiber', 'lycopene', 'protein', 'riboflavin', 'selenium', 'thiamin', 'water'
                             'monosaturated_fat', 'polysaturated_fat', 'copper', 'iron', 'magnesium', 'phosphorus', 'potassium',
                             'zinc', 'vitamin_b12', 'vitamin_b6']
food_harmful = ['carbohydrate', 'cholesterol', 'niacin', 'sugar_total', 'total_lipid', 'calcium',
                          'sodium']
food_not_confirmed = ['beta_carotene','lutein_and_zeaxanthin', 'choline', 'retinol', 'vitamin_a', 'vitamin_c', 'vitamin_e', 'vitamin_k']

# Define the Streamlit app function
# Define the Streamlit app function
# Define the Streamlit app function
# Define the Streamlit app function
def check_nutrition_status(food_category):
    # Filter the 'food_df' DataFrame to get data for the specified food category
    food_data = food_df[food_df['category'] == food_category]

    if food_data.empty:
        st.error("Food not found in the database.")
        return

    # Calculate the sum of nutritions for the specified food
    nutrition_sum = food_data.iloc[:, 2:].sum()

    # Check if the nutrition sum exceeds the limits
    nutrition_limit_series = nutrition_limit_df.transpose().iloc[[0]]
    exceeds_limits = nutrition_sum > nutrition_limit_series.squeeze()

    # Check if the nutritions are beneficial, harmful, or unconfirmed
    beneficial_nutrients = [col for col in food_data.columns.tolist() if col in food_beneficial]
    harmful_nutrients = [col for col in food_data.columns.tolist() if col in food_harmful]
    unconfirmed_nutrients = [col for col in food_data.columns.tolist() if col in food_not_confirmed]

    # Display the results using Streamlit methods
    st.subheader("Nutrition Sum:")
    #st.write(nutrition_sum)


    nutrition_sum_transposed = nutrition_sum.to_frame().transpose().rename(index={0: 'Total Nutrition (mg)'})

    # Convert all the numbers to integers (without decimals)
    nutrition_sum_transposed = nutrition_sum_transposed.astype(int)

    st.markdown("""
       <style>
           table {
               border-collapse: collapse;
               width: 100%;
               font-size: 18px;
               text-align: left;
           }
           th, td {
               padding: 12px;
               border-bottom: 1px solid #ddd;
           }
           th {
               background-color: #f2f2f2;
           }
       </style>
       """, unsafe_allow_html=True)

    st.table(nutrition_sum_transposed)

    # Check if any harmful nutrient exceeds the limit and print the message
    harmful_nutrient_exceeds_limit = []
    for nutrient in harmful_nutrients:
        if exceeds_limits[nutrient]:
            harmful_nutrient_exceeds_limit.append(nutrient)

    if harmful_nutrient_exceeds_limit:
        st.warning("This food has a high amount of the following harmful nutrients: " + ", ".join(harmful_nutrient_exceeds_limit) + ". You should eat it moderately!")
        # Display an image
        st.image("200w.gif", use_column_width=True, width=200)

    # If no harmful nutrient exceeds the limit, display that the food is safe
    else:
        st.info("This food is safe to eat.")
        st.image("odo-ds9.gif", use_column_width=True, width=200)


def get_dynamic_subheader_text():
    # Add your logic here to determine the subheader text based on user input or any other condition
    # For example, you can use a variable to store the dynamic text
    dynamic_text = "A good food should lift the heart, warm the soul, and make you feel good."
    return dynamic_text

# Create the Streamlit app
def main():
    dynamic_text = get_dynamic_subheader_text()
    st.markdown(
        f'<p style="font-size: 24px; color: green; font-family: \'Times New Roman\', Times, serif;">{dynamic_text}</p>',
        unsafe_allow_html=True)
    # title
    st.title('Check the Nutrition Status of a Food Item')



    st.sidebar.header('User Input Parameters')


    food_category = st.sidebar.text_input("Enter the food category:")


    if st.sidebar.button('Food Nutrition Status Identifier'):
        check_nutrition_status(food_category)

    sidebar_image = Image.open("heart.health.blog.jpg")
    st.sidebar.image(sidebar_image, use_column_width=True)

if __name__ == '__main__':
    main()