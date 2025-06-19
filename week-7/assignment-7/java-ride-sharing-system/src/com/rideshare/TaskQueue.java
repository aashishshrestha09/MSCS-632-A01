package com.rideshare;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Shared Resource Queue.
 * - Manages task queue access with synchronization.
 */
public class TaskQueue {
    private final Queue<String> queue = new LinkedList<>();
    private final ReentrantLock lock = new ReentrantLock();

    /**
     * Adds a task to the queue.
     */
    public void addTask(String task) {
        lock.lock();
        try {
            queue.add(task);
        } finally {
            lock.unlock();
        }
    }

    /**
     * Retrieves a task from the queue or returns null if empty.
     */
    public String getTask() {
        lock.lock();
        try {
            return queue.poll();
        } finally {
            lock.unlock();
        }
    }
}
