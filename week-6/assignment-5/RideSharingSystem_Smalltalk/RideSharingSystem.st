"===========================
 Base Class: Ride
==========================="
Object subclass: Ride [
    | rideID pickupLocation dropoffLocation distance |

    Ride >> initialize [
        distance := 0.0.
    ]

    "Setters"
    Ride >> rideID: anID [ rideID := anID. ]
    Ride >> pickupLocation: aPickup [ pickupLocation := aPickup. ]
    Ride >> dropoffLocation: aDropoff [ dropoffLocation := aDropoff. ]
    Ride >> distance: aDistance [ distance := aDistance asFloat. ]

    "Getters"
    Ride >> rideID [ ^ rideID. ]
    Ride >> pickupLocation [ ^ pickupLocation. ]
    Ride >> dropoffLocation [ ^ dropoffLocation. ]
    Ride >> distance [ ^ distance. ]

    "Abstract polymorphic method for subclasses"
    Ride >> fare [
        self subclassResponsibility.
    ]

    "Display ride details"
    Ride >> rideDetails [
        Transcript
            show: 'Ride ID: ', rideID printString, 
                  ', From: ', pickupLocation, 
                  ', To: ', dropoffLocation, 
                  ', Distance: ', distance printString, ' miles, Fare: $', (self fare printString); cr.
    ]
].

"===========================
 Derived Class: StandardRide
==========================="
Ride subclass: StandardRide [
    "Fare calculation for StandardRide"
    StandardRide >> fare [
        ^ self distance * 2.0.
    ]
].

"===========================
 Derived Class: PremiumRide
==========================="
Ride subclass: PremiumRide [
    "Fare calculation for PremiumRide"
    PremiumRide >> fare [
        ^ self distance * 3.5.
    ]
].

"===========================
 Class: Driver
==========================="
Object subclass: Driver [
    | driverID name rating assignedRides |

    Driver >> initialize [
        assignedRides := OrderedCollection new.
    ]

    Driver >> initializeWithID: anID name: aName rating: aRating [
        self initialize.
        driverID := anID.
        name := aName.
        rating := aRating asFloat.
    ]

    Driver >> addRide: aRide [
        assignedRides add: aRide.
    ]

    Driver >> getDriverInfo [
        Transcript
            show: 'Driver ', name, ' (ID: ', driverID printString, ', Rating: ', rating printString, ')'; cr.
        Transcript show: 'Assigned Rides:'; cr.
        assignedRides do: [ :ride | ride rideDetails ].
    ]
].

"===========================
 Class: Rider
==========================="
Object subclass: Rider [
    | riderID name requestedRides |

    Rider >> initialize [
        requestedRides := OrderedCollection new.
    ]

    Rider >> initializeWithID: anID name: aName [
        self initialize.
        riderID := anID.
        name := aName.
    ]

    Rider >> requestRide: aRide [
        requestedRides add: aRide.
    ]

    Rider >> viewRides [
        Transcript
            show: 'Rider ', name, ' (ID: ', riderID printString, ')'; cr.
        Transcript show: 'Requested Rides:'; cr.
        requestedRides do: [ :ride | ride rideDetails ].
    ]
].

"===========================
 System Demonstration Block
==========================="
| sRide pRide driver rider |

Transcript show: '--- Ride Sharing System Started 🚗 ---'; cr.

"Create a StandardRide"
sRide := StandardRide new.
sRide initialize.
sRide rideID: 1.
sRide pickupLocation: 'Downtown'.
sRide dropoffLocation: 'Airport'.
sRide distance: 10.

"Create a PremiumRide"
pRide := PremiumRide new.
pRide initialize.
pRide rideID: 2.
pRide pickupLocation: 'Hotel'.
pRide dropoffLocation: 'Stadium'.
pRide distance: 8.

"Create a Driver and assign rides"
driver := Driver new.
driver initializeWithID: 101 name: 'Aashish Shrestha' rating: 4.9.
driver addRide: sRide.
driver addRide: pRide.
driver getDriverInfo.

"Create a Rider and request rides"
rider := Rider new.
rider initializeWithID: 201 name: 'Ashmin Shrestha'.
rider requestRide: sRide.
rider requestRide: pRide.
rider viewRides.

Transcript show: '--- System Demo Complete ✅ ---'; cr.
