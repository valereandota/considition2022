import random
from solution import Solution



class Solver:
    bagType_price = [0, 1.7, 1.75, 6, 25, 200]
    bagType_co2_production = [0, 5, 7, 3, 6, 20]
    bagType_co2_transport = [0, 50, 40, 60, 70, 100]

    def __init__(self, game_info):
        self.days = None
        self.population = game_info["population"]
        self.companyBudget = game_info["companyBudget"]
        self.behavior = game_info["behavior"]


    def Solve(self, bagtype, days, recycle):
        self.days = days
        refund = 1
        solution = Solution(bool(recycle), self.bagType_price[bagtype], refund, bagtype)
        for day in range(0, days):
            # if day%7 == 0:
            #     solution.addOrder(self.wasteMoney(bagtype))
            # else :
            #     solution.addOrder(self.holdMoney(bagtype))
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
