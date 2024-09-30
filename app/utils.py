import datetime  # 引入datetime模組

# 格式化日期時間
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    """格式化日期時間。"""
    return value.strftime(format) if value else None  # 如果有值，則格式化日期時間，否則返回None

# 簡單的活動日誌函數
def log_activity(activity_type, details):
    """簡單的活動日誌函數，可擴展用於系統日誌記錄。"""
    print(f"[{datetime.datetime.now()}] {activity_type}: {details}")  # 輸出當前時間、活動類型和詳細信息
