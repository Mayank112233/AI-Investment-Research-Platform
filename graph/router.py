"""
Industry Router

This module decides which workflow template should be used
based on the company information returned by the Company Search Tool.
"""

from schemas.company import Company


class IndustryRouter:
    """
    Routes a company to the correct workflow.
    """

    # Mapping of sectors/industries to workflows
    WORKFLOW_MAPPING = {
        "technology": [
            "technology",
            "consumer electronics",
            "software",
            "semiconductors",
            "internet services",
            "communication equipment",
        ],
        "banking": [
            "financial",
            "banks",
            "banking",
            "insurance",
            "asset management",
            "capital markets",
        ],
        "healthcare": [
            "healthcare",
            "biotechnology",
            "pharmaceuticals",
            "drug manufacturers",
            "medical devices",
        ],
        "energy": [
            "energy",
            "oil",
            "gas",
            "renewable",
            "utilities",
        ],
        "automobile": [
            "automobile",
            "auto manufacturers",
            "electric vehicles",
            "automotive",
        ],
    }

    def route(self, company: Company) -> str:
        """
        Decide which workflow should execute.

        Parameters
        ----------
        company : Company
            Company metadata.

        Returns
        -------
        str
            Workflow name.
        """

        # Combine sector + industry into one searchable string
        search_text = (
            f"{company.sector} {company.industry}"
        ).lower()

        for workflow, keywords in self.WORKFLOW_MAPPING.items():

            for keyword in keywords:

                if keyword in search_text:
                    return workflow

        # Default workflow
        return "technology"