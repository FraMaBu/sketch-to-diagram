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

Important: Create actual Mermaid.js flowchart code that can be rendered. Return ONLY the Mermaid.js code without any explanation or markdown formatting."
"""

STYLE_GUIDE = """
# Mermaid Flowchart Guide

## 1. Basic Syntax and Direction

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

2.1 **Oval (Terminator symbol)**  
   - **Description:** Represents the start or end of a process.  
   - **Mermaid code:**  
   ```mermaid
   graph TD;
       A([Start/End])
   ```

2.2 **Rectangle (Process symbol)**  
   - **Description:** Represents a process, operation, or action to be performed.  
   - **Mermaid code:**  
   ```mermaid
   graph TD;
       B[Process]
   ```

2.3 **Diamond (Decision symbol)**  
   - **Description:** Represents a decision point, typically with "Yes" or "No" branches.  
   - **Mermaid code:**  
   ```mermaid
   graph TD;
       C{Decision}
   ```

2.4 **Parallelogram (Input/Output symbol)**  
   - **Description:** Represents an input (e.g., user input) or output (e.g., display result).  
   - **Mermaid code:**  
   ```mermaid
   graph TD;
       D[/Input/Output/]
   ```

2.5 **Arrow (Connector/Flowline)**  
   - **Description:** Represents the flow of the process from one step to the next.  
   - **Mermaid code:**  
   ```mermaid
   graph TD;
       E1 --> E2
   ```

2.6 **Cylinder (Database symbol)**  
   - **Description:** Represents a database or stored data.  
   - **Mermaid code:**  
   ```mermaid
   graph TD;
       F[(Database)]
   ```

## 3. Links Between Nodes

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

## 5. Styling

Define and apply custom classes for each node type to ensure consistent styling:
```mermaid
flowchart LR
    A:::process --> B
    classDef process fill:#f96,stroke:#333,stroke-width:4px
```

## 6. Advanced Features

6.1 Markdown strings
Format text with markdown:
```mermaid
flowchart LR
    A["`This is **bold** text`"] --> B["`This is *italic* text`"]
```

6.2 Comments
Add comments to explain complex parts:
```mermaid
flowchart LR
    A --> B
    %% This is a comment
    B --> C
```

## 7. Configuration

Customize themes and layouts for diagrams:
```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "linear",
    "diagramPadding": 20,
    "rankSpacing": 50,
    "nodeSpacing": 60
  }
}}%%
flowchart LR
    A[Input] --> B[Process] --> C[Output]
```

## 8. Best Practices

1. **Meaningful IDs:** Use clear, descriptive IDs for nodes.
2. **Subgraphs:** Use subgraphs only if they enhance the flowchart's visual structure.
3. **Consistent Styling:** Apply consistent styling for the different node types.
4. **Node Shapes:** Differentiate node types (e.g., processes, decisions) with appropriate shapes.
5. **Flow Direction:** Keep a uniform direction (e.g., left-to-right or top-to-bottom).
6. **Comments:** Add comments for clarity in complex diagrams.

Create actual Mermaid.js flowchart code that can be rendered. Return ONLY the styled Mermaid.js code without any explanation or markdown formatting.
"""
