# main.py
from sales_analysis import read_data, calculate_total_sales, get_top_products

def main():
    file_path = 'sales_data.csv'
    report_path = 'sales_report.txt'

    data = read_data(file_path)
    if not data:
        print("No data to analyze.")
        return

    total_sales = calculate_total_sales(data)
    top_products = get_top_products(data, 5)

    with open(report_path, mode='w') as report_file:
        report_file.write(f"Total Sales: {total_sales}\n")
        report_file.write("Top Products:\n")
        for product in top_products:
            report_file.write(f"{product['product_name']}: {product['sales']}\n")

if __name__ == "__main__":
    main()