.PHONY: compile test clean

compile:
	echo "nahh"

test:
	trial test/test*.py

clean:
	rm -f _trial_temp
	find . -name "*.pyc"|xargs rm
