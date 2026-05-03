# 2603-ITT440
# NURAINI HUSNA BINTI ROSMAN
# DISCOUNT PRICE CALCULATOR
# INDIVIDUAL ASSIGNMENT: ITT440 NETWORK PROGRAMMING
Project Title: Discount Price Calculator
Student Name: Nuraini Husna binti Rosman
Student ID: 2024298464
Group: M3CS2554B
# 1. PROBLEM STATEMENT
The retail and e-commerce industries often need to process price updates for millions of products simultaneously during promotional events. A standard sequential approach is inefficient for such large volumes of data. This Discount Price Calculator project demonstrates how to optimize high-volume data processing using Concurrent and Parallel programming in Python, comparing their efficiency against a traditional Sequential approach across 6,000,000 retail items.
# 2. SYSTEM REQUIREMENTS
i) Operating System: Windows/Linux/macOS (Optimized for GitHub Codespaces/Ubuntu)
ii) Programming Language: Python 3.x
iii) Libraries Required:
     - time, threading, multiprocessing, random (Standard Python libraries)
     - matplotlib (For performance visualization and benchmarking)
# 3. KEY FEATURES
i) Dynamic User Input: The program allows users to manually define the discount and tax percentages at runtime.
ii) Multi-Category Processing: Processes 1,000,000 items each for six categories: Top, Bottom, Accessories, Footwear, Outerwear, and Bags.
iii) Scalable Performance: Utilizes multiple CPU cores to handle 6 million calculations efficiently.
# 4. INSTALLATION AND USAGE
1. Clone the repository to your local machine or open it in GitHub Codespaces.
2. Install the visualization library:
   pip install matplotlib
3. Run the program:
   python3 main.py
4. Provide Input: When prompted, enter your desired discount and tax rates (e.g., 50 for 50%, 6 for 6%).
# 5. SAMPLE OUTPUT
File: results.txt
The program outputs 10 detailed calculations for every category to verify the mathematical accuracy of the calculator.
<img width="739" height="373" alt="Screenshot 2026-05-03 174018" src="https://github.com/user-attachments/assets/46a575bb-11de-4e0f-ae35-b3db1ee74800" />
# 6. PERFORMANCE BENCHMARKING
Based on the execution results:
i) Parallel Execution: Achieves the lowest execution time by distributing tasks across all available CPU cores.
ii) Concurrent Execution: Performance is improved via multi-threading but remains limited by the Global Interpreter Lock (GIL).
iii) Sequential Execution: The slowest method as it processes items one by one.
The results are visually summarized in the automatically generated (performance_graph.png)
# 7. SCREENSHOTS
i) Terminal Output:
<img width="928" height="206" alt="Screenshot 2026-05-03 173930" src="https://github.com/user-attachments/assets/e784dd5d-fe14-45cb-9cc3-8324359234cf" />
ii) Generated Graph: 
<img width="766" height="456" alt="Screenshot 2026-05-03 174838" src="https://github.com/user-attachments/assets/c03dc73a-17e3-45ea-aeef-e9602b0b205c" />
iii) Source Code:
Sequential approach:
<img width="539" height="90" alt="Screenshot 2026-05-03 181748" src="https://github.com/user-attachments/assets/0560982d-4233-476d-ba7d-e011f11ef628" />
Concurrent Approach (Threading):
<img width="1261" height="181" alt="Screenshot 2026-05-03 181810" src="https://github.com/user-attachments/assets/246f8657-bfcc-4751-86fb-547ffff5e21d" />
Parallel Approach (Multiprocessing):
<img width="663" height="140" alt="Screenshot 2026-05-03 181824" src="https://github.com/user-attachments/assets/c45d28fb-a65a-4cdf-b5b2-6064797aff8b" />
# 8. DEMOSTRATION VIDEO

The video covers the dynamic input feature, the generation of 6 million price calculations, and a comparison of the three computing techniques.
