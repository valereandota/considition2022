from solver import Solver
import api

api_key = "c5e9d57d-cd56-4a65-4817-08da97ce1ad5"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
map_name = "Fancyville"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
 

def main():
	for i in range(5):
		print(i)
		print("Starting game...")
		response = api.mapInfo(api_key, map_name)
		bag_type = i
		days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365
		solver = Solver(game_info=response)
		solution = solver.Solve(bag_type, days)
		submit_game_response = api.submit_game(api_key, map_name, solution)
		print(f'Result for map {map_name} with bag type {bag_type}')
		if i !=0 :
			print(submit_game_response.get('dailys')[-1])
			print('Score = '+str(submit_game_response.get('dailys')[-1].get('customerScore') - submit_game_response.get('dailys')[-1].get('c02')))
		else:
			print(submit_game_response)

if __name__ == "__main__":
	main()