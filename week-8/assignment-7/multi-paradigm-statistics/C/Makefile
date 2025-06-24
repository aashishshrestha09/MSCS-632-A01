# Compiler to use
CC = gcc

# Compiler flags: show all warnings, use C11 standard
CFLAGS = -Wall -Wextra -std=c11

# Output executable name
TARGET = statistics

# Source file
SRC = statistics.c

# Default target: build the executable
all: $(TARGET)

# Rule to build the executable from the source
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Clean up build artifacts
clean:
	rm -f $(TARGET)
