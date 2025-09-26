import Cocoa

var statusCode: Int = 418
var errorString: String = "The request failed: "

switch statusCode {
case 401:
    errorString += "Unauthorized"
case 400...417:
    errorString += "Client error, \(statusCode)"
case 500...505:
    errorString += "Server error, \(statusCode)"
case let code where code < 100 || code > 600:
    errorString = "\(code) is an illegal status code."
default:
    errorString = "Unexpected error encountered."
}

let error = (code: statusCode, msg: errorString)
error.code
error.msg

let firstErrorCode = 404
let secondErrorCode = 418
let errorCodes = (firstErrorCode, secondErrorCode)

switch errorCodes {
case (404, 404):
    print("Both error codes were 404.")
case (404, _):
    print("Only the 1st code is 404, and we don't care about the 2nd code.")
case (_, 404):
    print("Only the 2nd code is 404, and we don't care about the 1st code.")
default:
    print("Neighter code is 404.")
}

let age = 26
if case 18...35 = age, age >= 25, age < 30 {
    print("Cool demographic, can rent a car and not in their thirties")
}
