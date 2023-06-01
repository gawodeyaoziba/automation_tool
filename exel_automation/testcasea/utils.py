import pytest

"""
function: 函数级，每个测试函数都会执行一次固件；默认的作用域为 function
class: 类级别，每个测试类执行一次，所有方法都可以使用；
module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。

"""

@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass