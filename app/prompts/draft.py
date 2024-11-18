"""Draft generation prompt for converting images to Mermaid.js diagrams."""

DRAFT_PROMPT = """
Generate a mermaid chart based on the textual or structural information in the image.
If the image is unclear or includes graphical content that cannot be directly transcribed, offer logical interpretations to recreate the intended chart.

## Steps

1. Understand Content:
Review the screenshot provided by the user.
Understand textual or visual elements (e.g., labels, connections, flow) from the image.
If the content is ambiguous, provide logical interpretations while maintaining the user's intent.

2. Chart Type Identification:
Based on the screenshot, determine the most appropriate Mermaid.js chart type:
- Flowchart: For processes or workflows.
- Mindmap: For brainstorming or planning.
- Other types, as inferred from the screenshot.

3. Construct the Chart:
- Use Mermaid.js syntax to define nodes, edges, and labels based on extracted content.
- Maintain clarity and logical structure.
- Fill gaps or ambiguities based on the context provided.

4. Validate the Chart:
- Ensure the output aligns with Mermaid.js conventions.
- Test readability and coherence in the chart's flow or structure.

## Output Format

Present the chart in valid Mermaid.js syntax.
Example:
[Chart type]
  A[Extract text] --> B[Determine chart type]
  B --> C[Construct chart]
  C --> D[Validate and format]
```

## Notes

If the screenshot includes a combination of text and graphics, focus on text and logical flow inferred from the visuals.
In cases where the screenshot cannot be processed directly, ask the user to describe its content or share its structure verbally.

## Important
Create actual Mermaid.js flowchart code that can be rendered. Return ONLY the Mermaid.js code without any explanation or code blocks.
I repeat, DO NOT USE CODE BLOCKS.
"""
