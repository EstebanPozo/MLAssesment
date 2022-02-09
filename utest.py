import unittest
from datainput import data_load
import pandas as pd

class HelloworldTests(unittest.TestCase):
    

    def test_get_helloworld(self):
        data = pd.read_csv(r"C:\Users\Dell\Niologic\Seattle_Real_Time_Fire_911_Calls-v.csv")
        self.assertEqual(data_load(data), 'Data loaded')

if __name__ == '__main__':
    unittest.main()