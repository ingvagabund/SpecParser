.PHONY: test

run:
ifdef SPEC
	python specparser.py -i ${SPEC}
endif
ifndef SPEC
	python specparser.py
endif

test:
	python tests.py