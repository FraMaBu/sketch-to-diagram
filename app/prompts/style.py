"""Style guide for Mermaid.js diagram formatting."""

FLOWCHART_STYLE = """
Apply the following styling rules to the Mermaid.js diagram while preserving the original structure and labels:

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

7. Important: Return ONLY the styled Mermaid.js code without any explanation or code blocks.
"""


MINDMAP_STYLE = """
Apply the following styling rules to the Mermaid.js mindmap diagram while preserving the original structure and labels:

1. Determine node types and symbols:
   - Root nodes: ((text))
   - Main branch nodes: [text]
   - Sub-branch nodes: {{text}}
   - Leaf nodes: )text(

2. Respect the depth of the hierarchy:
   - Do not add additional depth, nodes, or node types if they are not present in the draft.
   - If a level of the hierarchy (e.g., sub-branch or leaf) is missing, skip its representation entirely.

3. Node hierarchy:
   - Use indentation to define parent-child relationships.
   - Root connects to main branches.
   - Main branches connect to sub-branches.
   - Sub-branches connect to leaves.

4. Output example:
The following mindmap example demonstrates the use of symbols for node types:
mindmap
  root((Central Concept))
    [Main Branch 1]
      {{Subtopic 1}}
        )Leaf Node 1(
        )Leaf Node 2(
      {{Subtopic 2}}
    [Main Branch 2]
      {{Subtopic 3}}
        )Leaf Node 3(
      {{Subtopic 4}}
      {{Subtopic 5}}

5. Important: Ensure no extra nodes are added if they are not present in the original draft. Return ONLY the styled Mermaid.js code without any explanation or code blocks.
"""


STYLE_GUIDE = f"""
# Style Guide

## Mindmap Style
{MINDMAP_STYLE}

## Flowchart Style
{FLOWCHART_STYLE}
"""

STYLE_PROMPT = """
Apply the style guide to the following Mermaid code. Do not change the labels, only apply proper styling and formatting.
Keep the original flow and structure intact. Return only the Mermaid.js code without any explanations or code blocks
I repeat, do not use CODE BLOCKS.

Code:
{mermaid_code}
"""
