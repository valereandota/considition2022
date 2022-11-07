from solver import Solver
import api
import json


api_key = "c5e9d57d-cd56-4a65-4817-08da97ce1ad5"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
map_name = "Fancyville"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
 


def main():
	highscore = 0
	runs = 10
	recycle = [0,1]
	bags = [1,2,3,4,5]
	print("Starting game...")
	response = api.mapInfo(api_key, map_name)
	highscore, best_sol = run_logic(response, highscore, runs+1, bags, recycle, 1)
	print(f'Highscore: {highscore}')
	print(best_sol.bagPrice, best_sol.bagType, best_sol.recycleRefundChoice, best_sol.refundAmount, best_sol.orders)
	highscore, best_sol = run_logic(response, highscore, 1000, [best_sol.bagType], [best_sol.recycleRefundChoice], 2)
	print(highscore)
	store_data(highscore, best_sol.toJSON())

def run_logic(response, highscore, runs, bags, recycle, mode):
	for bag in bags:
		for ref in range(1,11): 
			for rec in recycle:
					for iteration in range(1,runs):
						try:
							bag_type = bag
							days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365
							solver = Solver(game_info=response)
							solution = solver.Solve(bag_type, days, rec, mode, ref)
							submit_game_response = api.submit_game(api_key, map_name, solution)
							print(f'Result for map {map_name} with bag type {bag_type}')
							print(submit_game_response.get('dailys')[-1])
							score = submit_game_response.get('dailys')[-1].get('positiveCustomerScore') - submit_game_response.get('dailys')[-1].get('c02')
							if score > highscore:
								highscore = score
								best_sol = solution
							print('Score = '+str(score))
						except Exception:
							pass
	print(highscore)
	return highscore, best_sol

def store_data(params, sol):
	with open ("params.txt", "a") as f:
		f.write(json.dumps(params))
		f.write(json.dumps(sol))
		f.write("\n")

if __name__ == "__main__":
	main()