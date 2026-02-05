# Week 02 – System Info Script

## Assignment Overview

This assignment follows the demonstration video and focuses on completing a simple Python script by filling in missing logic.

To improve my understanding and make the process clearer, I documented the assignment step by step using text and visual references. The goal is to understand **why each part works**, not just to make the script run.

---

## Goal

Based on the example shown in the first video, the expected final output of this assignment is a **System Report**, similar to the following:

```
System Report
Time: [xxxx]
Date: [xxxx]
Operating System: [xxxx]
Python Version: [xxxx]
```

---

## Process & Thinking

- Reviewed the base script provided in the demonstration.
- Identified which values needed to be generated dynamically.
- Used Python standard libraries (`time`, `platform`, and `sys`) to retrieve system information.
- Filled in each missing part step by step and tested the output incrementally.
- Adjusted string formatting to improve readability.

This breakdown helped me better understand how simple Python scripts gather and format system-level information.

---

## Step-by-Step Breakdown

### Step 1 — Understanding the Base Script

```python
import time

# Define data
current_time = time.asctime()
current_date = str()
current_clock = str()
operating_system = str()
python_version = str()
title = 'System Report'

# Process data
output_string = (
    title + 'Time: ' + current_clock +
    'Date: ' + current_date +
    'Operating System: ' + operating_system +
    'Python Version: ' + python_version
)

print(output_string)
```

This is the basic framework of the script.  
At this stage, the output string is written as a long concatenation, which makes the code harder to read and maintain.

---

### Step 2 — Improving Readability with Line Continuation

An initial improvement uses explicit line continuation (`\`) to split the long line:

```python
output_string = (title + \
                 'Time: ' + current_clock + \
                 'Date: ' + current_date + \
                 'Operating System: ' + operating_system + \
                 'Python Version: ' + python_version)
```

This improves readability, but modern Python style guidelines (such as PEP 8) recommend avoiding explicit backslashes when possible.

The preferred approach is **implicit line continuation inside parentheses**, which results in cleaner and more readable code.

---

### Step 3 — Reading Time Data as Strings

The function `time.asctime()` converts the current system time into a readable string.

<img width="510" height="192" alt="time.asctime output example" src="https://github.com/user-attachments/assets/dd1885d9-698f-498a-855a-f12ef509cd1c" />

However, the script only needs two parts of this string:
- `current_clock`
- `current_date`

---

### Method 1 — String Slicing

One possible approach is slicing the string by character index:

<img width="400" height="120" alt="string slicing example" src="https://github.com/user-attachments/assets/62b88d6e-a0ed-4c33-8e41-21e418a50ac5" />

This works, but becomes inconvenient when the string grows longer or changes format, since manually counting character positions is error-prone.

---

### Method 2 — Using `split()` (Preferred)

A more flexible approach is using `split()`.

<img width="1186" height="386" alt="using split method" src="https://github.com/user-attachments/assets/a464559d-d110-45a3-8512-e2f728e6d29f" />

Using `dir(current_time)` shows that `split()` is available as a string method.

In Python, `split()`:
- Separates a string using a delimiter (default is whitespace)
- Returns a list of smaller strings

<img width="608" height="130" alt="split result example" src="https://github.com/user-attachments/assets/086ee480-6d71-4896-8a4a-74b485a64bd2" />

This makes it much easier to extract the required values for `current_clock` and `current_date`.

<img width="678" height="78" alt="extracted date and time" src="https://github.com/user-attachments/assets/f51c1613-d176-4bea-b8d2-c9c5c7f0ec91" />

---

### Formatting the Date with `.format()`

Because `current_date` requires combining multiple string components, writing it as direct concatenation quickly becomes messy.

The demo video uses the **dot format command**, which refers to the `.format()` string method.

```
"template string".format(value1, value2, ...)
```

This allows values to be inserted cleanly into `{}` placeholders.

<img width="1066" height="136" alt="format method example" src="https://github.com/user-attachments/assets/3c3e078c-205d-451c-9c7c-2fa299256145" />

The date formatting code was refactored using `.format()` to improve clarity and readability.

<img width="1096" height="286" alt="formatted date code" src="https://github.com/user-attachments/assets/4b4b37d7-e276-4737-b499-46d23712c578" />

<img width="762" height="464" alt="final date output" src="https://github.com/user-attachments/assets/cd05184c-339d-4cd2-b2b3-ea8a4165c66e" />

---

## Completing the Assignment Logic

According to the video, the remaining task is similar to a fill-in exercise:  
finding the correct system and Python version information.

The `sys` module is used for this purpose.

After inspecting available attributes with `dir(sys)`:

<img width="2300" height="706" alt="dir(sys) output" src="https://github.com/user-attachments/assets/7bdaeaf1-84bf-4a9a-a94c-03cfa71d3e7a" />

The required values are identified following the same process shown in the demo.

<img width="2290" height="292" alt="selected sys attributes" src="https://github.com/user-attachments/assets/6a6d1fb6-7353-4e05-8409-2d6fb97206d2" />

These values are inserted into the original script to complete the assignment.

<img width="982" height="1090" alt="final script output" src="https://github.com/user-attachments/assets/a0ff4d5b-319a-49d7-9751-c3e3f3e9f997" />

---

## Files

- `ANM_65501_ZuoLi_05423182_m01_1_system_info.py`  
  Final Python script for the Week 02 assignment
