from login import get_username,get_password

def test_login_username():
    #预期结果:自己登入的账号
    expect_username = 'test01'
    #实际结果:显示在页面上的账号
    acutl_username = get_username()
    assert expect_username == acutl_username

def test_login_password():
    #预期结果:登入的密码
    expect_password = 'test01'
    #实际结果:显示在页面上的密码
    acutl_password = get_password()
    assert expect_password == acutl_password


#test_login_username()
#test_login_password()


