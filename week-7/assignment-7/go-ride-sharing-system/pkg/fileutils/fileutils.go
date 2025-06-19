package fileutils

import (
	"bufio"
	"os"

	"rideshare/pkg/logger"
)

/*
	Writing results to file with error handling
*/

func WriteResultsToFile(results []string, fileName string) {
	// Ensure outputs directory exists
	os.MkdirAll("outputs", os.ModePerm)

	file, err := os.OpenFile("outputs/"+fileName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		logger.Logger.Println("Failed to open file:", err)
		return
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	for _, line := range results {
		_, err := writer.WriteString(line + "\n")
		if err != nil {
			logger.Logger.Println("Failed to write result:", err)
		}
	}
	writer.Flush()
}
