"""
Automobile Workflow Template
"""


class AutomobileWorkflow:

    def __init__(self):

        self.name = "Automobile Workflow"

    def get_nodes(self):

        return [
            "financial_agent",
            "ev_agent",
            "competition_agent",
            "risk_agent",
            "consensus_agent",
        ]
    
