def get_name():
    name = input("please enter your name:  ")
    return name 

def get_mail():
    mail = input("please enter your email:  ")
    return mail 

def get_ticket():
    #tickets = ["regular", 'vip', 'vvip', 'premium']
    ticket_type = input("enter the type of ticket you want, \n Availale options include: regular, vip, vvip, premium:\n")
    return ticket_type

def finalize(name, email, ticket_type):
    print(f"""
        You have successfully registered for the Nutec Festival Event
        Name: {name} 
        e-mail: {email}
        ticket: {ticket_type}
    """)

NO_OF_TICKETS = 200
available_tickets = 200

for i in range(NO_OF_TICKETS):
    print('Welcome to the Nutec Booking system')
    name = get_name()
    mail = get_mail()
    ticket = get_ticket()
    finalize(name, mail, ticket)
    available_tickets -= 1
    print(f"{available_tickets} tickets remaining")