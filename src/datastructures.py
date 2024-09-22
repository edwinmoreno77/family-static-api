"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):

        self.last_name = last_name
        self._members = [
            {"id":1, "first_name":"John", "last_name":"Jackson", "age":33, "lucky_numbers":[7,13,22]},
            {"id":2, "first_name":"Jane", "last_name":"Jackson", "age":35, "lucky_numbers":[10,14,3]},
            {"id":3, "first_name":"Jimmy ", "last_name":"Jackson", "age":5, "lucky_numbers":[1]}
            ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):

        member_name_exist = list(filter(lambda user:user["first_name"] == member["first_name"], self._members))
        if len(member_name_exist) > 0:
            return None
        else:
            member["last_name"] = self.last_name
            member["id"] = self._generateId()
            self._members.append(member)
            return member

    def delete_member(self, id):
        self._members = list(filter(lambda user:user["id"] != id, self._members))
        return self._members

    def get_member(self, id):
        member = list(filter(lambda user: user["id"] == id, self._members))
        return member
    
    def get_member_by_first_name(self, first_name):
        member = list(filter(lambda user: user["first_name"] == first_name, self._members))
        return member

    def get_all_members(self):
        return self._members
