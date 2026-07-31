"""
Energy Workflow Template
"""


class EnergyWorkflow:

    def __init__(self):

        self.name = "Energy Workflow"

    def get_nodes(self):

        return [
            "financial_agent",
            "commodity_agent",
            "policy_agent",
            "risk_agent",
            "consensus_agent",
        ]