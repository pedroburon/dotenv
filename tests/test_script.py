import os
from tempfile import mkstemp
from unittest import TestCase

from dotenv import set_variable, Dotenv, get_variable


class FunctionalTest(TestCase):
    def setUp(self):
        fd, self.file_path = mkstemp()
        with open(self.file_path, 'w') as file:
            file.write("FOO='bar'\n")
            file.write("Bar=foo'\n")
            file.write("baz=1234'\n")
        self.dotenv = Dotenv(self.file_path)

    def tearDown(self):
        os.unlink(self.file_path)

	def test_set_new_variable(self):
		result = set_variable(self.file_path, 'asd', 'qwe')

		self.assertEqual(0, result)

		dotenv = Dotenv(self.file_path)
		self.assertIn('asd', dotenv)
		self.assertEqual('qwe', dotenv['asd'])

	def test_set_existing_variable(self):
		result = set_variable(self.file_path, 'baz', '987')

		self.assertEqual(0, result)

		dotenv = Dotenv(self.file_path)
		self.assertIn('baz', dotenv)
		self.assertEqual('987', dotenv['baz'])

	def test_get_variable(self):
		result = get_variable(self.file_path, 'baz')

		self.assertEqual('1234', result)
