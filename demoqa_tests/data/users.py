import dataclasses


@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth_day: str
    date_of_birth_month: str
    date_of_birth_year: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


test_user = User(name='leia', last_name='organa', email='leia@gmail.com',
                 gender='Female', number='0123456789',
                 date_of_birth_day='25', date_of_birth_month='May', date_of_birth_year='1977',
                 subject='English', hobby='Reading', picture='image_test.JPG',
                 address='1 RIDGE AVE SUFFERN NY 10901-5807 US', state='NCR', city='Delhi'
                 )
