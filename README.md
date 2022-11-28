# Autotest_project
___

### Useful info:

- cmd command available parameters (*conftest.py*):  
--language=... *English language is set by default*  
--headless=true *tests will run in a visible mode by default*  
--browser_name=firefox *tests will run in a chrome browser by default*  

- **implicitly_wait** method is available, currently commented out *(base_page.py)*

- Available marks:

**login_guest:**  
test_guest_should_see_login_link *(test_main_page.py)*  
test_guest_can_go_to_login_page *(test_main_page.py)*

**need_review:**  
test_user_can_add_product_to_basket *(test_product_page.py)*  
test_guest_can_add_product_to_basket *(test_product_page.py)*  
test_guest_cant_see_product_in_basket_opened_from_product_page *(test_product_page.py)*  
test_guest_can_go_to_login_page_from_product_page *(test_product_page.py)*

**new:**  
test_guest_cant_see_product_in_basket_opened_from_product_page *(test_product_page.py)*  
test_guest_cant_see_product_in_basket_opened_from_main_page *(test_main_page.py)*

**registered_user:**  
test_user_cant_see_success_message *(test_product_page.py)*  
test_user_can_add_product_to_basket *(test_product_page.py)*

- **parametrize** example:  
test_guest_can_add_product_to_basket *(test_product_page.py)*

- The following tests are marked as **xfail**:  
test_guest_can_add_product_to_basket *(test_product_page.py)*  
test_guest_cant_see_success_message_after_adding_product_to_basket *(test_product_page.py)*  
test_message_disappeared_after_adding_product_to_basket *(test_product_page.py)*


------

pytest -v --tb=line --language=es --headless=true --browser_name=firefox -m need_review