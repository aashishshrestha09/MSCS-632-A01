package com.rideshare;

import java.util.List;

/**
 * Worker thread.
 * - Processes tasks, simulates delay, and writes results.
 * - Manages concurrency and resource access.
 * - Exception handling and logging per thread.
 */
public class Worker implements Runnable {
    private final int id;
    private final TaskQueue taskQueue;
    private final List<String> results;

    public Worker(int id, TaskQueue taskQueue, List<String> results) {
        this.id = id;
        this.taskQueue = taskQueue;
        this.results = results;
    }

    @Override
    public void run() {
        LoggerConfig.LOGGER.info("Worker " + id + " started.");
        try {
            String task;
            while ((task = taskQueue.getTask()) != null) {
                LoggerConfig.LOGGER.info("Worker " + id + " processing: " + task);
                try {
                    // Simulate processing delay (computational work)
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    // Handle InterruptedException
                    LoggerConfig.LOGGER.warning("Worker " + id + " interrupted.");
                    Thread.currentThread().interrupt();
                    break;
                }
                // Synchronize results list access to prevent race conditions
                synchronized (results) {
                    results.add("Completed by Worker " + id + ": " + task);
                }
            }
        } catch (Exception e) {
            // Handle any unexpected exceptions
            LoggerConfig.LOGGER.severe("Worker " + id + " encountered error: " + e.getMessage());
        } finally {
            LoggerConfig.LOGGER.info("Worker " + id + " finished.");
        }
    }
}
