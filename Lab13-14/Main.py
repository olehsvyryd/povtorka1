from packages.Laptop import Laptop
from packages.PersonalComputer import PersonalComputer
from packages.Netbook import Netbook
from Manager import *

if __name__ == '__main__':
    manager = Manager()

    pc1 = PersonalComputer(30.00, "producer1", "metal", 3.00, 20.00, 10.00, 15.00)
    pc2 = PersonalComputer(15.00, "producer2", "cardboard", 0.40, 10.00, 5.00, 8.00)
    netbook1 = Netbook(13.00, "producer1", "paper", 20.00, 30.00)
    netbook2 = Netbook(13.00, "producer3", "plastic", 40.00, 60.00)
    laptop1 = Laptop(20.00, "producer1", "glass", 1.00, "stopper")
    laptop2 = Laptop(10.00, "producer2", "plastic", 1.50, "plastic cap")

    manager.list_of_computers = [pc1, pc2, netbook1, netbook2, laptop1, laptop2]
    print("Initial list:")
    manager.print_list()
    manager.sort_by_weight()
    print("Sorted by weight:")
    manager.print_list()
    manager.sort_by_material()
    print("Sorted by material:")
    manager.print_list()
    manager.sort_by_type()
    print("Sorted by type:")
    manager.print_list()

    pass
