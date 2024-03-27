import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.urls import reverse
from django.contrib.auth.models import User, Group
from customer.models import Customer, Orders, Feedback
from customer.forms import CustomerUserForm, CustomerForm
from customer.views import is_customer


@pytest.mark.django_db
def test_customer_creation():
    user = User.objects.create(username="test_user", first_name="Test", last_name="User")
    customer = Customer.objects.create(user=user, address="Test Address", mobile="1234567890")
    assert customer.get_name == "Test User"
    assert customer.get_id == user.id

@pytest.mark.django_db
def test_orders_creation():
    customer = Customer.objects.create(address="Test Address", mobile="1234567890")
    order = Orders.objects.create(customer=customer, email="test@example.com", address="Test Address", mobile="1234567890", status="Pending")
    assert order.status == "Pending"

@pytest.mark.django_db
def test_feedback_creation():
    feedback = Feedback.objects.create(name="Test User", feedback="Test Feedback")
    assert str(feedback) == "Test User"



@pytest.fixture(scope="module")
def browser():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close browser
    driver.quit()

def test_home_page(browser):
    # Open the home page
    browser.get("http://localhost:8000/")
    assert "Home Page" in browser.title

def test_login(browser):
    # Open the login page
    browser.get("http://localhost:8000/customerlogin/")
    assert "Login" in browser.title
    # Enter username and password and submit the form
    username = browser.find_element_by_name("username")
    password = browser.find_element_by_name("password")
    username.send_keys("test_user")
    password.send_keys("test_password")
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    # Check if login was successful by checking for presence of certain elements on the page
    assert browser.find_element_by_id("customer-home")

@pytest.fixture
def setup_user():
    user = User.objects.create_user(username='testuser', password='12345')
    customer_group, _ = Group.objects.get_or_create(name='CUSTOMER')
    customer_group.user_set.add(user)
    return user

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('customer-home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_customer_signup_view(client):
    response = client.get(reverse('customer-signup'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_customer_signup_form_valid(setup_user):
    user = setup_user
    data = {
        'username': 'testuser2',
        'password1': 'testpassword',
        'password2': 'testpassword',
        'address': 'Test Address',
        'mobile': '1234567890',
        
    }
    form = CustomerUserForm(data=data)
    assert form.is_valid()

@pytest.mark.django_db
def test_customer_address_view(setup_user, client):
    client.force_login(setup_user)
    response = client.get(reverse('customer-address'))
    assert response.status_code == 200

