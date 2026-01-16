# gen_requirements.py
import tomllib

with open("pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)

deps = pyproject.get("project", {}).get("dependencies", [])

optional_deps_dict = pyproject.get("project", {}).get("optional-dependencies", {})
for group_deps in optional_deps_dict.values():
    deps.extend(group_deps)

deps = [d for d in deps if not d.startswith("pathway")]
with open("requirements.txt", "w") as f:
    f.write("\n".join(deps))


