#!/usr/bin/env python


class Person:

    id = None
    next = None
    status = None    
    def __init__(self,id):
        self.id = id
        self.status = "Alive"
        print "Person with id %d created" % (self.id) 

    def set_next(self,next):
        self.next = next
        print self 

    def get_next(self):
        return self.next

    def go(self,count,num,prev):
        print "Go count %d %s prev (%s)" % (count,self,prev)
        #if next is myself I am last man
        if self.id == self.next.id:
            print "Last Man: %s" % (self)
            return

        if (count == num):
            self.status = "Dead"
            print "Dead %s" % (self)
            prev.next = self.next
            self.next.go(0,num,prev)

        else:
            self.next.go(count+1,num,self)



    def __str__(self):

        return "Person %d %s next id %d" % (self.id,self.status,self.next.id)


def main():
    
    num_people = 1063

    first = Person(0)
    prev = first
    for i in range(num_people-1):
        prev.set_next(Person(i+1))
        prev = prev.get_next()
    prev.set_next(first)

    print "Start Game"
    first.go(0,2,prev)


if __name__ == '__main__':
    main()


