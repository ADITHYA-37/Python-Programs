# Workout timer countdown 

workout_time = int(input())

while workout_time>=0:
    print(f"Time reaming: {workout_time} seconds")
    workout_time = workout_time -1

    if(workout_time == 0):
        print(f"Time reaming: {workout_time} seconds")
        print("Workout Completed Great job!!")
        break
        