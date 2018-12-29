from prac_08.taxi import Taxi

def main():

    taxi1 = Taxi("Prius 1", 100, 1.23)
    taxi1.drive(40)
    print("The current fare is ${}".format(taxi1.get_fare()))
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1)
    print("The current fare is ${}".format(taxi1.get_fare()))

main()