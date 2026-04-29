import time
import threading
import multiprocessing
import sys
import random

# Core calculation with a heavy loop to justify Parallelism
def calculate_price(price, discount, tax):
    for _ in range(100): 
        res = (price * (1 - discount/100)) * (1 + tax/100)
    return res

def run_benchmarks(data_size, discount, tax, file):
    file.write(f"\n{'#'*20} DATA SCALE: {data_size:,} ITEMS {'#'*20}\n")
    
    # Generate random prices between $10 and $500 for variety
    prices = [random.uniform(10.0, 500.0) for _ in range(data_size)]

    # --- SEQUENTIAL ---
    start = time.time()
    seq_results = [calculate_price(p, discount, tax) for p in prices[:100000]] # Limit storage
    seq_time = time.time() - start

    # --- CONCURRENT (THREADS) ---
    num_threads = 4
    chunk = data_size // num_threads
    start = time.time()
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=lambda: [calculate_price(100.0, discount, tax) for _ in range(chunk)])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    con_time = time.time() - start

    # --- PARALLEL (PROCESSES) ---
    start = time.time()
    with multiprocessing.Pool() as pool:
        data_stream = [(p, discount, tax) for p in prices]
        _ = pool.starmap(calculate_price, data_stream, chunksize=5000)
    par_time = time.time() - start

    # Write a few real results to the notepad to show the math works
    file.write(f"Sample Results (First 5 items with different prices):\n")
    for i in range(5):
        file.write(f" Item {i+1}: Original: ${prices[i]:.2f} -> Final: ${calculate_price(prices[i], discount, tax):.2f}\n")
    
    return seq_time, con_time, par_time

if __name__ == "__main__":
    print("=== Professional Discount Processor ===")
    try:
        disc = float(input("Enter Discount % (e.g. 30): "))
        tx = float(input("Enter Tax % (e.g. 5): "))
        
        with open("results.txt", "w") as f:
            f.write("=== DISCOUNT PRICE CALCULATOR REPORT ===\n")
            f.write(f"Parameters: {disc}% Discount | {tx}% Tax\n")

            scales = [100000, 500000, 1000000, 2500000, 5000000]
            summary = []

            for size in scales:
                print(f"Processing {size:,} items... Writing to results.txt")
                s_t, c_t, p_t = run_benchmarks(size, disc, tx, f)
                summary.append((size, s_t, c_t, p_t))

            # Final Table
            f.write("\n" + "="*65 + "\n")
            f.write(" PERFORMANCE COMPARISON TABLE ".center(65, " ") + "\n")
            f.write("="*65 + "\n")
            f.write(f"{'Data Size':<15} | {'Sequential':<12} | {'Concurrent':<12} | {'Parallel'}\n")
            f.write("-" * 65 + "\n")
            for size, s, c, p in summary:
                f.write(f"{size:<15,} | {s:<12.4f} | {c:<12.4f} | {p:.4f}\n")
            f.write("="*65 + "\n")

        print("\nAll done! Check 'results.txt' in your folder.")

    except ValueError:
        print("Please enter valid numbers.")
