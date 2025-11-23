#!/usr/bin/env bash
DATA_DIR="./"
ARCHIVE_DIR="$DATA_DIR/archives"
LOG_FILE="$DATA_DIR/archive_log.txt"

mkdir -p "$ARCHIVE_DIR"

timestamp() { date +"%Y%m%d-%H%M%S"; }

echo ''
echo "Expense Report Manager"
echo ''
echo "1) Archive all expense files"
echo "2) Search archives by date"
echo ''
read -p "Select an option [1-2]: " choice

if [ "$choice" = "1" ]; then
  count=0
  for file in "$DATA_DIR"/expenses_*.txt; do
    [ -e "$file" ] || continue
    base=$(basename "$file")
    ts=$(timestamp)
    new="${base%.txt}-$ts.txt"

    echo "Archiving $base → $new"
    {
      echo "Archive Run: $(date)"
      echo "Original: $base"
      echo "Archive: $new"
      cat "$file"
      echo ''
    } >> "$LOG_FILE"

    mv "$file" "$ARCHIVE_DIR/$new"
    ((count++))
  done
  
  if [ "$count" -eq 0 ]; then
      echo "No expense files found to archive."
  else
      echo "Archive complete. Moved $count file(s)."
  fi
  exit 0
fi

if [ "$choice" = "2" ]; then
  read -p "Enter date to search (YYYY-MM-DD): " date
  echo
  found=false
  for f in "$ARCHIVE_DIR"/*"$date"*; do
    [ -e "$f" ] || continue
    echo "Found: $(basename "$f")"
    cat "$f"
    echo ''
    found=true
  done
  
  if [ "$found" = false ]; then
      echo "No archived records found for $date"
  fi
  exit 0
fi


echo "Invalid choice. Exiting."
exit 1
