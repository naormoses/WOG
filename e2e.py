from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

url = sys.argv[1]


def test_scores_service(url):
    try:
        opt = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=opt)
        driver.get(url)
        print(f"Opening {url} in your default browser...Check your scores!")
        score_element = driver.find_element(By.ID, "score")
        score_value = int(score_element.text)
        return 1<score_value<1000
        # return score_value
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


def main(url):
    if test_scores_service(url):
        print("true")
    else:
        print("false")
    # return test_scores_service(url)
    # print(url)

# 'http://localhost:5000/scores'

if __name__ == '__main__':
    print(main(url))