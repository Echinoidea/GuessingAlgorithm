import random
import math

x = int(input("Input highest possible random number: "))
answer = random.randrange(0, x) + 1

nums = []

def fill_nums():
    for i in range(x + 1):
        nums.append(i)
    print(nums)

def guess_loop():
    isRunning = True
    attempts = 0

    # !!! For some reason, after a few times, the length of nums is 0 when it shouldn't be.

    # !!! If the guess is too low, delete everything before the guess in the array. If the 
    #     guess is too high, then delete everything after the guess. Eventually, the array will be 
    #     reduced to only the answer. But, it doesn't happen for some reason.

    while isRunning == True:
        guess = nums[int(len(nums) / 2)]
        if guess < answer:
            print("{} IS TOO LOW".format(guess))
            attempts += 1
            del nums[0:nums[int(len(nums) / 2)]]
        elif guess > answer:
            print("{} IS TOO HIGH".format(guess))
            attempts += 1
            del nums[nums[int(len(nums) / 2)]:]
        else:
            print("{} IS CORRECT".format(guess))
            attempts += 1
            isRunning = False
    print("GUESSING TOOK {} ATTEMTPS".format(attempts))

def __main__():
    fill_nums()
    guess_loop()

if __name__ == "__main__":
    __main__()

print("END")
