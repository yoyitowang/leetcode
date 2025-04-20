讓我詳細解釋左中位數和右中位數的差異及其使用原理。

## 1. 基本定義

### 1.1 左中位數
```python
mid = (left + right) // 2
# 或者
mid = left + (right - left) // 2
```

### 1.2 右中位數
```python
mid = left + (right - left + 1) // 2
# 或者
mid = (left + right + 1) // 2
```

## 2. 實際例子說明

假設我們有一個區間 [3, 4]：

### 2.1 左中位數計算
```python
left = 3, right = 4
mid = (3 + 4) // 2 = 3  # 向下取整
```

### 2.2 右中位數計算
```python
left = 3, right = 4
mid = (3 + 4 + 1) // 2 = 4  # 向上取整
```

## 3. 為什麼需要區分？

關鍵在於避免死循環。讓我們看兩個典型場景：

### 3.1 查找第一個滿足條件的元素（使用左中位數）

```python
def find_first_greater_equal(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2  # 左中位數
        if nums[mid] >= target:
            right = mid    # 收縮右邊界
        else:
            left = mid + 1 # 收縮左邊界
    return left
```

在這種情況下，當 `nums[mid] >= target` 時，我們需要繼續向左查找，使用左中位數是安全的，因為：
- 如果 mid 處的值符合條件，我們將 right 設為 mid
- 如果 mid 處的值不符合條件，我們將 left 設為 mid + 1

### 3.2 查找最後一個滿足條件的元素（使用右中位數）

```python
def find_last_less_equal(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left + 1) // 2  # 右中位數
        if nums[mid] <= target:
            left = mid    # 收縮左邊界
        else:
            right = mid - 1 # 收縮右邊界
    return left
```

在這種情況下，必須使用右中位數，否則會陷入死循環：

## 4. 死循環示例

讓我們看一個具體例子來理解為什麼會發生死循環：

假設數組 `[1, 2]`，要找最後一個小於等於 2 的元素：

### 4.1 使用左中位數（錯誤示範）：
```python
初始：left = 0, right = 1
循環1：
    mid = (0 + 1) // 2 = 0
    nums[mid] = 1 <= 2
    left = mid = 0  # left 沒有變化！
循環2：
    mid = (0 + 1) // 2 = 0
    nums[mid] = 1 <= 2
    left = mid = 0  # 死循環！
```

### 4.2 使用右中位數（正確示範）：
```python
初始：left = 0, right = 1
循環1：
    mid = (0 + 1 + 1) // 2 = 1
    nums[mid] = 2 <= 2
    left = mid = 1
循環結束，因為 left == right
```

## 5. 選擇指南

### 5.1 使用左中位數當：
1. 向左收縮區間（right = mid）
2. 查找第一個滿足條件的元素
```python
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid       # 向左收縮
    else:
        left = mid + 1
```

### 5.2 使用右中位數當：
1. 向右收縮區間（left = mid）
2. 查找最後一個滿足條件的元素
```python
while left < right:
    mid = (left + right + 1) // 2
    if condition(mid):
        left = mid       # 向右收縮
    else:
        right = mid - 1
```

## 6. 實際應用：TimeMap 的例子

在 TimeMap 問題中，我們使用右中位數是因為：

```python
def get(self, key: str, timestamp: int) -> str:
    values = self.store[key]
    left, right = 0, len(values) - 1
    
    while left < right:
        # 使用右中位數，因為我們在向右收縮
        mid = left + ((right - left + 1) >> 1)
        if values[mid][0] <= timestamp:
            left = mid    # 向右收縮
        else:
            right = mid - 1
```

這裡使用右中位數的原因：
1. 我們在尋找最後一個小於等於 timestamp 的值
2. 當找到符合條件的值時，我們用 `left = mid` 向右收縮
3. 如果使用左中位數，可能會在區間長度為 2 時陷入死循環

## 7. 記憶技巧

1. **向左收縮**（right = mid）：
   - 使用左中位數
   - 尋找第一個滿足條件的元素

2. **向右收縮**（left = mid）：
   - 使用右中位數
   - 尋找最後一個滿足條件的元素

3. **判斷依據**：
   - 看更新區間時是否有 +1 或 -1
   - 如果是 left = mid，用右中位數
   - 如果是 right = mid，用左中位數

理解這些原理可以幫助你在實現二分搜索時避免常見的錯誤，寫出更穩健的代碼。記住，選擇左中位數還是右中位數主要取決於你如何收縮搜索區間。