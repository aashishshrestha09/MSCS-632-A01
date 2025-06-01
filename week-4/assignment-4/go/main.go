package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/aashishshrestha09/employee-shift-scheduler-go/helpers"
	"github.com/aashishshrestha09/employee-shift-scheduler-go/scheduler"
)

func main() {
	schedulerInstance := scheduler.NewScheduler()
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println("\nWhat would you like to do?")
		fmt.Println("1. Add employee")
		fmt.Println("2. View current schedule")
		fmt.Println("3. Exit")

		fmt.Print("Enter your choice (1, 2, 3): ")
		choiceInput, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading input, please try again.")
			continue
		}
		choiceInput = strings.TrimSpace(choiceInput)

		switch choiceInput {
		case "1":
			helpers.AddEmployee(reader, schedulerInstance)
		case "2":
			schedulerInstance.AssignShifts()
			helpers.DisplayScheduleTable(schedulerInstance)
		case "3":
			fmt.Println("Exiting program.")
			return
		default:
			fmt.Println("Invalid choice. Please enter 1, 2, or 3.")
		}
	}
}
