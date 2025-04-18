doc:
	uv run --with rich readme.py

update: doc
	# Git operations are now handled by GitHub Actions