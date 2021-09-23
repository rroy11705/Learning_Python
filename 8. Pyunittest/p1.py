class Person:
    name = []
    interests = {}

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'there is no such user'
        else:
            return self.name[user_id]

    def set_interests(self, user_id, interest):
        if user_id >= len(self.name):
            return 'not added successfully'
        else:
            if user_id in self.interests.keys():
                self.interests[user_id].append(interest)
            else:
                self.interests[user_id] = [interest]
            return 'added successfully'

    def get_interests(self, user_id):
        if user_id >= len(self.name):
            return 'there is no such user'
        else:
            if user_id in self.interests.keys():
                return self.interests[user_id]
            else:
                return f'no interest of user associated with user id {user_id} is found'


if __name__ == '__main__':
    person = Person()
    print('User andre is been added with id', person.set_name('andre'))
    print('User associated with id 0 is', person.get_name(0))
    print('An Interest of User associated with id 0 which is c++ is', person.set_interests(0, 'c++'))
    print('An Interest of User associated with id 0 which is c++ is', person.set_interests(0, 'python'))
    print('An Interest of User associated with id 0 which is c++ is', person.set_interests(0, 'java'))
    print('Interests of User associated with id 0 is', person.get_interests(0))
