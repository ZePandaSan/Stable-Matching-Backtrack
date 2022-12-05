import random
listWorkers=[]
listCompanies=[]
nbWorkers=4
nbCompanies=2

class Worker:
    def __init__(self, wid) -> None:
        """
            The worker ID 
        """
        self.id=wid
        self.wantedCompanies=[]
        self.company=None    

    
    def addWanted(self, company):
        self.wantedCompanies.append(company)    
    def addCompany(self, company):
        self.company=company
    
    def __str__(self) -> str:
        return f"Worker ID : {self.id}\nPreference : {self.wantedCompanies}\nComapny : {self.company}\n"


class Company:
    def __init__(self, cid) -> None:
        """
            The company ID
        """
        self.id=cid
        self.wantedWorkers=[]
        self.workers=[]
        
    def addWanted(self, worker):
        self.wantedWorkers.append(worker)

    def addWorkers(self, worker):
        self.workers.append(worker)

    def __str__(self) -> str:
        return f"Worker ID : {self.id}\nPreference : {self.wantedWorkers}\nWorkers : {self.workers}\n"
    
def createWorkers(nb):
    global listWorkers
    for i in range(1,nb+1):
        tmp=Worker("w"+str(i))
        listWorkers.append(tmp)
        tmp=None


def createCompagnies(nb):
    global listCompanies
    for i in range(1, nb+1):
        tmp = Company("c"+str(i))
        listCompanies.append(tmp)
        tmp = None

def printData():
    for worker in listWorkers:
        print(worker)
    print("\n")
    for company in listCompanies:
        print(company)


def enumerateNumbers(nb):
    enum = [i for i in range(0, nbCompanies)]
    return enum

def addPrefWorker():
    for i in range(0, nbWorkers):
        enum = [i for i in range(0, nbCompanies)]
        for j in range(0, nbCompanies):
            if len(enum) == 0:
                pass
            else:
                company = random.choice(enum)
                listWorkers[i].addWanted(listCompanies[company].id)
                enum.remove(company)


def addPrefCompany():
    for i in range(0, nbCompanies):
        enum = [i for i in range(0, nbWorkers)]
        for j in range(0, nbWorkers):
            if len(enum) == 0:
                pass
            else:
                worker = random.choice(enum)
                listCompanies[i].addWanted(listWorkers[worker].id)
                enum.remove(worker)



def main():
    global nbWorkers
    global nbCompanies
    global listCompanies
    global listWorkers
    createWorkers(nbWorkers)
    createCompagnies(nbCompanies)
    addPrefCompany()
    addPrefWorker()
    printData()


main()

