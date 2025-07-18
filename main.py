from random import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import pyautogui
import random

if __name__ == "__main__":
    load_dotenv()

    form_link = os.getenv("FORM_LINK")
    driver = uc.Chrome()

    driver.get(form_link)
    driver.maximize_window()
    time.sleep(5)
    pyautogui.click(673, 525)
    print("Clicked!")
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div").click()
    print("Clicked next!")
    time.sleep(2.5)
    #page 1 surpassed
    num = random.randint(1, 5)
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(str(num))
    genders = ['male', 'female']
    if random.choice(genders) == 'male':
        #about to click male as gender of child
        driver.find_element(By.CSS_SELECTOR, "#i11 > div.vd3tt > div").click()
    else:
        #driver about to click female as gender of child
        driver.find_element(By.CSS_SELECTOR, "#i14 > div.vd3tt > div").click()

    #mom's education
    element = driver.find_element(By.CSS_SELECTOR, "#i17 > span.M7eMe")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    education = random.randint(1, 8)
    if(education == 1):
        driver.find_element(By.CSS_SELECTOR, "#i22 > div.vd3tt > div").click()
    elif(education == 2):
        driver.find_element(By.CSS_SELECTOR, "#i25 > div.vd3tt > div").click()
    elif(education == 3):
        driver.find_element(By.CSS_SELECTOR, "#i28 > div.vd3tt > div").click()
    elif(education == 4):
        driver.find_element(By.CSS_SELECTOR, "#i31 > div.vd3tt > div").click()
    elif(education == 5):
        driver.find_element(By.CSS_SELECTOR, "#i34 > div.vd3tt > div").click()
    elif(education == 6):
        driver.find_element(By.CSS_SELECTOR, "#i37 > div.vd3tt > div").click()
    elif(education == 7):
        driver.find_element(By.CSS_SELECTOR, "#i40 > div.vd3tt > div").click()
    elif(education == 8):
        driver.find_element(By.CSS_SELECTOR, "#i43 > div.vd3tt > div").click()

    #dad's education
    element = driver.find_element(By.CSS_SELECTOR, "#i46 > span.M7eMe")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    education = random.randint(1, 8)
    if(education == 1):
        driver.find_element(By.CSS_SELECTOR, "#i51 > div.vd3tt > div").click()
    elif(education == 2):
        driver.find_element(By.CSS_SELECTOR, "#i54 > div.vd3tt > div").click()
    elif(education == 3):
        driver.find_element(By.CSS_SELECTOR, "#i57 > div.vd3tt > div").click()
    elif(education == 4):
        driver.find_element(By.CSS_SELECTOR, "#i60 > div.vd3tt > div").click()
    elif(education == 5):
        driver.find_element(By.CSS_SELECTOR, "#i63 > div.vd3tt > div").click()
    elif(education == 6):
        driver.find_element(By.CSS_SELECTOR, "#i66 > div.vd3tt > div").click()
    elif(education == 7):
        driver.find_element(By.CSS_SELECTOR, "#i69 > div.vd3tt > div").click()
    elif(education == 8):
        driver.find_element(By.CSS_SELECTOR, "#i72 > div.vd3tt > div").click()

    #residence
    residences = ['urban', 'rural']
    if(random.choice(residences) == 'urban'):
        driver.find_element(By.CSS_SELECTOR, "#i80 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i83 > div.vd3tt > div").click()

    #type of house
    types = ['kutcha', 'pucca', 'semi-pucca']
    if(random.choice(types) == 'kutcha'):
        driver.find_element(By.CSS_SELECTOR, "#i91 > div.vd3tt > div").click()
    elif(random.choice(types) == 'pucca'):
        driver.find_element(By.CSS_SELECTOR, "#i94 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i97 > div.vd3tt > div").click()

    #type of family
    element = driver.find_element(By.CSS_SELECTOR, "#i100 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    types = ['joint', 'nuclear']
    if(random.choice(types) == 'nuclear'):
        driver.find_element(By.CSS_SELECTOR, "#i105 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i108 > div.vd3tt > div").click()
    
    #number of family members
    num = random.randint(3, 10)
    num_family = num
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(9) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(str(num))    
    
    #socioeconomic status
    types = ['upper', 'middle', 'lower']
    if(random.choice(types) == 'upper'):
        driver.find_element(By.CSS_SELECTOR, "#i121 > div.vd3tt > div").click()
    elif(random.choice(types) == 'middle'):
        driver.find_element(By.CSS_SELECTOR, "#i124 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i127 > div.vd3tt > div").click()
    
    #occupational status of mother
    jobs = ['unemployed', 'self employed', 'labourer', 'government job', 'private job']
    if random.choice(jobs) == 'government job':
        driver.find_element(By.CSS_SELECTOR, "#i135 > div.vd3tt > div").click()
    elif random.choice(jobs) == 'private job':    
        driver.find_element(By.CSS_SELECTOR, "#i138 > div.vd3tt > div").click()
    elif random.choice(jobs) == 'labourer':
        driver.find_element(By.CSS_SELECTOR, "#i141 > div.vd3tt > div").click()
    elif random.choice(jobs) == 'self employed':
        driver.find_element(By.CSS_SELECTOR, "#i144 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i147 > div.vd3tt > div").click()
    
    #occupational status of father
    element = driver.find_element(By.CSS_SELECTOR, "#i150 > span.M7eMe")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(jobs) == 'government job':
        driver.find_element(By.CSS_SELECTOR, "#i155 > div.vd3tt > div").click()
    elif random.choice(jobs) == 'private job':    
        driver.find_element(By.CSS_SELECTOR, "#i158 > div.vd3tt > div").click()
    elif random.choice(jobs) == 'labourer':
        driver.find_element(By.CSS_SELECTOR, "#i161 > div.vd3tt > div").click()
    elif random.choice(jobs) == 'self employed':
        driver.find_element(By.CSS_SELECTOR, "#i164 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i167 > div.vd3tt > div").click()
    
    #place of cooking
    places = ['inside room', 'separate room']
    if random.choice(places) == 'inside room':
        driver.find_element(By.CSS_SELECTOR, "#i175 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i178 > div.vd3tt > div").click()

    #type of fuel used
    fuels = ['lpg', 'firewood']
    if random.choice(fuels) == 'lpg':
        driver.find_element(By.CSS_SELECTOR, "#i186 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i189 > div.vd3tt > div").click()
    
    #is there a window
    binary = ['yes', 'no']
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i200 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i203 > div.vd3tt > div").click()
    
    #is your child present at the time of cooking
    element = driver.find_element(By.CSS_SELECTOR, "#i206 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i211 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i214 > div.vd3tt > div").click()

    #is there adequate cross ventilation
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i222 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i225 > div.vd3tt > div").click()
    
    #are there pets or cattle present
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i233 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i236 > div.vd3tt > div").click()

    #smoking near child
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i244 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i247 > div.vd3tt > div").click()

    #acute respriatory infection
    element = driver.find_element(By.CSS_SELECTOR, "#i250 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i255 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i258 > div.vd3tt > div").click()

    #next button
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2)").click()
    
    #section 2 
    time.sleep(2.5)
    
    #gestational age
    types = ['preterm', 'term', 'post term']
    if random.choice(types) == 'preterm':
        driver.find_element(By.CSS_SELECTOR, "#i6 > div.vd3tt > div").click()
    elif random.choice(types) == 'term':
        driver.find_element(By.CSS_SELECTOR, "#i9 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i12 > div.vd3tt > div").click()
    
    #birth order
    num = random.randint(1, 3)
    if num == 1:
        driver.find_element(By.CSS_SELECTOR, "#i20 > div.vd3tt > div").click()
    elif num == 2:
        driver.find_element(By.CSS_SELECTOR, "#i23 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i26 > div.vd3tt > div").click()

    #gap between births
    element = driver.find_element(By.CSS_SELECTOR, "#i29 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i34 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i37 > div.vd3tt > div").click()
    
    #place of birth
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i45 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i48 > div.vd3tt > div").click()

    #weight at birth
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i56 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i59 > div.vd3tt > div").click()

    #number of siblings
    siblings = num_family - 3
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(7) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(str(siblings))
    
    #immunization status
    element = driver.find_element(By.CSS_SELECTOR, "#i67 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i72 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i75 > div.vd3tt > div").click()
    #next button
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2)").click()
    
    #section 3
    time.sleep(2.5)

    #breastfeeding initiated
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i6 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i9 > div.vd3tt > div").click()

    #breastfeeding time
    times = ['within 1 hour', '1 to 4 hours', 'after 4 hours']
    if random.choice(times) == 'within 1 hour':
        driver.find_element(By.CSS_SELECTOR, "#i17 > div.vd3tt > div").click()
    elif random.choice(times) == '1 to 4 hours':
        driver.find_element(By.CSS_SELECTOR, "#i20 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i23 > div.vd3tt > div").click()

    #colostrum
    element = driver.find_element(By.CSS_SELECTOR, "#i26 > span.M7eMe")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i31 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i34 > div.vd3tt > div").click()
    
    #food given
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i42 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i45 > div.vd3tt > div").click()
    
    #exclusive breastfeeding
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i53 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i56 > div.vd3tt > div").click()
    
    #supplementary feeding
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i64 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i67 > div.vd3tt > div").click()
    
    #mixed feeding
    element = driver.find_element(By.CSS_SELECTOR, "#i70 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i75 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i78 > div.vd3tt > div").click()
    
    #bottle
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i86 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i89 > div.vd3tt > div").click()

    #bottle cleaning
    types = ['after every feed', 'once a day', 'less frequently']
    if random.choice(types) == 'after every feed':
        driver.find_element(By.CSS_SELECTOR, "#i97 > div.vd3tt > div").click()
    elif random.choice(types) == 'once a day':
        driver.find_element(By.CSS_SELECTOR, "#i100 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i103 > div.vd3tt > div").click()

    #next button
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2)").click()
    
    #section 4
    time.sleep(2.5)
    
    #number of meals
    num_meals =[1,2,3,4]
    if random.choice(num_meals) == 1:
        driver.find_element(By.CSS_SELECTOR, "#i6 > div.vd3tt > div").click()
    elif random.choice(num_meals) == 2:
        driver.find_element(By.CSS_SELECTOR, "#i9 > div.vd3tt > div").click()
    elif random.choice(num_meals) == 3:
        driver.find_element(By.CSS_SELECTOR, "#i12 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i15 > div.vd3tt > div").click()
    
    #meals skipped?
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i23 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i26 > div.vd3tt > div").click()

    #fast food consumed?
    element = driver.find_element(By.CSS_SELECTOR, "#i29 > span")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    types = ['frequently', 'occasionally', 'rarely']
    if random.choice(types) == 'frequently':
        driver.find_element(By.CSS_SELECTOR, "#i34 > div.vd3tt > div").click()
    elif random.choice(types) == 'rarely':
        driver.find_element(By.CSS_SELECTOR, "#i37 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i40 > div.vd3tt > div").click()
    
    #meat consumption
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i48 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i51 > div.vd3tt > div").click()

    #vegetable consumption
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i59 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i62 > div.vd3tt > div").click()
    
    #fruit consumption
    if random.choice(binary) == 'yes':
        driver.find_element(By.CSS_SELECTOR, "#i70 > div.vd3tt > div").click()
    else:
        driver.find_element(By.CSS_SELECTOR, "#i73 > div.vd3tt > div").click()

    #next button
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2)").click()

    #section 5
    time.sleep(2.5)
    diseases = ['acute otitis', 'pertussis', 'tonsillopharyngitis', 'pneumonia', 'bronchiolitis']
    disease_choice = random.choice(diseases)
    if disease_choice == 'acute otitis':
        driver.find_element(By.CSS_SELECTOR, "#i10").click()
    elif disease_choice == 'pertussis':
        driver.find_element(By.CSS_SELECTOR, "#i13").click()
    elif disease_choice == 'tonsillopharyngitis':
        driver.find_element(By.CSS_SELECTOR, "#i16").click()
    elif disease_choice == 'pneumonia':
        driver.find_element(By.CSS_SELECTOR, "#i19").click()
    
    #next button
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div:nth-child(2)").click()
    
    #section 6
    time.sleep(2.5)
    if disease_choice == 'acute otitis':
        driver.find_element(By.CSS_SELECTOR, "#i10").click()
    elif disease_choice == 'pertussis':
        driver.find_element(By.CSS_SELECTOR, "#i13").click()
    elif disease_choice == 'tonsillopharyngitis':
        driver.find_element(By.CSS_SELECTOR, "#i16").click()
    elif disease_choice == 'pneumonia':
        driver.find_element(By.CSS_SELECTOR, "#i19").click()
    
    #submit button
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd").click()
    time.sleep(5)