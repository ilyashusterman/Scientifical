################################################################################
# Makefile for Scientifical
################################################################################

# Prefer bash shell
export SHELL=/bin/bash

## Define repositories dependencies paths

## Make sure of current python path
export PYTHONPATH=$(pwd)

self := $(abspath $(lastword $(MAKEFILE_LIST)))
parent := $(dir $(self))

ifneq (,$(VERBOSE))
    override VERBOSE:=
else
    override VERBOSE:=@
endif

.PHONY: setup
setup:
	$(VERBOSE) virtualenv -p python3.6 venv
	$(VERBOSE) pip install -r requirements.txt
	$(VERBOSE) python data_center_monitor/manage.py migrate
.PHONY: update
update:
	$(VERBOSE) git pull origin master
	$(VERBOSE) python data_center_monitor/manage.py migrate
.PHONY: updatedb
updatedb:
	$(VERBOSE) export PYTHONPATH=$(pwd):$(pwd)/data_center_monitor
	$(VERBOSE) cd data_center_monitor && export PYTHONPATH=$(pwd):$(pwd)/data_center_monitor && python data_center_monitor/dashboard/scripts/update.py
.PHONY: deleteall
deleteall:
	$(VERBOSE) export PYTHONPATH=$(pwd):$(pwd)/data_center_monitor
	$(VERBOSE) cd data_center_monitor && export PYTHONPATH=$(pwd):$(pwd)/data_center_monitor && python data_center_monitor/dashboard/scripts/delete.py
.PHONY: runserver
runserver:
	$(VERBOSE) python data_center_monitor/manage.py runserver
.PHONY: test
test:
	$(VERBOSE) python data_center_monitor/manage.py test data_center_monitor.dashboard.test
.PHONY: test_statistics
test_statistics:
	$(VERBOSE) python data_center_monitor/manage.py test