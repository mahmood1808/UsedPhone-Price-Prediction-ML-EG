import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# --- 1. تجهيز البيانات والتدريب ---
df_test = pd.read_excel(r"C:\Users\Mahmood\OneDrive\Desktop\datafinallllll.xlsx")

brand_model_mapping = {
    'realme C51': 65, 'realme C53': 66, 'realme C55': 67, 'realme Narzo 60x 5g': 77, 'realme Narzo 60 5g': 75,
    'realme Narzo 60 pro 5g': 76, 'realme 11 4g': 56, 'realme 11x 5g': 58, 'realme 11 pro+ 5g': 57, 'realme Gt neo5 se': 74,
    'realme C61': 68, 'realme C63': 69, 'realme C65 4g': 70, 'realme C65 5g': 71, 'realme C67': 72, 'realme Narzo n65 5g': 80,
    'realme Narzo 70x 5g': 79, 'realme Narzo 70 pro 5g': 78, 'realme 12+ 5g': 59, 'realme 13+ 5g': 61, 'realme 13 pro+ 5g': 60,
    'realme Gt 6t': 73, 'realme 14 pro 5g': 62, 'realme 14 pro+ 5g': 63, 'realme 16 5g': 64, 'samsung Galaxy a14': 104,
    'samsung Galaxy a24': 108, 'samsung Galaxy a34 5g': 111, 'samsung Galaxy a54 5g': 114, 'samsung Galaxy s23': 120,
    'samsung Galaxy s23+': 123, 'samsung Galaxy s23 ultra': 122, 'samsung Galaxy s23 fe': 121, 'samsung Galaxy z flip5': 136,
    'samsung Galaxy z fold5': 139, 'samsung Galaxy a15': 105, 'samsung Galaxy a15 5g': 106, 'samsung Galaxy a25 5g': 109,
    'samsung Galaxy a35 5g': 112, 'samsung Galaxy a55 5g': 115, 'samsung Galaxy s24': 124, 'samsung Galaxy s24+': 127,
    'samsung Galaxy s24 ultra': 126, 'samsung Galaxy s24 fe': 125, 'samsung Galaxy z flip6': 137, 'samsung Galaxy z fold6': 140,
    'samsung Galaxy a26 5g': 110, 'samsung Galaxy a36 5g': 113, 'samsung Galaxy a56 5g': 116, 'samsung Galaxy s25': 128,
    'samsung Galaxy s25+': 132, 'samsung Galaxy s25 ultra': 131, 'samsung Galaxy s25 edge': 129, 'samsung Galaxy s25 fe': 130,
    'samsung Galaxy s26': 133, 'samsung Galaxy s26+': 135, 'samsung Galaxy s26 ultra': 134, 'samsung Galaxy z flip7': 138,
    'samsung Galaxy a06': 103, 'samsung Galaxy a16 5g': 107, 'samsung Galaxy m15 5g': 117, 'samsung Galaxy m35 5g': 118,
    'samsung Galaxy m55 5g': 119, 'samsung Galaxy z fold7': 141, 'google Pixel 9 pro fold': 41, 'google Pixel 10 pro fold': 31,
    'google Pixel 7 pro': 160, 'google Pixel 6a': 159, 'google Pixel 3xl': 156, 'google Pixel 9 pro xl': 42, 'google Pixel 3': 154,
    'google Pixel 6': 158, 'google Pixel 3a': 155, 'google Pixel 8a': 40, 'google Pixel 4': 34, 'google Pixel 7': 36,
    'google Pixel 6 pro': 35, 'google Pixel 7a': 161, 'google Pixel 4xl': 157, 'google Pixel 10 pro xl': 32, 'google Pixel 10': 33,
    'google Pixel 8 pro': 39, 'XIAOMI Redmi note 14': 97, 'XIAOMI Redmi note 14 pro plus 5g': 99, 'XIAOMI 17 ultra': 12,
    'XIAOMI Mix fold 4': 30, 'XIAOMI 14 ultra': 5, 'XIAOMI Redmi note 14 pro': 98, 'XIAOMI Redmi note 15 pro 5g': 101,
    'XIAOMI Redmi note 15 pro 4g': 100, 'XIAOMI Redmi 15c': 87, 'XIAOMI Redmi 14c': 85, 'XIAOMI Redmi 13c': 84,
    'XIAOMI Redmi note 15 pro plus 5g': 102, 'XIAOMI Redmi note 13': 95, 'XIAOMI Redmi note 13 pro plus 5g': 94,
    'XIAOMI Redmi note 15': 96, 'XIAOMI 15t': 10, 'XIAOMI 14t pro': 7, 'XIAOMI Redmi 15': 86, 'XIAOMI Poco x7': 54,
    'XIAOMI Poco x7 pro': 55, 'XIAOMI Poco f7': 47, 'XIAOMI Poco f7 pro': 48, 'XIAOMI 15t pro': 11, 'XIAOMI 15': 8,
    'XIAOMI 15 ultra': 9, 'XIAOMI Poco m6 pro': 49, 'XIAOMI Poco x6': 52, 'XIAOMI Poco x6 pro': 53, 'XIAOMI Poco f6': 45,
    'XIAOMI Poco f6 pro': 46, 'XIAOMI Redmi a3': 88, 'XIAOMI Redmi 13': 83, 'XIAOMI Redmi note 13 pro 4g': 92,
    'XIAOMI Redmi note 13 pro 5g': 93, 'XIAOMI 14t': 6, 'XIAOMI 14': 3, 'XIAOMI 14 pro': 4, 'XIAOMI Poco x5': 50,
    'XIAOMI Poco x5 pro': 51, 'XIAOMI Poco f5': 43, 'XIAOMI Poco f5 pro': 44, 'XIAOMI Redmi 12c': 82, 'XIAOMI Redmi 12': 81,
    'XIAOMI Redmi note 12s': 91, 'XIAOMI Redmi note 12 4g': 89, 'XIAOMI Redmi note 12 pro': 90, 'XIAOMI 13t pro': 2,
    'XIAOMI 13': 0, 'XIAOMI 13 ultra': 1, 'Honor Magic 7 pro': 27, 'Honor Magic 7': 26, 'Honor 400 pro': 18, 'Honor 400': 17,
    'Honor X9c': 153, 'Honor X8c': 150, 'Honor X7c': 147, 'Honor Magic 6 pro': 25, 'Honor 200 pro': 15, 'Honor 200': 13,
    'Honor Magic v3': 29, 'Honor X9b': 152, 'Honor X8b': 149, 'Honor X7b': 146, 'Honor Magic 5 pro': 23, 'Honor 90': 19,
    'Honor X9a': 151, 'Honor 90 smart': 21, 'Honor 200 smart': 16, 'Honor Magic 6 lite': 24, 'Honor Magic 5 lite': 22,
    'Honor Magic v2': 28, 'Honor 200 lite': 14, 'Honor 90 lite': 20, 'Honor X8a': 148, 'Honor X7a': 145, 'Honor X6a': 142,
    'Honor X6b': 143, 'Honor X6c': 144
}

# تدريب الموديل
X = df_test.drop(['Price', 'Model', 'FIX'], axis=1) 
y = df_test['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=500, max_depth=15, min_samples_split=5, random_state=42)
rf_model.fit(X_train, y_train)

# --- 2. دوال المساعدة والتحويل ---

def convert_storage(storage_str):
    if isinstance(storage_str, (int, float)):
        return int(storage_str)
    s = str(storage_str).lower().strip()
    if 't' in s:
        val = s.replace('t', '').replace('b', '').strip()
        return int(float(val) * 1024)
    elif 'g' in s:
        val = s.replace('g', '').replace('b', '').strip()
        return int(float(val))
    try:
        return int(float(s))
    except:
        return 128

# --- 3. المنطق الهجين (Hybrid Logic) ---

def egypt_market_final_logic(phone_name, ram, storage, condition, needs_fix):
    # AI Prediction
    model_code = brand_model_mapping.get(phone_name)
    features = pd.DataFrame([[ram, storage, condition, model_code, 0, 0, 0, 0, 1]], columns=X.columns)
    raw_pred = rf_model.predict(features)[0]

    # Limits
    samsung_realme_limits = {
        "a34": {"min": 10000, "max": 13000},
        "a14": {"min": 6000, "max": 8500},
        "s23 ultra": {"min": 40000, "max": 55000},
        "c61": {"min": 5000, "max": 7500}
    }

    xiaomi_limits = {
        "17 ultra": {"min": 60000, "max": 75000},
        "15 ultra": {"min": 55000, "max": 58000},
        "14 ultra": {"min": 30000, "max": 35000},
        "redmi note 14 pro plus": {"min": 13000, "max": 20000},
        "redmi note 14": {"min": 3500, "max": 9500},
        "poco f7": {"min": 25000, "max": 27000}
    }

    name_lower = phone_name.lower()
    current_limit = {"min": raw_pred * 0.8, "max": raw_pred * 1.2}

    is_xiaomi = any(brand in name_lower for brand in ["xiaomi", "redmi", "poco"])
    
    if is_xiaomi:
        for key in xiaomi_limits:
            if key in name_lower:
                current_limit = xiaomi_limits[key]
                break
        else:
            if raw_pred > 35000 and "ultra" not in name_lower:
                current_limit = {"min": 15000, "max": 25000}
    else:
        for key in samsung_realme_limits:
            if key in name_lower:
                current_limit = samsung_realme_limits[key]
                break

    base_price = max(min(raw_pred, current_limit['max']), current_limit['min'])

    # Application of Fix logic
    if needs_fix == 1:
        base_price -= 10000 if base_price > 30000 else 2000

    # Condition multipliers
    multipliers = {4: 1.0, 3: 0.90, 2: 0.82, 1: 0.70}
    return base_price * multipliers.get(condition, 1.0)

# --- 4. معالجة طلب المستخدم (Process Request) ---

def process_user_request(user_list):
    """
    Input: ['SAMSUNG', 'samsung Galaxy a34 5g', '8 GB', '256 GB','No Fix', 'Excellent']
    """
    # استخراج البيانات بناءً على ترتيب الليست الجديد
    full_model_name = user_list[1] 
    ram_raw = user_list[2]
    storage_raw = user_list[3]
    fix_status_text = user_list[4]
    condition_text = user_list[5]

    # تحويل حالة الـ Fix
    needs_fix_val = 0 if str(fix_status_text).lower() == "no fix" else 1
    
    # تحويل الـ Condition
    cond_map = {"Excellent": 4, "Good": 3, "Average": 2, "Poor": 1}
    condition_val = cond_map.get(condition_text, 4)

    # تنظيف الأرقام
    clean_ram = int(str(ram_raw).lower().replace('gb', '').strip())
    clean_storage = convert_storage(storage_raw)

    return egypt_market_final_logic(
        phone_name=full_model_name,
        ram=clean_ram,
        storage=clean_storage,
        condition=condition_val,
        needs_fix=needs_fix_val
    )

# --- تجربة التشغيل النهائية ---
sample_user_input = ['SAMSUNG', 'samsung Galaxy s23 ultra', '12 GB', '256 GB', 'Fix', 'Excellent']
final_result = process_user_request(sample_user_input)
print(f" {final_result:,.0f} EGP")