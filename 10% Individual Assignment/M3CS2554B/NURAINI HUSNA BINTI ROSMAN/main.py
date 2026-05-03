import time
import threading
import multiprocessing
import matplotlib.pyplot as plt
import random

def calculate_price(price, discount, tax):
    for _ in range(100): 
        res = (price * (1 - discount/100)) * (1 + tax/100)
    return res

def run_task(category_name, data_size, disc, tx, f):
    f.write(f"\n{'='*20} CATEGORY: {category_name.upper()} ({data_size:,} items) {'='*20}\n")
    prices = [random.uniform(10.0, 500.0) for _ in range(data_size)]

    start = time.time()
    _ = [calculate_price(p, disc, tx) for p in prices]
    seq_t = time.time() - start

    start = time.time()
    num_threads = 4
    chunk = data_size // num_threads
    threads = [threading.Thread(target=lambda: [calculate_price(100.0, disc, tx) for _ in range(chunk)]) for _ in range(num_threads)]
    for t in threads: t.start()
    for t in threads: t.join()
    con_t = time.time() - start

    start = time.time()
    with multiprocessing.Pool() as pool:
        data_stream = [(p, disc, tx) for p in prices]
        _ = pool.starmap(calculate_price, data_stream, chunksize=5000)
    par_t = time.time() - start

    f.write(f"Sample Results:\n  1. Original: RM{prices[0]:.2f} -> Final: RM{calculate_price(prices[0], disc, tx):.2f}\n")
    
    return seq_t, con_t, par_t

if __name__ == "__main__":
    categories = ["Top", "Bottom", "Accessories", "Footwear", "Outerwear", "Bags"]
    data_per_category = 1000000 
    
    disc = 50.0
    tx = 6.0
    
    results_summary = []

    with open("results.txt", "w") as f:
        f.write("=== E-COMMERCE CATEGORY PERFORMANCE REPORT ===\n")
        f.write(f"Settings: Discount {disc}% | Tax {tx}%\n")
        
        for cat in categories:
            print(f"Processing Category: {cat}...")
            s, c, p = run_task(cat, data_per_category, disc, tx, f)
            results_summary.append((cat, s, c, p))

    last_cat, final_seq, final_con, final_par = results_summary[-1]
    
    methods = ["Sequential", "Threading", "Multiprocessing"]
    times = [final_seq, final_con, final_par]

    plt.figure(figsize=(10, 6))
    plt.bar(methods, times, color=['skyblue', 'lightgreen', 'salmon'])

    plt.title(f"Performance Comparison for {last_cat} Category ({data_per_category:,} items)")
    plt.xlabel("Computing Technique")
    plt.ylabel("Execution Time (seconds)")

    for index, value in enumerate(times):
        plt.text(index, value, f"{value:.2f}s", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig("performance_graph.png")
    
    print("\nSUCCESS! Check results.txt and performance_graph.png in your folder.")
