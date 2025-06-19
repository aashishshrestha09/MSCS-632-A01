package com.rideshare;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * Main driver.
 * - Launches worker threads.
 * - Manages concurrency with ExecutorService.
 * - Handles InterruptedException and shutdown logic.
 */
public class Main {
    public static void main(String[] args) {
        LoggerConfig.LOGGER.info("Ride Sharing Data Processing System started.");

        TaskQueue taskQueue = new TaskQueue();
        List<String> results = new ArrayList<>();

        // Add tasks to shared queue
        for (int i = 1; i <= 20; i++) {
            taskQueue.addTask("Ride Task " + i);
        }

        // Set up fixed thread pool
        int numWorkers = 5;
        ExecutorService executor = Executors.newFixedThreadPool(numWorkers);

        // Launch worker threads
        for (int i = 1; i <= numWorkers; i++) {
            executor.execute(new Worker(i, taskQueue, results));
        }

        // Shutdown logic and concurrency management
        executor.shutdown();
        try {
            // Wait for all threads to finish or timeout
            if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                LoggerConfig.LOGGER.warning("Forcing shutdown due to timeout.");
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            // Handle InterruptedException during shutdown
            LoggerConfig.LOGGER.severe("Main thread interrupted: " + e.getMessage());
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }

        // Write results to file
        FileUtils.writeResultsToFile(results, "ride_results.txt");

        LoggerConfig.LOGGER.info("Ride Sharing Data Processing System completed.");
    }
}
