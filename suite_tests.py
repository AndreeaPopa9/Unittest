import unittest
import HtmlTestRunner
from tests import test_login

class TestSuite(unittest.TestSuite):

    def test_suite(self):
        smoke_tests = unittest.TestSuite()
        smoke_tests.addTest([unittest.defaultTestLoader.loadTestsFromTestCase(test_login.Login)])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports =True, report_name="suiteCodePen").run(smoke_tests)