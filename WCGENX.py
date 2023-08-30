import numpy as np
import random
import sys
import os
import json
from wordcloud import WordCloud
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6 import QtWidgets as widget
from PySide6.QtGui import QFont, QFontDatabase, QPixmap, QImage, QPainter
from PySide6.QtWidgets import QFileDialog, QListWidgetItem
from PySide6.QtSvg import QSvgRenderer
from ui.ui import Ui_MainWindow


userPath = os.path.expanduser("~")
system_c = os.getenv("SystemDrive")


##### ----- Resource Fix #####
def resource_path(rel_path):
    """Get absolute path to resource - PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, rel_path)


##### ----- Resource Fix #####

## Read emojis.json for processing ##
emojis_json = resource_path("emojis.json")
# Load the JSON file containing Unicode Emojis metadata
with open(emojis_json, "r", encoding="utf-8") as json_file:
    emoji_data = json.load(json_file)

##### Read fontAwesomeIcons.json for processing #####
fontAwesomeIcons_json = resource_path("fontAwesomeIcons.json")
# Load the JSON file containing FontAwesome icon metadata
with open(fontAwesomeIcons_json, "r", encoding="utf-8") as fontAwesome_icons:
    fontAwesome_data = json.load(fontAwesome_icons)

emoji_fonts_path = resource_path("emojiFonts")
system_fonts_path = os.path.join(system_c, "Windows", "Fonts")


class WCGX(widget.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ## Future color preset implementation(list needs sorting)
        # import matplotlib.cm as cm
        # for palette_names in cm.cmap_d:
        #     self.colormaps_dropdown.addItem(palette_names)
        #     print(palette_names)

        self.parametersButtonGroup.buttonClicked.connect(self.change_tab_based_on_selected_item)
        ##  Emoji handling ##
        self.populateEmojiList()
        self.unicode_Emojis_btn.clicked.connect(self.unicodeEmojiList_fnc)
        self.font_Awesome_Icons_btn.clicked.connect(self.fontAwesomeIconsList_fnc)
        self.emoji_list.itemClicked.connect(self.insertEmojiOnClick)
        self.emoji_filter_list.currentTextChanged.connect(self.populateEmojiList)
        ## Modifications/data-setup for the start of the app
        # Make sure text input is not empty
        self.word_input.textChanged.connect(self.text_input_Changed)
        self.destination_path = None
        self.mask_path = None
        self.mask_image_thumbnail.setVisible(False)
        self.mask_dimensions_label.setText("")
        ### scan fonts set by default (windows path) and populate the list
        self.fonts_directory = system_fonts_path  # default font directory on start of the app
        self.scan_fonts(self.fonts_directory)  # This scans the default directory for fonts
        self.font_list.currentItemChanged.connect(self.apply_selected_font)  # This enables clicks, as well as keyboard arrows to browse through the list

        self.custom_font_directory_selection.clicked.connect(self.select_custom_fonts_folder)
        self.load_emoji_fonts_btn.clicked.connect(self.load_emoji_fonts_fnc)
        self.load_system_fonts_btn.clicked.connect(self.load_system_fonts_fnc)

        ## HIDE WORDCLOUD BUTTON BY DEFAULT ##
        # self.generate_wordcloud_button.setVisible(False)
        # self.export_as_frame.setVisible(False)
        # Open destination folder if it's selected
        self.enable_WordCloud_Generator_Button()
        self.open_destination_folder.setVisible(False)
        self.open_destination_folder.clicked.connect(self.open_destination_folder_function)

        # Hide random colors frame
        self.RandomColorFrame.setVisible(False)

        # Connect dropdown list to function
        self.colormaps_dropdown.currentTextChanged.connect(self.check_dropdown_selected_item)
        ## Connect Delete and Stash Buttons to functions
        # Stash
        self.stash_last_generated_button.setVisible(False)
        self.stash_last_generated_button.clicked.connect(self.stash_generated_files)
        # Delete
        self.delete_last_generated_button.setVisible(False)
        self.delete_last_generated_button.clicked.connect(self.delete_last_generated)
        ## MASK IMAGE SELECTION
        # Connect the "Select Mask" button's clicked signal to the custom slot
        self.mask_select_button.clicked.connect(self.mask_select_button_clicked)
        # Connect the "Path Changed" signal of the mask_path to the custom slot (Update path)
        ## INFO LABELS UPDATE
        self.update_info_labels()
        self.repeat_checkbox.clicked.connect(self.update_info_labels)
        self.collocations_checkbox.clicked.connect(self.update_info_labels)
        self.include_number_checkbox.clicked.connect(self.update_info_labels)
        self.regxp_any_character_checkbox.clicked.connect(self.update_info_labels)
        self.connected_punctuation_checkbox.clicked.connect(self.update_info_labels)
        ## EXPORT DESTINATION SELECTION
        # Connect the button click to the slot function
        self.select_destination_button.clicked.connect(self.select_destination_button_clicked)

        # ## FONT HANDLING
        # self.font_path = None

        ## Margin.current
        # Connect the slider to the function that updates the label to reflect changes
        self.margin_slider.valueChanged.connect(self.margin_slider_changed)
        # Connect the slider to the function that updates the label to reflect changes
        self.margin_slider_changed(self.margin_slider.value())
        ## Image Scale Slider
        # Connect the slider to the function that updates the label to reflect changes
        self.scale_slider.valueChanged.connect(self.scale_slider_changed)
        # Call the slot initially to update label from start
        self.scale_slider_changed(self.scale_slider.value())
        ## Minimum Font Size Slider
        self.min_font_size_slider.valueChanged.connect(self.min_font_size_slider_changed)
        # Call the slot initially to set the initial value of the label
        self.min_font_size_slider_changed(self.min_font_size_slider.value())

        ## Maximum Font Size Slider
        self.max_font_size_slider.valueChanged.connect(self.max_font_size_slider_changed)
        # Call the slot initially to set the initial value of the label
        self.max_font_size_slider_changed(self.max_font_size_slider.value())

        ## Prefer Horizontal Slider
        # self.prefer_horizontal_slider.setValue(7)
        self.prefer_horizontal_slider.valueChanged.connect(self.prefer_horizontal_slider_changed)
        # Call the slot initially to set the initial value of the label
        self.prefer_horizontal_slider_changed(self.prefer_horizontal_slider.value())

        ## Collocation Thresh Slider

        self.collocations_thresh_slider.valueChanged.connect(self.collocations_thresh_slider_changed)
        # Connect the slider to the function that updates the label to reflect changes from the start
        self.collocations_thresh_slider_changed(self.collocations_thresh_slider.value())
        ## Font Step Slider
        self.font_step_slider.valueChanged.connect(self.font_step_slider_changed)
        # Connect the slider to the function that updates the label to reflect changes from the start
        self.font_step_slider_changed(self.font_step_slider.value())

        ## PRESET BUTTONS FOR RANDOM COLORS - connect to function ##
        self.randomColorsPresetsGroup.buttonClicked.connect(self.random_colors_presets_function)

        ## WordCloud Button ##
        self.generate_wordcloud_button.clicked.connect(self.generate_WordCloud)
        ## Connect font slider presets to function
        self.fontSizePresetsGroup.buttonClicked.connect(self.font_size_slider_presets)

        # # # # # Create WordCloud object and Export Image(s) # # # # #

    def generate_WordCloud(self):
        # @ PARAMETERS
        wordcloud = WordCloud(
            mask=self.mask_image,
            # width=width,
            # height=height,
            regexp=self.custom_regexp(),
            background_color=None,
            scale=self.scale_slider.value(),  # this controls the size of the image - multiplier for original size
            margin=self.margin_slider.value(),
            font_path=self.font_list.currentItem().data(1001),
            repeat=self.repeat_checkbox.isChecked(),
            collocation_threshold=self.collocations_thresh_slider.value(),
            collocations=self.collocations_checkbox.isChecked(),
            mode="RGBA",
            prefer_horizontal=self.prefer_horizontal_slider.value() / 10,
            color_func=self.color_function_conditions(),
            colormap=self.colormap_conditions(),
            max_font_size=self.max_font_size_slider.value(),
            min_font_size=self.min_font_size_slider.value(),
            font_step=self.font_step_slider.value(),
            stopwords=set(),
            min_word_length=0,
            include_numbers=self.include_number_checkbox.isChecked(),
            # random_state=, # Generated WC will be the same color, until random_state int is different
        )
        # @ generate wc
        wordcloud.generate(self.word_input.toPlainText())

        # @ Export Image @ #
        ##PNG
        if self.export_format_options.currentText() == "PNG":
            # Convert the word cloud image to a numpy array
            wordcloud_image = np.array(wordcloud)

            # Create a PIL Image object from the numpy array
            wordcloud_image = Image.fromarray(wordcloud_image)

            # Export the PIL Image object as a PNG image file
            self.output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].png"
            wordcloud_image.save(self.output_image_path)
            os.startfile(self.output_image_path)  # Open file after generating it
        ## SVG
        elif self.export_format_options.currentText() == "SVG":
            # Generate the SVG representation of the word cloud
            svg_code = wordcloud.to_svg()
            # Export the SVG code to a file
            self.output_image_path_1 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].svg"
            with open(f"{self.output_image_path_1}", "w", encoding="utf-8") as f:
                f.write(svg_code)
        ## BOTH
        else:
            # Generate the SVG representation of the word cloud
            svg_code = wordcloud.to_svg()
            # Export the SVG code to a file
            self.output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].svg"
            with open(f"{self.output_image_path}", "w", encoding="utf-8") as f:
                f.write(svg_code)

            # Convert the word cloud image to a numpy array
            wordcloud_image = np.array(wordcloud)
            # Create a PIL Image object from the numpy array
            wordcloud_image = Image.fromarray(wordcloud_image)

            # Export the PIL Image object as a PNG image file
            self.output_image_path_2 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].png"
            wordcloud_image.save(self.output_image_path_2)
            os.startfile(self.output_image_path_2)  # Open the PNG file after generating both formats
        self.stash_last_generated_button.setVisible(True)  # Display Stash button
        self.delete_last_generated_button.setVisible(True)  # Delete Stash button

    ### !!!!! FUNCTIONS !!!!! ###
    ## FONT HANDLING ##

    def mask_select_button_clicked(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Mask Image", "", "Image Files (*.png;*.svg;*.jpg;*.jpeg)", options=options)
        if file_name:
            self.mask_path = file_name
            self.enable_WordCloud_Generator_Button()

        if self.mask_path:
            if self.mask_path.endswith(".png".lower()) or self.mask_path.endswith(".jpg".lower()) or self.mask_path.endswith(".jpeg".lower()):
                # Open Mask Image
                self.mask_image = np.array(Image.open((self.mask_path)))
                try:
                    self.mask_image[(self.mask_image[..., 3] == 0)] = [255, 255, 255, 255]  # Replace transparent with white
                except:
                    self.mask_image = np.array(Image.open((self.mask_path)))
                self.update_image_dimensions()
                self.mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
            elif self.mask_path.endswith(".svg".lower()):
                # Create a QSvgRenderer for the SVG file
                svg_filename = self.mask_path
                svg_renderer = QSvgRenderer(svg_filename)

                # Get the dimensions of the SVG
                svg_size = svg_renderer.defaultSize()

                # Create a QImage with an appropriate format (ARGB32 is a common choice)
                mask_test = QImage(svg_size, QImage.Format_ARGB32)
                mask_test.fill(0)  # Fill with transparent (0 alpha)

                # Create a QPainter to render the SVG onto the QImage
                painter = QPainter(mask_test)

                # Render the SVG onto the QImage
                svg_renderer.render(painter)

                # Clean up
                painter.end()
                # Convert QImage to Pillow Image
                pil_image = Image.fromqpixmap(mask_test)

                # Transform Pillow Image to NumPy array
                mask_array = np.array(pil_image)
                try:
                    mask_array[(mask_array[..., 3] == 0)] = [255, 255, 255, 255]  # Replace transparent with white
                    self.mask_image = mask_array
                except:
                    self.mask_image = mask_array
                self.update_image_dimensions()
                self.mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
        else:
            self.update_image_dimensions()
            self.mask_select_button.setStyleSheet(
                """
            QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
            QPushButton{border:2px solid red; background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
            )

    # @ CHECK FIELDS FOR CHANGES @ #

    # Check text input field for changes
    def text_input_Changed(self):
        self.enable_WordCloud_Generator_Button()

    def select_destination_button_clicked(self):
        options = QFileDialog.Options()
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if selected_folder:
            self.destination_path = selected_folder
            self.enable_WordCloud_Generator_Button()
        else:
            self.enable_WordCloud_Generator_Button()
        # If there was a destination set, but the second time the selection was cancelled, make sure the button does not disappear
        if not self.destination_path:
            self.open_destination_folder.setVisible(False)
            self.select_destination_button.setStyleSheet(
                """
            QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
            QPushButton{border:2px solid red; background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
            )
        else:
            self.select_destination_button.setStyleSheet(
                """
            QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
            QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA ;border-radius:10px;}"""
            )
            self.open_destination_folder.setVisible(True)

    def open_destination_folder_function(self):
        os.startfile(rf"{self.destination_path}")

    def margin_slider_changed(self, value: int):
        # Update corresponding label
        self.label_margin_slider.setText(f"{value}")
        self.margin_info_label.setText(f"{value}")

    def scale_slider_changed(self, value: int):
        # Update corresponding label
        self.label_scale_slider.setText(f"{value}")
        self.scale_multiplier_info_label.setText(f"{value}x")

    def prefer_horizontal_slider_changed(self, value: int):
        # Update the QLabel's text with the current value of the slider
        if value == 0:
            self.label_text_orientation_slider.setText("0")
            self.prefer_horizontal_info_label.setText("0")
        elif value == 10:
            self.label_text_orientation_slider.setText("1")
            self.prefer_horizontal_info_label.setText("1")
        else:
            self.label_text_orientation_slider.setText(f"{(value)/10}")
            self.prefer_horizontal_info_label.setText(f"{(value)/10}")

    def min_font_size_slider_changed(self, value: int):
        # Update the QLabel's text with the current value of the slider
        self.label_min_font_size_slider.setText(f"{(value)}")
        self.min_font_size_info_label.setText(f"{(value)}")

    def max_font_size_slider_changed(self, value: int):
        # Update the QLabel's text with the current value of the slider
        self.label_max_font_size_slider.setText(f"{(value)}")
        self.max_font_size_info_label.setText(f"{(value)}")

    def collocations_thresh_slider_changed(self, value: int):
        self.collocation_thresh_slider_label.setText(f"{(value)}")
        self.collocations_thresh_info_label.setText(f"{value}")

    def font_step_slider_changed(self, value: int):
        self.font_step_indicator_label.setText(f"{(value)}")
        self.fontstep_info_label.setText(f"{(value)}")

    ## IMAGE DIMENSIONS INFO
    def update_image_dimensions(self):
        # global image_state
        global width
        global height
        if self.mask_path:
            if self.mask_path.endswith(".png".lower()) or self.mask_path.endswith(".jpg".lower()) or self.mask_path.endswith(".jpeg".lower()):
                try:
                    with Image.open(self.mask_path) as img:
                        width, height = img.size
                        self.mask_dimensions_label.setText(f"Mask Dimensions: {width}x{height}")
                        self.mask_dimensions_label.setStyleSheet("color: green;")
                        resizeMax = 200, 10000  # Height will be calculated based on original width, so that aspect ratio is maintained
                        img.thumbnail(resizeMax, resample=Image.Resampling.LANCZOS)
                        resized_thumb = ImageQt(img)
                        pixmap = QPixmap.fromImage(resized_thumb)
                        self.mask_image_thumbnail.setPixmap(pixmap)
                    self.mask_image_thumbnail.setVisible(True)
                except:
                    self.mask_dimensions_label.setText("Incorrect image path!")
                    self.mask_dimensions_label.setStyleSheet("color: red;")
                    self.export_as_frame.setVisible(False)
                    self.mask_image_thumbnail.setVisible(False)
            elif self.mask_path.endswith(".svg".lower()):
                try:
                    # Create a QSvgRenderer for the SVG file
                    svg_filename = self.mask_path
                    svg_renderer = QSvgRenderer(svg_filename)

                    # Get the dimensions of the SVG
                    svg_size = svg_renderer.defaultSize()
                    width = str(svg_size.width())
                    height = str(svg_size.height())
                    self.mask_dimensions_label.setText(f"Mask Dimensions: {width}x{height}")
                    self.mask_dimensions_label.setStyleSheet("color: green;")
                    # # Create a QImage with an appropriate format (ARGB32 is a common choice)
                    mask_test = QImage(svg_size, QImage.Format_ARGB32)
                    mask_test.fill(0)  # Fill with transparent (0 alpha)
                    # Create a QPainter to render the SVG onto the QImage
                    painter = QPainter(mask_test)
                    # Render the SVG onto the QImage
                    svg_renderer.render(painter)
                    # Clean up
                    painter.end()
                    # Convert QImage to Pillow Image
                    pil_image = Image.fromqpixmap(mask_test)
                    resizeMax = 200, 10000  # Height will be calculated based on original width, so that aspect ratio is maintained
                    pil_image.thumbnail(resizeMax, resample=Image.Resampling.LANCZOS)
                    resized_thumb = ImageQt(pil_image)
                    pixmap = QPixmap.fromImage(resized_thumb)

                    self.mask_image_thumbnail.setPixmap(pixmap)
                    self.mask_image_thumbnail.setVisible(True)
                except:
                    self.mask_dimensions_label.setText("Incorrect image path!")
                    self.mask_dimensions_label.setStyleSheet("color: red;")
                    self.export_as_frame.setVisible(False)
                    self.mask_image_thumbnail.setVisible(False)

        if not self.mask_path:
            self.mask_dimensions_label.setText(f"")
            # mask image
            self.mask_image_thumbnail.setText(f"")
            self.mask_image_thumbnail.setVisible(False)

    ## ENABLE WORDCLOUD BUTTON##
    def enable_WordCloud_Generator_Button(self):
        if self.mask_path and self.destination_path and self.word_input.toPlainText() != "":
            self.WC_GeneratorFrame.setVisible(True)
        else:
            self.WC_GeneratorFrame.setVisible(False)

    def change_color(self, color):
        # Set the background color to red when the button is clicked
        self.name_here.setStyleSheet(f"color: {color};")

    ## SELECT FONT and FONT HANDLING
    def apply_selected_font(self, item):
        try:
            font_path = item.data(1001)
            font_id = QFontDatabase.addApplicationFont(font_path)
            font_families = QFontDatabase.applicationFontFamilies(font_id)

            if font_families:
                selected_font = QFont(font_families[0], 15)  # Use the first font family
                self.word_input.setFont(selected_font)

        except:
            pass

    # Scan font firectory and populate list with font names
    def scan_fonts(self, fontDirectory):
        self.font_list.clear()
        font_files = self.get_font_files(fontDirectory)

        for font_path in font_files:
            try:
                font_name = os.path.basename(font_path)
                font_name_display = font_name.split(".")[0].capitalize()
                item = QListWidgetItem(font_name_display)
                item.setData(1001, font_path)  # Using an arbitrary ID (1001) to store font path
                self.font_list.addItem(item)  # - populate the list with fonts
                self.font_list.setCurrentItem(self.font_list.item(0))  # Automatically select the first item
            except:
                pass
        # Disable the Generate WordCloud button if the selected path contains no font files
        if self.font_list.count() == 0:
            self.generate_wordcloud_button.setEnabled(False)
        else:
            self.generate_wordcloud_button.setEnabled(True)

    # Allow users to specify custom font directory (using the "Change Fonts Folder"(custom_fonts_directory_selection) button)
    def select_custom_fonts_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        # initial_directory = rf"{userPath}\AppData\Local\Microsoft\Windows\Fonts"
        initial_directory = system_fonts_path
        selected_directory = QFileDialog.getExistingDirectory(self, "Select Fonts Directory", initial_directory, options=options)

        if selected_directory:
            self.fonts_directory = selected_directory
            self.font_list.clear()
            self.scan_fonts(self.fonts_directory)

    # Scan a folder for font files
    def get_font_files(self, directory):
        font_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith((".ttf", ".otf")):
                    font_files.append(os.path.join(root, file))
        return font_files

    def load_emoji_fonts_fnc(self):
        self.scan_fonts(emoji_fonts_path)

    def load_system_fonts_fnc(self):
        self.scan_fonts(system_fonts_path)

    ## RANDOM COLOR PRESETS FUNCTIONS ##
    def random_colors_presets_function(self, button):
        if button == self.rcp_bright:
            self.red_max.setValue(255)
            self.green_max.setValue(255)
            self.blue_max.setValue(255)
            self.red_min.setValue(175)
            self.green_min.setValue(175)
            self.blue_min.setValue(175)
        if button == self.rcp_gray:
            self.red_max.setValue(125)
            self.green_max.setValue(125)
            self.blue_max.setValue(125)
            self.red_min.setValue(125)
            self.green_min.setValue(125)
            self.blue_min.setValue(125)

        if button == self.rcp_dark:
            self.red_max.setValue(150)
            self.green_max.setValue(150)
            self.blue_max.setValue(150)
            self.red_min.setValue(50)
            self.green_min.setValue(50)
            self.blue_min.setValue(50)
        if button == self.rcp_reset:
            self.red_max.setValue(255)
            self.green_max.setValue(255)
            self.blue_max.setValue(255)
            self.red_min.setValue(20)
            self.green_min.setValue(20)
            self.blue_min.setValue(20)
        if button == self.rcp_maximize_red:
            self.red_max.setValue(255)
            self.red_min.setValue(255)
        if button == self.rcp_minimize_red:
            self.red_max.setValue(0)
            self.red_min.setValue(0)
        if button == self.rcp_maximize_green:
            self.green_max.setValue(255)
            self.green_min.setValue(255)
        if button == self.rcp_minimize_green:
            self.green_max.setValue(0)
            self.green_min.setValue(0)
        if button == self.rcp_maximize_blue:
            self.blue_max.setValue(255)
            self.blue_min.setValue(255)
        if button == self.rcp_minimize_blue:
            self.blue_max.setValue(0)
            self.blue_min.setValue(0)

    ## ColorMap and Color Function Conditions ##
    def colormap_conditions(self):
        if self.colormaps_dropdown.currentText() == "Default":
            self.colormap = "gist_ncar"
            self.color_function = None
            return self.colormap
        elif self.colormaps_dropdown.currentText() != "Default" and self.colormaps_dropdown.currentText() != "Random Colors":
            self.colormap = self.colormaps_dropdown.currentText()
            self.color_function = None
            return self.colormap
        elif self.colormaps_dropdown.currentText() == "Random Colors":
            self.colormap = None
            self.color_function = self.random_color_func
            return self.colormap

    def color_function_conditions(self):
        if self.colormaps_dropdown.currentText() == "Default":
            self.colormap = "gist_ncar"
            self.color_function = None
            return self.color_function
        elif self.colormaps_dropdown.currentText() != "Default" and self.colormaps_dropdown.currentText() != "Random Colors":
            self.colormap = self.colormaps_dropdown.currentText()
            self.color_function = None
            return self.color_function
        elif self.colormaps_dropdown.currentText() == "Random Colors":
            self.colormap = None
            self.color_function = self.random_color_func
            return self.color_function

    def check_dropdown_selected_item(self):
        if self.colormaps_dropdown.currentText() == "Random Colors":
            self.RandomColorFrame.setVisible(True)
        else:
            self.RandomColorFrame.setVisible(False)

    def random_color_func(self, *args, **kwargs):
        # Generate a random color for each trigram
        r, g, b = (
            random.randint(self.red_min.value(), self.red_max.value()),
            random.randint(self.green_min.value(), self.green_max.value()),
            random.randint(self.blue_min.value(), self.blue_max.value()),
        )
        return f"rgb({r}, {g}, {b})"

    def change_tab_based_on_selected_item(self, button):
        if button == self.scaleSettings_btn:
            self.parameters_window.setCurrentIndex(5)
        elif button == self.collocationSettings_btn or button == self.collocationSettings_btn2:
            self.parameters_window.setCurrentIndex(7)
        elif button == self.fontSizeSettings_btn or button == self.fontSizeSettings_btn2:
            self.parameters_window.setCurrentIndex(1)
        elif button == self.repeatWords_btn:
            self.parameters_window.setCurrentIndex(0)
        elif button == self.textOrientationSettings_btn:
            self.parameters_window.setCurrentIndex(4)
        elif button == self.charInclusion_btn:
            self.parameters_window.setCurrentIndex(8)
        elif button == self.marginSettings_btn:
            self.parameters_window.setCurrentIndex(3)
        elif button == self.fontStepSettings_btn:
            self.parameters_window.setCurrentIndex(2)

    def update_info_labels(self):
        self.repeat_info_label.setText(f"{self.repeat_checkbox.isChecked()}")
        self.collocations_info_label.setText(f"{self.collocations_checkbox.isChecked()}")
        if self.regxp_any_character_checkbox.isChecked() or self.include_number_checkbox.isChecked():
            self.include_numbers_info_label.setText(f"True")
        else:
            self.include_numbers_info_label.setText(f"False")

    ## GENERATED FILE HANDLING FUNCTIONS ##
    # Generate a random string anf place it before a file name's extension
    def random_string_generator(self, filename, length=5):
        character_set = "abcdefghkmnopqrstuwxz01234578"  # set of characters to use for generating random string
        name, ext = os.path.splitext(rf"{filename}")
        random_string = "".join(random.choice(character_set) for _ in range(length))
        new_filename = f"{name}_{random_string}{ext}"
        os.rename(rf"{filename}", os.path.join(new_filename))
        return new_filename

    # Rename the file and stash it in a separate folder
    def stash_generated_files(self):
        os.chdir(self.destination_path)
        # Name of the folder to store stashed files in:
        stash_folder_name = "Keep"
        # Check if the folder already exists
        if not os.path.exists(stash_folder_name):
            os.mkdir(stash_folder_name)  # Create the folder if it doesn't exist
        if self.export_format_options.currentText() == "PNG":
            output_full_path = rf"{self.output_image_path}"
            new_image_name = self.random_string_generator(output_full_path)
            # transfer newly renamed file to stash folder
            stashed_file_location = rf"{os.path.join(stash_folder_name, os.path.basename(new_image_name))}"
            os.rename(new_image_name, stashed_file_location)
        elif self.export_format_options.currentText() == "BOTH":
            output_full_path = rf"{self.output_image_path_2}"
            new_image_name = self.random_string_generator(output_full_path)
            # ----- # Take the initially generated random string and rename other file format
            png_name, png_ext = os.path.splitext(rf"{new_image_name}")
            svg_name, svg_ext = os.path.splitext(rf"{self.output_image_path}")
            output_full_path_svg = rf"{png_name}{svg_ext}"
            os.rename(self.output_image_path, output_full_path_svg)  # rename the actual file on disk
            # transfer newly renamed file to stash folder
            stashed_file_location = rf"{os.path.join(stash_folder_name, os.path.basename(output_full_path_svg))}"
            os.rename(rf"{output_full_path_svg}", rf"{stashed_file_location}")
            # transfer PNG to stash folder
            stashed_file_location_PNG = rf"{os.path.join(stash_folder_name, os.path.basename(new_image_name))}"
            os.rename(new_image_name, stashed_file_location_PNG)
        else:
            output_full_path = rf"{self.output_image_path_1}"
            new_image_name = self.random_string_generator(output_full_path)
            # transfer newly renamed file to stash folder
            stashed_file_location = rf"{os.path.join(stash_folder_name, os.path.basename(new_image_name))}"
            os.rename(new_image_name, stashed_file_location)

        self.stash_last_generated_button.setVisible(False)  # Hide button after stashing
        self.delete_last_generated_button.setVisible(False)  # Hide Delete button

    def delete_last_generated(self):
        if self.export_format_options.currentText() == "PNG":
            os.remove(self.output_image_path)
        elif self.export_format_options.currentText() == "BOTH":
            os.remove(self.output_image_path_2)
            os.remove(self.output_image_path)
        else:
            os.remove(self.output_image_path_1)
        self.delete_last_generated_button.setVisible(False)  # Hide button after deleting
        self.stash_last_generated_button.setVisible(False)  # Hide Stash button

    ## Font Size Sliders - Preset Buttons
    def font_size_slider_presets(self, button):
        if button == self.MinFSp10:
            self.min_font_size_slider.setValue(10)
        if button == self.MinFSp21:
            self.min_font_size_slider.setValue(21)
        if button == self.MinFSp31:
            self.min_font_size_slider.setValue(31)
        if button == self.MinFSp49:
            self.min_font_size_slider.setValue(49)
        if button == self.MaxFSp150:
            self.max_font_size_slider.setValue(150)
        if button == self.MaxFSp250:
            self.max_font_size_slider.setValue(250)
        if button == self.MaxFSp50:
            self.max_font_size_slider.setValue(50)
        if button == self.MaxFSp73:
            self.max_font_size_slider.setValue(73)

    def fontAwesomeIconsList_fnc(self):
        self.emoji_list.clear()
        fontAwesome_font_path = resource_path("emojiFonts/Font Awesome 6 Free-Solid-900.otf")  # Replace with the actual file path
        font_id = QFontDatabase.addApplicationFont(fontAwesome_font_path)
        font_family_fontAwesome = QFontDatabase.applicationFontFamilies(font_id)[0]
        q_font_fontAwesome = QFont(font_family_fontAwesome, 28)
        self.emoji_list.setFont(q_font_fontAwesome)
        for icon_key, icon_info in fontAwesome_data.items():
            if "styles" in icon_info and "solid" in icon_info["styles"]:
                icon_unicode = chr(int(icon_info["unicode"], 16))  # Transform hexadecimal to Unicode
                search_terms = ", ".join(icon_info["search"]["terms"])  # Join search terms with commas
                item_text = f"{icon_unicode} {search_terms}"
                item = QListWidgetItem(icon_unicode)
                self.emoji_list.addItem(item)
        self.FilterListFrame.setVisible(False)

    def unicodeEmojiList_fnc(self):
        self.emoji_list.clear()
        # Set the font family for the listWidget
        unicode_font_path = resource_path("emojiFonts/Segue UI Emoji.ttf")  # Replace with the actual file path
        font_id = QFontDatabase.addApplicationFont(unicode_font_path)
        font_family_unicode = QFontDatabase.applicationFontFamilies(font_id)[0]
        q_font_unicode = QFont(font_family_unicode, 28)
        self.emoji_list.setFont(q_font_unicode)
        # Populate the list with the filtered emojis from the json
        emoji_edition_filter = ["13.0", "13.1", "14.0", "15.0"]
        selected_emoji_group = self.emoji_filter_list.currentText()

        for emoji, data in emoji_data.items():
            unicode_edition = data["unicode_version"]
            emoji_group = data["group"]

            if unicode_edition not in emoji_edition_filter:
                if self.emoji_filter_list.currentText() == "All":
                    item = QListWidgetItem(emoji)
                    self.emoji_list.addItem(item)
                elif emoji_group == selected_emoji_group:
                    self.emoji_list.addItem(emoji)
        self.FilterListFrame.setVisible(True)

    def populateEmojiList(self):
        self.emoji_list.clear()
        emoji_edition_filter = ["13.0", "13.1", "14.0", "15.0"]
        selected_emoji_group = self.emoji_filter_list.currentText()

        for emoji, data in emoji_data.items():
            unicode_edition = data["unicode_version"]
            emoji_group = data["group"]

            if unicode_edition not in emoji_edition_filter:
                if self.emoji_filter_list.currentText() == "All":
                    item = QListWidgetItem(emoji)
                    self.emoji_list.addItem(item)
                elif emoji_group == selected_emoji_group:
                    self.emoji_list.addItem(emoji)

    def insertEmojiOnClick(self, item):
        current_text = self.word_input.toPlainText()
        if current_text != "":
            self.word_input.setText(f"{current_text} {item.text()}")
        else:
            self.word_input.setText(f"{current_text}{item.text()}")

    def custom_regexp(self):
        # Any + Numbers
        if self.regxp_any_character_checkbox.isChecked() and self.include_number_checkbox.isChecked():
            regxp = r"\S"  # treats all special characters as a single word
        # Any - Numbers
        elif self.regxp_any_character_checkbox.isChecked() and not self.include_number_checkbox.isChecked():
            regxp = r"[^0-9\s]+"  # includes all special characters, except numbers
        # Any + Punctuation
        elif self.regxp_any_character_checkbox.isChecked() and self.connected_punctuation_checkbox.isChecked():
            regxp = r"\S"  # treats all special characters as a single word
        # Any - Punctuation
        elif self.regxp_any_character_checkbox.isChecked() and not self.connected_punctuation_checkbox.isChecked():
            regxp = r"\S"  # treats all special characters as a single word
        # Punctuation - Numbers - Any
        elif self.connected_punctuation_checkbox.isChecked() and not self.include_number_checkbox.isChecked() and not self.regxp_any_character_checkbox.isChecked():
            regxp = r"\w+(?:\.\w+)*"  # Includes "." punctuation, but only if attached to a word Ex.: x.com
        # Punctuation + Numbers - Any
        elif self.connected_punctuation_checkbox.isChecked() and self.include_number_checkbox.isChecked() and not self.regxp_any_character_checkbox.isChecked():
            regxp = r"[\w\p{P}']+(\.\w+(?:\.\w+)*)*|\d+"  # Includes any punctuation if part of a word and any number as stand-alone word
        # Numbers - Punctuation - Any
        elif self.include_number_checkbox.isChecked() and not self.connected_punctuation_checkbox.isChecked() and not self.regxp_any_character_checkbox.isChecked():
            regxp = r"\b(?:[a-zA-Z]+\d+\w*|\d+\w*)\b"
        return regxp
        # regxp = r"\w+(?:\.\w+)*" # Includes "." punctuation, but only if attached to a word Ex.: x.com
        # this still needs to be adjusted, as not all regex combinations are correct!


if __name__ == "__main__":
    app = widget.QApplication(sys.argv)
    window = WCGX()
    window.show()
    sys.exit(app.exec())
