### What is Generative AI?
- Generative AI is a subset of artificial intelligence capable of creating text, images, or other data using generative models. 
- It responds to prompts and has grown in popularity since 2021. 
- Generative AI models act like conversational programs that generate content based on inputs.

### What is a Large Language Model (LLM)?
- LLMs are sophisticated programs trained on massive datasets (text, images, code). “Large” refers to dataset size and the number of model parameters (can be billions/trillions). 
- They are pre-trained for general purposes and fine-tuned for specific goals. 
- LLMs act as an advanced autocomplete, predicting responses based on the input prompt. 
- They are subject to hallucination (incorrect or nonsensical outputs) if not enough context or data is provided.

### Hallucinations in LLMs
- Hallucinations occur due to limited data, noisy training data, lack of context, or too few constraints. 
- LLMs only know what they’ve been explicitly trained on and have no real-time knowledge.
-  Scenario Example
    - Sasha, a cloud architect, uses generative AI tools and prompt engineering to quickly design a Google Cloud VPC network.

### What is Prompt Engineering?
- **Prompt**: Text or instruction fed to the model.
- **Prompt Engineering**: Structuring prompts to get the best possible output. The better the prompt, the better the output.

### Types of Prompts

- **Zero-shot**: Asking the model to complete a task with no prior examples.
- **One-shot**: Providing the model with one example to learn from.
- **Few-shot**: Giving the model multiple examples to learn from.
- **Role**: Assigning a persona to the model to influence its style, tone, and focus.
- **Prompt chaining**: Engaging in a back-and-forth conversation with the AI.

### Prompt Structure
- **Preamble**: Context, instructions, examples—sets the stage for the model.
- **Input**: The main request or instruction.
- Not every component is required; structure depends on the task.


### Reasoning Loop: Prompt Engineering Techniques

- **ReAct (reason and act)**: Allow the LLM to reason and take action on a user query.
- **CoT (chain-of-thought)**: Guide an LLM through a problem-solving process by providing examples with intermediate reasoning steps.

### Model Guidance and Refinement

- **Grounding**: Connecting the AI's output to verifiable sources of information.
- **RAG (Retrieval-Augmented Generation)**:
  1. **Retrieval**: The LLM retrieves relevant information from external sources using tooling.
  2. **Augmentation**: The retrieved information is incorporated into the prompt to the LLM.
  3. **Generation**: The LLM processes the prompt and generates a response.
  4. **Iteration (optional)**: The LLM can iterate on the retrieval process as necessary.
- **Metaprompting**: Use prompting to guide the AI model to generate, modify, or interpret other prompts.

### Streamlining Prompting Workflows

- **Reusing prompts**: Saving prompts as templates for repeated use.
- **Leveraging prompt chaining**: Continuing conversations within the same chatbot to maintain context.
- **Using saved info in Gemini**: Storing specific information for the model to use consistently.
- **Gems**: Personalized AI assistants within Gemini. They provide personalized responses tailored to specific instructions. They also streamline workflows like templates, prompts, and guided interactions.

### Prompt Engineering Best Practices
- Write explicit and detailed instructions; avoid vague prompts.
- Define boundaries (what to do, not what not to do).
- Use fallback outputs for uncertain cases (“I’m still learning about that”).
- Adopt a persona to focus the model and improve accuracy.
- Keep sentences concise; prefer short, clear instructions.
- Break long sentences into simpler, shorter sentences and tasks.

### Example Use Case
Sasha’s refined prompt yields a highly relevant VPC network design suggestion (hub-and-spoke architecture). Refining and amending prompts helps articulate requirements for optimal model output.


### Sampling Parameters

Settings that influence the AI model's behavior, allowing for customized results.

- **Token count**: This represents meaningful chunks of text (like words and punctuation).
- **Temperature**: This parameter controls the "creativity" or randomness of the model's word choices during text generation.
- **Top-p (nucleus sampling)**: The cumulative probability of the most likely tokens considered during text generation. This is another way to control the randomness of the model's output.
- **Safety settings**: These settings allow you to filter out potentially harmful or inappropriate content from the model's output.
- **Output length**: This determines the maximum length of the generated text.