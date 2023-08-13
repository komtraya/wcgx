import numpy as np
import random
import sys
import os
from wordcloud import WordCloud


# from PySide6 import QtCore as core
from PySide6 import QtWidgets as widget

from PySide6.QtGui import QFont, QFontDatabase, QPixmap

# from PySide6 import QtGui as gui
from ui.output import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QListWidgetItem
from PIL import Image

userPath = os.path.expanduser("~")


# from PySide6.QtGui import QFontInfo
##### ----- Resource Fix #####
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


##### ----- Resource Fix #####


class WCGX(widget.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ## Modifications/data-setup for the start of the app
        # Make sure text input is not empty
        self.word_input.textChanged.connect(self.text_input_Changed)
        self.destination_path = None
        self.mask_path = None
        self.mask_image_thumbnail.setVisible(False)
        self.mask_dimensions_label.setText("")
        ### scan fonts set by default (windows path) and populate the list
        self.fonts_directory = rf"{userPath}\AppData\Local\Microsoft\Windows\Fonts"  # default font directory on start of the app
        self.scan_fonts(self.fonts_directory)  # This scans the default directory for fonts
        self.font_list.currentItemChanged.connect(self.apply_selected_font)  # This enables clicks, as well as keyboard arrows to browse through the list

        self.custom_font_directory_selection.clicked.connect(self.select_custom_fonts_folder)

        ## HIDE WORDCLOUD BUTTON BY DEFAULT ##
        self.generate_wordcloud_button.setVisible(False)
        self.export_as_frame.setVisible(False)
        # Open destination folder if it's selected
        self.open_destination_folder.setVisible(False)
        self.open_destination_folder.clicked.connect(self.open_destination_folder_function)

        # Hide random colors frame
        self.RandomColorGroupBox.setVisible(False)

        # Connect dropdown list to function
        self.colormaps_dropdown.currentTextChanged.connect(self.check_dropdown_selected_item)

        ## MASK IMAGE SELECTION
        # Connect the "Select Mask" button's clicked signal to the custom slot
        self.mask_select_button.clicked.connect(self.mask_select_button_clicked)
        # Connect the "Path Changed" signal of the mask_path to the custom slot (Update path)
        # self.mask_path.textChanged.connect(self.mask_path_Changed)
        ## INFO LABELS UPDATE
        self.update_info_labels()
        self.repeat_checkbox.clicked.connect(self.update_info_labels)
        self.collocations_checkbox.clicked.connect(self.update_info_labels)
        self.include_number_checkbox.clicked.connect(self.update_info_labels)
        ## EXPORT DESTINATION SELECTION

        # Connect the button click to the slot function
        self.select_destination_button.clicked.connect(self.select_destination_button_clicked)

        # ## FONT HANDLING
        # self.font_path = None

        ## Browsing through the list of parameters
        self.parameters_list.currentItemChanged.connect(self.change_tab_based_on_selected_item)

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

        ## REPEAT ON/OFF
        # self.repeat_checkbox.isChecked.connect(self.state_of_repeat_checkbox)
        ## PRESET BUTTONS FOR RANDOM COLORS FUNCTION ##

        self.rcp_bright.clicked.connect(self.rcp_bright_function)
        self.rcp_dark.clicked.connect(self.rcp_dark_function)
        self.rcp_reset.clicked.connect(self.rcp_reset_function)
        self.rcp_maximize_red.clicked.connect(self.rcp_maximize_red_function)
        self.rcp_minimize_red.clicked.connect(self.rcp_minimize_red_function)
        self.rcp_maximize_green.clicked.connect(self.rcp_maximize_green_function)
        self.rcp_minimize_green.clicked.connect(self.rcp_minimize_green_function)
        self.rcp_maximize_blue.clicked.connect(self.rcp_maximize_blue_function)
        self.rcp_minimize_blue.clicked.connect(self.rcp_minimize_blue_function)
        ## WordCloud Button ##
        self.generate_wordcloud_button.clicked.connect(self.generate_WordCloud)

        # # # # # Create a WordCloud object with the mask # # # # #
        ## ENABLE SPECIAL CHARACTERS:
        self.custom_regexp = r"\w+(?:\.\w+)*"

    def generate_WordCloud(self):
        # @ PARAMETERS
        # Open Mask Image
        mask_image = np.array(Image.open((self.mask_path)))
        try:
            mask_image[(mask_image[..., 3] == 0)] = [255, 255, 255, 255]  # Replace transparent with white
        except:
            mask_image = np.array(Image.open((self.mask_path)))

        wordcloud = WordCloud(
            mask=mask_image,
            # width=width,
            # height=height,
            regexp=self.custom_regexp,
            background_color=None,
            scale=self.scale_slider.value(),  # this controls the size of the image - multiplier for original size
            contour_color=0,
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
            # relative_scaling=0,
        )
        # @ generate wc
        wordcloud.generate(self.word_input.toPlainText())

        ###########
        # @ Export Image @ #
        ##PNG
        if self.export_format_options.currentText() == "PNG":
            # Convert the word cloud image to a numpy array
            wordcloud_image = np.array(wordcloud)

            # Create a PIL Image object from the numpy array
            wordcloud_image = Image.fromarray(wordcloud_image)

            # Export the PIL Image object as a PNG image file
            output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].png"
            wordcloud_image.save(output_image_path)
        ## SVG
        elif self.export_format_options.currentText() == "SVG":
            # Generate the SVG representation of the word cloud
            svg_code = wordcloud.to_svg()
            # Export the SVG code to a file
            output_image_path_1 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].svg"
            with open(f"{output_image_path_1}", "w", encoding="utf-8") as f:
                f.write(svg_code)
        ## BOTH
        else:
            # Generate the SVG representation of the word cloud
            svg_code = wordcloud.to_svg()
            # Export the SVG code to a file
            output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].svg"
            with open(f"{output_image_path}", "w", encoding="utf-8") as f:
                f.write(svg_code)

            # Convert the word cloud image to a numpy array
            wordcloud_image = np.array(wordcloud)
            # Create a PIL Image object from the numpy array
            wordcloud_image = Image.fromarray(wordcloud_image)

            # Export the PIL Image object as a PNG image file
            output_image_path_2 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--M{self.margin_slider.value()}--mF{self.min_font_size_slider.value()}--MF{self.max_font_size_slider.value()}--{self.colormaps_dropdown.currentText()}[WCGX].png"
            wordcloud_image.save(output_image_path_2)

    ### !!!!! FUNCTIONS !!!!! ###
    ## FONT HANDLING ##

    def mask_select_button_clicked(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PNG Image", "", "PNG Files (*.png);;All Files (*)", options=options)
        if file_name:
            self.mask_path = file_name
            self.enable_WordCloud_Generator_Button()
        else:
            self.mask_path = None
            self.enable_WordCloud_Generator_Button()

        if self.mask_path:
            self.update_image_dimensions()
            self.mask_select_button.setStyleSheet("background-color: #7754c8; color: #3cf3b6; border-radius:10px;")
        else:
            self.update_image_dimensions()
            self.mask_select_button.setStyleSheet("border:2px solid red; background-color: #7754c8; color: #3cf3b6; border-radius:10px;")

    # @ CHECK FIELDS FOR CHANGES @ #

    # Check text input field for changes
    def text_input_Changed(self):
        self.enable_WordCloud_Generator_Button()
        if self.word_input.toPlainText():
            self.word_input.setStyleSheet("border:2px solid green;")
        else:
            self.word_input.setStyleSheet("border:1px solid red;")

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
            self.select_destination_button.setStyleSheet("border:2px solid red; background-color: #7754c8; color: #3cf3b6; border-radius:10px;")
        else:
            self.select_destination_button.setStyleSheet("background-color: #7754c8; color: #3cf3b6 ;border-radius:10px;")
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
        global image_state
        global width
        global height
        if self.mask_path:
            try:
                with Image.open(self.mask_path) as img:
                    width, height = img.size
                    self.mask_dimensions_label.setText(f"Mask Dimensions: {width}x{height}")
                    self.mask_dimensions_label.setStyleSheet("color: green;")
                    # mask image
                    self.mask_image_thumbnail.setVisible(True)
                    pixmap = QPixmap(self.mask_path)
                    self.mask_image_thumbnail.setPixmap(pixmap)

            except:
                self.mask_dimensions_label.setText("Incorrect image path!")
                self.mask_dimensions_label.setStyleSheet("color: red;")
                self.export_as_frame.setVisible(False)
                # mask image
                self.mask_image_thumbnail.setVisible(False)

        if not self.mask_path:
            self.mask_dimensions_label.setText(f"")
            # mask image
            self.mask_image_thumbnail.setText(f"")
            self.mask_image_thumbnail.setVisible(False)

    ## ENABLE WORDCLOUD BUTTON##
    def enable_WordCloud_Generator_Button(self):
        if self.mask_path and self.destination_path and self.word_input.toPlainText() != "":
            # self.generate_wordcloud_button.setEnabled(True)
            self.generate_wordcloud_button.setVisible(True)
            self.export_as_frame.setVisible(True)
        else:
            # self.generate_wordcloud_button.setEnabled(False)
            self.generate_wordcloud_button.setVisible(False)
            self.export_as_frame.setVisible(False)

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
        initial_directory = rf"{userPath}\AppData\Local\Microsoft\Windows\Fonts"
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

    ## RANDOM COLOR PRESETS FUNCTIONS ##
    def rcp_bright_function(self):
        self.red_max.setValue(250)
        self.green_max.setValue(250)
        self.blue_max.setValue(250)
        self.red_min.setValue(150)
        self.green_min.setValue(150)
        self.blue_min.setValue(150)

    def rcp_dark_function(self):
        self.red_max.setValue(140)
        self.green_max.setValue(140)
        self.blue_max.setValue(140)
        self.red_min.setValue(40)
        self.green_min.setValue(40)
        self.blue_min.setValue(40)

    def rcp_reset_function(self):
        self.red_max.setValue(255)
        self.green_max.setValue(255)
        self.blue_max.setValue(255)
        self.red_min.setValue(0)
        self.green_min.setValue(0)
        self.blue_min.setValue(0)

    def rcp_maximize_red_function(self):
        self.red_max.setValue(255)
        self.red_min.setValue(255)

    def rcp_minimize_red_function(self):
        self.red_max.setValue(0)
        self.red_min.setValue(0)

    def rcp_maximize_green_function(self):
        self.green_max.setValue(255)
        self.green_min.setValue(255)

    def rcp_minimize_green_function(self):
        self.green_max.setValue(0)
        self.green_min.setValue(0)

    def rcp_maximize_blue_function(self):
        self.blue_max.setValue(255)
        self.blue_min.setValue(255)

    def rcp_minimize_blue_function(self):
        self.blue_max.setValue(0)
        self.blue_min.setValue(0)

    ## ColorMap and Color Function Conditions ##
    def colormap_conditions(self):
        if self.colormaps_dropdown.currentText() == "Default":
            self.colormap = "tab20b"
            self.color_function = None
            # return self.colormap
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
            self.colormap = "tab20b"
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
            # self.RandomColorsFrame.setVisible(True)
            self.RandomColorGroupBox.setVisible(True)
            # self.Presets_all_rcpg.setVisible(True)
        else:
            # self.RandomColorsFrame.setVisible(False)
            self.RandomColorGroupBox.setVisible(False)

    def random_color_func(self, *args, **kwargs):
        # Generate a random color for each trigram
        r, g, b = (
            random.randint(self.red_min.value(), self.red_max.value()),
            random.randint(self.green_min.value(), self.green_max.value()),
            random.randint(self.blue_min.value(), self.blue_max.value()),
        )
        return f"rgb({r}, {g}, {b})"

    def change_tab_based_on_selected_item(self):
        if self.parameters_list.currentItem().text() == "Scale":
            self.parameters_window.setCurrentIndex(5)
        elif self.parameters_list.currentItem().text() == "Collocations":
            self.parameters_window.setCurrentIndex(7)
        elif self.parameters_list.currentItem().text() == "Collocations Threshold":
            self.parameters_window.setCurrentIndex(8)
        elif self.parameters_list.currentItem().text() == "Min/Max Font-size":
            self.parameters_window.setCurrentIndex(1)
        elif self.parameters_list.currentItem().text() == "Repeat Words":
            self.parameters_window.setCurrentIndex(0)
        elif self.parameters_list.currentItem().text() == "Prefer-Horizontal":
            self.parameters_window.setCurrentIndex(4)
        # elif self.parameters_list.currentItem().text() == "StopWords":
        #     self.parameters_window.setCurrentIndex(5)
        elif self.parameters_list.currentItem().text() == "Include Numbers":
            self.parameters_window.setCurrentIndex(9)
        elif self.parameters_list.currentItem().text() == "Margin between words":
            self.parameters_window.setCurrentIndex(3)
        elif self.parameters_list.currentItem().text() == "Font Step":
            self.parameters_window.setCurrentIndex(2)

    def update_info_labels(self):
        self.repeat_info_label.setText(f"{self.repeat_checkbox.isChecked()}")
        self.collocations_info_label.setText(f"{self.collocations_checkbox.isChecked()}")
        self.include_numbers_info_label.setText(f"{self.include_number_checkbox.isChecked()}")
        ###
        # self.collocations_thresh_info_label.setText(f"{self.collocations_thresh_slider.value()}")
        # self.margin_info_label.setText(f"{self.margin_slider.value()}")
        # self.min_font_size_info_label.setText(f"{self.min_font_size_slider.value()}")
        # self.max_font_size_info_label.setText(f"{self.max_font_size_slider.value()}")
        # self.fontstep_info_label.setText(f"{self.font_step_slider.value()}")


if __name__ == "__main__":
    app = widget.QApplication(sys.argv)
    window = WCGX()
    window.show()
    sys.exit(app.exec())
