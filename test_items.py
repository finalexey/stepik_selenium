link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_addtobasket_button(browser):

    browser.get(link)

    try:
        button = browser.find_element_by_class_name('btn-primary')
        result = True
    except:
        result = False

    assert result is True, 'Кнопка не найдена'
