import json
from pathlib import Path
from datetime import datetime

class FileUtils:
    def delete_all_files_in_dir(self, output_dir="output/api-responses"):
        dir_path = Path.cwd() / output_dir
        if dir_path.exists() and dir_path.is_dir():
            for file_path in dir_path.iterdir():
                if file_path.is_file():
                    file_path.unlink()
            print(f"✅ All files deleted in: {dir_path}")
        else:
            print(f"ℹ️ Directory does not exist: {dir_path}")

    def save_json_with_timestamp(self, data, name):
        timestamp = int(datetime.now().timestamp() * 1000)
        dir_path = Path.cwd() / "output/api-responses"
        dir_path.mkdir(parents=True, exist_ok=True)
        file_path = dir_path / f"{name}_{timestamp}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return str(file_path)

    def compare_json_files(self, file_name, file_path2):
        with open(f"./data/{file_name}", "r", encoding="utf-8") as f1, open(file_path2, "r", encoding="utf-8") as f2:
            json1 = json.load(f1)
            json2 = json.load(f2)
        # Use direct comparison
        are_equal = json1 == json2
        if are_equal:
            print("✅ JSON files are deeply equal.")
        else:
            print("❌ JSON files differ.")
        return are_equal
