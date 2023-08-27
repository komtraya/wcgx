# WordCloud Generator X-Treme

## G2K:

    - *Words will be printed on black/color*
    - *White color is ignored*
    - *App treats transparency in mask image as white, so it will be ignored*
    - Special characters are supported - depends on font used
    - StopWords are disabled for now
    - *Export Formats: PNG, SVG*

### Roadmap:

- Additional parameter controls
- StopWords
- Check for updates button
- Better UI
- Add additional color export options
- Decrease compiled app size
- Add additional QoL tools:
  - list of characters/symbols that can be used as words to populate the WordCloud
  - single/bulk image resizer

# List of dependencies:

## Python: 3.7.7

## Main Python libraries used:

- [PySide6](https://pypi.org/project/PySide6/) - includes QT Designer (UI)
- [Wordcloud](https://pypi.org/project/wordcloud/)
- [Pillow](https://pypi.org/project/Pillow/)
- [PyInstaller](https://pypi.org/project/pyinstaller/) (compiler)
