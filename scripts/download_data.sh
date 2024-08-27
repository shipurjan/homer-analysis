#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

download_poem() {
  poem_name="$1"
  expected_book_count="$2"
  sources_dir="$SCRIPT_DIR/${poem_name}_sources.txt"
  output_dir="$SCRIPT_DIR/../data/${poem_name}"

  aria2c --auto-file-renaming=false -c -s 16 -x 16 -k 1M -j 16 -i "$sources_dir" -d "$output_dir"

  actual_book_count=$(ls 2>/dev/null "$output_dir" | wc -l)
  ls -Ubad1 -- "$output_dir"
  if [ ! "$actual_book_count" -eq "$expected_book_count" ]; then
    echo "[ERROR] Expected the script to have downloaded ${expected_book_count} ${poem_name} books, but downloaded ${actual_book_count} books. Try again."
    exit 1
  fi
}

download_poem iliad 24
download_poem odyssey 24
