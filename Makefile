.PHONY: compile test clean

compile:
	echo "nahh"

test:
	trial test/test*.py

linecount:
	find . -name "*.py" | xargs wc -l

clean:
	rm -rf _trial_temp
	find . -name "*.pyc"|xargs rm
