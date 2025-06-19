package taskqueue

/*
	Shared Resource Queue using Go channels (safe concurrency queue)
*/

// TaskQueue is a buffered channel wrapper representing the shared queue
type TaskQueue struct {
	Tasks chan string
}

// NewTaskQueue initializes a new queue
func NewTaskQueue(size int) *TaskQueue {
	return &TaskQueue{
		Tasks: make(chan string, size),
	}
}

// AddTask adds a task to the queue
func (q *TaskQueue) AddTask(task string) {
	q.Tasks <- task
}

// Close closes the channel
func (q *TaskQueue) Close() {
	close(q.Tasks)
}
