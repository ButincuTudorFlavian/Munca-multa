from Tdomain import Train,Ticket_menu
import random
from datetime import time

class Exception(Exception):
    pass

class Service:
    def __init__(self,repo,ticket_repo):
        self._repo=repo
        self._ticket_repo=ticket_repo

    def find_route(self,number_test):
        test_list=self._repo.get_data()
        for r in test_list:
            if r.get_number()==number_test:
                return r
        raise Exception('No route found')

    def add_route(self,d_city,d_time,a_city,a_time,tickets):
        if tickets<0:
            raise Exception('tickets cannot be negative')

        while True:
            number=random.randint(1000,10000)
            try:
                self.find_route(number)
            except:
                break

        new_route=Train(number,d_city,d_time,a_city,a_time,tickets)
        self._repo.add_route(new_route)

    def display_all_routes(self):
        return self._repo.get_data()


#SWITCH

    def display_all_tickets(self):
        return self._ticket_repo.get_data()

    #Train id
    #ticket price
    #tickets sold
    #money made
    def add_purchase(self,A,B,train_number,tickets_sold):

        _train_number=train_number
        _ticket_price=self.buy_tickets(A,B)
        #tickets_sold+=1
        purchase=Ticket_menu(_train_number,_ticket_price,tickets_sold)
        self._ticket_repo.buy_ticket(purchase)

    def buy_tickets(self,A,B):
        hourly_rate=15
        time_clock,time_in_min=self.route_travel_time(A,B)
        ticket_price=hourly_rate*time_in_min

        return ticket_price

    def route_travel_time(self,hour_a,hour_b):
        a_h,a_m=hour_a.split(":")
        b_h,b_m=hour_b.split(":")

        t_h=0
        t_m=0
        a_h=int(a_h)
        a_m=int(a_m)
        b_h=int(b_h)
        b_m=int(b_m)
        if a_h>b_h:
            t_h=a_h-b_h
            if a_m>b_m:
                t_m=a_m-b_m
            else:
                t_m=b_m-a_h
        elif a_h<b_h:
            t_h=b_h-a_h
            if a_m>b_m:
                t_m=a_m-b_m
            else:
                t_m=b_m-a_h

        t_h=str(t_h)
        t_m=str(t_m)

        time=[]
        time.append(t_h)
        time.append(":")
        time.append(t_m)

        t_h=int(t_h)
        t_m=int(t_m)

        time_min=t_h*60+t_m
        time_min=time_min/60

        return "".join(time),time_min