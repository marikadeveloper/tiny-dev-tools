# Trims large log files keeping only the last N lines to prevent excessive storage use
#!/bin/bash
LOG_FILE=${1:-"app.log"}
LINES_TO_KEEP=${2:-1000}

if [[ -f "$LOG_FILE" ]]; then
    tail -n "$LINES_TO_KEEP" "$LOG_FILE" > temp.log && mv temp.log "$LOG_FILE"
    echo "Cleaned $LOG_FILE, keeping last $LINES_TO_KEEP lines."
else
    echo "File not found: $LOG_FILE"
fi

# Usage: ./log-cleaner.sh <path/to/log-file> <lines-to-keep>