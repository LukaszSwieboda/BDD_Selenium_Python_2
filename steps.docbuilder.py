from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@given('Go to home page')
def visitHomePage(context):
    context.driver = webdriver.Chrome('/Users/lukaszswieboda/Downloads/chromedriver90')
    context.driver.get('https://test-ask.ztable.se/doc-wizard')

@then('Fill in forms and download file')
def choosePropertyContract(context):
    propertyButton = context.driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-0"]/form/div/div[1]/div')
    propertyButton.click()

def applicantForm(context):
    context.driver.find_element(By.ID, 'mat-input-0').send_keys('Jan Kowalski')
    context.driver.find_element(By.ID, 'mat-input-1').send_keys('otrzymania')
    context.driver.find_element(By.ID, 'mat-input-2').clear()
    context.driver.find_element(By.ID, 'mat-input-2').send_keys('12345677')
    context.driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div/button[2]').click()

def defendantForm(context):
    context.driver.find_element(By.ID, 'mat-input-3').send_keys('John Smith')
    context.driver.find_element(By.ID, 'mat-input-4').send_keys('ukradl auto')
    element = context.driver.find_element(By.ID, 'mat-input-5')
    drp = Select(element)
    drp.select_by_visible_text('Wyłącz netflixa')
    context.driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-2"]/form/div/button[2]').click()
    context.driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-3"]/div[1]/div/button').click()

