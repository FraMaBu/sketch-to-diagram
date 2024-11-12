DRAFT_PROMPT = """
Generate a mermaid chart based on the textual or structural information in the image. If the image is unclear or includes graphical content that cannot be directly transcribed, offer logical interpretations to recreate the intended chart.

## Steps

1. Understand Content:
Review the screenshot provided by the user.
Understand textual or visual elements (e.g., labels, connections, flow) from the image.
If the content is ambiguous, provide logical interpretations while maintaining the user's intent.

2. Chart Type Identification:
Based on the screenshot, determine the most appropriate Mermaid.js chart type:
- Flowchart: For processes or workflows.
- Sequence Diagram: For time-sequenced events.
- Class Diagram: For relationships or hierarchies.
- Gant chart: For project timelines.
Other types, as inferred from the screenshot.

3. Construct the Chart:
Use Mermaid.js syntax to define nodes, edges, and labels based on extracted content.
Maintain clarity and logical structure.
Fill gaps or ambiguities based on the context provided.

4. Validate the Chart:
Ensure the output aligns with Mermaid.js conventions.
Test readability and coherence in the chart's flow or structure.

## Output Format

Present the chart in valid Mermaid.js syntax.
Example:
```mermaid
graph TD
  A[Extract Text] --> B[Determine Chart Type]
  B --> C[Construct Chart]
  C --> D[Validate and Format]
```

## Notes

If the screenshot includes a combination of text and graphics, focus on text and logical flow inferred from the visuals.
In cases where the screenshot cannot be processed directly, ask the user to describe its content or share its structure verbally.

Important: Create actual Mermaid.js flowchart code that can be rendered. Return ONLY the Mermaid.js code without any explanation or code blocks. I repeat, DO NOT USE CODE BLOCKS."
"""

STYLE_GUIDE = """
# Mermaid flowchart guide

## 1. Basic syntax and direction

- Start with `flowchart` or `graph`.
- Define direction: 
  - **TB (Top to Bottom)**  
  - **TD (Top-Down)**  
  - **BT (Bottom to Top)**  
  - **RL (Right to Left)**  
  - **LR (Left to Right)**

Example:
```mermaid
flowchart LR
    A --> B
```

## 2. Node Shapes

The following sections describe each node type, along with the **custom style definitions** that should be applied in flowcharts for better visualization and differentiation.

1. **Oval (Terminator Symbol)**  
- **Description:** Represents the start or end of a process.  
- **Style Definition:** Use the `terminator` class.  
- **Example with Style Applied:**
```mermaid
flowchart LR
    A([Start/End]):::terminator
    classDef terminator fill:#f9f,stroke:#333,stroke-width:2px,color:#333,stroke-dasharray:5 5;
```

2. **Rectangle (Process Symbol)**  
- **Description:** Represents a process, operation, or action to be performed.  
- **Style Definition:** Use the `process` class.  
- **Example with Style Applied:**
```mermaid
flowchart LR
    B[Process]:::process
    classDef process fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#333;
```

3. **Diamond (Decision Symbol)**  
- **Description:** Represents a decision point, typically with "Yes" or "No" branches.  
- **Style Definition:** Use the `decision` class.  
- **Example with Style Applied:**
```mermaid
flowchart LR
    C{Decision}:::decision
    classDef decision fill:#e1bee7,stroke:#6a1b9a,stroke-width:2px,color:#333;
```

4. **Parallelogram (Input/Output Symbol)**  
- **Description:** Represents an input (e.g., user input) or output (e.g., display result).  
- **Style Definition:** Use the `inputOutput` class.  
- **Example with Style Applied:**
```mermaid
flowchart LR
    D[/Input/Output/]:::inputOutput
    classDef inputOutput fill:#d1edf2,stroke:#0277bd,stroke-width:2px,color:#333;
```
 
5. **Arrow (Connector/Flowline)**  
- **Description:** Represents the flow of the process from one step to the next.  
- **Style Definition:** Links can be styled using `linkStyle`.  
- **Example with Style Applied:**
```mermaid
flowchart LR
    E1[Start] --> E2[End]
    linkStyle 0 stroke:#ff3,stroke-width:4px;
```

6. **Cylinder (Database Symbol)**  
- **Description:** Represents a database or stored data.  
- **Style Definition:** Use the `database` class.  
- **Example with Style Applied:**
```mermaid
flowchart LR
    F[(Database)]:::database
    classDef database fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333;
```

## 3. Links between nodes

- **Arrow head:** `A --> B`
- **Open link:** `A --- B`
- **Text on links:** `A -- This is the text! --- B` or `A---|This is the text|B`
- **Dotted link:** `A -.-> B`
- **Thick link:** `A ==> B`

## 4. Subgraphs (Optional)

Use subgraphs to group related nodes **only if it improves clarity and visual design**.

Example:
```mermaid
flowchart TB
    subgraph SubGraph1
        a1-->a2
    end
    subgraph SubGraph2
        b1-->b2
    end
    SubGraph1 --> SubGraph2
```

## 5. Advanced features

1.  Markdown Strings
Format text with markdown:
```mermaid
flowchart LR
    A["`This is **bold** text`"] --> B["`This is *italic* text`"]
```

2. Comments
Add comments to explain complex parts:
```mermaid
flowchart LR
    A --> B
    %% This is a comment
    B --> C
```

## 6. Example flowchart with styles

The following example demonstrates all node types combined into a meaningful flowchart with custom styles applied:

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

## 7. Best Practices

1. **Meaningful IDs:** Use clear, descriptive IDs for nodes.
2. **Subgraphs:** Use subgraphs only if they enhance the flowchart's visual structure.
3. **Consistent Styling:** Apply consistent styles for readability.
4. **Node Shapes:** Differentiate node types (e.g., processes, decisions) with appropriate shapes.
5. **Flow Direction:** Keep a uniform direction (e.g., left-to-right or top-to-bottom).
6. **Comments:** Add comments for clarity in complex diagrams.

IMPORTANT: Create actual Mermaid.js flowchart code that can be rendered. Return ONLY the Mermaid.js code without any explanation or code blocks. I repeat DO NOT USE CODEBLOCKS
"""
