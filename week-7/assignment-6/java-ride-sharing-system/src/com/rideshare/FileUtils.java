package com.rideshare;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import java.util.logging.Logger;

/**
 * Utility for writing results to a file.
 * - Logs errors during file operations.
 */
public class FileUtils {
    private static final String OUTPUT_DIR = "outputs";
    private static final String RESULT_FILE = OUTPUT_DIR + "/ride_results.txt";

    public static void writeResultsToFile(List<String> results, String fileName) {
        // Use try-with-resources to ensure file is closed
        try {
            // Ensure outputs directory exists
            new File(OUTPUT_DIR).mkdirs();

            BufferedWriter writer = new BufferedWriter(new FileWriter(RESULT_FILE, true));
            for (String line : results) {
                writer.write(line);
                writer.newLine();
            }
            writer.close();
        } catch (IOException e) {
            // Handle IOException
            LoggerConfig.LOGGER.severe("Failed to write results to file: " + e.getMessage());
        }
    }
}
