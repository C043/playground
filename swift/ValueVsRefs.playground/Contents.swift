import Cocoa

var str = "Hello, playground"
var playgroundGreeting = str
playgroundGreeting += "! How are you today?"
str

class Employee {
    var id: Int = 0
}
let anika = Employee()
let theBoss = anika

anika.id = 16
anika.id
theBoss.id

struct Company {
    var boss: Employee
}
let acme = Company(boss: anika)
let mel = Employee()
mel.id = 86
mel.id

acme.boss.id
let widgetCo = acme
anika.id=15
widgetCo.boss.id

let juampa = Employee()

let employees = [anika, mel, juampa]
let partyGoers = employees
employees.last?.id = 4
employees
partyGoers
