#!/bin/bash

if [ "$1" = "archive" ]; then
    date=$2
    filename="expenses_${date}.txt"
    
    if ! [[ $date =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        echo "Error: Invalid date format. Use YYYY-MM-DD"
        exit 1
    fi
    
    if [ ! -f "$filename" ]; then
        echo "Error: File '$filename' not found"
        exit 1
    fi
    
    year=$(echo $date | cut -d'-' -f1)
    month=$(echo $date | cut -d'-' -f2)
    archive_path="expenses/${year}/${month}"
    
    mkdir -p "$archive_path"
    mv "$filename" "$archive_path/"
    
    echo "Successfully archived '$filename' to '$archive_path/'"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ARCHIVED: $filename to $archive_path/" >> archive_log.txt

elif [ "$1" = "search" ]; then
    date=$2
    filename="expenses_${date}.txt"
    
    if ! [[ $date =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        echo "Error: Invalid date format. Use YYYY-MM-DD"
        exit 1
    fi
    
    year=$(echo $date | cut -d'-' -f1)
    month=$(echo $date | cut -d'-' -f2)
    archive_path="expenses/${year}/${month}/${filename}"
    
    if [ ! -f "$archive_path" ]; then
        echo "Error: Archived file not found for date $date"
        exit 1
    fi
    
    echo "ARCHIVED EXPENSES FOR: $date"
    echo "--------------------------------------------------------------------------------"
    while IFS='|' read -r id date time item amount; do
        printf "%-5s | %-10s | %-8s | %-30s | \$%.2f\n" "$id" "$date" "$time" "$item" "$amount"
    done < "$archive_path"
    echo "--------------------------------------------------------------------------------"
    
    total=$(awk -F'|' '{sum += $5} END {printf "%.2f", sum}' "$archive_path")
    echo "Total: \$$total"
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] SEARCHED: $archive_path" >> archive_log.txt

else
    echo "Usage: $0 [archive|search] DATE"
    echo "Examples:"
    echo "  $0 archive 2025-11-07"
    echo "  $0 search 2025-11-07"
    exit 1
fi
