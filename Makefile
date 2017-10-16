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

examples:
	python specparser_main.py -e 1

clean:
	rm -rf *.pyc ./Tests/Outputs ./Examples/Outputs

gen:
	yapps2 specparser.g specparser.py
	sed -i "s/from __future__ import print_function//" specparser.py
	sed -i "s/# FROMFUTUREIMPORT/from __future__ import print_function/" specparser.py
