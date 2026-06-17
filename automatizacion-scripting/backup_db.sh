#!/bin/bash

DB_FILE="database.db"
BACKUP_DIR="backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_NAME="backup_${TIMESTAMP}.tar.gz"

echo "===== INICIO BACKUP ====="

if [ ! -f "$DB_FILE" ]; then
    echo "ERROR: No existe $DB_FILE"
    exit 1
fi

mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$DB_FILE"

if [ $? -eq 0 ]; then
    echo "OK: Backup creado correctamente"
else
    echo "ERROR en backup"
    exit 1
fi

cd "$BACKUP_DIR"
ls -1t | tail -n +8 | xargs -r rm -f
cd ..

echo "===== FIN BACKUP ====="

