# Autotest_project
___

### Полезная инфо:


- Тесты should_be_login_form и should_be_register_form вынесены в test_login_page.py (тесты для страницы с логином и регистрацией)

- Метод **implicitly_wait** закомментирован *(base_page.py)*

- Доступные метки:

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

- Пример **параметризации**:  
test_guest_can_add_product_to_basket *(test_product_page.py)*

- Помечены **xfail**:  
test_guest_can_add_product_to_basket *(test_product_page.py)*  
test_guest_cant_see_success_message_after_adding_product_to_basket *(test_product_page.py)*  
test_message_disappeared_after_adding_product_to_basket *(test_product_page.py)*


------

pytest -v --tb=line --language=en -m need_review