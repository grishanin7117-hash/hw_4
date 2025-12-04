from selene import browser, have
from pathlib import Path


def test ():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type( 'Игорь')
    browser.element('#lastName').type('Киров')
    browser.element('#userEmail').type('qwerty@mail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('81678731878')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value ="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value ="1944"]').click()
    browser.element('[aria-label="Choose Tuesday, July 4th, 1944"]').click()
    picture_path = str(Path.home().joinpath('Desktop', "qa.bmp").resolve())
    browser.element('#uploadPicture').set_value(picture_path)
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').type('red polyna')
    browser.execute_script("arguments[0].click();", browser.element('#state').locate())
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()
    browser.element('#subjectsInput').type('language').press_enter()


