# Clock demonstration using stamp
import time

my_time = int(input("Enter the time in seconds :"))

for x in range(my_time,0,-1):
    seconds = x%60
    minutes = int(x/60) %60
    hours = int(x/3600)%60
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")

"""
Perfect! Let’s carefully go **step by step** for your code when `my_time = 20000` seconds.

### Step 1: Calculate **seconds**

```python
seconds = x % 60
seconds = 20000 % 60
```

* 60 goes into 20000 → 333 times (333 × 60 = 19980)
* Remainder = 20000 − 19980 = **20**

✅ `seconds = 20`

---

### Step 2: Calculate **minutes**

```python
minutes = int(x / 60) % 60
minutes = int(20000 / 60) % 60
minutes = int(333.3333) % 60
minutes = 333 % 60
```

* 60 goes into 333 → 5 times (5 × 60 = 300)
* Remainder = 333 − 300 = **33**

✅ `minutes = 33`

---

### Step 3: Calculate **hours**

```python
hours = int(x / 3600) % 60
hours = int(20000 / 3600) % 60
hours = int(5.5555) % 60
hours = 5
```

✅ `hours = 5`

---

### Step 4: Combine in print

```python
print(f"{hours}:{minutes}:{seconds}")
```

* hours = 5
* minutes = 33
* seconds = 20

**Output:**

```
5:33:20
```

---

### ⚠️ Note on `% 60` in hours

* Using `% 60` for hours **limits the hours to 0–59**.
* For 20000 seconds it’s fine, but if you input very large seconds (like 200000), hours will **wrap around after 59**.
* Better way (for unlimited hours) is **remove `% 60` for hours**:

```python
hours = x // 3600
```

---

✅ **Summary:**

20000 seconds = **5 hours, 33 minutes, 20 seconds**

* `seconds = 20000 % 60 = 20`
* `minutes = (20000 // 60) % 60 = 333 % 60 = 33`
* `hours = (20000 // 3600) % 60 = 5`

"""
    

