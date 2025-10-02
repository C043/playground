import Cocoa

var errorCodeString: Optional<String>
errorCodeString = Optional("404")

var errorCodeStringAlternative: String?
errorCodeStringAlternative = "404"

if errorCodeString != nil {
    let theError = errorCodeString!
    print(theError)
}

// Optional Binding
if let temporaryConstant = errorCodeStringAlternative {
    print(temporaryConstant)
} else {
    print("\(errorCodeStringAlternative) is nil")
}

if let theError = errorCodeStringAlternative, let errorCodeInt = Int(theError), errorCodeInt == 404 {
        print("\(theError): \(errorCodeInt)")
}

// Implicitly Unwrapped Optionals
var errorCodeStringImplicit: String!
let yetAnotherErrorCodeString = errorCodeStringImplicit
// let anotherErrorCodeString: String = errorCodeStringImplicit
// errorCodeStringImplicit = "404"
print(errorCodeStringImplicit)

// Optional Chaining
var errorDescription: String?
if let theError = errorCodeStringAlternative, let errorCodeInt = Int(theError), errorCodeInt == 404 {
    errorDescription = "\(errorCodeInt + 200): resource not found."
}

var upCaseErrorDescription = errorDescription?.uppercased()
upCaseErrorDescription?.append(" PLEASE TRY AGAIN.")
upCaseErrorDescription

// The Nil Coalescing Operator
let description = errorDescription ?? "No error."

// Silver challenge
// let testOptionalToForceUnwrap: String?
// let unwrapping = testOptionalToForceUnwrap!
