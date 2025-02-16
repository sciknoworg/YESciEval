import os

class Prompts:
    def __init__(self, prompts_dir="sciqaeval/prompts"):
        self.prompts_dir = prompts_dir
        self.prompts = self.load_prompts()

    def load_prompts(self):
        """Loads all prompt files from the directory."""
        prompts = {}
        if not os.path.exists(self.prompts_dir):
            raise FileNotFoundError(f"Directory {self.prompts_dir} not found.")
        
        for filename in os.listdir(self.prompts_dir):
            if filename.endswith(".txt"):  # Ensure only .txt files are read
                file_path = os.path.join(self.prompts_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    prompts[filename.split(".")[0]] = f.read() # Read and store the content
        return prompts

    def get_prompt(self, criteria):
        """Retrieve a specific prompt by filename."""
        return self.prompts[criteria]

    