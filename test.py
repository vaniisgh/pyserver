# contains the tests that run 

import unittest
import server

class Test(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'looking for tests? \n')

    def test_server_ok(self):
        rv = self.app.get('/test/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'looking for tests? \n')

    def test_run_tests(self):
        request = 'some request'
        rv = self.app.get(f'/tests/{request}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{request}", 'utf-8'), rv.data)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()