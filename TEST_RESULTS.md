# 任務三：執行測試，觀察綠燈與紅燈結果

## 測試結果記錄

### 綠燈（通過）測試結果

執行 Copilot 生成的單元測試後，所有預期的測試案例都通過，顯示為綠燈。

**測試執行命令：**
```bash
python -m unittest test_safe_division.py -v
```

**測試結果：**
```
test_both_negative (test_safe_division.TestSafeDivision.test_both_negative)
Test division with both negative numbers ... ok

test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero - Critical test case ... ok

test_float_division (test_safe_division.TestSafeDivision.test_float_division)
Test division with float numbers ... ok

test_large_numbers (test_safe_division.TestSafeDivision.test_large_numbers)
Test division with large numbers ... ok

test_negative_denominator (test_safe_division.TestSafeDivision.test_negative_denominator)
Test division with negative denominator ... ok

test_negative_division_by_zero (test_safe_division.TestSafeDivision.test_negative_division_by_zero)
Test division by zero with negative numerator ... ok

test_negative_numerator (test_safe_division.TestSafeDivision.test_negative_numerator)
Test division with negative numerator ... ok

test_normal_division (test_safe_division.TestSafeDivision.test_normal_division)
Test normal division with positive numbers ... ok

test_small_numbers (test_safe_division.TestSafeDivision.test_small_numbers)
Test division with very small numbers ... ok

test_zero_divided_by_zero (test_safe_division.TestSafeDivision.test_zero_divided_by_zero)
Test zero divided by zero edge case ... ok

test_zero_numerator (test_safe_division.TestSafeDivision.test_zero_numerator)
Test division with zero as numerator ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```

**測試通過的案例包括：**
1. ✅ 正常數值相除（10 / 2 = 5.0）
2. ✅ 負數相除（-10 / 2 = -5.0）
3. ✅ 負數除數（10 / -2 = -5.0）
4. ✅ 兩個負數相除（-10 / -2 = 5.0）
5. ✅ 浮點數除法（7 / 2 = 3.5）
6. ✅ 零作為被除數（0 / 5 = 0.0）
7. ✅ **除以零（10 / 0 = None）** - 關鍵測試
8. ✅ 負數除以零（-10 / 0 = None）
9. ✅ 零除以零（0 / 0 = None）
10. ✅ 大數字相除（1000000 / 1000 = 1000.0）
11. ✅ 小數字相除（0.001 / 0.1 = 0.01）

這代表 `safe_division` 函式能正確處理各種情境，包含處理除以零的狀況，使程式不會當機。

---

## 紅燈（失敗）測試場景

### 模擬：移除除以零的處理機制

當我將 `safe_division` 函式中的「處理除以零」的程式碼（try-except 區塊）移除後，再次執行單元測試，結果會出現紅燈。

**修改後的程式碼（移除防呆機制）：**
```python
def safe_division(a, b):
    # 移除了 try-except 區塊
    return a / b
```

**預期的測試失敗結果：**

失敗的測試案例會是：
- `test_division_by_zero` - 當 b 為零時的測試
- `test_negative_division_by_zero` - 負數除以零的測試
- `test_zero_divided_by_zero` - 零除以零的測試

### 哪個測試失敗？請簡單說明原因：

**失敗的測試：**
- `test_division_by_zero`
- `test_negative_division_by_zero`
- `test_zero_divided_by_zero`

**失敗原因：**

失敗的是測試「當 b 為零時，safe_division 是否能妥善處理」的單元測試。原因是函式內部沒有處理除以零的例外（移除了 try-except 區塊），導致執行時直接拋出 `ZeroDivisionError` 錯誤，而測試預期函式應該回傳 `None`。因此，這也證明了防呆機制的重要性，能讓程式更加穩定安全。

具體來說：
1. **原本的行為（有防呆機制）：** 當執行 `safe_division(10, 0)` 時，函式捕獲 `ZeroDivisionError` 並回傳 `None`
2. **移除防呆機制後的行為：** 當執行 `safe_division(10, 0)` 時，Python 直接拋出 `ZeroDivisionError` 例外，測試無法通過
3. **測試預期：** 測試使用 `self.assertIsNone(result)` 來驗證函式應該回傳 `None`，而不是拋出例外

### 實際驗證（建立測試用版本）

為了驗證紅燈場景，我們建立了一個沒有防呆機制的版本供測試：

**測試執行命令：**
```bash
python -m unittest test_safe_division_unsafe.py -v
```

**實際的紅燈測試結果：**
```
test_division_by_zero (test_safe_division_unsafe.TestUnsafeDivision.test_division_by_zero)
Test division by zero - This will FAIL ... ERROR

test_negative_division_by_zero (test_safe_division_unsafe.TestUnsafeDivision.test_negative_division_by_zero)
Test division by zero with negative numerator - This will FAIL ... ERROR

test_normal_division (test_safe_division_unsafe.TestUnsafeDivision.test_normal_division)
Test normal division with positive numbers ... ok

test_zero_divided_by_zero (test_safe_division_unsafe.TestUnsafeDivision.test_zero_divided_by_zero)
Test zero divided by zero - This will FAIL ... ERROR

======================================================================
ERROR: test_division_by_zero (test_safe_division_unsafe.TestUnsafeDivision.test_division_by_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division_unsafe.py", line 27, in test_division_by_zero
    result = safe_division(10, 0)
  File "safe_division_unsafe.py", line 17, in safe_division
    return a / b
ZeroDivisionError: division by zero

======================================================================
ERROR: test_negative_division_by_zero (test_safe_division_unsafe.TestUnsafeDivision.test_negative_division_by_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division_unsafe.py", line 32, in test_negative_division_by_zero
    result = safe_division(-10, 0)
  File "safe_division_unsafe.py", line 17, in safe_division
    return a / b
ZeroDivisionError: division by zero

======================================================================
ERROR: test_zero_divided_by_zero (test_safe_division_unsafe.TestUnsafeDivision.test_zero_divided_by_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division_unsafe.py", line 37, in test_zero_divided_by_zero
    result = safe_division(0, 0)
  File "safe_division_unsafe.py", line 17, in safe_division
    return a / b
ZeroDivisionError: division by zero

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=3)
```

**結果分析：**
- ❌ 3 個測試失敗（ERROR）
- ✅ 1 個測試通過（正常除法測試）

所有與「除以零」相關的測試都失敗了，因為程式直接拋出 `ZeroDivisionError` 例外，而不是像預期的那樣回傳 `None`。

---

## 結論

### 綠燈與紅燈的對比

| 測試場景 | 有防呆機制（safe_division.py） | 無防呆機制（safe_division_unsafe.py） |
|---------|--------------------------|------------------------------|
| 正常除法 | ✅ 通過 | ✅ 通過 |
| 除以零測試 | ✅ 通過（回傳 None） | ❌ 失敗（拋出 ZeroDivisionError） |
| 總測試數 | 11 個全部通過 | 4 個測試中 3 個失敗 |

### 重要性說明

這個實驗清楚地展示了：

1. **防呆機制的必要性：** try-except 區塊確保程式遇到除以零時不會崩潰
2. **測試驅動開發的價值：** 單元測試能夠快速發現程式中的問題
3. **程式穩定性：** 有了適當的錯誤處理，程式能夠優雅地處理異常情況
4. **使用者體驗：** 回傳 None 比讓程式崩潰提供了更好的使用者體驗

通過這個練習，我們證明了單元測試和防呆機制對於編寫高品質、穩定的程式碼至關重要。
