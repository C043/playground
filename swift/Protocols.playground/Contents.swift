import Cocoa

protocol TabularDataSource {
    var numberOfRows: Int { get }
    var numberOfColumns: Int { get }

    func label(forColumn column: Int) -> String
    func itemFor(row: Int, collumn: Int) -> String
}

func printTable(_ dataSource: TabularDataSource & CustomStringConvertible) {
    print("Table: \(dataSource)")
    
    var headerRow = "|"
    var columnWidths = [Int]()

    for i in 0 ..< dataSource.numberOfColumns {
        let columnLabel = dataSource.label(forColumn: i)
        columnWidths.append(columnLabel.count)
    }
    
    for i in 0 ..< dataSource.numberOfRows {
        for j in 0 ..< dataSource.numberOfColumns {
            let item = dataSource.itemFor(row: i, collumn: j)
            columnWidths[j] = max(columnWidths[j], item.count)
        }
    }
    
    for i in 0 ..< dataSource.numberOfColumns {
        let columnLabel = dataSource.label(forColumn: i)
        var paddingNeeded = columnWidths[i] - columnLabel.count
        if paddingNeeded < 0 {
            paddingNeeded = 0
        }
        let padding = repeatElement(" ", count: paddingNeeded).joined(
            separator: ""
        )
        headerRow += " \(padding)\(columnLabel) |"
    }

    print(headerRow)

    for i in 0 ..< dataSource.numberOfRows {
        var out = "|"
        for j in 0 ..< dataSource.numberOfColumns {
            let item = dataSource.itemFor(row: i, collumn: j)
            var paddingNeeded = columnWidths[j] - item.count
            if paddingNeeded < 0 {
                paddingNeeded = 0
            }
            let padding = repeatElement(" ", count: paddingNeeded).joined(
                separator: ""
            )
            out += " \(padding)\(item) |"
        }

        print(out)
    }
}

struct Person {
    let name: String
    let age: Int
    let yearsOfExperience: Int
}

struct Department: TabularDataSource, CustomStringConvertible{
    let name: String
    var people = [Person]()
    
    var description: String {
        return "Department (\(name))"
    }

    init(name: String) {
        self.name = name
    }

    mutating func add(_ person: Person) {
        people.append(person)
    }
    
    var numberOfRows: Int {
        return people.count
    }
    
    var numberOfColumns: Int {
        return 3
    }
    
    func label(forColumn column: Int) -> String {
        switch column {
        case 0: return "Employee Name"
        case 1: return "Age"
        case 2: return "Years of Experience"
        default: fatalError("Invalid column!")
        }
    }
    
    func itemFor(row: Int, collumn: Int) -> String {
        let person = people[row]
        switch collumn{
        case 0: return person.name
        case 1: return String(person.age)
        case 2: return String(person.yearsOfExperience)
        default: fatalError("Invalid column!")
        }
    }
}

var department = Department(name: "Engineering")
department.add(Person(name: "Eva", age: 30, yearsOfExperience: 6))
department.add(Person(name: "Saleh", age: 40, yearsOfExperience: 18))
department.add(Person(name: "Amit", age: 50, yearsOfExperience: 20))

printTable(department)

struct Book {
    let title: String
    let author: String
    let avgReview: Int
}

struct BookCollection: TabularDataSource, CustomStringConvertible {
    var bookList = [Book]()
    
    var description: String {
        return "Book Collection"
    }
    
    mutating func add(_ book: Book){
        self.bookList.append(book)
    }
    
    var numberOfRows: Int {
        return bookList.count
    }
    
    var numberOfColumns: Int {
        return 3
    }
    
    func label(forColumn column: Int) -> String {
        switch column {
        case 0: return "Book Title"
        case 1: return "Author"
        case 2: return "Average Review"
        default: fatalError("Invalid column!")
        }
    }
    
    func itemFor(row: Int, collumn: Int) -> String {
        let book = bookList[row]
        switch collumn{
        case 0: return book.title
        case 1: return book.author
        case 2: return String(book.avgReview)
        default: fatalError("Invalid column!")
        }
    }

}

var bookCollection = BookCollection()

bookCollection.add(Book(title: "Tender is the Flesh", author: "Agustina Bazterrica", avgReview: 5))
bookCollection.add(Book(title: "Dungeon Crawler Carl", author: "Matt Dinniman", avgReview: 4))
bookCollection.add(Book(title: "Swift Programming", author: "John Gallagher", avgReview: 5))

printTable(bookCollection)
