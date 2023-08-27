import calendar
from datetime import datetime

def except_telework(num_days: int, tele_weekdays) -> int:
    # テレワーク日数を計算
    telework_days = 0
    for i in range(1, num_days + 1):
        if datetime(year, month, i).strftime('%A') not in tele_weekdays:
            telework_days += 1
    return telework_days

def cal_tran_cost(year, month, one_way_cost, tele_weekdays, days_off):
    # 月の日数を取得
    num_days1 = calendar.monthrange(year, month)[1]
    
    # 休日を除いた日数を計算
    work_days = num_days1 - days_off
    
    # テレワーク日数を除いた日数を計算
    commute_days = work_days - except_telework(num_days1, tele_weekdays)
    
    # 交通費の合計を計算
    total_cost = commute_days * one_way_cost * 2
    
    # 計算式を表示
    print(f"{commute_days} days * {one_way_cost} yen * 2 = {total_cost} yen")
    
    return total_cost

if __name__ == "__main__":
    year = 2022
    month = 11
    one_way_cost = 250
    telework_weekdays = ['Monday', 'Wednesday']
    days_off = 2
    
    total_cost = cal_tran_cost(year, month, one_way_cost, telework_weekdays, days_off)
    print(f"{year}/{month}: {total_cost} yen")
