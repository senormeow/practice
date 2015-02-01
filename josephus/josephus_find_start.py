#!/usr/bin/env python


class Person:

    id = None
    next = None
    status = None    
    def __init__(self,id):
        self.id = id
        self.status = "Alive"
        #print "Person with id %d created" % (self.id) 

    def kill(self):
        #print "Person %d Killed" % (self.id)
        self.status = "Dead"

    def is_alive(self):
        return self.status == 'Alive'

    def is_dead(self):
        return self.status == "Dead"

    def __str__(self):
        return "Person %d" % (self.id)


def get_last(num_people,skip):

    people = []
    for i in range(num_people):
        people.append(Person(i))

    count = 0
    index = 0
    numdead = 0
    last_person = None
    while(numdead < num_people):

        #print "evaluating person %d" % (index)

        if people[index].is_alive() and count == skip:
            people[index].kill()
            last_person = people[index]
            numdead += 1
            count = 0
            index = (index + 1) % num_people

        if people[index].is_dead():
            index = (index + 1) % num_people

        if people[index].is_alive() and count < skip:
            count = count + 1
            index = (index + 1) % num_people

    return last_person

def main():

    for i in range(1,41):
        if get_last(i,2).id == 0:
            print "Numpeople %d last_id %d" % (i,0) 


if __name__ == '__main__':
    main()


