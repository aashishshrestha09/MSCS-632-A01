package scheduler

import (
	"math/rand"
	"sort"
	"time"

	"github.com/aashishshrestha09/employee-shift-scheduler-go/config"
	"github.com/aashishshrestha09/employee-shift-scheduler-go/models"
)

// Scheduler contains employee data and the generated schedule
type Scheduler struct {
	Employees map[string]*models.Employee
	Schedule  map[string]map[string][]string
}

var (
	Days   = config.Days
	Shifts = config.Shifts
)

// NewScheduler initializes a Scheduler with empty employee list and schedule map
func NewScheduler() *Scheduler {
	scheduler := &Scheduler{
		Employees: make(map[string]*models.Employee),
		Schedule:  make(map[string]map[string][]string),
	}
	// Initialize schedule map
	for _, day := range Days {
		scheduler.Schedule[day] = make(map[string][]string)
		for _, shift := range Shifts {
			scheduler.Schedule[day][shift] = []string{}
		}
	}
	return scheduler
}

// GetSchedule returns the full current schedule mapping days and shifts to assigned employees
func (s *Scheduler) GetSchedule() map[string]map[string][]string {
	return s.Schedule
}

// GetEmployees returns the map of all employees managed by the scheduler
func (s *Scheduler) GetEmployees() map[string]*models.Employee {
	return s.Employees
}

// GetEmployeePreferences returns the shift preferences of an employee by name
func (s *Scheduler) GetEmployeePreferences(name string) []string {
	if employee, ok := s.Employees[name]; ok {
		return employee.Preferences
	}
	return nil
}

// AddEmployee adds a new employee with their ordered shift preferences
func (s *Scheduler) AddEmployee(name string, preferences []string) {
	rank := make(map[string]int)
	for i, shift := range preferences {
		rank[shift] = i
	}
	employee := &models.Employee{
		Name:           name,
		Preferences:    preferences,
		PreferenceRank: rank,
		AssignedDays:   make(map[string]bool),
	}
	s.Employees[name] = employee
}

// ResetScheduleAndCounters clears the current schedule and resets employee assignment counters
func (s *Scheduler) ResetScheduleAndCounters() {
	for _, day := range Days {
		for _, shift := range Shifts {
			s.Schedule[day][shift] = []string{}
		}
	}
	for _, employee := range s.Employees {
		employee.AssignedDays = make(map[string]bool)
	}
}

// GetEligibleEmployeesForDay returns employees who have less than 5 assigned days and are free on the given day
func (s *Scheduler) GetEligibleEmployeesForDay(day string) []*models.Employee {
	eligible := []*models.Employee{}
	for _, employee := range s.Employees {
		if len(employee.AssignedDays) < 5 && !employee.AssignedDays[day] {
			eligible = append(eligible, employee)
		}
	}
	return eligible
}

// employeeSortHelper is used for sorting employees by days assigned and preference rank
type employeeSortHelper struct {
	DaysAssigned   int
	PreferenceRank int
	Employee       *models.Employee
}

// SortedEmployeesByPreferenceAndDaysAssigned returns employees eligible for a day sorted by fewest days assigned and best preference rank for the shift
func (s *Scheduler) SortedEmployeesByPreferenceAndDaysAssigned(day string, shift string) []employeeSortHelper {
	availableEmployees := []employeeSortHelper{}
	for _, employee := range s.GetEligibleEmployeesForDay(day) {
		rank, ok := employee.PreferenceRank[shift]
		if !ok {
			rank = 99 // Low preference if not in preferences
		}
		availableEmployees = append(availableEmployees, employeeSortHelper{
			DaysAssigned:   len(employee.AssignedDays),
			PreferenceRank: rank,
			Employee:       employee,
		})
	}

	sort.Slice(availableEmployees, func(i, j int) bool {
		if availableEmployees[i].DaysAssigned == availableEmployees[j].DaysAssigned {
			return availableEmployees[i].PreferenceRank < availableEmployees[j].PreferenceRank
		}
		return availableEmployees[i].DaysAssigned < availableEmployees[j].DaysAssigned
	})

	return availableEmployees
}

// AssignEmployee assigns an employee to a specific day and shift and marks the day as assigned for that employee
func (s *Scheduler) AssignEmployee(employee *models.Employee, day string, shift string) {
	s.Schedule[day][shift] = append(s.Schedule[day][shift], employee.Name)
	employee.AssignedDays[day] = true
}

// AssignShifts runs the scheduling algorithm to assign employees to shifts across the week
func (s *Scheduler) AssignShifts() {
	s.ResetScheduleAndCounters()

	rand.Seed(time.Now().UnixNano())

	for dayIndex, day := range Days {
		for _, shift := range Shifts {

			// Get employees sorted by fewest assigned days and preference for this shift
			availableEmployees := s.SortedEmployeesByPreferenceAndDaysAssigned(day, shift)

			// Assign top preferred employees until 2 per shift
			for len(s.Schedule[day][shift]) < 2 && len(availableEmployees) > 0 {
				employee := availableEmployees[0].Employee
				availableEmployees = availableEmployees[1:]
				s.AssignEmployee(employee, day, shift)
			}

			// If still unfilled, assign random eligible employees
			if len(s.Schedule[day][shift]) < 2 {
				eligibleEmployees := s.GetEligibleEmployeesForDay(day)
				rand.Shuffle(len(eligibleEmployees), func(i, j int) {
					eligibleEmployees[i], eligibleEmployees[j] = eligibleEmployees[j], eligibleEmployees[i]
				})
				for _, employee := range eligibleEmployees {
					if len(s.Schedule[day][shift]) < 2 {
						s.AssignEmployee(employee, day, shift)
					}
				}
			}
		}

		// Handle unassigned employees for the day
		unassignedEmployees := s.GetEligibleEmployeesForDay(day)

		for _, employee := range unassignedEmployees {
			shiftAssigned := false
			for _, preferenceShift := range employee.Preferences {
				if len(s.Schedule[day][preferenceShift]) < 2 {
					s.AssignEmployee(employee, day, preferenceShift)
					shiftAssigned = true
					break
				}
			}

			if !shiftAssigned {
				// Try next days shifts if current day is full
				for offset := 1; offset < len(Days); offset++ {
					nextDay := Days[(dayIndex+offset)%len(Days)]
					for _, preferenceShift := range employee.Preferences {
						if len(s.Schedule[nextDay][preferenceShift]) < 2 && !employee.AssignedDays[nextDay] {
							s.AssignEmployee(employee, nextDay, preferenceShift)
							shiftAssigned = true
							break
						}
					}
					if shiftAssigned {
						break
					}
				}
			}
		}
	}
}
