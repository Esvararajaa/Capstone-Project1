from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import pytest
from Test_Data import data
from Test_Locators import locators


class TestEmploy:

    # booting method
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    # Test Case ID: TC_Login_01
    def test_login01(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(
            data.Data().username01)
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(
            data.Data().password01)
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        msg = self.driver.find_element(By.XPATH, locators.Login().header_text).text
        assert msg == 'Dashboard'
        print(f"{msg} page displayed succesfully")
        print(f"SUCCESS : Logged with username {data.Data().username01} and password {data.Data().password01}")

    # Test Case ID: TC_Login_02
    def test_login02(self, booting_function):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(
            data.Data().username02)
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(
            data.Data().password02)
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        msg = self.driver.find_element(By.XPATH, locators.Login().invalid_msg).text
        assert msg == 'Invalid credentials'
        print(msg)
        print(f"SUCCESS : Logged with username {data.Data().username02} and password {data.Data().password02}")

    # Test Case ID: TC_PIM_01
    def test_create_emp(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Data().url)
        self.wait = WebDriverWait(self.driver, 20)
        self.alert = Alert(self.driver)
        self.act = ActionChains(self.driver)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(data.Data().username01)
        print("Username entered")
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(data.Data().password01)
        print("Password entered")
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        print("Submit button clicked")
        self.driver.find_element(By.XPATH, locators.Add_Employee().PIM).click()
        print("Clicked PIM button")
        self.driver.find_element(By.XPATH, locators.Add_Employee().add_employee).click()
        print("Add employee button is clicked")
        self.driver.find_element(By.CSS_SELECTOR, locators.Add_Employee().add_img).send_keys(data.Data().upload_img)
        print("Image uploaded")
        ran_name = data.Data().fst_name + str(random.randrange(1000, 9999))
        print(ran_name)
        self.driver.find_element(By.XPATH, locators.Add_Employee().first_name).send_keys(ran_name)
        print("First name entered")
        self.driver.find_element(By.XPATH, locators.Add_Employee().middle_name).send_keys(data.Data().mid_name)
        print("Middle name entered")
        self.driver.find_element(By.XPATH, locators.Add_Employee().last_name).send_keys(data.Data().lst_name)
        print("Last name entered")
        id = self.driver.find_element(By.XPATH, locators.Add_Employee().emp_id)
        id.send_keys(Keys.CONTROL + "a")
        id.send_keys(Keys.DELETE)
        print("Employee ID is cleared")
        ran_id = random.randrange(1000, 9999)
        id.send_keys(ran_id)
        print("Employee ID is newly added")
        self.driver.find_element(By.XPATH, locators.Add_Employee().create_login_rb).click()
        print("Toggle button is clicked")
        ran_name1 = data.Data().fst_name + str(random.randrange(1000, 9999))
        print(ran_name1)
        self.driver.find_element(By.XPATH, locators.Add_Employee().user_name).send_keys(ran_name1)
        print("Username is entered")
        self.driver.find_element(By.XPATH, locators.Add_Employee().pass_word).send_keys(data.Data().pass_word)
        print("Password is entered")
        self.driver.find_element(By.XPATH, locators.Add_Employee().con_pwd).send_keys(data.Data().con_pass)
        print("Confirmed the password")
        self.driver.find_element(By.CSS_SELECTOR, locators.Add_Employee().save1).click()
        print("Save button clicked")
        success_msg1 = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Add_Employee().success1))).text
        print(f"{success_msg1} the employee into the orangehrm")
        self.driver.implicitly_wait(20)
        # Personal Details
        self.driver.find_element(By.XPATH, locators.Personal_Detail().dl).send_keys(data.Personal().dl_no)
        print("Driving License number entered")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().exp_dl).send_keys(data.Personal().exp_dl)
        print("Expiry of driving license is entered")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().ssn_no).send_keys(data.Personal().ssn_no)
        print("SSN number is entered")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().sin_no).send_keys(data.Personal().sin_no)
        print("SIN number is entered")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().nation).send_keys('i'*4 + Keys.ENTER)
        print("Nationality dropdown used")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().mat_stat).send_keys('s' + Keys.ENTER)
        print("Marital status updated")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().dob).send_keys(data.Personal().dob)
        print("Date of birth is entered")
        male = self.driver.find_element(By.XPATH, locators.Personal_Detail().gender)
        if male.is_selected():
            pass
        else:
            male.click()
        print("Gender is selected")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().miltary).send_keys(data.Personal().miltary)
        print("Miltary service data entered")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().save2).click()
        print("Save button is clicked")
        success_msg2 = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators.Personal_Detail().success2))).text
        print(f"{success_msg2} the personal details of the employee into the orangehrm")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().blood).send_keys('a'*3 + Keys.ENTER)
        print("Blood group is entered")
        self.driver.find_element(By.XPATH, locators.Personal_Detail().save3).click()
        print("Save button clicked")
        success_msg3 = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators.Personal_Detail().success3))).text
        print(f"{success_msg3} the personal details of the employee with blood group")
        assert success_msg3 == 'Successfully Saved' or 'Successfully Updated'
        print(f"SUCCESS : Logged with username {data.Data().username02} and password {data.Data().password01}")

    # Test Case ID: TC_PIM_02
    def test_edit_emp(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Data().url)
        self.wait = WebDriverWait(self.driver, 20)
        self.alert = Alert(self.driver)
        self.act = ActionChains(self.driver)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(data.Data().username01)
        print("Username entered")
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(data.Data().password01)
        print("Password entered")
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        print("Submit button clicked")
        self.driver.find_element(By.XPATH, locators.Add_Employee().PIM).click()
        print("Clicked PIM button")
        for _ in range(20):
            self.act.send_keys(Keys.DOWN).perform()
        self.driver.find_element(By.XPATH, locators.Edit_Details().edit_btn).click()
        print("Edit button is clicked for the first employee")
        dl = self.driver.find_element(By.XPATH, locators.Edit_Details().dl_ed)
        dl.send_keys(Keys.CONTROL + 'a')
        dl.send_keys(Keys.DELETE)
        print("Driver license field cleared")
        dl.send_keys(data.Edit().dl_no_ed)
        print("Driving License number entered")
        ex_dl = self.driver.find_element(By.XPATH, locators.Edit_Details().exp_dl_ed)
        ex_dl.send_keys(Keys.CONTROL + 'a')
        ex_dl.send_keys(Keys.DELETE)
        print("Expiry driving license field cleared")
        ex_dl.send_keys(data.Edit().exp_dl_ed)
        print("Expiry of driving license is entered")
        ss_n = self.driver.find_element(By.XPATH, locators.Edit_Details().ssn_no_ed)
        ss_n.send_keys(Keys.CONTROL+'a')
        ss_n.send_keys(Keys.DELETE)
        print("SSN field cleared")
        ss_n.send_keys(data.Edit().ssn_no_ed)
        print("SSN number is entered")
        sin_n = self.driver.find_element(By.XPATH, locators.Edit_Details().sin_no_ed)
        sin_n.send_keys(Keys.CONTROL+'a')
        sin_n.send_keys(Keys.DELETE)
        print("SIN Number field cleared")
        sin_n.send_keys(data.Edit().sin_no_ed)
        print("SIN number is entered")
        self.driver.find_element(By.XPATH, locators.Edit_Details().nation_ed).send_keys('i' * 4 + Keys.ENTER)
        print("Nationality dropdown used")
        self.driver.find_element(By.XPATH, locators.Edit_Details().mat_stat_ed).send_keys('s' + Keys.ENTER)
        print("Marital status updated")
        dob = self.driver.find_element(By.XPATH, locators.Edit_Details().dob_ed)
        dob.send_keys(Keys.CONTROL+'a')
        dob.send_keys(Keys.DELETE)
        print("Date of birth field cleared")
        dob.send_keys(data.Edit().dob_ed)
        print("Date of birth is entered")
        gen = self.driver.find_element(By.XPATH, locators.Edit_Details().gender_ed)
        if gen.is_selected():
            pass
        else:
            gen.click()
        print("Gender is selected")
        mil = self.driver.find_element(By.XPATH, locators.Edit_Details().miltary_ed)
        mil.send_keys(Keys.CONTROL+'a')
        mil.send_keys(Keys.DELETE)
        print("Military field cleared")
        mil.send_keys(data.Edit().miltary_ed)
        print("Miltary service data entered")
        self.driver.find_element(By.XPATH, locators.Edit_Details().save2_ed).click()
        print("Save button is clicked")
        success_msg2 = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locators.Edit_Details().success2_ed))).text
        print(f"{success_msg2} the personal details of the employee into the orangehrm")
        self.driver.find_element(By.XPATH, locators.Edit_Details().blood_ed).send_keys('a' * 3 + Keys.ENTER)
        print("Blood group is entered")
        self.driver.find_element(By.XPATH, locators.Edit_Details().save3_ed).click()
        print("Save button clicked")
        success_msg3_ed = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locators.Edit_Details().success3_ed))).text
        print(f"{success_msg3_ed} the personal details of the employee with blood group")
        self.driver.find_element(By.CSS_SELECTOR, locators.Edit_Details().add).click()
        print("Add button clicked")
        self.driver.find_element(By.CSS_SELECTOR, locators.Edit_Details().up_res).send_keys(data.Edit().res)
        print("Resume file uploaded")
        success_msg4_ed = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locators.Edit_Details().success4_ed))).text
        print(f"{success_msg4_ed} the personal details of the employee with file")
        assert success_msg4_ed == 'Successfully Updated'

    # Test Case ID: TC_PIM_03
    def test_delete_emp(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Data().url)
        self.wait = WebDriverWait(self.driver, 20)
        self.alert = Alert(self.driver)
        self.act = ActionChains(self.driver)
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.NAME, locators.Login().username_input_box).send_keys(data.Data().username01)
        print("Username entered")
        self.driver.find_element(By.NAME, locators.Login().password_input_box).send_keys(data.Data().password01)
        print("Password entered")
        self.driver.find_element(By.XPATH, locators.Login().submit_button).click()
        print("Submit button clicked")
        self.driver.find_element(By.XPATH, locators.Add_Employee().PIM).click()
        print("Clicked PIM button")
        for _ in range(20):
            self.act.send_keys(Keys.DOWN).perform()
        self.driver.find_element(By.XPATH, locators.Delete_emp().dele_btn).click()
        print("delete button clicked")
        yes = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Delete_emp().yes_btn)))
        yes.click()
        print("Clicked the 'yes' button on the popup")
        suc_del_msg = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators.Delete_emp().del_msg))).text
        assert suc_del_msg == 'Successfully Deleted'
        print(f'{suc_del_msg} a employee record')
