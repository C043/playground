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
