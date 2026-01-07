import Cocoa

protocol Excercise {
    var caloriesBurned: Double { get set }
    var minutes: Double { get set }
}

struct EllipticalWorkout: Excercise {
    var caloriesBurned: Double
    var minutes: Double
}

let ellipticalWorkout = EllipticalWorkout(caloriesBurned: 335, minutes: 30)

struct RunningWorkout: Excercise {
    var caloriesBurned: Double
    var minutes: Double
    var meters: Double
}

let runningWorkout = RunningWorkout(caloriesBurned: 350, minutes: 25, meters: 5000)

func caloriesBurnedPerMinute<E: Excercise>(for excercise: E) -> Double {
    return excercise.caloriesBurned / excercise.minutes
}

print(caloriesBurnedPerMinute(for: ellipticalWorkout))
print(caloriesBurnedPerMinute(for: runningWorkout))
