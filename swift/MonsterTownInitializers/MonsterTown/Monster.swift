//
//  Monster.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

class Monster {
    static let isTerrifying = true
    var town: Town?
    var name: String
    var victimPool: Int {
        get {
            return town?.population ?? 0
        }
        set(newVictimPool) {
            town?.population = newVictimPool
        }
    }

    required init?(town: Town?, monsterName: String) {
        self.town = town
        if monsterName == "" {
            return nil
        } else {
            name = monsterName
        }
    }

    func terrorizeTown() {
        if town != nil {
            print("\(name) is terrorizing a town!")
            town?.mayor.notify()
        } else {
            print("\(name) has not found a town to terrorize yet...")
        }
    }

    class var spookyNoise: String {
        return "Grrr"
    }
}
