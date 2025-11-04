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

### Prompting Techniques

- **Zero-shot**: Asking the model to complete a task with no prior examples.
- **One-shot**: Providing the model with one example to learn from.
- **Few-shot**: Giving the model multiple examples to learn from.
- **Role**: Assigning a persona to the model to influence its style, tone, and focus.
- **Prompt chaining**: Engaging in a back-and-forth conversation with the AI.
- **ReAct (reason and act)**: Allow the LLM to reason and take action on a user query.
- **CoT (chain-of-thought)**: Guide an LLM through a problem-solving process by providing examples with intermediate reasoning steps.
- **Self-reflection**: Asking the model to evaluate its own output.


### Prompt Structures (templates)

1. Alpaca-style:
- Alpaca prompting is a plain text template where you give the LLM a clear instruction or question, optionally with additional context/input, and the model is expected to produce a direct response ("output")—all usually within a single turn.
- mainly used for fine-tuning open-source LLMs to follow instructions.
[Read-more](https://github.com/tatsu-lab/stanford_alpaca?tab=readme-ov-file#data-release)

- **Structure:**
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}[task or question for the model]

### Input:
{input}[optional extra context—often omitted for simple tasks]

### Output: [model fills this in with its best response]
```
- **Example:**
```
Instruction: Summarize the following text in one sentence.
Input: The quick brown fox jumps over the lazy dog.
Output:
```
- **when to use:**
 - Fine-tuning or training open-source LLMs for instruction-following tasks.
 - Single-turn, direct Q&A, or text generation tasks (summarization, translation, coding, etc.).
  - Scripting simple bots or non-conversational agents.
  - Benchmarking or evaluating clear, short-form model instructions.

2.CHATML:
- CHATML is the prompt schema designed by OpenAI for conversational LLMs (e.g., GPT-3.5, GPT-4). It structures dialogue into distinct message blocks (system, user, assistant) using XML/Markdown-like tags, separating roles and content.
- This format makes conversation state, persona, and histories more explicit for multi-turn chat and agentic workflows.

- **Structure:**
```
<|im_start|>system
{system message}
<|im_end|>

<|im_start|>user
{user message / query}
<|im_end|>

<|im_start|>assistant
{model output}
<|im_end|>
```

- so the below json format is used in code to represent the messages:

```
{
  "role": "system",
  "content": "Sets the 'persona,' general behavior, or global instructions for the assistant"
},
{
  "role": "user" ,
  "content": "Any prompt, instruction, or query from the human user—the input that the model is to answer or respond to."
},
{
  "role": "assistant",
  "content": "The LLM’s/model’s reply or completion in response to the "user" message, influenced by the optional "system" instruction"
}

```

- **Function to convert messages to CHATML format:**
```python

def to_chatml(messages):
    chatml = ""
    for m in messages:
        chatml += f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>\n"
    chatml += "<|im_start|>assistant\n"  # Leave open for AI's reply
    return chatml
```
- **Example:**

```python
  messages = [{'role': 'system',
  'content': 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.'},
 {'role': 'user', 'content': 'Hello world!'},
 {'role': 'assistant', 'content': 'Hello there!'},
 {'role': 'system', 'content': 'Now, you are Elon Musk. Speak like him.'},
 {'role': 'user', 'content': 'Hello world!'}]
  chatml_prompt = to_chatml(messages)
```
- **when to use:**
  - Fine-tuning or using chat-based models (OpenAI, Mistral, etc.).
  - Multi-turn conversations, chatbots, or agentic use-cases.
  - RAG systems and conversational memory chaining.
  - When explicit role/context separation is needed.

3.INST Format (LLaMA-2/Mistral Style)
- The INST format is used for instruction tuning with the LLaMA-2 family. It uses clear delimiters and tags to separate instructions and responses, optimizing for direct single-turn Q&A or task completion.

- **Structure:**
```
<<SYS>>
{system prompt}
<</SYS>>

[INST] {instruction or user message} [/INST]
{model response}

```

- **Example:**
```
<<SYS>>
You are a helpful assistant that translates English to French.
<</SYS>>
[INST] Translate the following sentence to French: "Hello, how are you?" [/INST]
Bonjour, comment ça va?
```

- **when to use:**
  - Instruction-tuning open-source models (especially LLaMA-2 variants).
  - Direct Q&A, text transformation, or task completion.
  - Benchmarking models for short-form and role-based completions.ompts is needed.


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