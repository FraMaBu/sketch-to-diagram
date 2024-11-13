"""Style guide for Mermaid.js diagram formatting."""

STYLE_GUIDE = """Apply the following styling rules to the Mermaid.js diagram while preserving the original structure and labels:

1. Determine node types and styles:
   - Start/End nodes: ([text]):::terminator
   - Process nodes: [text]:::process
   - Decision nodes: {text}:::decision
   - Input/Output nodes: [/text/]:::inputOutput
   - Database nodes: [(text)]:::database

2. Apply class definitions:
classDef terminator fill:#f9f,stroke:#333,stroke-width:2px,color:#333,stroke-dasharray:5 5;
classDef process fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#333;
classDef decision fill:#e1bee7,stroke:#6a1b9a,stroke-width:2px,color:#333;
classDef inputOutput fill:#d1edf2,stroke:#0277bd,stroke-width:2px,color:#333;
classDef database fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333;

3. Flow direction:
   - Use TB (top to bottom) for vertical flows
   - Use LR (left to right) for horizontal flows
   - Maintain the original flow direction if specified

4. Link styles:
   - Normal flow: -->
   - Labeled flow: -->|text|
   - Alternative flow: -.->
   - Thick flow: ==>

5. Use the following output schema:
```mermaid
flowchart [TB or LR]
	%% Symbol definitions
    [Define node types with classes]
	
	%% Syntax definitions
    [Define connections between nodes]

    %% Styling definitions
    [Define custom styling classes]
```

6. Example output:
The following flowchart example demonstrates all node types with custom styling in the output schema:
```mermaid
flowchart TB
	%% Symbol definitions
    A([Start/End]):::terminator
    B[Process]:::process
    C{Decision}:::decision
    D[/Input/Output/]:::inputOutput
    F[(Database)]:::database
	
	%% Syntax definitions
    A --> B
    B --> C
    C -->|Yes| D
    C -->|No| F

    %% Styling definitions
    classDef terminator fill:#f9f,stroke:#333,stroke-width:2px,color:#333,stroke-dasharray:5 5;
    classDef process fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#333;
    classDef decision fill:#e1bee7,stroke:#6a1b9a,stroke-width:2px,color:#333;
    classDef inputOutput fill:#d1edf2,stroke:#0277bd,stroke-width:2px,color:#333;
    classDef database fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333;
```

7. Important: Return ONLY the styled Mermaid.js code without any explanation or code blocks."""

STYLE_PROMPT = """
Apply the style guide to the following Mermaid code. Do not change the labels, only apply proper styling and formatting.
Keep the original flow and structure intact. Return only the Mermaid.js code without any explanations or code blocks
I repeat, do not use CODE BLOCKS.

Code:
{mermaid_code}
"""
