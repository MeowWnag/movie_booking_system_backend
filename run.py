from app import create_app  # 請替換為你實際的套件名稱

# 使用 create_app 工廠函數創建 Flask 應用
app = create_app()

# 檢查是否直接運行該檔案
if __name__ == "__main__":
    app.run()
