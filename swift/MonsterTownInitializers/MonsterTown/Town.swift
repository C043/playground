//
//  Town.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

struct Town {
    static let world = "Earth"
    let region: String
    var mayor: Mayor = Mayor()
    var population: Int {
        didSet(oldPopulation) {
            if population < oldPopulation {
                print(
                    "The population has changed to \(population) from \(oldPopulation)"
                )
                mayor.apology()
            }
        }
    }
    var numberOfStoplights: Int
    init?(region: String, population: Int, stoplights: Int) {
        guard population > 0 else {
            return nil
        }
        self.region = region
        self.population = population
        self.numberOfStoplights = stoplights
    }
    
    init?(population: Int, stoplights: Int) {
        self.init(
            region: "N/A",
            population: population,
            stoplights: stoplights
        )
    }

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
