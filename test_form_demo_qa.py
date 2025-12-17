import os
from selene import browser, have, by, be
from selene.support.conditions import be as sbe

def get_image_path(image_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'images', image_name)

def test():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('#firstName').type('Игорь')
    browser.element('#lastName').type('Киров')
    browser.element('#userEmail').type('qwerty@mail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8167873187')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element(by.text("1944")).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element(by.text("July")).click()
    browser.element('.react-datepicker__day--004').click()

    browser.element('#subjectsInput').type('commerce').press_enter()


    image_path = get_image_path('qa11.jpg.jpg')
    browser.element('#uploadPicture').send_keys(image_path)

    browser.element('label[for="hobbies-checkbox-1"]').click()

    browser.element('#currentAddress').type('red polyna')

    browser.element('#state').click()
    browser.element('#state').element(by.text("Rajasthan")).click()
    browser.element('#city').click()
    browser.element('#city').element(by.text("Jaipur")).click()

    browser.element('#submit').click()

    browser.element('.modal-dialog').should(sbe.visible)

    browser.element('.modal-body').should(have.text('Игорь'))
    browser.element('.modal-body').should(have.text('Киров'))
    browser.element('.modal-body').should(have.text('qwerty@mail.com'))
    browser.element('.modal-body').should(have.text('8167873187'))
    browser.element('.modal-body').should(have.text('04 July,1944'))
    browser.element('.modal-body').should(have.text('Commerce'))
    browser.element('.modal-body').should(have.text('Sports'))
    browser.element('.modal-body').should(have.text('qa11.jpg'))
    browser.element('.modal-body').should(have.text('red polyna'))
    browser.element('.modal-body').should(have.text('Rajasthan'))
    browser.element('.modal-body').should(have.text('Jaipur'))


