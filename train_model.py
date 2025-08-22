
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os


df = pd.read_csv('dataset/KDDTrain+.csv')


if 'difficulty_level' in df.columns:
    df = df.drop(columns=['difficulty_level'])


categorical_cols = df.select_dtypes(include=['object']).columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


X = df.drop('label', axis=1)
y = df['label'].apply(lambda x: 0 if x == 'normal' else 1)  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Create the saved_model directory if it doesn't exist
os.makedirs('saved_model', exist_ok=True)

with open('saved_model/rf_model.pkl', 'wb') as f:
    pickle.dump(model, f)


with open('saved_model/label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)
