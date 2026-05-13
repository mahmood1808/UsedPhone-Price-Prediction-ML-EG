import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import customtkinter as ctk
import csv
import os
from PIL import Image

# ==========================================================
# --- 1. تجهيز البيانات والتدريب (الماشين) للأندرويد ---
# ==========================================================
df_test = pd.read_excel(r"C:\Users\DreamCE\Desktop\programing 1\datafinallllll.xlsx")

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

X = df_test.drop(['Price', 'Model', 'FIX'], axis=1) 
y = df_test['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=500, max_depth=15, min_samples_split=5, random_state=42)
rf_model.fit(X_train, y_train)

# ==========================================================
# --- 1.1 تجهيز البيانات والتدريب (الماشين) للآيفون ---
# ==========================================================
df_iphone = pd.read_excel(r"C:\Users\DreamCE\Desktop\programing 1\datafinaliphone.xlsx")

iphone_mapping = {
    'iphone11': 0, 'iphone11 pro': 1, 'iphone11 pro max': 2, 'iphone12': 3,
    'iphone12 mini': 4, 'iphone12 pro': 5, 'iphone12 pro max': 6, 'iphone13': 7,
    'iphone13 mini': 8, 'iphone13 pro': 9, 'iphone13 pro max': 10, 'iphone14': 11,
    'iphone14 plus': 12, 'iphone14 pro': 13, 'iphone14 pro max': 14, 'iphone15': 15,
    'iphone15 plus': 16, 'iphone15 pro': 17, 'iphone15 pro max': 18, 'iphone16': 19,
    'iphone16 plus': 20, 'iphone16 pro': 21, 'iphone16 pro max': 22, 'iphone17': 23,
    'iphone17 air': 24, 'iphone17 pro': 25, 'iphone17 pro max': 26
}

features_iphone = ['Model_Encoded', 'Storage', 'Battery_Health', 'Condition', 'FIX']
X_iph = df_iphone[features_iphone]
y_iph = df_iphone['Price']

X_train_iph, X_test_iph, y_train_iph, y_test_iph = train_test_split(X_iph, y_iph, test_size=0.15, random_state=42)

iphone_model = RandomForestRegressor(n_estimators=500, max_depth=12, random_state=42)
iphone_model.fit(X_train_iph, y_train_iph)


# --- 2. دوال المساعدة ---
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

# --- 3. الـ GUI ---
ctk.set_appearance_mode("light") 

class SmartApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Price Predictor - 2026")
        self.geometry("700x800") 
        self.configure(fg_color="#F0F9F7") 

        base_path = os.path.dirname(__file__)
        try:
            iphone_path = os.path.join(base_path, "images.gif")
            self.iphone_logo = ctk.CTkImage(light_image=Image.open(iphone_path), size=(100, 100))
            android_path = os.path.join(base_path, "android-3383929_1280.gif")
            self.android_logo = ctk.CTkImage(light_image=Image.open(android_path), size=(100, 100))
        except:
            self.iphone_logo = None
            self.android_logo = None

        self.lang = "EN" 
        self.saved_data_list = [] 
        self.current_input = []  
        self.last_price = None  # لتخزين آخر سعر تم توقعه
        self.last_details = None # لتخزين آخر بيانات تم إدخالها
        self.android_csv = "android_history.csv"
        self.iphone_csv = "iphone_history.csv"
        self.file_path = self.iphone_csv
        self.load_old_data()

        self.texts = {
            "EN": {
                "welcome_title": "Welcome",
                "subtitle": "Full Database (Android & iPhone)",
                "start": "Start Now",
                "platform_title": "Choose OS",
                "android_brands": "Android Brands",
                "specs_title": "Specifications",
                "back": "← Back",
                "save": "Save & Predict Price 🚀",
                "result_title": "Prediction Result",
                "price_is": "Expected Price:",
                "currency": "EGP",
                "model_lbl": "Select Model:",
                "ram_lbl": "RAM Capacity:",
                "mem_lbl": "Storage Memory:",
                "batt_lbl": "Battery Health (%):",
                "fix_lbl": "Repair Status:",
                "cond_lbl": "Device Condition:",
                "android": "ANDROID",
                "iphone": "iPHONE"
            },
            "AR": {
                "welcome_title": "مرحباً بكِ ",
                "subtitle": "قاعدة البيانات الشاملة (أندرويد وآيفون)",
                "start": "ابدأ الآن",
                "platform_title": "اختر نظام التشغيل",
                "android_brands": "ماركات أندرويد",
                "specs_title": "المواصفات",
                "back": "عودة →",
                "save": "حفظ البيانات والتوقع 🚀",
                "result_title": "نتيجة التوقع",
                "price_is": "السعر المتوقع:",
                "currency": "جنيه",
                "model_lbl": "اختر الموديل:",
                "ram_lbl": "سعة الرام:",
                "mem_lbl": "مساحة التخزين:",
                "batt_lbl": "صحة البطارية (%):",
                "fix_lbl": "حالة الصيانة:",
                "cond_lbl": "حالة الجهاز:",
                "android": "أندرويد",
                "iphone": "آيفون"
            }
        }

        self.brands_data = {
            'SAMSUNG': [
                'samsung Galaxy a14', 'samsung Galaxy a24', 'samsung Galaxy a34 5g', 'samsung Galaxy a54 5g', 
                'samsung Galaxy s23', 'samsung Galaxy s23+', 'samsung Galaxy s23 ultra', 'samsung Galaxy s23 fe', 
                'samsung Galaxy z flip5', 'samsung Galaxy z fold5', 'samsung Galaxy a15', 'samsung Galaxy a15 5g', 
                'samsung Galaxy a25 5g', 'samsung Galaxy a35 5g', 'samsung Galaxy a55 5g', 'samsung Galaxy s24', 
                'samsung Galaxy s24+', 'samsung Galaxy s24 ultra', 'samsung Galaxy s24 fe', 'samsung Galaxy z flip6', 
                'samsung Galaxy z fold6', 'samsung Galaxy a06', 'samsung Galaxy a16 5g', 'samsung Galaxy m15 5g', 
                'samsung Galaxy m35 5g', 'samsung Galaxy m55 5g'
            ],
            'XIAOMI': [
                'XIAOMI Redmi note 14', 'XIAOMI Redmi note 14 pro plus 5g', 'XIAOMI 17 ultra', 'XIAOMI Mix fold 4', 
                'XIAOMI 14 ultra', 'XIAOMI Redmi note 14 pro', 'XIAOMI Redmi note 15 pro 5g', 'XIAOMI Redmi note 15 pro 4g', 
                'XIAOMI Redmi 15c', 'XIAOMI Redmi 14c', 'XIAOMI Redmi 13c', 'XIAOMI Redmi note 15 pro plus 5g', 
                'XIAOMI Redmi note 13', 'XIAOMI Redmi note 13 pro plus 5g', 'XIAOMI Redmi note 15', 'XIAOMI 15t', 
                'XIAOMI 14t pro', 'XIAOMI Redmi 15', 'XIAOMI Poco x7', 'XIAOMI Poco x7 pro', 'XIAOMI Poco f7', 
                'XIAOMI Poco f7 pro', 'XIAOMI 15t pro', 'XIAOMI 15', 'XIAOMI 15 ultra', 'XIAOMI Poco m6 pro', 
                'XIAOMI Poco x6', 'XIAOMI Poco x6 pro', 'XIAOMI Poco f6', 'XIAOMI Poco f6 pro', 'XIAOMI Redmi a3', 
                'XIAOMI Redmi 13', 'XIAOMI Redmi note 13 pro 4g', 'XIAOMI Redmi note 13 pro 5g', 'XIAOMI 14t', 
                'XIAOMI 14', 'XIAOMI 14 pro', 'XIAOMI Poco x5', 'XIAOMI Poco x5 pro', 'XIAOMI Poco f5', 
                'XIAOMI Poco f5 pro', 'XIAOMI Redmi 12c', 'XIAOMI Redmi 12', 'XIAOMI Redmi note 12s', 
                'XIAOMI Redmi note 12 4g', 'XIAOMI Redmi note 12 pro', 'XIAOMI 13t pro', 'XIAOMI 13', 'XIAOMI 13 ultra'
            ],
            'REALME': [
                            'realme C51', 'realme C53', 'realme C55', 'realme Narzo 60x 5g', 'realme Narzo 60 5g', 
                'realme Narzo 60 pro 5g', 'realme 11 4g', 'realme 11x 5g', 'realme 11 pro+ 5g', 'realme Gt neo5 se', 
                'realme C61', 'realme C63', 'realme C65 4g', 'realme C65 5g', 'realme C67', 'realme Narzo n65 5g', 
                'realme Narzo 70x 5g', 'realme Narzo 70 pro 5g', 'realme 12+ 5g', 'realme 13+ 5g', 'realme 13 pro+ 5g', 
                'realme Gt 6t', 'realme 14 pro 5g', 'realme 14 pro+ 5g', 'realme 16 5g'
            ],
            'HONOR': [
                'Honor Magic 7 pro', 'Honor Magic 6 pro', 'Honor 200 pro', 'Honor X9c', 'Honor X8b', 
                'Honor X7b', 'Honor 90', 'Honor X9a', 'Honor Magic 5 lite', 'Honor X6b'
            ],
            'GOOGLE': [
                'google Pixel 9 pro xl', 'google Pixel 9', 'google Pixel 8 pro', 'google Pixel 8a', 
                'google Pixel 7 pro', 'google Pixel 7a', 'google Pixel 6 pro', 'google Pixel 6a'
            ]
        }
        
        self.iphone_data = ['iphone11', 'iphone11 pro', 'iphone11 pro max', 'iphone12', 'iphone12 mini', 
                            'iphone12 pro', 'iphone12 pro max', 'iphone13', 'iphone13 mini', 'iphone13 pro',
                            'iphone13 pro max', 'iphone14', 'iphone14 plus', 'iphone14 pro', 'iphone14 pro max',
                            'iphone15', 'iphone15 plus', 'iphone15 pro', 'iphone15 pro max', 'iphone16', 'iphone16 plus',
                            ' iphone16 pro', ' iphone16 pro max', ' iphone17', ' iphone17 air', ' iphone17 pro', ' iphone17 pro max']

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both")

        self.current_page = "welcome"
        self.show_welcome_screen()

    def load_old_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                self.saved_data_list = list(reader)

    def save_to_csv(self, data_list):
        with open(self.file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data_list)

    def toggle_language(self):
        self.lang = "AR" if self.lang == "EN" else "EN"
        self.refresh_page()

    def refresh_page(self):
        self.clear_screen()
        if self.current_page == "welcome": 
            self.show_welcome_screen()
        elif self.current_page == "platform": 
            self.show_platform_selection()
        elif self.current_page == "brands": 
            self.show_android_brands()
        elif self.current_page == "details": 
            self.show_device_details(self.last_brand, self.last_models)
        elif self.current_page == "result": 
            self.show_result_screen(self.last_price, self.last_details)
            
    def clear_screen(self):
        for widget in self.container.winfo_children(): widget.destroy()

    def save_to_csv(self, filename, data_list):
        import os, csv 
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                if "android" in filename:
                    writer.writerow(["Brand", "Model", "RAM", "Storage", "Fix_Status", "Condition", "Predicted_Price"])
                else:
                    writer.writerow(["Brand", "Model", "Storage", "Battery_Health", "Fix_Status", "Condition", "Predicted_Price"])
            writer.writerow(data_list)
    
    def create_header(self, text):
        header = ctk.CTkFrame(self.container, fg_color="#BCE3D8", height=70, corner_radius=15)
        header.pack(fill="x", padx=100, pady=(20, 10))
        header.pack_propagate(False) 
        ctk.CTkLabel(header, text=text, font=("Segoe UI", 22, "bold"), text_color="#1A4D4E").place(relx=0.5, rely=0.5, anchor="center")
        lang_txt = "English" if self.lang == "AR" else "العربية"
        ctk.CTkButton(header, text=lang_txt, command=self.toggle_language, width=80, height=32, corner_radius=10,
                      fg_color="#A8D5C8", hover_color="#92C7B8", text_color="#1A4D4E", font=("Segoe UI", 12, "bold")).place(relx=0.98, rely=0.5, anchor="e")
        return header

    def add_back_button(self, header, target_command):
        t = self.texts[self.lang]
        ctk.CTkButton(header, text=t['back'], command=target_command, width=90, height=35, corner_radius=12,
                      fg_color="#A8D5C8", hover_color="#92C7B8", text_color="#1A4D4E", font=("Segoe UI", 13, "bold")).place(relx=0.02, rely=0.5, anchor="w")

    def show_welcome_screen(self):
        self.current_page = "welcome"
        self.clear_screen()
        t = self.texts[self.lang]
        self.create_header(t['welcome_title'])
        ctk.CTkLabel(self.container, text="📱", font=("Segoe UI", 120)).pack(pady=(40, 10))
        ctk.CTkLabel(self.container, text=t['subtitle'], font=("Segoe UI", 18), text_color="#555555").pack(pady=10)
        ctk.CTkButton(self.container, text=t['start'], command=self.show_platform_selection,
                      corner_radius=25, fg_color="#FF9F67", hover_color="#E88F5C",
                      font=("Segoe UI", 24, "bold"), height=60, width=320).pack(pady=40)

    def show_platform_selection(self):
        self.current_page = "platform"
        self.clear_screen()
        t = self.texts[self.lang]
        h = self.create_header(t['platform_title'])
        self.add_back_button(h, self.show_welcome_screen)
        
        btn_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        btn_frame.pack(expand=True)

        ctk.CTkButton(btn_frame, text=t['android'], image=self.android_logo, compound="top",
                      command=self.show_android_brands,
                      width=240, height=220, corner_radius=30, fg_color="white", border_width=2,
                      border_color="#BCE3D8", text_color="#1A4D4E", font=("Segoe UI", 24, "bold")).grid(row=0, column=0, padx=20)

        ctk.CTkButton(btn_frame, text=t['iphone'], image=self.iphone_logo, compound="top",
                      command=lambda: self.show_device_details("APPLE", self.iphone_data),
                      width=240, height=220, corner_radius=30, fg_color="white", border_width=2,
                      border_color="#BCE3D8", text_color="#1A4D4E", font=("Segoe UI", 24, "bold")).grid(row=0, column=1, padx=20)

    def show_android_brands(self):
        self.current_page = "brands"
        self.clear_screen()
        t = self.texts[self.lang]
        h = self.create_header(t['android_brands'])
        self.add_back_button(h, self.show_platform_selection)
        
        scroll = ctk.CTkScrollableFrame(self.container, fg_color="transparent", width=500, height=450)
        scroll.pack(pady=30)
        for brand in self.brands_data.keys():
            ctk.CTkButton(scroll, text=brand, command=lambda b=brand: self.show_device_details(b, self.brands_data[b]),
                          width=400, height=55, corner_radius=15, fg_color="white", border_width=1,
                          border_color="#BCE3D8", text_color="#1A4D4E", font=("Segoe UI", 18, "bold")).pack(pady=8)

    def show_device_details(self, brand, models):
        self.current_page = "details"
        self.last_brand, self.last_models = brand, models
        self.clear_screen()
        t = self.texts[self.lang]
        h = self.create_header(f"{brand} {t['specs_title']}")
        back_dest = self.show_android_brands if brand != "APPLE" else self.show_platform_selection
        self.add_back_button(h, back_dest)

        form = ctk.CTkScrollableFrame(self.container, fg_color="white", width=550, height=550, corner_radius=25, border_width=2, border_color="#BCE3D8")
        form.pack(pady=20)

        def add_field(label_key, values, is_entry=False):
            align = "w" if self.lang == "EN" else "e"
            ctk.CTkLabel(form, text=t[label_key], font=("Segoe UI", 15, "bold"), text_color="#1A4D4E").pack(pady=(12, 2), padx=40, anchor=align)
            if is_entry:
                entry = ctk.CTkEntry(form, width=420, height=40, corner_radius=10); entry.pack(pady=5); return entry
            else:
                menu = ctk.CTkOptionMenu(form, values=values, width=420, height=40, fg_color="#F0F9F7", button_color="#BCE3D8", text_color="#1A4D4E", corner_radius=10); menu.pack(pady=5); return menu

        self.m_menu = add_field('model_lbl', models)
        self.ram_menu = add_field('ram_lbl', ["4 GB","6 GB", "8 GB", "12 GB", "16 GB", "24 GB"]) if brand != "APPLE" else None
        self.mem_menu = add_field('mem_lbl', ["64 GB", "128 GB", "256 GB", "512 GB", "1 TB"])
        self.batt_entry = add_field('batt_lbl', [], True) if brand == "APPLE" else None
        self.fix_menu = add_field('fix_lbl', ["No Fix", "Fixed"])
        self.cond_menu = add_field('cond_lbl', ["Excellent", "Good", "Average", "Poor"])

        ctk.CTkButton(form, text=t['save'], command=self.save_and_finish, fg_color="#FF9F67", height=55, width=300, corner_radius=20, font=("Segoe UI", 18, "bold")).pack(pady=40)

    def egypt_market_final_logic(self, phone_name, ram, storage, condition, needs_fix):
        model_code = brand_model_mapping.get(phone_name, 0)

        features = pd.DataFrame([[ram, storage, condition, model_code, 0, 0, 0, 0, 1]], columns=X.columns)
        raw_pred = rf_model.predict(features)[0]

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
            found_special_limit = False
            for key in xiaomi_limits:
                if key in name_lower:
                    current_limit = xiaomi_limits[key]
                    found_special_limit = True
                    break
            
            if not found_special_limit:
                if raw_pred > 35000 and "ultra" not in name_lower:
                    current_limit = {"min": 15000, "max": 25000}
        else:
            for key in samsung_realme_limits:
                if key in name_lower:
                    current_limit = samsung_realme_limits[key]
                    break

        base_price = max(min(raw_pred, current_limit['max']), current_limit['min'])

        if needs_fix == 1:
            base_price -= 10000 if base_price > 30000 else 2000

        multipliers = {4: 1.0, 3: 0.90, 2: 0.82, 1: 0.70}
        return base_price * multipliers.get(condition, 1.0)

    def iphone_final_logic(self, phone_name, storage_text, battery_val, condition_text, fix_text):
        try:
            clean_name = phone_name.lower().replace("apple ", "").replace("iphone ", "iphone").strip()
            
            m_encoded = iphone_mapping.get(clean_name, 0)
            
            storage = int(''.join(filter(str.isdigit, storage_text)))
            if "tb" in storage_text.lower(): 
                storage = 1024
            
            fix_val = 1 if fix_text.lower() == "fixed" else 0
            
            condition_map = {"Excellent": 4, "Good": 3, "Average": 2, "Poor": 1}
            cond_val = condition_map.get(condition_text, 4)

            b_val = int(battery_val) if battery_val else 100

            input_df = pd.DataFrame([[
                m_encoded, storage, b_val, cond_val, fix_val
            ]], columns=['Model_Encoded', 'Storage', 'Battery_Health', 'Condition', 'FIX'])
            
            base_prediction = iphone_model.predict(input_df)[0]

            adjustment_factors = {
                4: 1.0,    # Excellent
                3: 0.94,   # Good
                2: 0.85,   # Average/Fair
                1: 0.72    # Poor
            }
            
            factor = adjustment_factors.get(cond_val, 1.0)
            final_price = base_prediction * factor

            if fix_val == 1:
                final_price = final_price * 0.90 

            return round(final_price, 2)

        except Exception as e:
            return f"Error: {str(e)}"

    def save_and_finish(self):
        # 1. تحديد أي دالة حساب سنستخدم بناءً على نظام التشغيل
        if self.last_brand == "APPLE":
            # استدعاء دالة حساب سعر الآيفون
            final_price = self.iphone_final_logic(
                self.m_menu.get(),
                self.mem_menu.get(),
                self.batt_entry.get(),
                self.cond_menu.get(),
                self.fix_menu.get()
            )
            
            target_file = self.iphone_csv
            data = [
                self.last_brand, 
                self.m_menu.get(), 
                self.mem_menu.get(), 
                self.batt_entry.get() if hasattr(self, 'batt_entry') else "N/A", 
                self.fix_menu.get(), 
                self.cond_menu.get(), 
                round(final_price, 0)
            ]
        else:
            # استدعاء دالة حساب سعر الأندرويد
            # ملاحظة: تأكد من تحويل الحالة إلى أرقام إذا كانت دالتك تتطلب ذلك
            cond_map = {"Excellent": 4, "Good": 3, "Average": 2, "Poor": 1}
            fix_map = {"No Fix": 0, "Fixed": 1}
            
            final_price = self.egypt_market_final_logic(
                self.m_menu.get(),
                int(''.join(filter(str.isdigit, self.ram_menu.get()))),
                int(''.join(filter(str.isdigit, self.mem_menu.get()))),
                cond_map.get(self.cond_menu.get(), 4),
                fix_map.get(self.fix_menu.get(), 0)
            )

            target_file = self.android_csv
            data = [
                self.last_brand, 
                self.m_menu.get(), 
                self.ram_menu.get() if hasattr(self, 'ram_menu') else "N/A", 
                self.mem_menu.get(), 
                self.fix_menu.get(), 
                self.cond_menu.get(), 
                round(final_price, 0)
            ]

        self.save_to_csv(target_file, data)

        self.last_price = final_price
        self.last_details = data

        self.show_result_screen(self.last_price, self.last_details)

    def show_result_screen(self, price, details):
        self.current_page = "result"
        self.clear_screen()
        t = self.texts[self.lang]
        
        h = self.create_header(t['result_title'])

        info_card = ctk.CTkFrame(self.container, fg_color="white", width=550, height=180, 
                                 corner_radius=35, border_width=2, border_color="#BCE3D8")
        info_card.pack(pady=(60, 40))
        info_card.pack_propagate(False)

        model_name = details[1]
        ctk.CTkLabel(info_card, text=model_name, font=("Segoe UI", 28, "bold"), text_color="#1A4D4E").pack(pady=(40, 5))

        if self.last_brand == "APPLE":
            specs_line = f"Storage: {details[2]} | Battery: {details[3]}% | Fix: {details[4]} | Condition: {details[5]}"
        else:
            specs_line = f"RAM: {details[2]} | Storage: {details[3]} | Condition: {details[5]} | Fix: {details[4]}"
        
        ctk.CTkLabel(info_card, text=specs_line, font=("Segoe UI", 15), text_color="#7F8C8D").pack()

        ctk.CTkLabel(self.container, text=t['price_is'], font=("Segoe UI", 20), text_color="#555555").pack(pady=(20, 0))

        display_price = f"{price:,.0f} {t['currency']}" if isinstance(price, (int, float)) else price
        ctk.CTkLabel(self.container, text=display_price, font=("Segoe UI", 55, "bold"), text_color="#FF9F67").pack(pady=(5, 40))

        ctk.CTkButton(self.container, text="Finish ✅", command=self.show_welcome_screen, 
                      fg_color="#FF9F67", hover_color="#E88F5C", width=280, height=55, 
                      corner_radius=20, font=("Segoe UI", 20, "bold")).pack(pady=20)

if __name__ == "__main__":
    app = SmartApp()
    app.mainloop()