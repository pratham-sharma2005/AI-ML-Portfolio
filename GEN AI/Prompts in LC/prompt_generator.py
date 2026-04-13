from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}  
Explanation Length: {length_input}  

1. Mathematical Details:  
- Include relevant mathematical equations if present in the paper.  
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

2. Analogies:  
- Use relatable analogies to simplify complex ideas.  

If some exact details are unavailable, provide the best possible explanation based on known concepts without guessing unsupported facts.

Ensure clarity and accuracy.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

template.save("template.json")