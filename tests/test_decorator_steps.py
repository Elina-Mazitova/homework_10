import allure
from selene import by, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_repository("Elina-Mazitova/homework_10")
    go_to_repository("Elina-Mazitova/homework_10")
    open_issues_page()
    should_see_issue_for_homework_10()


@allure.step("открываем главную страницу GitHub")
def open_main_page():
    browser.open('https://github.com')

@allure.step("ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").press_enter()

@allure.step("кликаем по ссылке на найденный репозиторий {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("переходим во вкладку Issues")
def open_issues_page():
    s("#issues-tab").click()

@allure.step("проверяем что первая ссылка содержит текст issue_for_homework_10")
def should_see_issue_for_homework_10():
    s('a[href="/Elina-Mazitova/homework_10/issues/1"]').should(have.text("issue_for_homework_10"))