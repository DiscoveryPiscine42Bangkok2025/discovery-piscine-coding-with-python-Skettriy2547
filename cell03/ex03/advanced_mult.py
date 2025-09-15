import sys

# ตรวจสอบว่ามีการส่งอาร์กิวเมนต์ (argument) เข้ามาตอนรันโปรแกรมหรือไม่
if len(sys.argv) > 1:
    print("none")
else:
    # Loop ที่ 1: สำหรับวนสร้างตารางแม่สูตรคูณตั้งแต่ 0 ถึง 10
    outer_loop_counter = 0
    while outer_loop_counter <= 10:
        print(f"Table de {outer_loop_counter}: ", end="")
        
        # Loop ที่ 2: สำหรับวนคูณเลขในแต่ละแม่สูตรคูณตั้งแต่ 0 ถึง 10
        inner_loop_counter = 0
        while inner_loop_counter <= 10:
            result = outer_loop_counter * inner_loop_counter
            # ใช้ end=" " เพื่อให้ผลลัพธ์แสดงในบรรทัดเดียวกัน
            print(result, end="")
            
            # เพิ่มเว้นวรรคหลังตัวเลข (ยกเว้นตัวสุดท้าย)
            if inner_loop_counter < 10:
                print(" ", end="")
            
            inner_loop_counter = inner_loop_counter + 1
        
        # ขึ้นบรรทัดใหม่เมื่อจบแต่ละตาราง
        print()
        outer_loop_counter = outer_loop_counter + 1