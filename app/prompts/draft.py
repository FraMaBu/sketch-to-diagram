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

## Output

1. Schema:
Return your response as a JSON object with this structure:
{
    "chart_type": A Mermaid chart type based on the structure identified in the image,
    "reason": A one-sentence explanation of why this chart type best fits the image content,
    "code": The complete Mermaid.js diagram code
}

2. Example:
{
    "chart_type": "flowchart",
    "reason": "The image shows sequential steps connected by arrows indicating a process flow",
    "code": "flowchart TB\\n  A[Start] --> B[Process]\\n  B --> C[End]"
}

## Notes

If the screenshot includes a combination of text and graphics, focus on text and logical flow inferred from the visuals.
In cases where the screenshot cannot be processed directly, ask the user to describe its content or share its structure verbally.

## Important

Return ONLY the JSON response without any explanation or code blocks.
"""
