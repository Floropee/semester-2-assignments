from abc import ABC, abstractmethod
class Package(ABC):
    def __init__(self,subscriber):
        self.subscriber=subscriber
    @abstractmethod
    def amount(self):
        pass
class Small(Package):
    def amount(self):
        return 10000
class Medium(Package):
    def amount(self):
        return 30000
class Large(Package):
    def amount(self):
        return 70000
class TopupService:
    def __init__(self):
        self.topups=[]
    def add(self,package: Package):
        self.topups.append(package)
    def run(self,receipt, confirmation):
        receipt.write(self.topups)
        confirmation.confirm(self.topups)
class Receipt(ABC):
    @abstractmethod
    def write(self,topups):
        pass
class TextReceipt(Receipt):
    def write(self,topups):
        for package in topups:
            print(f'RECEIPT: {package.subscriber} +{package.amount()}')
class Confirmation(ABC):
    @abstractmethod
    def confirm(self,topups):
        pass
class SmsConfirmation(Confirmation):
    def confirm(self,topups):
        for package in topups:
            print(f'[SMS → {package.subscriber}] Top-up of {package.amount()} so`m successful')


carrier = TopupService()
carrier.add(Small("Peter"))
carrier.add(Medium("Natasha"))
carrier.add(Large("Bruce"))

carrier.run(TextReceipt(), SmsConfirmation())