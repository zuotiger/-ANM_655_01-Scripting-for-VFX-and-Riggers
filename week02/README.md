# Week 02 – System Info Script

## Assignment Overview

This assignment follows the demonstration video and focuses on completing a simple Python script by filling in missing logic.

To help myself review the material — and to make the process clearer — I break the assignment down step by step using text and visual references. The goal is to understand *why* each part works, not just to make it run.

---

## Goal

Based on the example shown in the first video, the expected final output of this assignment is a **System Report**, similar to the following:

```md
System Report
Time: [xxxx]
Date: [xxxx]
Operating System: [xxxx]
Python Version: [xxxx]
```

---

## Process & Thinking

- Started by reviewing the base script provided in the demonstration.
- Identified which values needed to be dynamically generated.
- Used Python standard libraries (`time`, `platform`, and `sys`) to retrieve system information.
- Filled in each missing part step by step and tested the output incrementally.
- Adjusted formatting to make the final report easier to read.

This breakdown helps me better understand how simple scripts can gather and format system-level information.

---

## Step-by-step Breakdown

### Step 1 — Understand the expected output

```md
import time

# Define data
current_time = time.asctime()
current_date = str()
current_clock = str()
operating_system = str()
python_version = str()
title = 'System Report'

# Process data

output_string = (title + 'Time: ' + current_clock + 'Date: ' + current_date + 'Operating System: ' + operating_system + 'Python Version: ' + python_version)
print (output_string)
```

这里是最基本的框架，但是如你所见，只是凭直觉输入的自然语言导致第13行的代码极长，不方便阅读，所以在这里我们要进行第二步的可读性优化。

第二步：
这里先介绍了简单的添加 “ \ ” 就可以进行换行，
优化后的13行如下：

```md
output_string = (title + \
                 'Time: ' + current_clock + \
                 'Date: ' + current_date + \
                 'Operating System: ' + operating_system + \
                 'Python Version: ' + python_version)
```

可读性有了提升！但是是否还有更好的办法？
---

## Files

- `system_info.py` – Final Python script for the Week 02 assignment.
