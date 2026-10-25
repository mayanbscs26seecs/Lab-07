# storage_estimator.py
# Estimates how much storage is needed for a number of files.

def main():
    print("=== Storage Estimator ===")
    num_files = int(input("Number of files: "))
    size_mb = float(input("Average size of one file (MB): "))
    total_mb = num_files * size_mb
    total_gb = total_mb / 1024
    print(f"Total storage needed: {total_mb:.2f} MB")
    print(f"Total storage needed: {total_gb:.4f} GB")
main()