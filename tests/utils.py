from unittest import TestCase

try:
    TestCase.assertIsInstance
    CompatibilityTestCase = TestCase
except AttributeError:
    class CompatibilityTestCase(TestCase):
        def assertIsInstance(self, obj, cls):
            assert obj, cls

        def assertNotIn(self, key, coll):
            assert key not in coll

        def assertIn(self, key, coll):
            assert key in coll

