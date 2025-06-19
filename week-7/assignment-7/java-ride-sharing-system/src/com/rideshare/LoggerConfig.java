package com.rideshare;

import java.io.File;
import java.io.IOException;
import java.util.logging.*;

/**
 * Centralized logger configuration.
 * Logs to a file with simple formatting.
 * - Logging for thread events and errors.
 */
public class LoggerConfig {
    public static final Logger LOGGER = Logger.getLogger(LoggerConfig.class.getName());
    private static final String OUTPUT_DIR = "outputs";
    private static final String LOG_FILE = OUTPUT_DIR + "/ride.log";

    static {
        try {
            // Ensure outputs directory exists
            new File(OUTPUT_DIR).mkdirs();

            // Set up the file handler to log into outputs/ride.log
            Handler fileHandler = new FileHandler(LOG_FILE, true);
            fileHandler.setFormatter(new SimpleFormatter());
            LOGGER.addHandler(fileHandler);
            LOGGER.setUseParentHandlers(false);
        } catch (IOException e) {
            LOGGER.severe("Failed to set up logger: " + e.getMessage());
        }
    }
}
