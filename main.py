import os
import shutil

def sort_files_by_extension(base_path):
    """
    Sortiert Dateien in jedem Unterordner (inklusive base_path) nach Dateiendung.
    Für jede Endung wird in diesem Ordner ein Unterordner erstellt.
    Dateien werden dorthin verschoben. Teil der automatischen Dateisortierung-Pipeline."""
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Endung ohne Punkt, in Großbuchstaben
            _, ext = os.path.splitext(file)
            if not ext:
                continue
            ext = ext[1:].upper()

            target_dir = os.path.join(root, ext)
            os.makedirs(target_dir, exist_ok=True)

            target_path = os.path.join(target_dir, file)

            if os.path.abspath(file_path) == os.path.abspath(target_path):
                continue

            shutil.move(file_path, target_path)
            print(f"Verschoben: {file_path} -> {target_path}")

if __name__ == "__main__":
    raw_path = input("Pfad eingeben oder hierher ziehen: ").strip()

    # Falls Pfad mit Anführungszeichen kommt -> entfernen
    if raw_path.startswith('"') and raw_path.endswith('"'):
        raw_path = raw_path[1:-1]

    if os.path.isdir(raw_path):
        sort_files_by_extension(raw_path)
        print("Sortierung abgeschlossen.")
    else:
        print("Pfad ist leider ungültig:", raw_path)
