if __name__ == '__main__':
    n = int(input())#5
    arr = map(int, input().split())
    sorted_arr = sorted(set(arr)) #unique scores
    sorted_arr_in_reverse = sorted(sorted_arr, reverse=True)
    runner_up_score = sorted_arr_in_reverse[1]
    print(runner_up_score)