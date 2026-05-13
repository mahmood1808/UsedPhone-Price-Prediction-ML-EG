import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
df=pd.read_excel(r"C:\Users\DreamCE\Desktop\programing 1\datafinaliphone.xlsx")
iphone_mapping = {
    'iphone11': 0, 'iphone11 pro': 1, 'iphone11 pro max': 2, 'iphone12': 3,
    'iphone12 mini': 4, 'iphone12 pro': 5, 'iphone12 pro max': 6, 'iphone13': 7,
    'iphone13 mini': 8, 'iphone13 pro': 9, 'iphone13 pro max': 10, 'iphone14': 11,
    'iphone14 plus': 12, 'iphone14 pro': 13, 'iphone14 pro max': 14, 'iphone15': 15,
    'iphone15 plus': 16, 'iphone15 pro': 17, 'iphone15 pro max': 18, 'iphone16': 19,
    'iphone16 plus': 20, 'iphone16 pro': 21, 'iphone16 pro max': 22, 'iphone17': 23,
    'iphone17 air': 24, 'iphone17 pro': 25, 'iphone17 pro max': 26
}

condition_map = {"Excellent": 4, "Good": 3, "Average": 2, "Poor": 1}
fix_map = {"No Fix": 0, "Fixed": 1}
features = ['Model_Encoded', 'Storage', 'Battery_Health', 'Condition', 'FIX']

X = df[features]
y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

from sklearn.ensemble import RandomForestRegressor
iphone_model = RandomForestRegressor(n_estimators=500, max_depth=12, random_state=42)

iphone_model.fit(X_train, y_train)

from sklearn.metrics import r2_score
y_pred = iphone_model.predict(X_test)

def get_final_prediction(user_list, model, iphone_mapping):
    try:
        m_name = user_list[0].strip()
        s_text = user_list[1].strip()
        b_val  = int(user_list[2])
        f_text = user_list[3].strip()
        c_text = user_list[4].strip()

        m_encoded = iphone_mapping.get(m_name)
        storage = int(''.join(filter(str.isdigit, s_text)))
        if "tb" in s_text.lower(): storage = 1024
        
        fix_val = fix_map.get(f_text, 0)
        cond_val = condition_map.get(c_text, 4)

        input_df = pd.DataFrame([[
            m_encoded, storage, b_val, cond_val, fix_val
        ]], columns=['Model_Encoded', 'Storage', 'Battery_Health', 'Condition', 'FIX'])
        
        base_prediction = model.predict(input_df)[0]

        adjustment_factors = {
            4: 1.0,   
            3: 0.94,   
            2: 0.85,   
            1: 0.72    
        }
        
        factor = adjustment_factors.get(cond_val, 1.0)
        final_price = base_prediction * factor

        if fix_val == 1:
            final_price = final_price * 0.90 
            
        return round(final_price, 2)

    except Exception as e:
        return f"Error: {str(e)}"
test_poor = ['iphone13', '128 GB', '100', 'No Fix', 'Fair']
print(f"Price : {get_final_prediction(test_poor, iphone_model, iphone_mapping)}")