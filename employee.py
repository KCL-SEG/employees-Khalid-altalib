"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum

class ContractType(Enum):
    MONTHLY = 1
    CONTRACT = 2
    NONE = 3
class CommissionType(Enum):
    BONUS = 1
    CONTRACT = 2
    NONE = 3

class Employee:

    def __init__(self, name, contractType, contractPay, commission_type, commission_pay, numOfHours=0, numOfContracts=0):
        self.name = name
        self.contractType = contractType
        self.contractPay = contractPay
        self.comissionType = commission_type
        self.commissionPay = commission_pay
        self.numOfHours = numOfHours
        self.numOfContracts = numOfContracts
        self.totalPay = self.calculatePay()

    def get_pay(self):
        return self.totalPay

    def calculatePay(self):

        if self.contractType == ContractType.MONTHLY:
            if self.comissionType == CommissionType.BONUS:
                return self.contractPay + self.commissionPay
            elif self.comissionType == CommissionType.CONTRACT:
                return self.contractPay + (self.commissionPay * self.numOfContracts)
            else:
                return self.contractPay
        elif self.contractType == ContractType.CONTRACT:
            if self.comissionType == CommissionType.BONUS:
                return (self.contractPay * self.numOfHours) + self.commissionPay
            elif self.comissionType == CommissionType.CONTRACT:
                return (self.contractPay * self.numOfHours) + (self.commissionPay * self.numOfContracts)
            else:
                return self.contractPay * self.numOfHours
        else:
            return 0

    def __str__(self):
        if self.contractType == ContractType.MONTHLY:
            if self.comissionType == CommissionType.BONUS:
                return f"{self.name} works on a monthly salary of {self.contractPay} and receives a bonus commission of {self.commissionPay}. Their total pay is {self.totalPay}."
            elif self.comissionType == CommissionType.CONTRACT:
                return f"{self.name} works on a monthly salary of {self.contractPay} and receives a commission for {self.numOfContracts} contract(s) at {self.commissionPay}/contract. Their total pay is {self.totalPay}."
            else:
                return f"{self.name} works on a monthly salary of {self.contractPay}. Their total pay is {self.totalPay}."
        elif self.contractType == ContractType.CONTRACT:
            if self.comissionType == CommissionType.BONUS:
                return f"{self.name} works on a contract of {self.numOfHours} hours at {self.contractPay}/hour and receives a bonus commission of {self.commissionPay}. Their total pay is {self.totalPay}."
            elif self.comissionType == CommissionType.CONTRACT:
                return f"{self.name} works on a contract of {self.numOfHours} hours at {self.contractPay}/hour and receives a commission for {self.numOfContracts} contract(s) at {self.commissionPay}/contract. Their total pay is {self.totalPay}."
            else:
                return f"{self.name} works on a contract of {self.numOfHours} hours at {self.contractPay}/hour. Their total pay is {self.totalPay}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ContractType.MONTHLY, 4000, CommissionType.NONE, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ContractType.CONTRACT, 25, CommissionType.NONE, 0, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', ContractType.MONTHLY, 3000, CommissionType.CONTRACT, 200, 0, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ContractType.CONTRACT, 25, CommissionType.CONTRACT, 220, 150, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', ContractType.MONTHLY, 2000, CommissionType.BONUS, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ContractType.CONTRACT, 30, CommissionType.BONUS, 600, 120)
