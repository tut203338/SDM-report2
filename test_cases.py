#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        #def test_sample1 (self):
        #        self.assertEqual (21, calc(3,7))

        #def test_sample2 (self):
        #        self.assertEqual (-1, calc(0,150))

        #def test_sample3 (self):
        #        self.assertEqual (-1, calc('a','b'))

        #def test_sample4 (self):
        #        self.assertEqual (-1, calc(0.1,999))

        def test1(self):
                self.assertEqual (-1,calc(0,0))
        def test2(self):
                self.assertEqual (-1,calc(0,1))
        def test3(self):
                self.assertEqual (-1,calc(0,1000))
        def test4(self):
                self.assertEqual (-1,calc(0,'b'))
        def test5(self):
                self.assertEqual (-1,calc(0,0.1))
        def test6(self):
                self.assertEqual (-1,calc(0,1.1))
        def test7(self):
                self.assertEqual (-1,calc(0,1000.1))
        def test8(self):
                self.assertEqual (-1,calc(1,0))
        def test9(self):
                self.assertEqual (1,calc(1,1))
        def test10(self):
                self.assertEqual (-1,calc(1,1000))
        def test11(self):
                self.assertEqual (-1,calc(1,'b'))
        def test12(self):
                self.assertEqual (-1,calc(1,0.1))
        def test13(self):
                self.assertEqual (-1,calc(1,1.1))
        def test14(self):
                self.assertEqual (-1,calc(1,1000.1))
        def test15(self):
                self.assertEqual (-1,calc(1000,0))
        def test16(self):
                self.assertEqual (-1,calc(1000,1))
        def test17(self):
                self.assertEqual (-1,calc(1000,1000))
        def test18(self):
                self.assertEqual (-1,calc(1000,'b'))
        def test19(self):
                self.assertEqual (-1,calc(1000,0.1))
        def test20(self):
                self.assertEqual (-1,calc(1000,1.1))
        def test21(self):
                self.assertEqual (-1,calc(1000,1000.1))
        def test22(self):
                self.assertEqual (-1,calc('a',0))
        def test23(self):
                self.assertEqual (-1,calc('a',1))
        def test24(self):
                self.assertEqual (-1,calc('a',1000))
        def test25(self):
                self.assertEqual (-1,calc('a','b'))
        def test26(self):
                self.assertEqual (-1,calc('a',0.1))
        def test27(self):
                self.assertEqual (-1,calc('a',1.1))
        def test28(self):
                self.assertEqual (-1,calc('a',1000.1))
        def test29(self):
                self.assertEqual (-1,calc(0.1,0))
        def test30(self):
                self.assertEqual (-1,calc(0.1,1))
        def test31(self):
                self.assertEqual (-1,calc(0.1,1000))
        def test32(self):
                self.assertEqual (-1,calc(0.1,'b'))
        def test33(self):
                self.assertEqual (-1,calc(0.1,0.1))
        def test34(self):
                self.assertEqual (-1,calc(0.1,1.1))
        def test35(self):
                self.assertEqual (-1,calc(0.1,1000.1))
        def test36(self):
                self.assertEqual (-1,calc(1.1,0))
        def test37(self):
                self.assertEqual (-1,calc(1.1,1))
        def test38(self):
                self.assertEqual (-1,calc(1.1,1000))
        def test39(self):
                self.assertEqual (-1,calc(1.1,'b'))
        def test40(self):
                self.assertEqual (-1,calc(1.1,0.1))
        def test41(self):
                self.assertEqual (-1,calc(1.1,1.1))
        def test42(self):
                self.assertEqual (-1,calc(1.1,1000.1))
        def test43(self):
                self.assertEqual (-1,calc(1000.1,0))
        def test44(self):
                self.assertEqual (-1,calc(1000.1,1))
        def test45(self):
                self.assertEqual (-1,calc(1000.1,1000))
        def test46(self):
                self.assertEqual (-1,calc(1000.1,'b'))
        def test47(self):
                self.assertEqual (-1,calc(1000.1,0.1))
        def test48(self):
                self.assertEqual (-1,calc(1000.1,1.1))
        def test49(self):
                self.assertEqual (-1,calc(1000.1,1000.1))
