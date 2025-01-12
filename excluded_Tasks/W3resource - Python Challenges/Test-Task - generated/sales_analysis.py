# sales_analysis.py
import csv
from typing import List, Dict

def read_data(file_path: str) -> List[Dict]:
    data = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return data

def calculate_total_sales(data: List[Dict]) -> float:
    total_sales = 0.0
    for entry in data:
        total_sales += float(entry['sales'])
    return total_sales

def get_top_products(data: List[Dict], n: int) -> List[Dict]:
    sorted_data = sorted(data, key=lambda x: float(x['sales']), reverse=True)
    return sorted_data[:n]