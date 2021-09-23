import unittest
from lessons.pyunittest.p1 import Person as PersonClass


class POneTest(unittest.TestCase):

    person = PersonClass()
    user_id = []
    user_name = []
    user_interests = {}

    def test_set_name(self):
        for i in range(1000):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNotNone(user_id)
            self.user_id.append(user_id)
        print('finish test case')

    def test_get_name(self):
        length = len(self.user_id)
        for i in range(6):
            if i < length:
                self.assertEqual(self.user_name[i],
                                 self.person.get_name(self.user_id(i)))
            else:
                self.assertEqual('there is no such user', self.person.get_name(i))

    def test_set_interests(self):
        length = len(self.user_id)
        for i in range(10):
            if i < length:
                for j in range(5):
                    interest = 'interest' + str(j)
                    if self.user_id(i) in self.user_interests.keys():
                        self.user_interests[self.user_id(i)].append(interest)
                        self.assertEqual('added successfully',
                                         self.person.set_interests(self.user_id(i), interest))
                    else:
                        self.user_interests[self.user_id(i)] = interest
                else:
                    for j in range(5):
                        interest = 'interest' + str(j)
                        self.assertEqual('not added successfully', self.person.set_interests(i, interest))


if __name__ == '__main__':
    unittest.main()
