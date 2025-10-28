//
//  Vampire.swift
//  MonsterTown
//
//  Created by Mario Fragnito on 28/10/25.
//

class Vampire: Monster {
    var thralls: [Vampire] = []
    
    override func terrorizeTown() {
        if town?.population ?? 0 > 0 {
            town?.population -= 1
            thralls.append(Vampire())
        }
    }
}
