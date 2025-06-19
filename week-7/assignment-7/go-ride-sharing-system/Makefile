# Go command
GOCMD=go

# Output files
RESULT_FILE=outputs/ride_results.txt
LOG_FILE=outputs/ride.log

# Build output binary name
BINARY_NAME=rideshare

# Main package path
MAIN_PKG=./cmd/rideshare

# Default target: build and run
all: prepare build run

# Prepare outputs directory
prepare:
	@mkdir -p outputs

# Build binary
build:
	@echo "Building Go program..."
	$(GOCMD) build -o $(BINARY_NAME) $(MAIN_PKG)
	@echo "Build complete."

# Run program using 'go run'
run:
	@echo "Running Go program..."
	$(GOCMD) run $(MAIN_PKG)
	@echo "Execution complete."

# Clean compiled binary, logs, and result files
clean:
	@echo "Cleaning up..."
	rm -f $(BINARY_NAME)
	rm -rf outputs/
	@echo "Cleanup complete."

# Format source code
fmt:
	@echo "Formatting Go source files..."
	$(GOCMD) fmt ./...
	@echo "Formatting complete."

# Tidy up modules
tidy:
	@echo "Tidying Go modules..."
	$(GOCMD) mod tidy
	@echo "Modules tidy."

.PHONY: all build run clean fmt tidy prepare
