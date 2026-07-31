"""
Workflow Builder

Loads the appropriate workflow template based on
the workflow selected by the Industry Router.
"""

from graph.templates.technology import TechnologyWorkflow
from graph.templates.banking import BankingWorkflow
from graph.templates.healthcare import HealthcareWorkflow
from graph.templates.energy import EnergyWorkflow
from graph.templates.automobile import AutomobileWorkflow


class WorkflowBuilder:
    """
    Builds and returns workflow templates.
    """

    def __init__(self):

        self.workflows = {

            "technology": TechnologyWorkflow,

            "banking": BankingWorkflow,

            "healthcare": HealthcareWorkflow,

            "energy": EnergyWorkflow,

            "automobile": AutomobileWorkflow,
        }

    def build(self, workflow_name: str):

        workflow = self.workflows.get(workflow_name)

        if workflow is None:

            raise ValueError(
                f"Workflow '{workflow_name}' not found."
            )

        return workflow()