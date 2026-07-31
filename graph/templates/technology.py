"""
Technology Workflow Template

Defines the execution plan for technology companies.
"""


class TechnologyWorkflow:
    """
    Technology workflow definition.
    """

    def __init__(self):

        self.name = "Technology Workflow"

    def get_nodes(self):
        """
        Returns all workflow nodes.
        """

        return [
            "financial_agent",
            "innovation_agent",
            "competition_agent",
            "risk_agent",
            "consensus_agent",
            "portfolio_agent",
        ]

    def get_edges(self):
        """
        Sequential execution.
        """

        return [

            ("financial_agent", "innovation_agent"),

            ("financial_agent", "competition_agent"),

            ("innovation_agent", "risk_agent"),

            ("competition_agent", "risk_agent"),

            ("risk_agent", "consensus_agent"),

            ("consensus_agent", "portfolio_agent"),
        ]

    def get_entry_node(self):
        """
        Starting node.
        """

        return "financial_agent"

    def get_finish_node(self):
        """
        Final node.
        """

        return "portfolio_agent"