//
//  Zombie.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 15/10/25.
//

import Foundation

class Zombie: Monster {
    var walskWithLimp = true
    
    func regenrate() {
        walskWithLimp = false
    }
    
    override func terrorizeTown() {
        town?.changePopulation(by: -10)
        super.terrorizeTown()
    }
}
