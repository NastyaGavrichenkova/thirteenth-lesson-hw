import os
import allure

from selene import have, command, be
from selene.support.shared import browser

from demoqa_tests import tests
from demoqa_tests.data.users import User


class RegistrationPage:

    @allure.step('Open the main page')
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    @allure.step('Fill name')
    def fill_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    @allure.step('Fill last name')
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    @allure.step('Fill email')
    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    @allure.step('Select gender')
    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    @allure.step('Fill phone number')
    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    @allure.step('Full date of birth')
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step('Select subject')
    def select_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    @allure.step('Select hobby')
    def select_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    @allure.step('Upload picture')
    def upload_picture(self, image):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{image}')
            )
        )

    @allure.step('Fill address')
    def fill_address(self, street):
        browser.element('#currentAddress').should(be.blank).type(street)

    @allure.step('Select state')
    def select_state(self, name):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()

    @allure.step('Select city')
    def select_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(name)).click()

    @allure.step('Submit the form')
    def submit_form(self):
        browser.element('#submit').press_enter()

    @allure.step('Fill the form')
    def registration(self, user: User):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_number(user.number)
        self.fill_date_of_birth(user.date_of_birth_year,
                                user.date_of_birth_month,
                                user.date_of_birth_day)
        self.select_subject(user.subject)
        self.select_hobby(user.hobby)
        self.upload_picture(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)

        self.submit_form()

    @allure.step('Check data of the registered user')
    def should_registration_user_with(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.name} {user.last_name}',
                             user.email,
                             user.gender,
                             user.number,
                             f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
                             user.subject,
                             user.hobby,
                             user.picture,
                             user.address,
                             f'{user.state} {user.city}'
                             )
        )
