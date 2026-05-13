import customtkinter as ctk
import csv
import os
from PIL import Image

ctk.set_appearance_mode("light") 

class SmartApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Price Predictor - 2026")
        self.geometry("700x900") 
        self.configure(fg_color="#F0F9F7") 

        base_path = os.path.dirname(__file__)
        iphone_path = os.path.join(base_path, "images.gif")
        self.iphone_logo = ctk.CTkImage(light_image=Image.open(iphone_path),
                                        dark_image=Image.open(iphone_path),
                                        size=(100, 100))
        
        android_path = os.path.join(base_path, "android-3383929_1280.gif")
        self.android_logo = ctk.CTkImage(light_image=Image.open(android_path),
                                         dark_image=Image.open(android_path),
                                         size=(100, 100))

        self.lang = "EN" 
        
        self.saved_data_list = [] 
        self.current_input = []  
        
        self.file_path = "phone_dataset.csv" 
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
                "model_lbl": "Select Model:",
                "ram_lbl": "RAM Capacity:",
                "mem_lbl": "Storage Memory:",
                "batt_lbl": "Battery Health (%):",
                "fix_lbl": "Repair Status:",
                "cond_lbl": "Device Condition:",
                "success": "Data Ready! ✅",
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
                "model_lbl": "اختر الموديل:",
                "ram_lbl": "سعة الرام:",
                "mem_lbl": "مساحة التخزين:",
                "batt_lbl": "صحة البطارية (%):",
                "fix_lbl": "حالة الصيانة:",
                "cond_lbl": "حالة الجهاز:",
                "success": "البيانات جاهزة! ✅",
                "android": "أندرويد",
                "iphone": "آيفون"
            }
        }

        # الداتا الأصلية كاملة كما طلبت
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
                'XIAOMI Redmi note 14', 'XIAOMI Redmi note 14 pro plus 5g', 'XIAOMI 14 ultra', 'XIAOMI Redmi note 13', 
                'XIAOMI Redmi note 13 pro plus 5g', 'XIAOMI 14t pro', 'XIAOMI Poco x6 pro', 'XIAOMI Poco f6', 
                'XIAOMI Redmi 13c', 'XIAOMI Redmi 12', 'XIAOMI 13 ultra', 'XIAOMI Poco x5 pro'
            ],
            'REALME': [
                'realme C51', 'realme C53', 'realme C55', 'realme 11 pro+ 5g', 'realme C61', 'realme C65', 
                'realme 12+ 5g', 'realme 13 pro+ 5g', 'realme Gt 6t', 'realme 11 4g'
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
        
        self.iphone_data = [f"Apple iPhone {i} {s}".strip() for i in range(11, 18) for s in ["", "Pro", "Pro Max"]]

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
        if self.current_page == "welcome": self.show_welcome_screen()
        elif self.current_page == "platform": self.show_platform_selection()
        elif self.current_page == "brands": self.show_android_brands()
        elif self.current_page == "details": self.show_device_details(self.last_brand, self.last_models)

    def clear_screen(self):
        for widget in self.container.winfo_children(): widget.destroy()

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
        self.ram_menu = add_field('ram_lbl', ["4 GB", "8 GB", "12 GB", "16 GB", "24 GB"]) if brand != "APPLE" else None
        self.mem_menu = add_field('mem_lbl', ["64 GB", "128 GB", "256 GB", "512 GB", "1 TB"])
        self.batt_entry = add_field('batt_lbl', [], True) if brand == "APPLE" else None
        self.fix_menu = add_field('fix_lbl', ["No Fix", "Fixed"])
        self.cond_menu = add_field('cond_lbl', ["Excellent", "Good", "Fair", "Poor"])

        ctk.CTkButton(form, text=t['save'], command=self.save_and_finish, fg_color="#FF9F67", height=55, width=300, corner_radius=20, font=("Segoe UI", 18, "bold")).pack(pady=40)

    def save_and_finish(self):
        if self.last_brand == "APPLE":
            temp_list = [
                self.last_brand,
                self.m_menu.get(),
                self.mem_menu.get(),
                self.batt_entry.get() if self.batt_entry.get() else "100",
                self.fix_menu.get(),
                self.cond_menu.get()
            ]
        else:
            temp_list = [
                self.last_brand,
                self.m_menu.get(),
                self.ram_menu.get(),
                self.mem_menu.get(),
                self.fix_menu.get(),
                self.cond_menu.get()
            ]

        self.current_input = temp_list
        self.saved_data_list.append(temp_list)
        self.save_to_csv(temp_list)
        
        print(f"--- DATA READY IN Variable 'self.current_input' ---")
        print(f"Content: {self.current_input}")
        
        t = self.texts[self.lang]
        msg = ctk.CTkLabel(self.container, text=t['success'], text_color="#27AE60", font=("Segoe UI", 20, "bold"))
        msg.place(relx=0.5, rely=0.9, anchor="center")
        
        self.after(1500, self.show_welcome_screen)

if __name__ == "__main__":
    app = SmartApp()
    app.mainloop()