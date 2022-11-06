import random
from solution import Solution



class Solver:
    bagType_price = [0, 1.7, 1.75, 6, 25, 200]
    bagType_co2_production = [0, 3.0, 4.2, 1.8, 3.6, 12.0]
    bagType_co2_transport = [0, 30, 24, 36, 42, 60]

    def __init__(self, game_info):
        self.days = None
        self.population = game_info["population"]
        self.companyBudget = game_info["companyBudget"]
        self.behavior = game_info["behavior"]


    def Solve(self, bagtype, days, recycle, mode, refund):
        self.days = days  
        refund = self.bagType_price[bagtype]/10*refund
        print(refund)
        solution = Solution(bool(recycle), self.bagType_price[bagtype], refund, bagtype)
        for day in range(0, days):
            number = random.randint(0,4)
            if number == 0:
                solution.addOrder(self.splitMoney(bagtype))
            elif number == 1:
                solution.addOrder(self.holdMoney(bagtype))
            elif number == 2:
                solution.addOrder(self.cranked())
            else : 
                solution.addOrder(self.wasteMoney(bagtype))
        return solution

    def rand_test(self):
            return int(random.random()*self.companyBudget)

    def cranked(self):
        return int(self.companyBudget/self.days)
        
    # Solution 1: "Spend all money day 1"
    def wasteMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype])

    # Solution 2: "Spend equally money every day"
    def splitMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype] / self.days)

    # Solution 3: "Everyone get one bag every day"
    def holdMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype] / self.population / self.days)
