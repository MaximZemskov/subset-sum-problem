from population import Population

MAX_GENERATIONS = 100

DEBUG = False

if __name__ == '__main__':
    array = [110002, 217804, 327806, 547810, 657812, 767814,
             1097820, 1317824, 1427826, 2197840, 3297310, 4177326,
             4617334, 5497350, 5937028, 6597040, 7257052, 7587058,
             8796860, 9236868, 9786768, 10446890, 10446890, 10446340,
             21996220, 27496320, 54996600, 1400115, 2750500, 4150090,
             5200030, 1640000, 3260000, 6516000, 11927300, 23854620,
             100800000, 201600024, 300600360, 398400048, 497881800,
             48000000, 96000000, 144000000, 4800000, 9600000, 38400000,
             47500000, 52250000, 56050000, 57006000, 57340000, 58280000,
             59220000, 60160000, 61100000, 62042640, 62980000, 63920000,
             64860000, 65800000, 66740000, 67680000, 68620000, 69560000,
             70500000, 75200000, 76140000, 77080000, 78020000, 78960000,
             79900000, 80840000, 81780000, 82720000, 83660000, 84600000,
             85540000, 86480000, 87420000, 88360000, 94000000, 98660310,
             103358420, 108056530, 112754160, 117452250, 122150340, 126848430,
             131546520, 136244610, 140942700, 184360400, 367927200]

    desired_number = 771984144

    population = Population(array, desired_number, 300)
    population.initialization()

    alpha_fitness = population.alpha.fitness
    answer = population.alpha.decoded_individual
    stagnation_generation_count = 0

    for generation_idx in range(MAX_GENERATIONS):
        print(f'GENERATION #{generation_idx}')
        if stagnation_generation_count == 30:
            print(f'SOLUTION NOT FOUND. Best solution:\n'
                  f'{sum(answer)}')
            break
        try:
            is_stop = population.selection()
        except Exception:
            population.start_armageddon()
            is_stop = population.selection()
        if alpha_fitness < population.alpha.fitness:
            if DEBUG:
                print(f'a: {alpha_fitness}\n'
                      f'p: {population.alpha.fitness}')
            alpha_fitness = population.alpha.fitness
            answer = population.alpha.decoded_individual
            stagnation_generation_count = 0
        else:
            stagnation_generation_count += 1
        if is_stop:
            print(f'SOLUTION FOUND.\n'
                  f'{sum(answer)}\n'
                  f'{answer}')
            break
        if DEBUG:
            print(f'alpha: {answer}\n'
                  f'fitness: {alpha_fitness}\n'
                  f'{desired_number - sum(answer)}')





