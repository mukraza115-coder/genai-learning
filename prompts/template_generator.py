from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications.

Explanation Style: {style_input}

Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present.
- Explain them with simple code snippets where applicable.

2. Analogies:
- Use relatable analogies.

3. Missing Information:
- If information is unavailable, respond with:
  "Insufficient Information available"

Ensure the summary is clear and accurate.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

template.save("template.json")