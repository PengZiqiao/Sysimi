---
name: markitdown
description: Converts various files and office documents to Markdown for use with LLMs and text analysis pipelines. Supports PDF, Word, Excel, PowerPoint, images, audio, HTML, and more.
allowed-tools: Bash(markitdown:*)
---

# Document Conversion with markitdown

## Quick start

```bash
# Convert a PDF file to Markdown
markitdown document.pdf > document.md

# Convert a Word document to Markdown with output file specified
markitdown document.docx -o document.md

# Pipe content for conversion
cat document.pdf | markitdown > output.md
```


## Commands

### Basic Usage

```bash
# Convert file to Markdown and output to stdout
markitdown input-file.pdf

# Convert file to Markdown with specified output file
markitdown input-file.pdf -o output.md

# Pipe content for conversion
cat input-file.pdf | markitdown

# List installed plugins
markitdown --list-plugins

# Enable plugins for conversion
markitdown --use-plugins input-file.pdf
```

### Azure Document Intelligence

```bash
# Use Azure Document Intelligence for conversion
markitdown input-file.pdf -o output.md -d -e "<document_intelligence_endpoint>"
```

## Supported Formats

- **PDF**
- **Microsoft Office**: Word (docx), Excel (xlsx, xls), PowerPoint (pptx)
- **Images**: EXIF metadata and OCR
- **Audio**: EXIF metadata and speech transcription
- **HTML**
- **Text-based formats**: CSV, JSON, XML
- **ZIP files**: Iterates over contents
- **YouTube URLs**
- **EPubs**
- **And more!**


## Python API

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)  # Set to True to enable plugins

# Convert a file
with open('document.pdf', 'rb') as f:
    markdown_content = md.convert_stream(f)
    print(markdown_content)

# Convert with Azure Document Intelligence
md = MarkItDown(use_azure_document_intelligence=True, azure_document_intelligence_endpoint="<endpoint>")
with open('document.pdf', 'rb') as f:
    markdown_content = md.convert_stream(f)
```

## Example: Convert PDF to Markdown

```bash
# Convert PDF to Markdown
markitdown report.pdf -o report.md

# View the converted Markdown
cat report.md
```

## Example: Convert Office Documents

```bash
# Convert Word document
markitdown document.docx -o document.md

# Convert PowerPoint presentation
markitdown presentation.pptx -o presentation.md

# Convert Excel spreadsheet
markitdown spreadsheet.xlsx -o spreadsheet.md
```

## Example: Convert Image with OCR

```bash
# Install markitdown with all dependencies
pip install 'markitdown[all]'

# Convert image with OCR
markitdown image.jpg -o image.md
```

## Example: Convert YouTube Video Transcription

```bash
# Convert YouTube video transcription
markitdown "https://www.youtube.com/watch?v=example" -o transcription.md
```

## Plugins

MarkItDown supports 3rd-party plugins. Plugins are disabled by default:

```bash
# List installed plugins
markitdown --list-plugins

# Enable plugins for conversion
markitdown --use-plugins input-file.pdf
```

To find available plugins, search GitHub for the hashtag #markitdown-plugin.


## Use Cases

- **LLM Input**: Convert documents to Markdown for better LLM processing
- **Text Analysis**: Prepare documents for text analysis pipelines
- **Content Extraction**: Extract structured content from various document formats
- **Document Processing**: Batch convert documents to a consistent format
- **Knowledge Base**: Create Markdown versions of documents for knowledge bases

## Benefits

- **Preserves Structure**: Maintains important document structure as Markdown
- **LLM-Friendly**: Optimized for use with large language models
- **Token Efficient**: Markdown conventions are highly token-efficient
- **Versatile**: Supports a wide range of file formats
- **Extensible**: Plugin architecture for additional functionality