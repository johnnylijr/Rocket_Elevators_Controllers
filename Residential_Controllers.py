import random
import time


class Elevator:
    number_of_floors = 0
    register_list = []
    elevator_current_floor = 1
    up = 1
    down = -1

    def __init__(self, number_of_floors, register_list):
        self.number_of_floors = number_of_floors
        self.register_list = register_list

    def move(self):
        pass

    def register_customer(self, customers):
        for reg in customers:
            self.register_list.append(reg)

    def cancel_customer(self, customers):
        pass


class Customer:
    user_current_floor = 1
    destination_floor = 0
    request_floor = 0  # floor where request is from
    customerID = 0
    in_elevator = False
    finished = False
    customer_direction = 0

    def __init__(self, customer_id, floors):
        self.customerID = customer_id
        self.elevator_current_floor = random.randint(1, floors)
        self.destination_floor = random.randint(1, floors)
        self.request_floor = random.randint(1, floors)  # floor where request comes from
        while self.destination_floor <= Elevator.elevator_current_floor:
            self.destination_floor = random.randint(1, floors)
        if Elevator.elevator_current_floor < self.destination_floor:
            self.customer_direction = 1
        elif self.destination_floor > Elevator.elevator_current_floor:
            self.customer_direction = -1


class Column:
    elevatorID = 0
    status = False  # Idle
    elevator_list = []

    def __init__(self, elevator_id, floors):
        self.elevatorID = elevator_id
        self.current_floor = random.randint(1, floors)



class Building:
    number_of_floors = 0
    number_of_elevators = 0
    elevator_list = []
    customer_list = []
    Elevator = 0

    def __init__(self, floors, customers):
        self.number_of_floors = floors
        for customerID in range(1, customers + 1):
            new = Customer(customerID, self.number_of_floors)
            self.customer_list.append(new)
        self.customer_list.sort(key=lambda x: x.user_current_floor)
        self.Elevator = Elevator(floors, self.customer_list)
        self.run()

    def run(self):
        print('Elevator is starting')
        print('There are %d customer(s) in the building' % (len(self.customer_list)))
        number_of_customers = len(self.customer_list)
        self.output()

    def output(self):
        for customer in self.customer_list:
            print("Customer", customer.customerID, "is on floor", customer.user_current_floor, "and wants to go to floor",
                  customer.destination_floor)
        if Elevator.elevator_current_floor < Customer.destination_floor:
            # Elevator moving up loop #
            while Elevator.elevator_current_floor < Customer.destination_floor:
                Elevator.elevator_current_floor += 1
                print(len(self.customer_list), 'Customer(s) in elevator.')
                print('Elevator moving up')
                print('+++++++++++++++++++++++++++++++++++')
                print('Floor', self.Elevator.elevator_current_floor)
                time.sleep(1)

                for customer in self.customer_list:
                    if self.Elevator.elevator_current_floor == customer.user_current_floor:
                        customer.in_elevator = True
                        print('Customer', customer.customerID, 'has entered the elevator')
                    if (self.Elevator.elevator_current_floor == customer.destination_floor) & (customer.in_elevator is True):
                        customer.in_elevator = False
                        self.customer_list.remove(customer)
                        print('Customer', customer.customerID, 'has exited the elevator')
                        break

        elif Customer.request_floor > Customer.destination_floor:
            # Elevator moving down loop #
            while Customer.request_floor > Customer.destination_floor:
                self.Elevator.elevator_current_floor += 1

                print(len(self.customer_list), 'Customer(s) in elevator.')
                print('Elevator moving down')
                print('+++++++++++++++++++++++++++++++++++')
                print('Floor', self.Elevator.elevator_current_floor)
                time.sleep(1)

                for customer in self.customer_list:
                    if customer.in_elevator is True:
                        customer.user_current_floor = self.Elevator.elevator_current_floor
                    elif (self.Elevator.elevator_current_floor == customer.destination_floor) & (customer.in_elevator is True) \
                            & (customer.customer_direction == -1):
                        self.customer_list.remove(customer)
                        print('Customer', customer.customerID, 'has exited the elevator')
        print('Elevator run is done')


def start():
    try:
        floors = int(input('Enter the number of floors: '))
        customers = int(input('Enter number of customers: '))
        elevators = int(input('Enter number of elevators: '))
        building = Building(floors, customers)
    except ValueError:
        print("You didn't enter a number. Try again.")
        start()


if __name__ == "__main__":
    start()
