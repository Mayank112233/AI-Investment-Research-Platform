"""
Healthcare Workflow Template
"""


class HealthcareWorkflow:

    def __init__(self):

        self.name = "Healthcare Workflow"

    def get_nodes(self):

        return [
            "financial_agent",
            "clinical_agent",
            "drug_pipeline_agent",
            "risk_agent",
            "consensus_agent",
        ]