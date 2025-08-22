import pandas as pd
import pickle

with open('saved_model/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

def analyze_packet(packet_data: dict):
    df = pd.DataFrame([packet_data])
    prediction = model.predict(df)
    return prediction[0]
