from prac_08.silver_service_taxi import SilverServiceTaxi

def main():

    silverTaxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    silverTaxi.drive(18)
    print("The current fare is ${}".format(silverTaxi.get_fare()))
    silverTaxi.start_fare()
    silverTaxi.drive(100)
    print(silverTaxi)
    print("The current fare is ${}".format(silverTaxi.get_fare()))

main()