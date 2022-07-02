from pathlib import Path

# Absolute path

# Relative path
path = Path("ecommerce")
print(path.exists())


for file in path.glob('*'):
    print(file)
