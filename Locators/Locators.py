class Locators:
    # Login page locators

    username_textbox_css = "input#username"
    password_textbox_css = "input#password"
    login_button_xpath = "//input[@class='btn btn-primary']"
    verify_button_xpath = "//input[@class='btn btn-primary']"

    # Project home page locators

    click_financial_dropdown_link_xpath = "//li[@id='el-3']//img"

    click_projects_link_xpath = "//a[@class='selected']"
    click_big_action_button_link_xpath = "(//DIV[@tabindex='0'])[2]"
    click_wa_link_xpath = "//*[@id='cose']/a[contains(., 'Withdrawal Application')]"
    click_withdrawal_application_xpath = "//div[@role='button'][contains(., 'Withdrawal Application')]"

    # Basic Details home page locators

    click_application_type_dropdown_xpath = "(//DIV[@class='v-filterselect-button'])[1]"
    select_direct_payment_xpath = "//td[@class='gwt-MenuItem'][contains(., 'Direct Payment')]"
    wa_number_textbox_css = "input#gwt-uid-8"
    application_currency_xpath = "(//DIV[@class='v-filterselect-button'])[2]"
    select_application_currency_xpath = "//td[@role='listitem'][contains(., 'USD')]"
    finance_dropdown_xpath = "(//DIV[@class='v-filterselect-button'])[3]"
    select_finance_xpath = "//TD[@class='gwt-MenuItem gwt-MenuItem-selected']"
    click_add_finance_xpath = "(//DIV[@tabindex='0'])[2]"
    amount_textbox_css = "#gwt-uid-22"
    confirm_proceed_button_xpath = "(//DIV[@tabindex='0'])[3]"

