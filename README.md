# Safe Division Function

這是一個 Python 專案，包含一個防呆的除法函式，能夠防止除以零的錯誤。

## 功能說明

`safe_division(a, b)` 函式提供安全的除法運算：
- 當除數不為零時，返回正常的除法結果
- 當除數為零時，返回 `None` 而不是拋出錯誤

## 使用方法

```python
from safe_division import safe_division

# 正常除法
result = safe_division(10, 2)  # 返回 5.0

# 除以零的情況（防呆處理）
result = safe_division(10, 0)  # 返回 None

# 負數除法
result = safe_division(-10, 2)  # 返回 -5.0

# 浮點數除法
result = safe_division(7, 3)  # 返回 2.3333333333333335
```

## 測試

執行測試套件：

```bash
python3 -m unittest test_safe_division.py -v
```

## 檔案結構

- `safe_division.py` - 包含 safe_division 函式的主要程式碼
- `test_safe_division.py` - 完整的測試套件
- `README.md` - 本說明文件