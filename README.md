# Task 3: Unit Testing with safe_division

## 概述 (Overview)

這個專案展示了單元測試的重要性，特別是如何透過測試來驗證防呆機制（除以零的處理）。

This project demonstrates the importance of unit testing, especially how to verify defensive programming mechanisms (handling division by zero).

## 檔案結構 (File Structure)

```
.
├── README.md                        # 本說明檔
├── safe_division.py                 # 安全除法函式（有防呆機制）
├── safe_division_unsafe.py          # 不安全版本（無防呆機制，用於示範）
├── test_safe_division.py            # 單元測試（測試安全版本）
├── test_safe_division_unsafe.py     # 單元測試（測試不安全版本）
└── TEST_RESULTS.md                  # 測試結果記錄
```

## 如何執行測試 (How to Run Tests)

### 執行安全版本的測試（綠燈場景）

```bash
python -m unittest test_safe_division.py -v
```

預期結果：所有 11 個測試都會通過 ✅

### 執行不安全版本的測試（紅燈場景）

```bash
python -m unittest test_safe_division_unsafe.py -v
```

預期結果：3 個除以零相關的測試會失敗 ❌

## 學習重點 (Key Learning Points)

1. **防呆機制的重要性：** `try-except` 區塊可以防止程式因為除以零而崩潰
2. **單元測試的價值：** 測試可以快速發現程式中的問題
3. **綠燈與紅燈：** 透過測試結果可以驗證程式的正確性

## 詳細測試結果 (Detailed Test Results)

請參閱 [TEST_RESULTS.md](TEST_RESULTS.md) 檔案查看完整的測試結果記錄。