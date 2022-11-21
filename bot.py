import os
import time
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
import botsettings

# CHANGE THIS TO WHERE YOUR WEB DRIVER IS
os.environ['PATH'] += r"C:/web-drivers"
driver = webdriver.Firefox()

# Opens cities war and inserts info from the botsettings
# Also it clicks the sign in button (WOAH ⭐⭐⭐)
driver.get("https://www.citieswar.com/")
driver.find_element(by="id", value="uid").send_keys(botsettings.username)
driver.find_element(by="id", value="pwd").send_keys(botsettings.password)
driver.find_element(by="id", value="signinplayer").click()
print("Log in sucessfull!")

# Checks if an element exists, returns true or false, idea is to
# keep checking untill it exists, to avoid failure due to the page taking too long
# to load
# the driver.find_element takes in 2 values, a method to find an element (id, class, xpath ...)
# so youll see how this is declared later on


def check_exists(by, value):
    try:
        driver.find_element(by=by, value=value)
    except NoSuchElementException:
        return False
    time.sleep(1)
    return True


# usage of the above function, keeps looking for the oil count to show up to continue
# the script
exists = False
while exists == False:
    exists = check_exists("id", "oil-count")
time.sleep(3)

# gets storage data and removes the commas to avoid
# future issues related to math
oil_count = driver.find_element(
    by="id", value="oil-count").text.replace(',', '')
steel_count = driver.find_element(
    by="id", value="steel-count").text.replace(',', '')
food_count = driver.find_element(
    by="id", value="food-count").text.replace(',', '')
rare_count = driver.find_element(
    by="id", value="rare-count").text.replace(',', '')
uranium_count = driver.find_element(
    by="id", value="uranium-count").text.replace(',', '')
gold_count = driver.find_element(
    by="id", value="money").text.replace(',', '')
# print the values for debugging reasons
print(f"oil = {oil_count}")
print(f"steel = {steel_count}")
print(f"food = {food_count}")
print(f"rare = {rare_count}")
print(f"uranium = {uranium_count}")
print(f"gold = {gold_count}")

# Calculates how many weapons can be produced by dividing cost by current amount


def minimum_amount_calculation(steel_cost, rare_cost, gold_cost):
    if steel_count == 0 or rare_count == 0 or gold_count == 0:
        # TODO check if they need just steel and gold
        return "ERROR: Not enough resources"
    else:
        if rare_cost != 0:
            steel_production = float(steel_count)/float(steel_cost)
        else:
            steel_production = 9999999
        if rare_cost != 0:
            rare_production = float(rare_count)/float(rare_cost)
        else:
            rare_production = 9999999
        if gold_cost != 0:
            gold_production = float(gold_count)/float(gold_cost)
        else:
            gold_production = 999999
        minimum_amount = min(
            steel_production, rare_production, gold_production)
        return minimum_amount
        # for the record i made a cool reference for a class name that
        #  would be steel division


# Best way i found of storing these values, to any maintainer who knows better im sorry
# can be easily expanded to include new equipment
# it just sets the values for equipment and uses them in that function above
# and the result goes into click_amount
match botsettings.equipment:
    case "M16":
        steel = 14
        rare = 0
        gold = 5
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "HK21":
        steel = 30
        rare = 0
        gold = 10
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "M240":
        steel = 35
        rare = 0
        gold = 15
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Striker40":
        steel = 70
        rare = 0
        gold = 18
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "SPG9":
        steel = 80
        rare = 15
        gold = 30
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "TwoS25":
        steel = 130
        rare = 60
        gold = 20
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "M777":
        steel = 160
        rare = 40
        gold = 50
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "BM21":
        steel = 180
        rare = 135
        gold = 150
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "M109":
        steel = 260
        rare = 110
        gold = 180
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "M41DK1":
        steel = 300
        rare = 110
        gold = 190
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "T90MS":
        steel = 390
        rare = 120
        gold = 180
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Merkava":
        steel = 395
        rare = 120
        gold = 200
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Challenger_2":
        steel = 480
        rare = 130
        gold = 260
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Abrams_M1A2":
        steel = 500
        rare = 130
        gold = 270
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Frigate":
        steel = 500
        rare = 130
        gold = 270
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Destroyer":
        steel = 500
        rare = 130
        gold = 270
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Cruiser":
        steel = 500
        rare = 130
        gold = 270
        click_amount = minimum_amount_calculation(steel, rare, gold)

    case "Submarine":
        steel = 500
        rare = 130
        gold = 270
        click_amount = minimum_amount_calculation(steel, rare, gold)


# setting exists to false to avoid problems since its just being reused
exists = False
while exists == False:
    exists = check_exists("id", "wnimage")

# opens weapons tab
driver.find_element(by="id", value="wnimage").click()


exists = False
while exists == False:
    exists = check_exists("link text", botsettings.equipment_class)

# picks chosen weapon type
driver.find_element(
    by="link text", value=botsettings.equipment_class).click()

# picks chosen weapon
# this is called a dictionary, the thing we're using to pick the equipment type is the
# produce button, the produce button has a different id for each equipment
weaponnames = {
    "M16": "makeeq1",
    "HK21": "makeeq2",
    "M240": "makeeq3",
    "Striker40": "makeeq4",
    "SPG9": "makeeq5",
    "TwoS25": "makeeq6",
    "M777": "makeeq7",
    "BM21": "makeeq8",
    "M109": "makeeq9",
    "M41DK1": "makeeq10",
    "T90MS": "makeeq11",
    "Merkava": "makeeq12",
    "Challenger_2": "makeeq13",
    "Abrams_M1A2": "makeeq14",
    "Frigate": "makeeq15",
    "Destroyer": "makeeq16",
    "Cruiser": "makeeq17",
    "Submarine": "makeeq18"
}
# turns the translation from the dictionary for the chosen equipment into a variable
desired_eqp = weaponnames[botsettings.equipment]

exists = False
while exists == False:
    exists = check_exists("id", desired_eqp)

driver.find_element(by="id", value=desired_eqp).click()
time.sleep(3)

# finally just clicks the + sign enough times to produce what you want
# prints click_amount to avoid issues
print(f" amount : {click_amount}")

for i in range(int(click_amount)):
    driver.find_element(by="css selector",
                        value=".bootstrap-touchspin-up").click()

driver.find_element(by="css selector",
                    value=".bootstrap-touchspin-down").click()

driver.find_element(by="id", value="produceWeapon").click()

time.sleep(1)

driver.find_element(
    by="xpath", value="/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]").click()

time.sleep(1)

# Checks if resources button is present
exists = False
while exists == False:
    exists = check_exists(
        "xpath", "/html/body/div[1]/div[16]/div[8]/ul/li[1]/div/i/img")

driver.find_element(
    by="xpath", value="/html/body/div[1]/div[16]/div[8]/ul/li[1]/div/i/img").click()

# gets storage data and removes the commas to avoid
# future issues related to math
oil_count = driver.find_element(
    by="id", value="oil-count").text.replace(',', '')
steel_count = driver.find_element(
    by="id", value="steel-count").text.replace(',', '')
food_count = driver.find_element(
    by="id", value="food-count").text.replace(',', '')
rare_count = driver.find_element(
    by="id", value="rare-count").text.replace(',', '')
uranium_count = driver.find_element(
    by="id", value="uranium-count").text.replace(',', '')
gold_count = driver.find_element(
    by="id", value="money").text.replace(',', '')
# print the values for debugging reasons
print(f"oil = {oil_count}")
print(f"steel = {steel_count}")
print(f"food = {food_count}")
print(f"rare = {rare_count}")
print(f"uranium = {uranium_count}")
print(f"gold = {gold_count}")

time.sleep(2)

if int(oil_count) > 10000:
    # checks if oil button is present
    exists = False
    while exists == False:
        exists = check_exists(
            "xpath", "/html/body/div[1]/div[16]/div[1]/article/header/ul/li[1]/a")

    # finds oil button
    driver.find_element(
        by="xpath", value="/html/body/div[1]/div[16]/div[1]/article/header/ul/li[1]/a").click()

    # types oil amount
    driver.find_element(by="id", value="convertCount1").send_keys(
        str(int(oil_count)-10000))

    # clicks sell button
    driver.find_element(by="id", value="turnres1").click()

    # checks if sell confirm pop-up appeared
    exists = False
    while exists == False:
        exists = check_exists(
            "xpath", "/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]")

    # Clicks the okay button
    driver.find_element(
        by="xpath", value="/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]").click()

time.sleep(2)

if int(food_count) > 10000:

    # checks if food button is present
    exists = False
    while exists == False:
        exists = check_exists(
            "xpath", "/html/body/div[1]/div[16]/div[1]/article/header/ul/li[3]/a")

    # finds food button
    driver.find_element(
        by="xpath", value="/html/body/div[1]/div[16]/div[1]/article/header/ul/li[3]/a").click()

    # types food amount
    driver.find_element(by="id", value="convertCount3").send_keys(
        str(int(food_count)-10000))

    # clicks sell button
    driver.find_element(by="id", value="turnres3").click()

    # checks if sell confirm pop-up appeared
    exists = False
    while exists == False:
        exists = check_exists(
            "xpath", "/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]")

    # Clicks the okay button
    driver.find_element(
        by="xpath", value="/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]").click()

time.sleep(2)

if int(uranium_count) > 0:

    # checks if food button is present
    exists = False
    while exists == False:
        exists = check_exists(
            "xpath", "/html/body/div[1]/div[16]/div[1]/article/header/ul/li[5]/a")

    # finds food button
    driver.find_element(
        by="xpath", value="/html/body/div[1]/div[16]/div[1]/article/header/ul/li[5]/a").click()

    # types food amount
    driver.find_element(by="id", value="convertCount5").send_keys(
        str(uranium_count))

    # clicks sell button
    driver.find_element(by="id", value="turnres5").click()

    # checks if sell confirm pop-up appeared
    exists = False
    while exists == False:
        exists = check_exists(
            "xpath", "/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]")

    # Clicks the okay button
    driver.find_element(
        by="xpath", value="/html/body/div[6]/div[2]/div/div/div/div/div[4]/input[1]").click()

driver.close()
