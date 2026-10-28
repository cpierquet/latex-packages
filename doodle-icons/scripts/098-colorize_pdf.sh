#!/bin/bash

# Usage: ./colorize_pdf.sh input.pdf output.pdf

INPUT="$1"
OUTPUT="$2"
TEMP1=$(mktemp --suffix=.pdf)
TEMP2=$(mktemp --suffix=.pdf)

if [[ -z "$INPUT" || -z "$OUTPUT" ]]; then
    echo "Usage: $0 input.pdf output.pdf"
    exit 1
fi

echo "1/ Décompression..."
qpdf --qdf --object-streams=disable "$INPUT" "$TEMP1"

echo "2/ Suppression des couleurs noires..."
sed -i 's/0 0 0 rg //g; s/0 0 0 RG //g' "$TEMP1"

echo "3/ Recalcul des xref..."
fix-qdf "$TEMP1" > "$TEMP2"

echo "4/ Recompression..."
qpdf --compress-streams=y --object-streams=generate "$TEMP2" "$OUTPUT"

# Nettoyage des fichiers temporaires
rm -f "$TEMP1" "$TEMP2"

echo "✅ Terminé : $OUTPUT"
qpdf --check "$OUTPUT"