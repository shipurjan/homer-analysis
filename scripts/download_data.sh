aria2c --auto-file-renaming=false -c -s 16 -x 16 -k 1M -j 16 -i iliad_sources.txt -d "../data/iliad"

iliad_books=$(ls 2>/dev/null -Ubad1 -- ../data/iliad/*.xml | wc -l)
if [ ! "$iliad_books" -eq 24 ]; then

  echo "[ERROR] Expected the script to have downloaded 24 Iliad books, but downloaded $iliad_books books. Try again."
  exit 1
fi

aria2c --auto-file-renaming=false -c -s 16 -x 16 -k 1M -j 16 -i odyssey_sources.txt -d "../data/odyssey"

odyssey_books=$(ls 2>/dev/null -Ubad1 -- ../data/odyssey/*.xml | wc -l)
if [ ! "$odyssey_books" -eq 24 ]; then

  echo "[ERROR] Expected the script to have downloaded 24 Odyssey books, but downloaded $odyssey_books books. Try again."
  exit 1
fi
