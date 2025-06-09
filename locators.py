
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Alllocarots():
    #PAGE_URL = Links.LOGIN_PAGE
    #Кнопка входа и регистрации
    BTN_ENTER_REGISTRATION = (By.XPATH, ".//button[text()='Вход и регистрация']")
    #BTN_ENTER_REGISTRATION_TWO = (By.XPATH, ".//button[text()='Вход и регистрация']")
    #Поп-ап входа с кнопкой "Нет аккаунта"
    POP_UP_ENTER = (By.XPATH, ".//form[@class='popUp_shell__LuyqR']")
    #Кнопка нет аккаунта
    BTN_WITHOUT_ACCOUNT = (By.XPATH, '//button[text()="Нет аккаунта"]')
    #Поп-ап окна регистрации после клика на кнопку "Нет аккаунта"
    POP_UP_REGISTRATION = (By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']")
    #Поле ввода почты в по-папе после нажатия на кнопку "Нет аккаунта"
    INPUT_EMAIL = (By.XPATH,".//input[@name='email']")
    #Поле ввода пароля в поп-апе после нажатия на кнопку "Нет аккаунта"
    INPUT_PASSWORD = (By.XPATH,".//input[@name='password']")
    #Повторение пароля в поле ввода, в поп-апе после нажатия на кнопку "Нет аккаунта"
    REPEAT_PASSWORD = (By.XPATH,".//input[@name='submitPassword']")
    # Кнопка создания аккаунта в поп-апе после нажатия на кнопку "Нет аккаунта"
    CREATE_ACCOUNT = (By.XPATH, ".//button[text()='Создать аккаунт']")
    # Шапка профиля созданного юзера на главной стр
    PROFILE_NAME = (By.XPATH, '/html/body/div/div/div[1]/div/div[1]/div/h3')
    # Отображение аватарки на главной странице
    AVATAR_MAIN_PAGE = (By.CLASS_NAME, "circleSmall")
    # Текст "Ошибка"
    TEXT_MISSTAKE = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[2]/div[1]/span')
    # Красная обводка во круг поля Почта
    EMAIL_RED_BORDER = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[2]/div[1]/div/div')
    # Красная обводка во круг поля Пароль
    PASSWORD_RED_BORDER = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input')
    # Красная обводка во круг поля Повторите пароль
    PASSWORD_REPEAT_RED_BORDER = (By.XPATH, '/html/body/div/div/div[2]/div[5]/form/div[2]/div[3]/div/div')
    # Поле ввода для почты в поп-апе Войти
    INPT_EMAIL = (By.XPATH, ".//input[@name='email']")
    # Поле ввода для паролья в поп-апе Войти
    INPT_PASSWORD = (By.XPATH, ".//input[@name='password']")
    # Кнопка войти в поп-апе Войти
    BUTTON_ENTER = (By.XPATH,".//button[text()='Войти']")
    # Кнопка Выйти на главной стр
    BUTTON_LOGOUT = (By.XPATH, ".//button[text()='Выйти']")
    # Кнопка Разместить объявление на главной странице
    BUTTON_CREATE_MESSAGE = (By.XPATH, ".//button[text()='Разместить объявление']")
    # Поп-ап с текстом "Чтобы разместить объявление, авторизуйтесь"
    POPUP_MESSAGE_AUTHORIZATE = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    # Заголовок страницы создания нового объявления
    CREATE_NEW_MESSAGE = (By.XPATH, ".//h1[text()='Новое объявление']")
    # Поле ввода Названия объявления на стр создания нового объявления
    NAME_MESSAGE = (By.XPATH, ".//input[@name='name']")
    # Проверка, что в поле Название появились данные
    NAME_INPUT_FULL = (By.XPATH, ".//input[@value='Гарри Поттер']")
    # Клик на дропдаун категории
    DROP_DOUN_CATEGORY = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    # Поле дропдауна выбора категории
    DROP_DOUN_CATEGORY_BUTTON = (By.XPATH, "//button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    # Выпавший список категорий
    LIST_CATEGORY = (By.XPATH, "//button[contains(@class, 'dropDownMenu_arrowUp__I25Xq')]")
    # Выбор категории Книги
    CATEGORY_BOOKS = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]/div[2]/button[2]")
    # Выбор состояния Б/У
    B_U = (By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/div/div[2]/div")
    # Клик на кнопку дропдауна города
    CITY_DROP_DOUN = (By.XPATH,"/html/body/div/div/div[2]/div/form/div[3]/div[1]/button")
    # Список городов
    LIST_CITY = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[2]")
    # Выбор города Санкт-Петербург
    CYTI_NAME = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[2]/button[2]/span")
    # Ввод описания
    DISCRIPTION = (By.XPATH, ".//textarea[@name='description']")
    # Ввод стоимости
    PRICE = (By.XPATH, ".//input[@name='price']")
    # Кнопка опубликовать
    BUTTON_PUBLISH = (By.XPATH, ".//button[text()='Опубликовать']")
    # Переход в профиль
    ENTER_TO_PROFILE = (By.XPATH, "/html/body/div/div/div[1]/div/div[1]/button")
    # Объявление
    MESSAGE_PUBLISH_BOOK = (By.XPATH, ".//h2[contains(text(), 'Приключения')]")


