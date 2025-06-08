import random
import string

def generate_random_string(length=8):
    """
    Generate a random alphanumeric string of the specified length.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_new_user_data():
    """
    Generate a new user data dictionary for UI tests.
    """
    rand = generate_random_string()
    return {
        "title": "Mr.",
        "name": rand,
        "email": f"{rand}@pwqavl.com",
        "password": generate_random_string(10),
        "dob": "1990-05-07",
        "newsletter": "yes",
        "offers": "yes",
        "firstName": "John",
        "lastName": "Doe",
        "company": "QA All Day",
        "address1": "123 Main St",
        "address2": "456 Some St",
        "country": "Canada",
        "city": "Toronto",
        "state": "Ontario",
        "zipcode": "M5H2N2",
        "mobile": "1234567890",
    }

def generate_new_user_api_data():
    """
    Generate a new user data dictionary for API tests.
    """
    rand = generate_random_string()
    return {
        "name": f"{rand} QA",
        "email": f"{rand}@pwqavl.com",
        "password": "SecureP@ss123",
        "title": "Mr",
        "birth_date": "18",
        "birth_month": "1",
        "birth_year": "1989",
        "firstname": "LV",
        "lastname": "QA",
        "company": "Test Co",
        "address1": "QA Street 11",
        "address2": "",
        "country": "United States",
        "zipcode": "M5H2N2",
        "state": "UT",
        "city": "QACity",
        "mobile_number": "1234567890"
    }