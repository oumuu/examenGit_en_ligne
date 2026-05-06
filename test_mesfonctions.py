import unittest

from mesfonctions import (
	addition,
	soustraction,
	multiplication,
	division,
	est_pair,
	factorielle,
	inverser_chaine,
	est_palindrome,
	maximum,
	compter_voyelles,
)


class TestMesFonctions(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(addition(2, 3), 5)
		self.assertEqual(addition(-1, 1), 0)

	def test_soustraction(self):
		self.assertEqual(soustraction(5, 3), 2)
		self.assertEqual(soustraction(0, 5), -5)

	def test_multiplication(self):
		self.assertEqual(multiplication(3, 4), 12)
		self.assertEqual(multiplication(-2, 3), -6)

	def test_division(self):
		self.assertEqual(division(10, 2), 5)
		with self.assertRaises(ValueError):
			division(5, 0)

	def test_est_pair(self):
		self.assertTrue(est_pair(4))
		self.assertFalse(est_pair(7))

	def test_factorielle(self):
		self.assertEqual(factorielle(0), 1)
		self.assertEqual(factorielle(5), 120)
		with self.assertRaises(ValueError):
			factorielle(-1)

	def test_inverser_chaine(self):
		self.assertEqual(inverser_chaine("abc"), "cba")
		self.assertEqual(inverser_chaine(""), "")

	def test_est_palindrome(self):
		self.assertTrue(est_palindrome("radar"))
		self.assertFalse(est_palindrome("python"))

	def test_maximum(self):
		self.assertEqual(maximum([1, 3, 2]), 3)
		with self.assertRaises(ValueError):
			maximum([])

	def test_compter_voyelles(self):
		self.assertEqual(compter_voyelles("aeiou"), 5)
		# "Bonjour" -> b o n j o u r => o, o, u = 3 voyelles
		self.assertEqual(compter_voyelles("Bonjour"), 3)


if __name__ == "__main__":
	unittest.main()