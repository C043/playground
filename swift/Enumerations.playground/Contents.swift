import Cocoa

enum TextAlignment: Int {
    case left = 20
    case right = 50
    case center = 40
    case justify = 70
}

TextAlignment.left.rawValue
TextAlignment.right.rawValue
TextAlignment.justify.rawValue

var alignment = TextAlignment.left
alignment = .justify

switch alignment {
case .left:
    print("Left")
case .right:
    print("Right")
case .center:
    print("Center")
case .justify:
    print("Justify")
}

// Methods
enum LightBulb {
    case on
    case off

    func surfaceTemperature(forAmbientTemperature ambient: Double) -> Double {
        switch self {
        case .on:
            return ambient + 150.0
        case .off:
            return ambient
        }
    }

    mutating func toggle() {
        switch self {
        case .on:
            self = .off
        case .off:
            self = .on
        }
    }
}

var bulb = LightBulb.on
let ambientTemperature = 77.0
var bulbTemerature = bulb.surfaceTemperature(
    forAmbientTemperature: ambientTemperature
)

bulb.toggle()
bulbTemerature = bulb.surfaceTemperature(
    forAmbientTemperature: ambientTemperature
)

// Associated Values
enum ShapeDimensions {
    // point has no associated value - it is dimensionless
    case point

    // Square's associated value is the length of on side
    case square(side: Double)

    // rectangle's associated value defines its width and height
    case rectangle(width: Double, height: Double)

    case rightTriangle(base: Double, heigth: Double, cateto: Double)

    func area() -> Double {
        switch self {
        case .point:
            return 0
        case .square(let side):
            return side * side

        case .rectangle(width: let w, height: let h):
            return w * h
        case .rightTriangle(base: let b, heigth: let h, cateto: let c):
            return b * h / 2
        }
    }

    func perimeter() -> Double {
        switch self {
        case .point:
            return 0
        case .square(let side):
            return side * 4
        case .rectangle(width: let w, height: let h):
            return w * 2 + h * 2
        case .rightTriangle(base: let b, heigth: let h, cateto: let c):
            return b + h + c
        }
    }
}

var squareShape = ShapeDimensions.square(side: 10.0)
var rectShape = ShapeDimensions.rectangle(width: 5.0, height: 10.0)

let squareArea = squareShape.area()
let rectArea = rectShape.area()

let rectPerimeter = rectShape.perimeter()
