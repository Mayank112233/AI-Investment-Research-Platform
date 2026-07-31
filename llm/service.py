class LLMService:

    def __init__(self, provider):
        self.provider = provider

    def generate(
        self,
        prompt,
        output_schema=None,
    ):
        return self.provider.generate(
            prompt=prompt,
            output_schema=output_schema,
        )