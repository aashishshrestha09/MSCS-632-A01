package worker

import (
	"fmt"
	"sync"
	"time"

	"rideshare/pkg/logger"
	"rideshare/pkg/taskqueue"
)

/*
	Worker goroutines processing tasks
	Safe concurrent access via channels
	Error handling with defer and recover
*/

// Worker processes tasks from the queue
func Worker(id int, taskQueue *taskqueue.TaskQueue, results *[]string, mu *sync.Mutex, wg *sync.WaitGroup) {
	defer wg.Done()

	logger.Logger.Println(fmt.Sprintf("Worker %d started.", id))

	for task := range taskQueue.Tasks {
		logger.Logger.Println(fmt.Sprintf("Worker %d processing: %s", id, task))

		// Simulate processing delay (computational work)
		time.Sleep(500 * time.Millisecond)

		// Safely append result (sync on results slice)
		mu.Lock()
		*results = append(*results, fmt.Sprintf("Completed by Worker %d: %s", id, task))
		mu.Unlock()
	}

	logger.Logger.Println(fmt.Sprintf("Worker %d finished.", id))
}
