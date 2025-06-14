# Ride Sharing System — GNU Smalltalk

A simple ride-sharing system implemented in **GNU Smalltalk 3.2.5**, demonstrating core Object-Oriented Programming (OOP) principles:

- **Encapsulation**
- **Inheritance**
- **Polymorphism**

## Features

- **Ride** base class with subclasses:
  - `StandardRide`
  - `PremiumRide`
- **Driver** class to manage assigned rides.
- **Rider** class to request rides.
- Polymorphic `fare` and `rideDetails` methods.
- Demonstration block creating and linking objects.

## OOP Principles Demonstrated

- **Encapsulation**:  
  Attributes like `assignedRides` and `requestedRides` are protected and accessed via specific methods.

- **Inheritance**:  
  `StandardRide` and `PremiumRide` inherit from the `Ride` base class.

- **Polymorphism**:  
  Each ride subclass overrides the `fare` method, and a shared interface (`rideDetails`) invokes subclass-specific behavior.

## Project Structure

```makefile
.
├── img
│   └── output.png
├── README.md
└── RideSharingSystem.st
```

## Running the Code

### Install GNU Smalltalk

- On macOS

  You can easily install GNU Smalltalk using Homebrew:

  ```
  brew install gnu-smalltalk
  ```

- On Other Platforms

  Check your system’s package manager or build from source:

  - Official site: https://www.gnu.org/software/smalltalk/

- Or use an online Smalltalk compiler

  No setup needed — just try it here: [JDoodle Smalltalk Online Compiler](https://www.jdoodle.com/execute-smalltalk-online)

### Run the Script

```bash
gst RideSharingSystem.st
```

## Sample Output

```text
--- Ride Sharing System Started 🚗 ---
Driver Aashish Shrestha (ID: 101, Rating: 4.9)
Assigned Rides:
Ride ID: 1, From: Downtown, To: Airport, Distance: 10.0 miles, Fare: $20.0
Ride ID: 2, From: Hotel, To: Stadium, Distance: 8.0 miles, Fare: $28.0
Rider Ashmin Shrestha (ID: 201)
Requested Rides:
Ride ID: 1, From: Downtown, To: Airport, Distance: 10.0 miles, Fare: $20.0
Ride ID: 2, From: Hotel, To: Stadium, Distance: 8.0 miles, Fare: $28.0
--- System Demo Complete ✅ ---
```
