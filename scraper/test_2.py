import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from transformers import pipeline

def is_element_avail(driver, att, value):
    return len(driver.find_elements(att, value)) != 0

# Initialize the WebDriver with WebDriver Manager
chrome_driver_path = ChromeDriverManager().install()
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://alnafi.com/auth/sign-in")
time.sleep(5)
driver.maximize_window()
time.sleep(4)

# Replace 'your_email' and 'your_password' with actual credentials
user_email = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[1]/div/div/input')
user_email.send_keys('abdullahkhanhr01@gmail.com')

user_passwd = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/div[2]/div/div/input')
user_passwd.send_keys('Khan..8090')

button_login = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/div/form/button')
button_login.click()
time.sleep(60)

dashboard = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/nav/div/div/div[3]/div/button')
dashboard.click()
time.sleep(15)

internship_mcqs = driver.find_element(By.XPATH,'/html/body/main/section[2]/div/ul/li[1]/div/div[1]/a[2]')
internship_mcqs.click()
time.sleep(15)

Assesment = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/nav/div/div[4]/div[2]/div[2]/ul/li[3]/a/div[2]/div/span[1]')
Assesment.click()
time.sleep(6)

# Load the model and tokenizer
model_name = "roberta-large-squad2"
qa_pipeline = pipeline('question-answering', model=model_name, tokenizer=model_name)

for i in range(15):  # Iterate through 15 questions
    mcqs = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/main/section/div/div[2]/div/section/div[2]/div/div[1]/span')
    question = mcqs.text
    print("Question:", question)
    time.sleep(6)

    # Fetch options
    options = []
    for i in range(4):
        xpath = f'/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/main/section/div/div[2]/div/section/div[2]/div/div[2]/div/div[{i+1}]/span'
        if is_element_avail(driver, By.XPATH, xpath):
            option = driver.find_element(By.XPATH, xpath)
            options.append(option.text)
            print(f'Option {i+1}: {option.text}')
        else:
            pass

    # Context for the QA model
    context = " ".join(options)

    # Find the answer
    answers = []
    for option in options:
        result = qa_pipeline(question=question, context=option)
        answers.append((option, result['score']))

    # Select the best answer based on the highest score
    best_answer = max(answers, key=lambda x: x[1])
    print(f"Best Answer: {best_answer[0]} with score {best_answer[1]}")

    # Click the correct option on the portal
    for i in range(4):
        xpath = f'/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/main/section/div/div[2]/div/section/div[2]/div/div[2]/div/div[{i+1}]/span'
        option_element = driver.find_element(By.XPATH, xpath)
        if option_element.text == best_answer[0]:
            option_element.click()
            time.sleep(2)
            confirm = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/main/section/div/div[2]/div/section/div[2]/div/div[3]/button/div/div/span')
            confirm.click()
            time.sleep(5)
            next = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/main/section/div/div[2]/div/section/div[2]/div/div[3]/button/div/div/span')
            next.click()


    time.sleep(6)  # Wait before moving to the next question

driver.quit()
