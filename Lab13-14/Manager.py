class Manager:
    list_of_computers = []

    def __init__(self):
        pass

    def sort_by_weight(self):
        self.list_of_computers.sort(key=lambda list_of_computers: list_of_computers.volume)

    def sort_by_material(self):
        self.list_of_computers.sort(key=lambda list_of_computers: list_of_computers.material)

    def sort_by_type(self):
        self.list_of_computers.sort(key=lambda list_of_computers: list_of_computers.package_type.value)

    def add_toy(self, computer):
        self.list_of_computers += computer

    def print_list(self):
        for computer in self.list_of_computers:
            print(computer)
        print("\n")

