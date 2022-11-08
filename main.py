from solver import Solver
import api
import json


api_key = "c5e9d57d-cd56-4a65-4817-08da97ce1ad5"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
map_name = "Fancyville"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
 


def main():
	runs = 100
	recycle = [0,1]
	bags = [1,2,3,4,5]
	print("Starting game...")
	response = api.mapInfo(api_key, map_name)
	run_logic(response, runs+1, bags, recycle, 1)


def run_logic(response, runs, bags, recycle, mode):
	for bag in bags:
		for price in range(1,11):
			for ref in range(1,11): 
				for rec in recycle:
						for iteration in range(1,runs):
							try:
								bag_type = bag
								days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365
								solver = Solver(game_info=response)
								solution = solver.Solve(bag_type, days, rec, mode, ref, price)
								api.submit_game(api_key, map_name, solution)
							except Exception:
								pass
			print("Running...")
		print(f"Bag {bag} finished")
	print("Done")


def store_data(params, sol):
	with open ("params.txt", "a") as f:
		f.write(json.dumps(params))
		f.write(json.dumps(sol))
		f.write("\n")

if __name__ == "__main__":
	main()