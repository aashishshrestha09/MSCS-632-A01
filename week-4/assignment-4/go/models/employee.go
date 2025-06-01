package models

// Employee represents an employee with shift preferences and assignment tracking
type Employee struct {
	Name           string          // Employee's name
	Preferences    []string        // Preferred shifts ordered by rank
	PreferenceRank map[string]int  // Map shift -> rank index (0 = top preference)
	AssignedDays   map[string]bool // Days already assigned to this employee (for max 5 days/week constraint)
}
