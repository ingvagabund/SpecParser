.PHONY: test clean

run:
ifdef SPEC
	python specparser_main.py -i ${SPEC}
endif
ifndef SPEC
	python specparser_main.py
endif

test:
	python specparser_main.py -t 1

clean:
	rm -rf *.pyc ./Tests/Outputs/*
