"""
Banking Workflow Template
"""


class BankingWorkflow:

    def __init__(self):

        self.name = "Banking Workflow"

    def get_nodes(self):

        return [
            "financial_agent",
            "credit_agent",
            "regulation_agent",
            "risk_agent",
            "consensus_agent",
        ]