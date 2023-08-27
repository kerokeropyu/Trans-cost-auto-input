import calendar
from datetime import datetime, date
import jpholiday
import configparser
# import datetime
from ConfigReader import ConfigReader


class TransportationCalculator:
    def __init__(self):
        # 設定情報をconfig.iniから読み取る
        config = configparser.ConfigParser()
        config.read('config.ini')

        # 使用例
        config_file_path = "config.ini"  # 設定ファイルのパス
        config_reader = ConfigReader(config_file_path)

        one_way_cost = config_reader.get_setting("Settings", "one_way_cost")
        telework_weekdays = config_reader.get_setting("Settings", "telework_weekdays").split(",")
        days_off = config_reader.get_setting("Settings", "days_off")
        
    
    def calculate_transportation_cost(self):
        # 現在の年月を取得
        today = date.today()
        year = today.year
        month = today.month
    
        # 土日祝を除いた労働日数を計算
        work_days = self._except_weekends_and_holidays(year, month, self.paid_leave_days)
    
        # テレワーク日数を除いた日数を計算
        telework_days = self._except_telework(year, month, self.telework_weekdays)
        commute_days = work_days - telework_days
    
        # 交通費の合計を計算
        total_cost = commute_days * self.one_way_cost * 2
    
        return total_cost
    
    def _except_weekends_and_holidays(self, year, month, paid_leave_days):
        # 月の日数を取得
        num_days = calendar.monthrange(year, month)[1]
    
        # 祝日を取り除く
        holidays = jpholiday.between(date(year, month, 1), date(year, month, num_days))
        holidays_and_weekends = [holiday for holiday in holidays]
        # for day in range(1, num_days + 1):
        #     if datetime(year, month, day).weekday() >= 5 or datetime(year, month, day) in holidays_and_weekends:
        #         holidays_and_weekends += 1
    
        # # 有給取得日数を考慮
        # work_days = num_days - len(holidays_and_weekends) - paid_leave_days
        return 1
    
    def _except_telework(self, year, month, tele_weekdays):
        # テレワーク日数を計算
        telework_days = 0
        num_days = calendar.monthrange(year, month)[1]
    
        for day in range(1, num_days + 1):
            if datetime(year, month, day).strftime('%A') in tele_weekdays:
                telework_days += 1
    
        return telework_days

