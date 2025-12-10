from selene import browser, have
from pathlib import Path


def test ():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type( 'Игорь')
    browser.element('#lastName').type('Киров')
    browser.element('#userEmail').type('qwerty@mail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8167873187')
    browser.element('#dateOfBirthInput').click()
    browser.element('#subjectsInput').type('commerce').press_enter()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value ="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value ="1944"]').click()
    browser.element('[aria-label="Choose Tuesday, July 4th, 1944"]').click()
    picture_path = str(Path.home().joinpath('Pycharmprojects', 'hw_4', 'images', 'qa11.jpg.jpg').resolve())
    browser.element('#uploadPicture').set_value(picture_path)
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').type('red polyna').press_enter()
    browser.execute_script("arguments[0].click();", browser.element('#state').locate())
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table td:nth-child(2)').should(have.exact_texts(
        'Игорь Киров',
        'qwerty@mail.com',
        'Male',
        '8167873187',
        '04 July,1944',
        'Commerce',
        'Sports',
        'qa11.jpg.jpg',
        'red polyna',
        'Rajasthan Jaipur'
    ))



