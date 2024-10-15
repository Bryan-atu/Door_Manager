class Car:
    def__init0(self, num_doors=4):
        self.num_doors=num_doors

    def get_num_doors(self):
        return self.num_doors

    def set_num_doors(self, num_doors):
        if num_doors > 0:
            self.num_doors = num_doors
        else:
            raise ValueError("number of doors must be positive int")