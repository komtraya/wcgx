**0.7.2**

- Added a few extra presets to Random Colors (Color Presets)
- When clicking on Update Settings Profile button, an extra step is required for the selected profile to be updated
- On app start, the first Settings Profile from the list will be applied
- Some UI touch-ups


**0.7.1**

- Implemented "Profile Fonts" - fonts added to this list can be stored in a Settings profile
- New button to update the selected Settings profile with the current settings
- Upon new Settings/Text profile creation, the created profile's name will be selected in the dropdown list


**0.7.0**

- Implemented StopWords
- StopWords are now included in the Settings profile
- Profile name input-box is now cleared after storing a profile, instead of keeping the last typed profile name
- Updated exported WordCloud image file-name structure to font_name--profile_name
- New button: Download some fonts - opens a new window, where you can download fonts
- Eliminated redundant tooltips
- Some UI touch-ups


**0.5.9**

- You can no longer store blank text in wcgx.db
- When storing text under an existing profile name, the profile is correctly updated with the new text
- WordCloud destination path is now added to the list of Settings that are stored in wcgx.db
- Some UI touch-ups


**0.5.7**

- The "URL" Character Filtering option in the "Char. Inc." tab now supports special characters as a single word
- Implemented wcgx.db - facilitates settings and text storage
    - wcgx.db will be created automatically on app start (if not yet created)


**0.5.6**

- You can now export Font Awesome masks to file (SVG or PNG)
- When modifying the Export Scale slider, the exact size of the exported wordcloud image will be reflected
- Tooltips for Unicode Emojis - name of selected emoji
- You can now filter Unicode Emojis based on name
- Minor UI adjustments


**0.5.5**

- Font Awesome icons can now be set as mask
- Fonts filter
- Additional gradient options


**0.5.2**

- **NEW**: Random state parameter
- **NEW**: Color Preset - "Gradient"
- **FIX**: System/user fonts should now load correctly
- **QoL**: Tooltip (search terms) for Font Awesome icons


**0.5.0**

- **NEW**: Filter for Font Awesome icons
- **Better**: Character inclusion options
- **UI**: 
    - Restyled sliders, checkboxes, parameters text
    - Placed scale slider under mask thumbnail
    - Bigger emojis/icons
    - Better spacing between FontAwesome icons


**0.4.5**

- NEW: You can now use .svg images as mask
- NEW: Font Awesome 6.4.2 solid icons
- NEW: Included a set of fonts with Emoji/Icon support
- Fix: Aspect ratio of selected mask thumbnail
- Fix: Default fonts folder should now be correct on all Windows editions


**0.4.4**

- NEW: Added Unicode Emojis
- UI Redesign
- Minor refactoring


**0.4.3**

- NEW: Generated PNG file now opens automatically upon creation (in default app)
- NEW: Added "Delete" and "Stash" buttons for newly created file handling
- NEW: Added presets for Min and Max font size sliders
- NEW: Renamed "Numbers" tab/list item to "Character Inclusions":
    - Added more Character Filtering options in "Character Inclusions"
    - You can now set any special character to be treated as a word (depends on font)
    - You can now disable/enable connected punctuations (was enabled)
- Deleted "seismic" from Color Presets list.
- UI: Fixed button pressed effect
- UI: Changed text color of buttons and color presets dropdown
- Minor refactoring


**0.4.2**

- Transparency of mask image will now be treated as white and ignored (depends on image)
- UI: Added button pressed feedback effect (all buttons)


**0.4.1**

- Exporting in "BOTH" formats fixed
- Corrected select mask and destination buttons' text colors
- Minor code clean-up


**Early releases**

- Eliminated input fields for mask and destination
- Changed location of "Generated Text" field - this enables more space for fonts list box
- Added red border around elements that require user input before being able to generate the word cloud
- Experimenting with some color changes
- Updated code to match the changes
- Updated Font display and selection options
- You can now specify a custom folder path for fonts