PYTEST ?= pytest
BLACK ?= black

.PHONY: format-check test-fast test-full verify

format-check:
	$(BLACK) --check src/ tests/ service/

test-fast:
	$(PYTEST) $(TEST_FILES)

test-full:
	$(PYTEST) tests/ --cov=src --cov=service --cov-fail-under=100 --cov-report=term-missing

verify: format-check test-full
