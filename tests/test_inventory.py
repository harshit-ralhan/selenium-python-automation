def test_sort_price_low_to_high(login_page,inventory_page):
  #login
  login_page.login("standard_user", "secret_sauce")
  # get all item names with prices
  initial_all_item_names = inventory_page.get_item_names_with_prices()
  # sorting items logic
  sorted_items = sorted(initial_all_item_names, key=lambda x: x["price"])
  # sorting items on ui
  inventory_page.select_sorting_by_value("lohi")
  # ui sorted items
  resulting_all_item_names_with_prices = inventory_page.get_item_names_with_prices()
  # comparing sorted and ui-sorted price
  assert [i['price'] for i in sorted_items] == [i['price'] for i in resulting_all_item_names_with_prices]
  # comparing sorted and ui-sorted name
  assert [i['name'] for i in sorted_items] == [i['name'] for i in resulting_all_item_names_with_prices]
def test_sort_price_high_to_low(login_page,inventory_page):
  #login
  login_page.login("standard_user", "secret_sauce")
  # get all item names with prices
  initial_all_item_names = inventory_page.get_item_names_with_prices()
  # sorting items logic
  sorted_items = sorted(initial_all_item_names, key=lambda x: x["price"], reverse=True)
  # sorting items on ui
  inventory_page.select_sorting_by_value("hilo")
  # ui sorted items
  resulting_all_item_names_with_prices = inventory_page.get_item_names_with_prices()
  # comparing sorted and ui-sorted price
  assert [i['price'] for i in sorted_items] == [i['price'] for i in resulting_all_item_names_with_prices]
  # comparing sorted and ui-sorted name
  assert [i['name'] for i in sorted_items] == [i['name'] for i in resulting_all_item_names_with_prices]
def test_sort_name_a_to_z(login_page,inventory_page):
  #login
  login_page.login("standard_user", "secret_sauce")
  # get all item names with prices
  initial_all_item_names = inventory_page.get_all_item_names()
  # sorting items logic
  sorted_items = sorted(initial_all_item_names, key=lambda x: x.text.lower())
  # sorting items on ui
  inventory_page.select_sorting_by_value("az")
  # ui sorted items
  resulting_all_item_names = inventory_page.get_all_item_names()
  # comparing sorted and ui-sorted name
  assert [i for i in sorted_items] == [i for i in resulting_all_item_names]
def test_sort_name_z_to_a(login_page,inventory_page):
  #login
  login_page.login("standard_user", "secret_sauce")
  # get all item names with prices
  initial_all_item_names = inventory_page.get_all_item_names()
  # sorting items logic
  sorted_items = sorted(initial_all_item_names, key=lambda x: x.text.lower(), reverse=True)
  # sorting items on ui
  inventory_page.select_sorting_by_value("za")
  # ui sorted items
  resulting_all_item_names = inventory_page.get_all_item_names()
  # comparing sorted and ui-sorted name
  assert [i for i in sorted_items] == [i for i in resulting_all_item_names]