//
//  Zombie.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

class Zombie: Monster {
    override class var spookyNoise: String {
        return "Brains..."
    }

    var walksWithLimp: Bool
    private(set) var isFallingApart: Bool

    required convenience init?(town: Town?, monsterName: String) {
        if monsterName == "" {
            return nil
        } else {
            self.init(limp: false, fallingApart: false, town: town, monsterName: monsterName)
        }
    }

    required init?(
        limp: Bool,
        fallingApart: Bool,
        town: Town?,
        monsterName: String
    ) {
        walksWithLimp = limp
        isFallingApart = fallingApart
        if monsterName == "" {
            return nil
        } else {
            super.init(town: town, monsterName: monsterName)
        }
    }

    convenience init?(limp: Bool, fallingApart: Bool) {
        self.init(
            limp: limp,
            fallingApart: fallingApart,
            town: nil,
            monsterName: "Fred"
        )
        if walksWithLimp {
            print("This zombie has a bad knee.")
        }
    }

    deinit {
        print("Zombie \(name) is no longer with us.")
    }

    func regenrate() {
        walksWithLimp = false
    }

    override func terrorizeTown() {
        town?.changePopulation(by: -10)
        super.terrorizeTown()
    }
}
