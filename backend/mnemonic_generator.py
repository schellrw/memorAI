from langchain import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Hugging Face model
model_name = os.getenv("HF_MODEL_NAME")
hf_pipeline = HuggingFacePipeline.from_model_id(
    model_id=model_name,
    task="text-generation",
    model_kwargs={"temperature": 0.7, "max_length": 256}
)

# Create a prompt template
template = """
Create a memorable mnemonic device to help students remember the following concept:

Concept: {concept}

Mnemonic device:
"""

prompt = PromptTemplate(template=template, input_variables=["concept"])

# Create an LLMChain
llm_chain = LLMChain(prompt=prompt, llm=hf_pipeline)

def generate_mnemonic(concept):
    response = llm_chain.run(concept)
    return response.strip()