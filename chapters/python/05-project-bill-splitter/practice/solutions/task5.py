# file: practice/solutions/task5.py
service_percent = 5
bill = float(input("Bill total: "))
service = bill * service_percent / 100
total = bill + service
service_label = f"Service {service_percent}%"
print(f"{'Bill':<16}{bill:>8.2f}")
print(f"{service_label:<16}{service:>8.2f}")
print(f"{'Total':<16}{total:>8.2f}")
