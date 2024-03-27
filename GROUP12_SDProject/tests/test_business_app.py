import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You may need to adjust this based on your browser driver
    yield driver
    driver.quit()

def test_signup(browser):
    browser.get('http://localhost:8000/business-signup/')  # Replace with your actual login URL
    assert 'Sign Up' in browser.title

    first_name = browser.find_element_by_name('first_name')
    last_name = browser.find_element_by_name('last_name')
    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    address = browser.find_element_by_name('address')
    mobile = browser.find_element_by_name('mobile')
    submit_button = browser.find_element_by_name('submit')

    first_name.send_keys('your_first_name')
    last_name.send_keys('your_last_name')
    username.send_keys('your_username')
    password.send_keys('your_password')
    address.send_keys('your_address')
    mobile.send_keys('your_mobile')
    submit_button.click()

    assert 'Login' in browser.title

def test_login(browser):
    browser.get('http://localhost:8000/business-login/')  # Replace with your actual login URL
    assert 'Login' in browser.title

    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    submit_button = browser.find_element_by_name('submit')

    username.send_keys('your_username')
    password.send_keys('your_password')
    submit_button.click()

    assert 'Business Dashboard' in browser.title

def test_view_customer(browser):
    browser.get('http://localhost:8000/business-dashboard/')  # Replace with your actual dashboard URL
    assert 'Business Dashboard' in browser.title

    view_customer_link = browser.find_element_by_link_text('View Customers')
    view_customer_link.click()

    assert 'View Customers' in browser.title

def test_add_product(browser):
    browser.get('http://localhost:8000/business-dashboard/')  # Replace with your actual dashboard URL
    assert 'Business Dashboard' in browser.title

    add_product_link = browser.find_element_by_link_text('Add Product')
    add_product_link.click()

    assert 'Add Product' in browser.title

    # Fill in product details and submit
    name_field = browser.find_element_by_name('name')
    category_field = browser.find_element_by_name('category')
    price_field = browser.find_element_by_name('price')
    description_field = browser.find_element_by_name('description')
    submit_button = browser.find_element_by_name('submit')

    name_field.send_keys('Test Product')
    category_field.send_keys('Test Category')
    price_field.send_keys('100')
    description_field.send_keys('Test Description')
    submit_button.click()

    # Check if product is added successfully
    assert 'Product Details' in browser.title

def test_view_booking(browser):
    browser.get('http://localhost:8000/business-dashboard/')  # Replace with your actual dashboard URL
    assert 'Business Dashboard' in browser.title

    view_booking_link = browser.find_element_by_link_text('View Bookings')
    view_booking_link.click()

    assert 'View Bookings' in browser.title

def test_view_feedback(browser):
    browser.get('http://localhost:8000/business-dashboard/')  # Replace with your actual dashboard URL
    assert 'Business Dashboard' in browser.title

    view_feedback_link = browser.find_element_by_link_text('View Feedback')
    view_feedback_link.click()

    assert 'View Feedback' in browser.title

def test_profile(browser):
    browser.get('http://localhost:8000/business-dashboard/')  # Replace with your actual dashboard URL
    assert 'Business Dashboard' in browser.title

    profile_link = browser.find_element_by_link_text('Profile')
    profile_link.click()

    assert 'Profile' in browser.title
