from tqdm import tqdm
from main import run_regular_algo, run_darwin_algo, run_lamarck_algo


d = {'A': 'Y', 'B': 'X', 'C': 'I', 'D': 'N', 'E': 'T', 'F': 'O', 'G': 'Z', 'H': 'J', 'I': 'C', 'J': 'E', 'K':
    'B', 'L': 'L', 'M': 'D', 'N': 'U', 'O': 'K', 'P': 'M', 'Q': 'S', 'R': 'V', 'S': 'P', 'T': 'Q', 'U': 'R', 'V':
    'H', 'W': 'W', 'X': 'G', 'Y': 'A', 'Z': 'F'}

if __name__ == '__main__':
    # ask from the user to enter algo type
    algo_type_lst = ["R", "D", "L"]
    file_name = "enc.txt"
    reg_lst= []
    dar_lst = []
    lam_lst = []
    for algo_type in algo_type_lst:
        for i in tqdm(range(1, 11)):
            if algo_type == "R":
                best, num_of_generations = run_regular_algo(file_name)
                if best == d:
                    reg_lst.append(num_of_generations)
            elif algo_type == "D":
                best, num_of_generations = run_darwin_algo(file_name)
                if best == d:
                    dar_lst.append(num_of_generations)
            elif algo_type == "L":
                best, num_of_generations = run_lamarck_algo(file_name)
                if best == d:
                    lam_lst.append(num_of_generations)
    print("Regular correct: " + str(len(reg_lst))+"/10")
    print("Darwin correct: " + str(len(dar_lst))+"/10")
    print("Lamarck correct: " + str(len(lam_lst))+"/10")
    print("################################")
    print("Regular average: " + str(sum(reg_lst)/len(reg_lst)))
    print("Darwin average: " + str(sum(dar_lst)/len(dar_lst)))
    print("Lamarck average: " + str(sum(lam_lst)/len(lam_lst)))
