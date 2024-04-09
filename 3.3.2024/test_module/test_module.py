import math_module
import included_module
import dicts_module


def test_the_module():
    my_dict = {
        "name" : "hasan",
        "age": 25
    }
    print(math_module.bigger(5,3))
    print(math_module.bigger(10,13))
    print(math_module.smaller(4,5))
    print(math_module.smaller(5,2))
    print(included_module.included(3,[1,2,3,5,6,]))
    print(included_module.included(3,[1,2,4,5,6,7,8]))
    print(math_module.is_equal(9,9))
    print(math_module.is_equal(7,9))
    print(dicts_module.is_a_key("name",my_dict))
    print(dicts_module.is_a_key("7",my_dict))
    print(dicts_module.is_a_value("25",my_dict))
    print(dicts_module.is_a_value("what",my_dict))


test_the_module()