package config

// ANSI escape codes for styling console output
const (
	BoldStart   = "\033[1m"
	BoldEnd     = "\033[0m"
	ItalicStart = "\033[3m"
	ItalicEnd   = "\033[0m"
)

// Days of the week to schedule shifts for
var Days = []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

// Possible shifts in a day
var Shifts = []string{"Morning", "Afternoon", "Evening"}
