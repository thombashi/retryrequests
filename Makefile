PACKAGE := python_package_template


.PHONY: build
build:
	@make clean
	@tox -e build
	ls -lh dist/*

.PHONY: clean
clean:
	@tox -e clean

.PHONY: fmt
fmt:
	@tox -e fmt

.PHONY: release
release:
	@python setup.py release --sign
	@make clean
