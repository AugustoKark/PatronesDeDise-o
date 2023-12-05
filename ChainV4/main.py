from Handler import Handler
from Fireman import Fireman
from Police import Police
from Medic import Medic


def main():
    
        fireman = Fireman()
        police = Police()
        medic = Medic()
    
        fireman.set_next(police).set_next(medic)
    
        print("Chain: Fireman > Police > Medic")
        print(fireman.handle("Fireman"))
        print(fireman.handle("Police"))
        print(fireman.handle("Medic"))
        print(fireman.handle("None"))

        print("Subchain: Police > Medic")
        print(police.handle("Police"))
        print(police.handle("Medic"))
        print(police.handle("None"))

if __name__ == "__main__":  
    main()