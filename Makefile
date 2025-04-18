doc:
	uv run --with rich readme.py

update: doc
	git add .
	git commit -m "Update README"
	git push origin main