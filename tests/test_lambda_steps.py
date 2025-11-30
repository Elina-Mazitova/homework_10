import allure
from selene import by, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_lambda_steps():
    with allure.step("открываем главную страницу GitHub"):
        browser.open('https://github.com')

    with allure.step("кликаем по кнопке поиска"):
        s(".header-search-button").click()
    with allure.step("вводим название репозитория в поле поиска"):
        s("#query-builder-test").send_keys("Elina-Mazitova/homework_10")
    with allure.step("нажимаем Enter и подтверждаем поиск"):
        s("#query-builder-test").press_enter()

    with allure.step("кликаем по ссылке на найденный репозиторий"):
        s(by.link_text("Elina-Mazitova/homework_10")).click()

    with allure.step("переходим во вкладку Issues"):
        s("#issues-tab").click()

    with allure.step("проверяем что первая ссылка содержит текст issue_for_homework_10"):
        s('a[href="/Elina-Mazitova/homework_10/issues/1"]').should(have.text("issue_for_homework_10"))