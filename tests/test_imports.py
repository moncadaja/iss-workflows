"""Every module of the package (and the Prefect flow entry points) must import."""
import importlib
import pkgutil

import pytest

import iss_workflows

MODULES = [m.name for m in pkgutil.walk_packages(iss_workflows.__path__, "iss_workflows.")]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    importlib.import_module(name)


@pytest.mark.parametrize("name", ["data_validation", "end_of_run_workflow"])
def test_flow_entry_points_import(name):
    importlib.import_module(name)
