# Java compiler and runtime
JAVAC=javac
JAVA=java

# Directories
SRC_DIR=src
OUT_DIR=out
OUTPUT_DIR=outputs

# Package path
PACKAGE_PATH=$(SRC_DIR)/com/rideshare

# Main class to run
MAIN_CLASS=com.rideshare.Main

# Files to compile
SRC_FILES=$(PACKAGE_PATH)/*.java

# Log and result files
RESULT_FILE=$(OUTPUT_DIR)/ride_results.txt
LOG_FILE=$(OUTPUT_DIR)/ride.log

# Default target: build and run
all: build run

# Compile Java source files into the out directory
build:
	@echo "Compiling Java source files..."
	mkdir -p $(OUT_DIR)
	$(JAVAC) -d $(OUT_DIR) $(SRC_FILES)
	@echo "Compilation complete."

# Run the Java program
run:
	@echo "Running the Ride Sharing Data Processing System..."
	mkdir -p $(OUTPUT_DIR)
	$(JAVA) -cp $(OUT_DIR) $(MAIN_CLASS)
	@echo "Execution complete."

# Clean class files and output logs
clean:
	@echo "Cleaning compiled files and outputs..."
	rm -rf $(OUT_DIR)
	rm -rf $(OUTPUT_DIR)
	@echo "Clean complete."

# Phony targets (so they always run when called)
.PHONY: all build run clean
