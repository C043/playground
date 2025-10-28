//
//  Town.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

struct Town {
    static let world = "Earth"
    let region = "Middle"
    var mayor: Mayor = Mayor()
    var population = 5_422 {
        didSet(oldPopulation) {
            if population < oldPopulation {
                print(
                    "The population has changed to \(population) from \(oldPopulation)"
                )
                mayor.apology()
            }
        }
    }
    var numberOfStoplights = 4

    enum Size {
        case small
        case medium
        case large
    }

    var townSize: Size {
        switch population {
        case 0...10_000:
            return Size.small
        case 10_001...100_000:
            return Size.medium
        default:
            return Size.large
        }
    }

    func printDescription() {
        print(
            "Population: \(population); number of stoplights: \(numberOfStoplights)"
        )
    }

    mutating func changePopulation(by amount: Int) {
        population += amount
    }
}
