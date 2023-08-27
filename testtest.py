from TransportationCalculator import TransportationCalculator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# TransportationCalculatorのインスタンスを作成
calculator = TransportationCalculator()

# 交通費を計算
total_cost = calculator.calculate_transportation_cost()

# 実行時のバージョンと同様の ChromeDriverをインストール
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# # Seleniumのドライバーを設定（Chromeドライバーを使用する例）
# driver = webdriver.Chrome(executable_path="path_to_chromedriver.exe")  # Chromeドライバーのパスを指定

# ウェブサイトにアクセス
driver.get("https://service.kaonavi.jp/")

# 必要な入力フィールドに交通費を入力
input_field = driver.find_element_by_id("transportation_cost_input_id")  # 入力フィールドのIDを指定
input_field.clear()  # 一度入力内容をクリア
input_field.send_keys(str(total_cost))  # 交通費を入力

# 送信ボタンをクリック（ボタンの要素とIDやクラス名を使って特定）
submit_button = driver.find_element_by_id("submit_button_id")  # 送信ボタンのIDを指定
submit_button.click()

# 送信完了を待つために一時停止（必要に応じて調整）
time.sleep(5)

# ドライバーを終了
driver.quit()
