from Tdomain import Train,Ticket_menu

class MemoryRepo:
    def __init__(self):
        self._data=[]

    def get_data(self):
        return list(self._data)

    def add_route(self,train_route):
        self._data.append(train_route)


class TextFileRepo(MemoryRepo):
    def __init__(self,filename):
        super().__init__()
        self._filename=filename
        self.load()


    def get_data(self):
        return list(self._data)

    def add_route(self,train_route):
        super().add_route(train_route)
        self.save()

    def load(self):
        try:
            with open(self._filename,'r') as file:
                for line in file:
                    _number,_d_city,_d_time,_a_city,_a_time,_tickets=line.strip().split(',')
                    self._data.append(Train(int(_number),_d_city,_d_time,_a_city,_a_time,int(_tickets)))

        except FileNotFoundError:
            self._data=[]

    def save(self):
        with open(self._filename,'w') as file:
            for t in self._data:
                file.write(f"{t.get_number()},{t.get_d_city()},{t.get_d_time()},{t.get_a_city()},{t.get_a_time()},{t.get_tickets()}\n")


class TicketMemoryRepo:
    def __init__(self):
        self._Tdata=[]

    def get_data(self):
        return list(self._Tdata)

    def buy_ticket(self,ticket_stats):
        self._Tdata.append(ticket_stats)


class TicketTextFileRepo(TicketMemoryRepo):
    def __init__(self,filename):
        super().__init__()
        self._filename=filename
        self.load

    def get_data(self):
        return list(self._Tdata)

    def buy_ticket(self,ticket_stats):
        super().buy_ticket(ticket_stats)
        self.save()

    def load(self):
        try:
            with open(self._filename,'r') as file:
                for line in file:
                    _train_number,_ticket_price,_tickets_sold=line.strip().split(',')
                    self._Tdata.append(Ticket_menu(int(_train_number),_ticket_price,int(_tickets_sold)))
        except:
            self._Tdata=[]

    def save(self):
        with open(self._filename,'w') as file:
            for t in self._Tdata:
                file.write(f"{t.get_train_number()},{t.get_ticket_price()},{t.get_tickets_sold()}\n")
