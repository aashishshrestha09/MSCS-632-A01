package helpers

import (
	"bufio"
	"fmt"
	"strings"

	"github.com/aashishshrestha09/employee-shift-scheduler-go/config"
	"github.com/aashishshrestha09/employee-shift-scheduler-go/scheduler"
	"github.com/jedib0t/go-pretty/v6/table"
	"github.com/jedib0t/go-pretty/v6/text"
	"os"
)

// PrintBold prints the given text in bold style
func PrintBold(text string) {
	fmt.Println(config.BoldStart + text + config.BoldEnd)
}

// PrintItalic prints the given text in italic style
func PrintItalic(text string) {
	fmt.Println(config.ItalicStart + text + config.ItalicEnd)
}

// FormatEmployeeList formats a list of employees assigned to a shift,
// appending icons based on their preference ranking for the shift.
func FormatEmployeeList(employees []string, sched *scheduler.Scheduler, shift string) string {
	var formattedEmployees []string

	for _, employee := range employees {
		prefences := sched.GetEmployeePreferences(employee)
		preferenceIndex := -1
		for i, p := range prefences {
			if p == shift {
				preferenceIndex = i
				break
			}
		}

		var icon string
		switch preferenceIndex {
		case 0:
			icon = "⭐️"
		case 1:
			icon = "2️⃣"
		case 2:
			icon = "3️⃣"
		default:
			icon = ""
		}

		formattedEmployees = append(formattedEmployees, fmt.Sprintf("%s %s", employee, icon))
	}

	employeeList := strings.Join(formattedEmployees, " | ")
	if employeeList == "" {
		employeeList = "-"
	}

	return employeeList
}

// DisplayScheduleTable prints the full schedule in a nicely formatted table
// including a legend explaining preference icons.
func DisplayScheduleTable(sched *scheduler.Scheduler) {

	fmt.Println()
	PrintBold("Generated Schedule:")
	PrintItalic("Legend: ⭐️ 1st preference | 2️⃣ 2nd preference | 3️⃣ 3rd preference\n")

	t := table.NewWriter()
	t.SetOutputMirror(os.Stdout)

	// Table headers
	t.AppendHeader(table.Row{
		text.FgBlue.Sprint("DAY"),
		text.FgBlue.Sprint("SHIFT"),
		text.FgBlue.Sprint("EMPLOYEES ASSIGNED"),
	})

	t.Style().Options.SeparateRows = false
	t.Style().Options.DrawBorder = false

	// Set column alignments: center day and shift, left-align employees
	t.SetColumnConfigs([]table.ColumnConfig{
		{Number: 1, Align: text.AlignCenter},
		{Number: 2, Align: text.AlignCenter},
		{Number: 3, Align: text.AlignLeft},
	})

	for _, day := range scheduler.Days {
		for i, shift := range scheduler.Shifts {
			dayDisplay := ""
			if i == 0 {
				dayDisplay = day
			}

			employees := sched.GetSchedule()[day][shift]
			employeeList := FormatEmployeeList(employees, sched, shift)

			t.AppendRow(table.Row{
				dayDisplay,
				strings.Title(shift),
				employeeList,
			})
		}
		// Add empty row after each day for spacing
		t.AppendRow(table.Row{"", "", ""})
	}

	t.Render()
}

// AddEmployee prompts the user to input an employee's name and their preferred shifts,
// validates the input, and adds the employee with preferences to the schedule.
func AddEmployee(reader *bufio.Reader, sched *scheduler.Scheduler) {
	fmt.Print("\nEnter employee name: ")
	name, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("Error reading input, please try again.")
		return
	}
	name = strings.TrimSpace(name)

	if name == "" {
		fmt.Println("Employee name cannot be empty. Please enter a valid name.")
		return
	}

	fmt.Println("Preferred shifts (in order of preference, separated by commas):")
	for i, shift := range config.Shifts {
		fmt.Printf("%d. %s\n", i+1, shift)
	}

	var prefences []string

	for {
		fmt.Print("Enter your preferred shifts (e.g. 1,2,3): ")
		preferenceInput, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading input, please try again.")
			continue
		}
		preferenceInput = strings.TrimSpace(preferenceInput)

		preferenceNums := strings.Split(preferenceInput, ",")

		if len(preferenceNums) != 3 {
			fmt.Println("You must enter exactly 3 unique shift numbers (1, 2, 3).")
			continue
		}

		uniqueNums := make(map[string]bool)
		valid := true
		prefences = []string{}

		for _, num := range preferenceNums {
			num = strings.TrimSpace(num)
			if uniqueNums[num] {
				fmt.Printf("Duplicate shift number: %s.\n", num)
				valid = false
				break
			}
			switch num {
			case "1":
				prefences = append(prefences, config.Shifts[0])
			case "2":
				prefences = append(prefences, config.Shifts[1])
			case "3":
				prefences = append(prefences, config.Shifts[2])
			default:
				fmt.Printf("Invalid shift number: %s.\n", num)
				valid = false
				break
			}
			uniqueNums[num] = true
		}

		if valid {
			break
		} else {
			fmt.Println("Please re-enter your preferences with unique, valid numbers 1, 2, and 3.")
		}
	}

	sched.AddEmployee(name, prefences)
	fmt.Printf("Employee '%s' added successfully.\n", name)
}
