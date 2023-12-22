class Login:
    # Login
    username_input_box = "username"
    password_input_box = "password"
    submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    invalid_msg = "//*[contains(@class,'alert-content-text')]"
    header_text = "//h6[contains(@class,'topbar-header')]"


class Add_Employee:
    # Add employee
    PIM = "//ul[@class='oxd-main-menu']//li[2]//a"
    add_employee = "//nav[@class='oxd-topbar-body-nav']//ul//li[3]"
    add_img = 'input[type="file"]'
    first_name = "//input[@name='firstName']"
    middle_name = '//input[@name="middleName"]'
    last_name = '//input[@name="lastName"]'
    emp_id = '//*[contains(@class,"employee-form")]/div/div[2]//input'
    create_login_rb = '//div[@class="oxd-switch-wrapper"]'
    user_name = '//*[contains(@class,"oxd-form-row")][3]//div[2]/input'
    pass_word = '//*[contains(@class,"gutters user-password-cell")]//input'
    con_pwd = '//*[contains(@class,"oxd-grid-2")]/div[2]//input[@type="password"]'
    save1 = 'button[type="submit"]'
    success1 = '//p[contains(@class,"message oxd-toast-content-text")]'


class Personal_Detail:
    # Personal Details
    ot_id = '(//input[@class="oxd-input oxd-input--active"])[4]'
    dl = '(//*[contains(text(),"License Number")]/../following::*/input)[1]'
    exp_dl = '(//input[@class="oxd-input oxd-input--active"])[6]'
    ssn_no = '(//*[text()="SSN Number"]/../following::div/input)[1]'
    sin_no = '(//*[text()="SIN Number"]/../following::div/input)[1]'
    nation = '(//div[@class="oxd-select-text-input"])[1]'
    mat_stat = '(//div[@class="oxd-select-text-input"])[2]'
    dob = '(//input[@class="oxd-input oxd-input--active"])[9]'
    gender = '//label[text()="Male"]'
    miltary = '(//input[@class="oxd-input oxd-input--active"])[10]'
    save2 = '(//button[@type="submit"])[1]'
    success2 = 'p[class*="toast-message oxd-toast-content-text"]'
    blood = '(//div[@class="oxd-select-text-input"])[3]'
    save3 = '(//button[@type="submit"])[2]'
    success3 = 'p[class*="toast-message oxd-toast-content-text"]'


class Edit_Details:
    # Edit
    emp_list = '//a[text()="Employee List"]'
    edit_btn = '(//div[@class="oxd-table-card"])[1]//i[@class="oxd-icon bi-pencil-fill"]'
    dl_ed = '(//input[@class="oxd-input oxd-input--active"])[5]'
    exp_dl_ed = '(//input[contains(@placeholder,"yyyy")])[1]'
    ssn_no_ed = '(//input[@class="oxd-input oxd-input--active"])[7]'
    sin_no_ed = '(//input[@class="oxd-input oxd-input--active"])[8]'
    nation_ed = '(//div[@class="oxd-select-text-input"])[1]'
    mat_stat_ed = '(//div[@class="oxd-select-text-input"])[2]'
    dob_ed = '(//input[contains(@placeholder,"yyyy")])[2]'
    gender_ed = '//label[text()="Male"]'
    miltary_ed = '(//input[@class="oxd-input oxd-input--active"])[10]'
    save2_ed = '(//button[@type="submit"])[1]'
    success2_ed = 'p[class*="toast-message oxd-toast-content-text"]'
    blood_ed = '(//div[@class="oxd-select-text-input"])[3]'
    save3_ed = '(//button[@type="submit"])[2]'
    success3_ed = 'p[class*="toast-message oxd-toast-content-text"]'
    add = 'i[class="oxd-icon bi-plus oxd-button-icon"]'
    up_res = 'input[type="file"]'
    save4_ed = 'div[class="orangehrm-attachment"] button[type="submit"]'
    success4_ed = 'p[class*="toast-message oxd-toast-content-text"]'


class Delete_emp:
    # Delete
    dele_btn = '(//div[@class="oxd-table-card"])[1]//i[@class="oxd-icon bi-trash"]'
    dele_pop = '//div[contains(@class,"dialog-popup")]'
    yes_btn = '//button[contains(@class,"button--label-danger")]'
    del_msg = 'p[class*="toast-message oxd-toast-content-text"]'

