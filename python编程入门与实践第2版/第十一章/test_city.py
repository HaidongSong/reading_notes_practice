import unittest

from city_function import city_function


class CityTestFunction(unittest.TestCase):
    """测试国家城市"""

    def test_citys(self):
        """
        测试1
        :return:
        """
        city_output = city_function("chile", "santiago")
        self.assertEqual(city_output, "Chile,Santiago")

    def test_citys_population(self):
        """测试添加population是否生效"""
        city_middle = city_function("chile", "santiago", "5000")
        self.assertEqual(city_middle, "Chile,Santiago-5000")


if __name__ == "__main__":
    unittest.main