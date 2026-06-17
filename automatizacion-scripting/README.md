# Automatización Scripting

## Scripts

- backup_db.sh → Backup de base de datos
- log_analyzer.py → Detección de ataques en logs

## Ejecutar

chmod +x backup_db.sh
./backup_db.sh

python3 log_analyzer.py

## Automatización CRON

crontab -e

0 2 * * * /workspaces/automatizacion-scripting/backup_db.sh
