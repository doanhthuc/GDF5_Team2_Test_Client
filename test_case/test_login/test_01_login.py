import pytest
import allure
import time

from common.logger import logger
from network import error_code

from utils.read_excel import *
from modules.game import Game

# get test data
test_login_data = get_data_from_xls("test_data\\test_login.xls", "Sheet1")

@allure.step("step 1 =>> user login")
def step_1(username):
    logger.info("step 1 ==>> user login：{}".format(username))

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("single_interface")
@allure.feature("login_module")
class TestUserLogin:

    @allure.story("use case - login")
    @allure.description("test user login ok")
    @allure.issue("https://mantistbt.zingplay.com", name="1")
    @allure.testcase("https://mantistbt.zingplay.com", name="2")
    @allure.title("Test data：【 {username}，{password}，{except_result}，{except_code},{except_msg}】")
    #@pytest.mark.single
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg", test_login_data)
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** start test case ***************")

        # Rule đăng kí name, pass: Số kí tự 6-20, bao gồm cả chữ và số, không chứa các kí tự đặc biệt
        logger.info("check {} {} {} {} {}".format(username, password, except_result, except_code, except_msg))

        game2 = Game()

        game2.login(username, password)
        step_1(username)
        time.sleep(0.5)

        login_code = game2.get_login_code()

        if login_code == 0:

            assert str(login_code) == except_code, "invalid error code"

            #assert except_code


            # check login success
            assert True, except_msg

            # get position
            game2.get_player_module().send_get_player_info()
            time.sleep(0.5)
            uId = game2.get_player_module().get_player_name()

            assert uId == username, "invalid user name"

            # logout
        
        game2.logout()
        logger.info("*************** end of test case ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_login.py"])