#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tính toán FIRE cuối cùng với lãi suất 6% và 3 mốc cụ thể
"""

print("=== FIRE ANALYSIS - LÃI SUẤT 6% & 3 MỐC CỤ THỂ ===\n")

# 3 mốc FIRE theo hình ảnh
lean_fire = 750_000_000      # 750 triệu VND
regular_fire = 3_000_000_000  # 3 tỷ VND  
fat_fire = 15_000_000_000    # 15 tỷ VND

# Chi phí tương ứng
lean_fire_annual_cost = 30_000_000    # 30 triệu/năm
regular_fire_annual_cost = 120_000_000 # 120 triệu/năm
fat_fire_annual_cost = 500_000_000    # 500 triệu/năm (trung bình 480-600)

print(f"3 MỐC FIRE MỤC TIÊU:")
print(f"1. Lean FIRE: {lean_fire:,} VND (chi phí {lean_fire_annual_cost:,}/năm)")
print(f"2. Regular FIRE: {regular_fire:,} VND (chi phí {regular_fire_annual_cost:,}/năm)")
print(f"3. Fat FIRE: {fat_fire:,} VND (chi phí {fat_fire_annual_cost:,}/năm)")

# Thu nhập thụ động với lãi suất 6%
lean_fire_income = lean_fire * 0.06
regular_fire_income = regular_fire * 0.06
fat_fire_income = fat_fire * 0.06

print(f"\nTHU NHẬP THỤ ĐỘNG 6%/NĂM:")
print(f"1. Lean FIRE: {lean_fire_income:,.0f}/năm ({lean_fire_income/12:,.0f}/tháng)")
print(f"2. Regular FIRE: {regular_fire_income:,.0f}/năm ({regular_fire_income/12:,.0f}/tháng)")
print(f"3. Fat FIRE: {fat_fire_income:,.0f}/năm ({fat_fire_income/12:,.0f}/tháng)")

# Chi phí hiện tại của Cường
current_monthly_expenses = 2_500_000  # 2.5 triệu/tháng
current_annual_expenses = current_monthly_expenses * 12  # 30 triệu/năm

family_monthly_expenses = 10_000_000  # 10 triệu/tháng
family_annual_expenses = family_monthly_expenses * 12  # 120 triệu/năm

print(f"\nCHI PHÍ THỰC TẾ CỦA CƯỜNG:")
print(f"- Hiện tại (độc thân): {current_annual_expenses:,}/năm")
print(f"- Khi có gia đình: {family_annual_expenses:,}/năm")

# Timeline với lãi suất 6%
print(f"\n=== TIMELINE ĐẠT 3 MỐC FIRE (LÃI SUẤT 6%) ===")

portfolio = 0
timeline_data = [
    (2025, 22, 18_000_000, current_annual_expenses),   # 18 triệu/tháng
    (2026, 23, 25_000_000, current_annual_expenses),   # 25 triệu/tháng
    (2027, 24, 42_000_000, current_annual_expenses),   # 35 + 20% = 42 triệu/tháng
    (2028, 25, 60_000_000, current_annual_expenses),   # 50 + 20% = 60 triệu/tháng
    (2029, 26, 84_000_000, current_annual_expenses),   # 70 + 20% = 84 triệu/tháng
    (2030, 27, 120_000_000, family_annual_expenses),   # 100 + 20% = 120 triệu/tháng, có gia đình
    (2031, 28, 120_000_000, family_annual_expenses),   
    (2032, 29, 180_000_000, family_annual_expenses),   # 150 + 20% = 180 triệu/tháng
    (2033, 30, 180_000_000, family_annual_expenses),
    (2034, 31, 180_000_000, family_annual_expenses),
    (2035, 32, 240_000_000, family_annual_expenses),   # 200 + 20% = 240 triệu/tháng
    (2036, 33, 240_000_000, family_annual_expenses),
    (2037, 34, 240_000_000, family_annual_expenses),
    (2038, 35, 240_000_000, family_annual_expenses),
    (2039, 36, 240_000_000, family_annual_expenses),
    (2040, 37, 240_000_000, family_annual_expenses),
]

milestones = {
    lean_fire: "🥉 Lean FIRE",
    regular_fire: "🥈 Regular FIRE", 
    fat_fire: "🥇 Fat FIRE"
}

achieved_milestones = set()
milestone_years = {}

for year, age, monthly_income, annual_expenses in timeline_data:
    annual_income = monthly_income * 12
    disposable = annual_income - annual_expenses
    
    # Tỷ lệ tiết kiệm thực tế
    if disposable <= 0:
        savings_rate = 0
        annual_savings = 0
    elif annual_income <= 600_000_000:  # <= 50 triệu/tháng
        savings_rate = 0.6
        annual_savings = disposable * savings_rate
    elif annual_income <= 1_200_000_000:  # <= 100 triệu/tháng
        savings_rate = 0.5
        annual_savings = disposable * savings_rate
    else:
        savings_rate = 0.4
        annual_savings = disposable * savings_rate
    
    # Tăng trưởng portfolio với lãi suất 6%
    portfolio = portfolio * 1.06 + annual_savings
    
    # Kiểm tra milestones
    new_milestones = []
    for target, name in milestones.items():
        if portfolio >= target and name not in achieved_milestones:
            new_milestones.append(name)
            achieved_milestones.add(name)
            milestone_years[name] = {'year': year, 'age': age, 'portfolio': portfolio}
    
    # In thông tin quan trọng
    if year <= 2030 or new_milestones or year % 2 == 0:
        print(f"\nNăm {year} (tuổi {age}):")
        print(f"  Thu nhập: {monthly_income:,}/tháng ({annual_income:,}/năm)")
        print(f"  Chi phí: {annual_expenses:,}/năm")
        print(f"  Tiết kiệm: {annual_savings:,}/năm (tỷ lệ {savings_rate:.0%})")
        print(f"  Tài sản: {portfolio:,.0f} VND")
        print(f"  Thu nhập thụ động 6%: {portfolio * 0.06:,.0f}/năm ({portfolio * 0.06 / 12:,.0f}/tháng)")
        
        if new_milestones:
            print(f"  🎯 {', '.join(new_milestones)}")

# Tính thêm nếu chưa đạt Fat FIRE
if portfolio < fat_fire:
    print(f"\n=== TÍNH THÊM ĐỂ ĐẠT FAT FIRE ===")
    current_portfolio = portfolio
    current_income = 240_000_000 * 12  # 240 triệu/tháng
    current_expenses = family_annual_expenses
    current_savings = (current_income - current_expenses) * 0.4
    
    for extra_year in range(1, 15):
        current_portfolio = current_portfolio * 1.06 + current_savings
        final_year = 2040 + extra_year
        final_age = 37 + extra_year
        
        if current_portfolio >= fat_fire and "🥇 Fat FIRE" not in achieved_milestones:
            milestone_years["🥇 Fat FIRE"] = {'year': final_year, 'age': final_age, 'portfolio': current_portfolio}
            print(f"✅ Đạt Fat FIRE vào năm {final_year} (tuổi {final_age})")
            print(f"Tài sản: {current_portfolio:,.0f} VND")
            passive_monthly = (current_portfolio * 0.06) / 12
            print(f"Thu nhập thụ động: {passive_monthly:,.0f}/tháng")
            break

print(f"\n=== TÓM TẮT 3 MỐC FIRE ===")
for milestone_name in ["🥉 Lean FIRE", "🥈 Regular FIRE", "🥇 Fat FIRE"]:
    if milestone_name in milestone_years:
        info = milestone_years[milestone_name]
        print(f"{milestone_name}: Năm {info['year']} (tuổi {info['age']}) - {info['portfolio']:,.0f} VND")
    else:
        print(f"{milestone_name}: Chưa đạt trong timeline")

print(f"\n=== PHÂN TÍCH CHI TIẾT ===")

# Lean FIRE Analysis
if "🥉 Lean FIRE" in milestone_years:
    lean_info = milestone_years["🥉 Lean FIRE"]
    lean_passive = lean_info['portfolio'] * 0.06
    print(f"\n🥉 LEAN FIRE (Năm {lean_info['year']}):")
    print(f"   - Tài sản: {lean_info['portfolio']:,} VND")
    print(f"   - Thu nhập thụ động: {lean_passive:,.0f}/năm ({lean_passive/12:,.0f}/tháng)")
    print(f"   - Đủ chi phí độc thân: {lean_passive >= current_annual_expenses}")

# Regular FIRE Analysis  
if "🥈 Regular FIRE" in milestone_years:
    regular_info = milestone_years["🥈 Regular FIRE"]
    regular_passive = regular_info['portfolio'] * 0.06
    print(f"\n🥈 REGULAR FIRE (Năm {regular_info['year']}):")
    print(f"   - Tài sản: {regular_info['portfolio']:,} VND")
    print(f"   - Thu nhập thụ động: {regular_passive:,.0f}/năm ({regular_passive/12:,.0f}/tháng)")
    print(f"   - Đủ chi phí gia đình: {regular_passive >= family_annual_expenses}")

# Fat FIRE Analysis
if "🥇 Fat FIRE" in milestone_years:
    fat_info = milestone_years["🥇 Fat FIRE"]
    fat_passive = fat_info['portfolio'] * 0.06
    print(f"\n🥇 FAT FIRE (Năm {fat_info['year']}):")
    print(f"   - Tài sản: {fat_info['portfolio']:,} VND")
    print(f"   - Thu nhập thụ động: {fat_passive:,.0f}/năm ({fat_passive/12:,.0f}/tháng)")
    print(f"   - Lifestyle cao: Chi tiêu thoải mái 40-50 triệu/tháng")

print(f"\n=== KẾT LUẬN ===")
print("Với lãi suất 6%/năm và 3 mốc FIRE:")
print("- Lean FIRE: Đạt được trong 3-5 năm đầu")
print("- Regular FIRE: Đạt được khi có gia đình ổn định")  
print("- Fat FIRE: Mục tiêu dài hạn cho lifestyle cao")
print("- Cần duy trì tỷ lệ tiết kiệm 40-60% để đạt các mốc")

