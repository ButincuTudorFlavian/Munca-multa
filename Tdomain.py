# 17:00

class Train:
    def __init__(self,number,d_city,d_time,a_city,a_time,tickets):
        self._number=number
        self._d_city=d_city
        self._d_time=d_time
        self._a_city=a_city
        self._a_time=a_time
        self._tickets=tickets

    def get_number(self):
        return self._number

    def get_d_city(self):
        return self._d_city

    def get_d_time(self):
        return self._d_time

    def get_a_city(self):
        return self._a_city

    def get_a_time(self):
        return self._a_time

    def get_tickets(self):
        return self._tickets

    def __str__(self):
        return f"Train no.: {self.get_number()}, going from: {self.get_d_city()} at: {self.get_d_time()}, going to: {self.get_a_city()}, arriving at: {self.get_a_time()}, remaing tickets: {self.get_tickets()} "

class Ticket_menu:
    def __init__(self,train_number,ticket_price,tickets_sold):
        self._train_number=train_number
        self._ticket_price=ticket_price
        self._tickets_sold=tickets_sold


    def get_train_number(self):
        return self._train_number

    def get_ticket_price(self):
        return self._ticket_price

    def get_tickets_sold(self):
        return self._tickets_sold



    def __str__(self):
        return f"Train no:{self.get_train_number()}, price:{self.get_ticket_price()}, sold: {self.get_tickets_sold()}\n"
