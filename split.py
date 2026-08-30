import os

# تحديد اسم ملف الخليج بالامتداد الصحيح لجهازك الحين
input_file = "gccstates260826osm_0.js"
output_dir = "split_parts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("⏳ جاري تفتيت وتقسيم ملف الخليج بالكامل غصب عن النظام... يرجى الانتظار ثواني...")

# حجم الجزء (42 ميجابايت ليناسب مستودع Supabase المجاني)
chunk_size = 42 * 1024 * 1024 
part_num = 1

with open(input_file, 'r', encoding='utf-8') as f:
    header = f.readline()
    while True:
        lines = f.readlines(chunk_size)
        if not lines:
            break
        output_file = os.path.join(output_dir, f"gcc_part_{part_num}.js")
        with open(output_file, 'w', encoding='utf-8') as out:
            if part_num > 1 and len(lines) > 0 and "json_" not in lines:
                out.write(header)
            out.writelines(lines)
        print(f"✅ تم إنتاج وحفظ: gcc_part_{part_num}.js")
        part_num += 1