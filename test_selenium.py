import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def github_url():
    return "https://github.com/youngDkWar"


@pytest.mark.smoke
def test_find_analysisDB_repository(github_url):
    """Открывает главную страницу моего GitHub и находит в списке репозиториев проект AnalysisDB"""
    driver = webdriver.Chrome(executable_path="C:/Users/Nikita/PycharmProjects/drivers/chromedriver.exe")
    driver.get(github_url)
    page_repositories = driver.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]')
    page_repositories.click()
    time.sleep(1)
    repository = driver.find_element(By.XPATH, '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')
    repository_name = repository.text
    driver.close()
    assert 'analysisDB' == repository_name


def test_check_pullRequests_is_empty(github_url):
    """Проверяет, что репозиторий не содержит открытых pullRequest"""
    driver = webdriver.Chrome(executable_path="C:/Users/Nikita/PycharmProjects/drivers/chromedriver.exe")
    driver.get(f'{github_url}/analysisDB/pulls')
    elem_pull_request = driver.find_elements(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[3]/div[2]/div/h3')
    assert len(elem_pull_request) > 0
    driver.close()
