package logger

import (
	"log"
	"os"
)

/*
	Logging
	- Logs events and errors to a file.
*/

var Logger *log.Logger

func InitLogger() {
	// Ensure outputs directory exists
	os.MkdirAll("outputs", os.ModePerm)

	logFile, err := os.OpenFile("outputs/ride.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal("Failed to open log file:", err)
	}
	Logger = log.New(logFile, "", log.LstdFlags)
}
