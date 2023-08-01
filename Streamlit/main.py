import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pickle

import os


# Get the current working directory of the Streamlit app
streamlit_dir = os.getcwd()

# Combine the Streamlit app's directory with the CSV file's name to create the absolute file path
csv_file_path = os.path.join(streamlit_dir, 'heart_normalized.csv')

# Read the CSV file
heart_df = pd.read_csv(csv_file_path)


#Splitting the X-y:

y = heart_df['heart_disease']
X = heart_df.drop("heart_disease", axis=1)


# Define a function to run the models


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

log_reg = LogisticRegression()
svc_ = SVC()
KNN = KNeighborsClassifier(n_neighbors = 2)
rndm_fo = RandomForestClassifier(random_state=0, max_features='sqrt', min_samples_leaf=1, min_samples_split=4, n_estimators=100)
dec_tree = DecisionTreeClassifier(criterion='entropy', max_features='sqrt', min_samples_leaf=1, min_samples_split=2, splitter='random', random_state=100)


log_reg_fit = log_reg.fit(X_train, y_train)
svc_fit = svc_.fit(X_train, y_train)
KNN_fit = KNN.fit(X_train, y_train)
rndm_fo_fit = rndm_fo.fit(X_train, y_train)
dec_tree_fit = dec_tree.fit(X_train, y_train)


#heart_df_columns = ['age', 'cp', 'trestbps', 'restecg', 'chol', 'oldpeak', 'thalach', 'slope', 'ca', 'thal', 'sex', 'fbs', 'exang']


# Creating pickle files
with open("log_reg.pkl", "wb") as lo:  # wb: mode write
    pickle.dump(log_reg_fit, lo)

with open("KNN.pkl", "wb") as kn:
    pickle.dump(KNN_fit, kn)

with open("svc_.pkl", "wb") as sv:
    pickle.dump(svc_fit, sv)

with open("rndm_fo.pkl", "wb") as rndm_fo:
    pickle.dump(rndm_fo_fit, rndm_fo)

with open("dec_tree.pkl", "wb") as dec_tree:
    pickle.dump(dec_tree_fit, dec_tree)

# function to classify diseases
def classify(num):
    if num == 0:
        return 'Patient doesn not have a heart disease'
    else:
        return 'Patient has a heart disease!'


def main():

    # title
    st.title('Listen to your HEART: When it is BROKEN!')

    st.sidebar.header('User Input Parameters')

if __name__ == '__main__':
    main()


    def user_input_parameters():
        age = st.sidebar.slider("age", 1, 90, 53)  # label, min, max, default value
        cp = st.sidebar.slider("Chest Pain", 1, 4, 2)  # label, min, max, default value
        trestbps = st.sidebar.slider("Resting Blood Pressure",  90.0, 204.0, 100.0)  # label, min, max, default value
        restecg = st.sidebar.slider("Resting Electrocardiographic Results",  0, 2, 1)
        chol = st.sidebar.slider("Cholestrol", 120.0, 569.0, 200.0)
        oldpeak = st.sidebar.slider("ST Depression", 0.0, 6.3, 2.0)
        thalach = st.sidebar.slider("Maximum Heart Rate", 70.0, 204.0, 80.0)
        slope = st.sidebar.slider("ST Depression", 0, 2, 1)
        ca = st.sidebar.slider("Number of Major Vessels", 0, 4, 2)
        thal = st.sidebar.slider("Thalassemia", 0, 3, 1)
        sex = st.sidebar.slider("sex", 0, 1, 0)
        fbs = st.sidebar.slider("Fasting Blood Sugar", 0, 1, 0)
        exang = st.sidebar.slider("Exercise Induced Angina", 0, 1, 0)


        data = {"age": age,
                "cp": cp,
                "trestbps": trestbps, "restecg" : restecg,
                "chol": chol, "oldpeak": oldpeak, "thalach": thalach, "slope": slope, "ca": ca, "thal": thal, "sex": sex, "fbs": fbs,
                 "exang": exang}
        features_df = pd.DataFrame(data, index=[0])
        return features_df

df = user_input_parameters()

option = {'Logistic Regression', 'KNN Classifier', 'SVM Classifier', 'Random Forest Classifier', 'Decision Tree Classifier'}
model = st.sidebar.selectbox('SELECT MODEL', option) # label, options displayed

# add another subheader with the chosen model and the df with the input parameters
st.subheader(model)
st.write(df)

# ... (previous code)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

if st.button("RUN"):
    # Scale the input data
    df_scaled = scaler.transform(df)

    if model == "Logistic Regression":
        st.success(classify(round(log_reg_fit.predict(df_scaled)[0], 0)))
    elif model == "KNN Classifier":
        st.success(classify(KNN_fit.predict(df_scaled)[0]))
    elif model == "SVM Classifier":
        st.success(classify(svc_fit.predict(df_scaled)[0]))
    elif model == "Random Forest Classifier":
        st.success(classify(rndm_fo_fit.predict(df_scaled)[0]))
    else:
        st.success(classify(dec_tree_fit.predict(df_scaled)[0]))



#Importing image into streamlit app
from PIL import Image

# Open the image
image = Image.open(r'C:\Users\nkhat\OneDrive\Desktop\heart.png')

# Resize the image to a specific size
width, height = 200, 150
resized_image = image.resize((width, height))

# Display the resized image in Streamlit
st.image(resized_image, caption="Resized Image", use_column_width=True)






