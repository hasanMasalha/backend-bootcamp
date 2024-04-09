import unittest
import main
import raffle
import person
import ticket
from unittest.mock import patch


class testRaffleFuncs(unittest.TestCase):
    def test_check_if_part(self):
        raffle1 = raffle.raffle(1,0,[],3,[])
        person_to_add = person.person("hasan",[])
        raffle1.partecipents.append(person_to_add)
        self.assertTrue(main.check_if_part(raffle1, "hasan"))
        self.assertFalse(main.check_if_part(raffle1,"yaniev"))

    def test_check_patrecipents_number(self):
        raffle1 = raffle.raffle(1, 0, [], 3, [])
        person_to_add = person.person("John", [])
        self.assertTrue(main.check_patrecipents_number(raffle1, person_to_add))

        raffle1.partecipents.append(person.person("Alice", []))
        raffle1.partecipents.append(person.person("Bob", []))
        raffle1.partecipents.append(person.person("hasan", []))
        self.assertFalse(main.check_patrecipents_number(raffle1, person_to_add))

    def test_load_data(self):
        raffle1 = raffle.raffle(1, 0, [], 3, [])
        raffle1.partecipents.append(person.person("hasan",[]))
        main.load_data(raffle1)
        self.assertEqual(len(raffle1.partecipents), 1)

if __name__ == '__main__':
    unittest.main()