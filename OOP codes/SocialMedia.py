class Person:
    def __init__(self, username, age, bio, interests):
        self.username = username
        self.age = age
        self.bio = bio
        self.interests = interests

    def update_bio(self, new_bio):
        self.bio = new_bio

    def add_interest(self, new_interest):
        self.interests.append(new_interest)

    def remove_interest(self, interest):
        self.interests.remove(interest)

    def __str__(self):
        return f"username: {self.username}\nAge: {self.age}\nBio: {self.bio}\nInterests: {self.interests}"


class SocialGraph:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        self.people[person] = []

    def add_connection(self, person1, person2):
        if person1 in self.people:
            self.people[person1].append(person2)
        else:
            self.people[person1] = [person2]
        if person2 in self.people:
            self.people[person2].append(person1)
        else:
            self.people[person2] = [person1]

    def remove_connection(self, person1, person2):
        if person1 in self.people:
            self.people[person1].remove(person2)
        if person2 in self.people:
            self.people[person2].remove(person1)

    def get_common_friends(self, person1, person2):
        common_friends = []
        if person1 in self.people:
            for friend in self.people[person1]:
                if friend in self.people[person2]:
                    common_friends.append(friend)
        return common_friends


if __name__ == "__main__":
    graph = SocialGraph()

    user1 = Person("johan", 28, "I am a programmer", ["football", "coding"])
    user2 = Person("joe", 25, "I am a doctor", [
                   "chess", "singing", "football"])
    user3 = Person("jane", 23, "I am a lawyer", [
                   "dancing", "singing", "football"])
    user4 = Person("jim", 21, "I am a student", ["painting", "basketball"])

    graph.add_person(user1)
    graph.add_person(user2)
    graph.add_person(user3)
    graph.add_person(user4)

    graph.add_connection(user1, user3)
    graph.add_connection(user1, user4)
    graph.add_connection(user2, user3)
    graph.add_connection(user4, user2)

    user1.update_bio("I am a programmer and I love to code")
    user2.add_interest("skiing")
    query = graph.get_common_friends(user1, user2)
