page_url = "https://www.samsung.com/pl/watches/all-watches/"
expected_status = 200
status_from_api = "200"
page_load_time = 0.5

print(type(page_url))
print(type(expected_status))
print(type(status_from_api))
print(type(page_load_time))

status_as_int = int(status_from_api)
test_result = status_as_int == expected_status

print(f"Test strony {page_url}: oczekiwano {expected_status}, otrzymano {status_as_int}, "
      f"czas {page_load_time}s, wynik: {test_result}")