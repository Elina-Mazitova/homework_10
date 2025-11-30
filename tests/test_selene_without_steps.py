from selene import by, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_selene_without_steps():
    browser.open('https://github.com') # открываем главную страницу GitHub

    s(".header-search-button").click() # кликаем по кнопке поиска
    s("#query-builder-test").send_keys("Elina-Mazitova/homework_10") # вводим название репозитория в поле поиска
    s("#query-builder-test").press_enter() # нажимаем Enter и подтверждаем поиск

    s(by.link_text("Elina-Mazitova/homework_10")).click() #кликаем по ссылке на найденный репозиторий

    s("#issues-tab").click()   # переходим во вкладку Issues

    s('a[href="/Elina-Mazitova/homework_10/issues/1"]').should(have.text("issue_for_homework_10"))
    # проверяем что первая ссылка содержит текст issue_for_homework_10