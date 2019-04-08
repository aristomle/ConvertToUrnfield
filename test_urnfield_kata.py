import urnfield_kata as classUnderTest
import unittest

class TestUrnfieldKata(unittest.TestCase):

    def test_convert_for_zero(self):
        self.assertEqual(classUnderTest.convert(0), '', 'should return empty string')
    
    def test_convert_for_one(self):
        self.assertEqual(classUnderTest.convert(1), '/', 'should be / for 1 input')

    def test_convert_for_five(self):
        self.assertEqual(classUnderTest.convert(5), '\\')

    def test_convert_for_ten(self):
        self.assertEqual(classUnderTest.convert(10), '\\\\')

    def test_convert_for_mixed_slashes(self):
        self.assertEqual(classUnderTest.convert(6), '/\\')

    def test_get_forward_slashes(self):
        self.assertEquals(classUnderTest.get_forward_slashes(1), '/')
    
    def test_get_backward_slashes(self):
        self.assertEquals(classUnderTest.get_backward_slashes(1), '\\')
    

if __name__ == '__main__':
    unittest.main()