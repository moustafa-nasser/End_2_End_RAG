<<<<<<< HEAD
import os
from dotenv import load_dotenv
from pathlib import Path    

env_path = Path(__file__).parent.parent / "data" / ".env"
load_dotenv(env_path)

model = os.getenv("QWEN_MODEL")
=======
import os
from dotenv import load_dotenv
from pathlib import Path    

env_path = Path(__file__).parent.parent / "data" / ".env"
load_dotenv(env_path)

model = os.getenv("QWEN_MODEL")
>>>>>>> 7697943 (fix: update project structure and paths)
print(f"QWEN_MODEL: {model}")