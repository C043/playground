//
//  Mayor.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 28/10/25.
//

struct Mayor {
    private var anxietyLevel = 0
    func apology() {
        print(
            "I'm deeply saddened to hear about this latest tragedy. I promise that my office is looking into the nature of this rash of violence."
        )
    }

    mutating func notify() {
        anxietyLevel += 5
    }
}
