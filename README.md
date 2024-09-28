# ChatGPT Wrapper

Simple wrapper for OpenAI GPT API.

Supports all models including `4o-mini` and `4o`.

## Installation

Add aliases to `.zshrc`:

```shell
  alias chatgpt="python [path-to-repo]/chatgpt-wrapper/chatgpt.py"
  alias chatgpt-4o="MODEL=gpt-4o python [path-to-repo]/chatgpt-wrapper/chatgpt.py"
```

Add secret key:

- Create `.env` file based on `sample.env`.
- Set `OPENAI_API_KEY` environment variable to OpenAI Secret.

> [!NOTE]
> Alternatively, export `OPENAI_API_KEY` in system configuration.
> ```shell
> export OPENAI_API_KEY="[YOUR_API_KEY]"
> ```

Add instructions (optional):

- Create `.instructions.txt` file based on `sample.instructions.txt`.
- Paste custom instructions to add with each request.

## Usage

Run gpt-4o-mini using `chatgpt` command.
```shell
chatgpt "Who is Barack Obama? Target Gen Z audience and generate answer by highlighting historical milestones, notable accomplishments, and lasting legacy of his presidency."
```

Run gpt-4o using `chatgpt-4o` command.
```shell
chatgpt-4o "Who is Barack Obama? Target Gen Z audience and generate answer by highlighting historical milestones, notable accomplishments, and lasting legacy of his presidency."
```

Run custom model by setting `MODEL` environment variable.
```shell
MODEL=gpt-o1 chatgpt "Help me understand the chain rule of calculus."
```
