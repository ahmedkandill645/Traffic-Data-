import pandas as pd
from pathlib import Path
from tabulate import tabulate  # مكتبة لعرض الجداول بشكل مرتب

# --- ترتيب الأعمدة المطلوب ---
desired_order = [
    "hotel","is_canceled","lead_time","arrival_date_year","arrival_date_month",
    "arrival_date_week_number","arrival_date_day_of_month","stays_in_weekend_nights",
    "stays_in_week_nights","adults","children","babies","meal","country","market_segment",
    "distribution_channel","is_repeated_guest","previous_cancellations",
    "previous_bookings_not_canceled","reserved_room_type","assigned_room_type",
    "booking_changes","deposit_type","agent","company","days_in_waiting_list",
    "customer_type","adr","required_car_parking_spaces","total_of_special_requests",
    "reservation_status","reservation_status_date"
]

# --- مسار ملف CSV الأصلي ---
csv_path = Path(r"D:\hotel_github_clone\hotel_bookings\hotel_bookings.csv")

# --- مسار حفظ الملفات الجديدة ---
output_dir = Path(r"D:\hotel_github_clone\hotel_bookings\read file")
output_dir.mkdir(parents=True, exist_ok=True)
output_csv_file = output_dir / "hotel_bookings_read.csv"
output_excel_file = output_dir / "hotel_bookings_read.xlsx"

# --- تحقق من وجود الملف الأصلي ---
print("🔍 هل الملف موجود؟", csv_path.exists())
print("حجم الملف (بايت):", csv_path.stat().st_size if csv_path.exists() else "غير موجود")
print("-" * 50)

if not csv_path.is_file():
    print("❌ ملف CSV غير موجود، تأكد من المسار")
    exit()

# --- قراءة CSV مع جعل أول صف كـ Header ---
df = pd.read_csv(csv_path, header=0, encoding="latin1", low_memory=False)

print("✅ تم قراءة الملف بنجاح")
print("صفوف:", df.shape[0], "| أعمدة:", df.shape[1])
print("\n👀 أسماء الأعمدة:")
print(df.columns)
print("-" * 50)

# --- إعادة ترتيب الأعمدة حسب desired_order ---
# لو في أعمدة ناقصة في DataFrame، يتجاهلها بدون خطأ
existing_columns = [col for col in desired_order if col in df.columns]
df = df[existing_columns]

# --- عرض أول 10 صفوف في هيئة جدول tabular ---
print("👀 أول 10 صفوف في شكل جدول:")
print(tabulate(df.head(10), headers='keys', tablefmt='grid', showindex=False))
print("-" * 50)

# --- حفظ CSV جديد بصيغة UTF-8 مع BOM لتسهيل الفتح في Excel ---
df.to_csv(output_csv_file, index=False, encoding="utf-8-sig")

# --- حفظ البيانات في ملف Excel بنفس ترتيب الأعمدة ---
df.to_excel(output_excel_file, index=False)

# --- رسالة تأكيدية ---
print("📁 الملفات اتحفظت وجاهزة للفتح:")
print("CSV:", output_csv_file, "| موجود؟", output_csv_file.exists())
print("Excel:", output_excel_file, "| موجود؟", output_excel_file.exists())
