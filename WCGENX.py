import numpy as np
import random
import sys
import os
import json
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt
from PySide6 import QtWidgets as widget
from PySide6.QtGui import QFont, QFontDatabase, QPixmap, QImage, QPainter, QColor, QIcon
from PySide6.QtWidgets import (
    QFileDialog,
    QListWidgetItem,
    QColorDialog,
)
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QStandardPaths, QSize, QThread, Signal, Qt

from ui.main import Ui_MainWindow
from ui.gradient import Ui_GradientWindow
from ui.error import Ui_Error
from ui.storeProfile import Ui_StoreProfileWindow
from ui.gallery import Ui_GalleryWindow
from ui.fsw import Ui_FontSquirrelWindow
import sqlite3
import requests
import zipfile
import shutil

# import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


##### ----- Resource Fix #####
def resource_path(rel_path):
    """Get absolute path to resource - PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, rel_path)


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


class ErrorWindow(widget.QMainWindow, Ui_Error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class AreYouSure(widget.QDialog, Ui_StoreProfileWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.profile_name.setVisible(False)
        self.setWindowTitle("Are You Sure?")
        

class StoreProfileWindow(widget.QDialog, Ui_StoreProfileWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class GradientWindow(widget.QWidget, Ui_GradientWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gradient_push_slider.valueChanged.connect(
            self.gradient_push_slider_changed_fnc
        )

    def gradient_push_slider_changed_fnc(self, int):
        self.gradient_push_indicator_lbl.setText(f"{int}")


class FontSquirrel(widget.QWidget, Ui_FontSquirrelWindow):
    update_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fs_category_list.currentTextChanged.connect(self.font_count_indicator_fnc)
        self.download_category_btn.clicked.connect(self.download_font_category_fnc)

    def download_font_category_fnc(self):
        classification_to_download = self.fs_category_list.currentText()
        options = QFileDialog.Options()
        destination_folder = QFileDialog.getExistingDirectory(
            self, "Select Folder", "", options=options
        )

        if destination_folder and self.fs_category_list.currentText() != "All":

            class DownloadThread(QThread):
                update_signal = Signal(str)
                downloading_lbl = self.downloading_lbl

                def run(self):
                    try:
                        self.downloading_lbl.setText("Downloading...")
                        font_list_url = f"https://www.fontsquirrel.com/api/fontlist/{classification_to_download}"
                        font_list_response = requests.get(font_list_url)
                        font_list = font_list_response.json()
                        font_properties_dict = {}

                        for font in font_list:
                            family_urlname = font["family_urlname"]
                            font_properties_dict[family_urlname] = font

                        for (
                            family_urlname,
                            font_properties,
                        ) in font_properties_dict.items():
                            try:
                                font_download_url = f"https://www.fontsquirrel.com/fontfacekit/{family_urlname}"
                                local_zip_path = f"{family_urlname}-fontfacekit.zip"
                                font_response = requests.get(font_download_url)

                                with open(local_zip_path, "wb") as font_zip:
                                    font_zip.write(font_response.content)

                                extracted_dir = os.path.join(
                                    destination_folder, classification_to_download
                                )
                                os.makedirs(extracted_dir, exist_ok=True)
                                extracted_dir = rf"{extracted_dir}"
                                with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
                                    zip_ref.extractall(extracted_dir)

                                for root, dirs, files in os.walk(extracted_dir):
                                    for file in files:
                                        if file.lower().endswith((".otf", ".ttf")):
                                            old_file_path = os.path.join(root, file)
                                            new_file_path = os.path.join(
                                                root, file.replace("-webfont", "")
                                            )
                                            os.rename(old_file_path, new_file_path)

                                for root, dirs, files in os.walk(extracted_dir):
                                    for file in files:
                                        if file.lower().endswith((".otf", ".ttf")):
                                            file_path = os.path.join(root, file)
                                            shutil.move(
                                                file_path,
                                                os.path.join(extracted_dir, file),
                                            )

                                for item in os.listdir(extracted_dir):
                                    item_path = os.path.join(extracted_dir, item)
                                    if os.path.isfile(
                                        item_path
                                    ) and not item.lower().endswith((".otf", ".ttf")):
                                        os.remove(item_path)
                                    elif os.path.isdir(item_path):
                                        shutil.rmtree(item_path)

                                os.remove(local_zip_path)

                                self.update_signal.emit(
                                    f'# {family_urlname}\n- downloaded\n- extracted\n- files renamed in "{extracted_dir}"'
                                )
                            except Exception as e:
                                self.update_signal.emit(
                                    f"Error downloading font '{family_urlname}':\n- {str(e)}"
                                )
                                self.downloading_lbl.setText("")
                        self.update_signal.emit("# Done.")
                        self.downloading_lbl.setText("")

                    except Exception as e:
                        self.update_signal.emit(f"Error: {str(e)}")
                        self.downloading_lbl.setText("")

            download_thread = DownloadThread(self)
            download_thread.update_signal.connect(self.update_ui)
            download_thread.start()
        elif destination_folder and self.fs_category_list.currentText() == "All":

            class DownloadAllFontsThread(QThread):
                update_signal = Signal(str)
                downloading_lbl = self.downloading_lbl

                def run(self):
                    try:
                        self.downloading_lbl.setText("Downloading...")
                        all_fonts_url = "https://www.fontsquirrel.com/api/fontlist/all"
                        all_fonts_response = requests.get(all_fonts_url)
                        all_fonts_list = all_fonts_response.json()

                        for font in all_fonts_list:
                            family_urlname = font["family_urlname"]
                            classification = font["classification"]

                            font_download_url = f"https://www.fontsquirrel.com/fontfacekit/{family_urlname}"
                            local_zip_path = f"{family_urlname}-fontfacekit.zip"
                            font_response = requests.get(font_download_url)

                            with open(local_zip_path, "wb") as font_zip:
                                font_zip.write(font_response.content)

                            extracted_dir = os.path.join(
                                destination_folder, classification
                            )
                            os.makedirs(extracted_dir, exist_ok=True)
                            extracted_dir = rf"{extracted_dir}"
                            with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
                                zip_ref.extractall(extracted_dir)

                            for root, dirs, files in os.walk(extracted_dir):
                                for file in files:
                                    if file.lower().endswith((".otf", ".ttf")):
                                        old_file_path = os.path.join(root, file)
                                        new_file_path = os.path.join(
                                            root, file.replace("-webfont", "")
                                        )
                                        os.rename(old_file_path, new_file_path)

                            for root, dirs, files in os.walk(extracted_dir):
                                for file in files:
                                    if file.lower().endswith((".otf", ".ttf")):
                                        file_path = os.path.join(root, file)
                                        shutil.move(
                                            file_path,
                                            os.path.join(extracted_dir, file),
                                        )

                            for item in os.listdir(extracted_dir):
                                item_path = os.path.join(extracted_dir, item)
                                if os.path.isfile(
                                    item_path
                                ) and not item.lower().endswith((".otf", ".ttf")):
                                    os.remove(item_path)
                                elif os.path.isdir(item_path):
                                    shutil.rmtree(item_path)

                            os.remove(local_zip_path)

                            self.update_signal.emit(
                                f'# {family_urlname}\n- downloaded\n- extracted\n- files renamed in "{extracted_dir}"'
                            )

                        self.update_signal.emit("# Done.")
                        self.downloading_lbl.setText("")

                    except Exception as e:
                        self.update_signal.emit(f"Error: {str(e)}")
                        self.downloading_lbl.setText("")

            download_all_fonts_thread = DownloadAllFontsThread(self)
            download_all_fonts_thread.update_signal.connect(self.update_ui)
            download_all_fonts_thread.start()

        self.downloading_lbl.setText("")

    def update_ui(self, message):
        self.info_lbl.setText(message)

    def font_count_indicator_fnc(self):
        text = self.fs_category_list.currentText()
        if text == "Blackletter":
            self.font_count_lbl.setText("21")
        elif text == "Calligraphic":
            self.font_count_lbl.setText("13")
        elif text == "Comic":
            self.font_count_lbl.setText("22")
        elif text == "Dingbat":
            self.font_count_lbl.setText("26")
        elif text == "Display":
            self.font_count_lbl.setText("245")
        elif text == "Grunge":
            self.font_count_lbl.setText("1")
        elif text == "Handdrawn":
            self.font_count_lbl.setText("54")
        elif text == "Monospaced":
            self.font_count_lbl.setText("27")
        elif text == "Novelty":
            self.font_count_lbl.setText("27")
        elif text == "Pixel":
            self.font_count_lbl.setText("2")
        elif text == "Pixel":
            self.font_count_lbl.setText("2")
        elif text == "Programming":
            self.font_count_lbl.setText("2")
        elif text == "Retro":
            self.font_count_lbl.setText("33")
        elif text == "Script":
            self.font_count_lbl.setText("72")
        elif text == "Serif":
            self.font_count_lbl.setText("148")
        elif text == "Stencil":
            self.font_count_lbl.setText("14")
        elif text == "Typewriter":
            self.font_count_lbl.setText("12")
        elif text == "All":
            self.font_count_lbl.setText("700+")


class GalleryWindow(widget.QWidget, Ui_GalleryWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.closed = (
            True  # Init this signal, because window closed detection is garbage
        )
        # Store references to QPixmap, QImage and tooltips separately
        self.svg_raw = []  # Store the raw svg data, so it can be exported to file
        self.pixmaps = []  # To store QPixmap objects
        self.images = []  # To store QImage objects
        self.tooltips = []

        # Create QListWidgetItems for each image and add them to the QListWidget
        for key, image_data in fontAwesome_data.items():
            svg_raw = image_data.get("svg", {}).get("solid", {}).get("raw", "")
            width = image_data.get("svg", {}).get("solid", {}).get("width", 128)
            height = image_data.get("svg", {}).get("solid", {}).get("height", 128)
            keywords = image_data.get("search", {}).get("terms", [])

            # Skip empty SVG data
            if not svg_raw:
                continue

            # Create a QPixmap from SVG data
            renderer = QSvgRenderer(svg_raw.encode())
            pixmap = QPixmap(width, height)
            pixmap.fill(QColor(0, 0, 0, 0))
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            # Change the color of the rendered pixmap
            self.change_pixmap_color(pixmap, QColor("#e6e6e6"))
            image = pixmap.toImage()
            self.images.append(image)
            self.pixmaps.append(pixmap)
            self.svg_raw.append(svg_raw)
            self.tooltips.append(" ".join(keywords).lower())
        # Store all items for filtering
        self.all_items = list(range(len(self.pixmaps)))
        # Set Icon Size
        self.masks_list.setIconSize(QSize(width, height))

    def change_pixmap_color(self, pixmap, color):
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()


class WCGX(widget.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.error_window = ErrorWindow()
        self.are_you_sure_window = AreYouSure()
        self.gradient_window = GradientWindow()
        self.error_window.close_btn.clicked.connect(lambda: self.error_window.close())
        self.storeProfile_window = StoreProfileWindow()
        self.deleteProfile_window = DeleteProfileWindow(self)
        self.fs_window = FontSquirrel()
        ##### ---------- #####
        self.gallery = GalleryWindow()
        ## Future color preset implementation(list needs sorting)
        # import matplotlib.cm as cm
        # for palette_names in cm.cmap_d:
        #     self.colormaps_dropdown.addItem(palette_names)
        #     print(palette_names)
        ## Font Squirrel
        self.open_fs_window.clicked.connect(self.open_fs_window_fnc)
        ## Gallery
        self.fa_mask_select_button.clicked.connect(self.start_gallery_window)
        self.gallery.fa_filter_input.textChanged.connect(self.filter_fa_images)
        self.gallery.masks_list.itemSelectionChanged.connect(self.update_mask_image)
        self.gallery.downloadButtonsGroup.buttonClicked.connect(
            self.download_selected_icon_fnc
        )

        ## Settings
        self.storeSettingsProfile_btn.clicked.connect(self.storeProfile_fnc)
        self.storeTextProfile_btn.clicked.connect(self.storeProfile_fnc)
        self.storeTextProfile_btn2.clicked.connect(self.storeProfile_fnc)
        self.storeProfile_window.cancel_store_btn.clicked.connect(
            self.cancelSettingsStorage_fnc
        )
        self.add_profile_font_btn.clicked.connect(self.add_font_to_profile_fonts_list)
        self.delete_profile_font_btn.clicked.connect(self.delete_font_from_profile_fonts_list)
        self.apply_profile_font_btn.clicked.connect(self.apply_selected_profile_font)
        self.update_settingsProfile_btn.clicked.connect(self.update_selected_settings_profile)
        ## Parameters display function connect
        self.parametersButtonGroup.buttonClicked.connect(
            self.change_tab_based_on_selected_item
        )
        ##  Emoji handling ##
        self.populateEmojiList()
        self.unicode_Emojis_btn.clicked.connect(self.unicodeEmojiList_fnc)
        self.font_Awesome_Icons_btn.clicked.connect(self.fontAwesomeIconsList_fnc)
        self.emoji_list.itemClicked.connect(self.insertEmojiOnClick)
        self.emoji_filter_list.currentTextChanged.connect(self.populateEmojiList)
        self.fontAwesome_filter_input.textChanged.connect(
            self.filter_fontAwesome_icons_fnc
        )
        self.unicodeEmojis_filter_input.textChanged.connect(
            self.filter_unicodeEmojis_byName_fnc
        )
        ## Modifications/data-setup for the start of the app
        # Make sure text input is not empty
        self.word_input.textChanged.connect(self.text_input_Changed)
        self.destination_path = None
        self.mask_path = None
        self.mask_image_thumbnail.setVisible(False)
        self.mask_dimensions_label.setText("")
        ### scan user fonts(appData) and populate font list
        self.scan_appData_fonts()
        self.font_list.currentItemChanged.connect(self.apply_selected_font)

        self.custom_font_directory_selection.clicked.connect(
            self.select_custom_fonts_folder
        )
        self.load_emoji_fonts_btn.clicked.connect(self.load_emoji_fonts_fnc)
        self.load_system_fonts_btn.clicked.connect(self.load_system_fonts_fnc)
        self.load_appData_fonts_btn.clicked.connect(self.load_appData_fonts_fnc)
        self.filter_fonts_input.textChanged.connect(self.filter_fonts_fnc)

        ## HIDE WORDCLOUD BUTTON BY DEFAULT ##
        self.enable_WordCloud_Generator_Button()
        self.open_destination_folder.setVisible(False)
        self.open_destination_folder.clicked.connect(
            self.open_destination_folder_function
        )

        # Hide random colors frame
        self.RandomColorFrame.setVisible(False)

        # Connect dropdown list to function
        self.colormaps_dropdown.currentTextChanged.connect(
            self.check_dropdown_selected_item
        )
        ## Connect Delete and Stash Buttons to functions
        # Stash
        self.stash_last_generated_button.setVisible(False)
        self.stash_last_generated_button.clicked.connect(self.stash_generated_files)
        # Delete
        self.delete_last_generated_button.setVisible(False)
        self.delete_last_generated_button.clicked.connect(self.delete_last_generated)
        ## MASK IMAGE SELECTION
        # Connect the "Select Mask" button's clicked signal to it's function
        self.mask_select_button.clicked.connect(self.mask_select_button_fnc)
        ## INFO LABELS UPDATE
        self.update_info_labels()
        self.repeat_checkbox.clicked.connect(self.update_info_labels)
        self.collocations_checkbox.clicked.connect(self.update_info_labels)
        ## EXPORT DESTINATION SELECTION
        # Connect the button click to the slot function
        self.select_destination_button.clicked.connect(
            self.select_destination_button_clicked
        )
        ## Turn the page
        self.pageSwitchButtonsGroup.buttonClicked.connect(self.turn_the_page)
        ## Margin.current
        # Connect the slider to the function that updates the label to reflect changes
        self.margin_slider.valueChanged.connect(self.margin_slider_changed)
        
        ## Image Scale Slider
        # Connect the slider to the function that updates the label to reflect changes
        self.scale_slider.valueChanged.connect(self.scale_slider_changed)
        
        ## Minimum Font Size Slider
        self.min_font_size_slider.valueChanged.connect(
            self.min_font_size_slider_changed
        )

        ## Maximum Font Size Slider
        self.max_font_size_slider.valueChanged.connect(
            self.max_font_size_slider_changed
        )
        
        ## Color detection thresh
        # Hide color frame on app start:
        self.colorEdgeSliderFrame.setVisible(False)
        self.color_thresh_slider.valueChanged.connect(self.color_thresh_slider_changed)
        ## Prefer Horizontal Slider
        self.prefer_horizontal_slider.valueChanged.connect(
            self.prefer_horizontal_slider_changed
        )
        ## Collocation Thresh Slider
        self.collocations_thresh_slider.valueChanged.connect(
            self.collocations_thresh_slider_changed
        )
        ## Font Step Slider
        self.font_step_slider.valueChanged.connect(self.font_step_slider_changed)
        
        ## Random Seed Slider
        self.random_seed_slider.valueChanged.connect(self.random_seed_slider_changed)
        ##Gradient Settings and Color selection Buttons
        self.gradient_settings_btn.clicked.connect(self.show_gradient_window_fnc)
        self.gradient_window.select_first_color_btn.clicked.connect(
            self.select_first_gradient_color_fnc
        )
        self.gradient_window.select_second_color_btn.clicked.connect(
            self.select_second_gradient_color_fnc
        )
        self.gradient_window.transparency_slider.valueChanged.connect(
            self.update_gradient_transparency_indicator_fnc
        )
        self.gradient_settings_btn.setVisible(False)
        ## PRESET BUTTONS FOR RANDOM COLORS - connect to function ##
        self.randomColorsPresetsGroup.buttonClicked.connect(
            self.random_colors_presets_function
        )

        ## WordCloud Button ##
        self.generate_wordcloud_button.clicked.connect(self.generate_WordCloud)
        ## Connect font slider presets to function
        self.fontSizePresetsGroup.buttonClicked.connect(self.font_size_slider_presets)

        ##Close all extra windows along with main window
        self.closeEvent = lambda close: self.on_close()

        self.gallery.closeEvent = lambda close: self.on_gallery_close()

        ##Settings
        self.init_wcgx_db()
        self.apply_SettingsProfile_fnc()
        self.applySettingsProfile_btn.clicked.connect(self.apply_SettingsProfile_fnc)
        self.applyTextProfile_btn.clicked.connect(self.applyTextProfile_fnc)
        
        # Initialize wordcloud_font_path
        self.wordcloud_font_path = None
        
        # Apply first font in the list of fonts on app start
        if self.font_list.count() > 0:
            first_item = self.font_list.item(0)
            self.apply_selected_font(first_item)
    # # # # # Create WordCloud object and Export Image(s) # # # # #
    def generate_WordCloud(self):

        if self.colormaps_dropdown.currentText() == "Mask Image Colors":
            # Maintain original colors 
            color_thresh = self.color_thresh_slider.value()
            color_mask = self.mask_image.copy()
            color_mask[np.sum(color_mask, axis=2) == 0] = 255

            # Enforce boundaries between colors
            edges = np.mean([np.gradient(color_mask[:, :, i].astype(float)) for i in range(3)], axis=0)
            color_mask[np.linalg.norm(edges, axis=0) > color_thresh] = 255  # Adjust the threshold as needed

            mask_image = color_mask

            # Create coloring from mask image
            image_colors = ImageColorGenerator(color_mask)
        else:
            mask_image = self.mask_image

        
        wordcloud = WordCloud(
            mask=mask_image,
            regexp=self.custom_regexp(),
            background_color=None,
            scale=self.scale_slider.value(),  # this controls the size of the image - multiplier for original size
            margin=self.margin_slider.value(),
            font_path=fr"{self.wordcloud_font_path}",
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
            stopwords=self.stopwords_fnc(),
            min_word_length=0,
            include_numbers=True,
            random_state=self.random_state_fnc(),  # Generated WC will be the same color/layout, until random_state int is different
            #relative_scaling="auto"
        )
        # @ generate wc
        try:
            wordcloud.generate(self.word_input.toPlainText())
            
        except Exception as e:
            self.error_window.error_lbl.setText(f"\n # Error:\n{e}")
            self.error_window.show()
            self.error_window.adjustSize()
        if self.colormaps_dropdown.currentText() == "Mask Image Colors":
                try:
                    wordcloud.recolor(color_func=image_colors)
                except:
                    self.error_window.error_lbl.setText(f"\n # Error:\nColor boundaries algorithm failed.\nApplying default color preset instead...")
                    self.error_window.show()
                    self.error_window.adjustSize()
        # @ Export Image @ #
        ##PNG
        if self.export_format_options.currentText() == "PNG":
            # Transform the word cloud image to a numpy array
            wordcloud_image = np.array(wordcloud)

            # Create a PIL Image object from the numpy array
            wordcloud_image = Image.fromarray(wordcloud_image)

            # Export the PIL Image object as a PNG image file
            if self.settingsProfiles_list.currentText() != "":
                self.output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--{self.settingsProfiles_list.currentText()}[WCGX].png"
            else:
                self.output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--No-Profile[WCGX].png"
            wordcloud_image.save(self.output_image_path)
            os.startfile(self.output_image_path)  # Open file after generating it
        ## SVG
        elif self.export_format_options.currentText() == "SVG":
            # Generate the SVG representation of the word cloud
            svg_code = wordcloud.to_svg()
            # Export the SVG code to a file
            if self.settingsProfiles_list.currentText() != "":
                self.output_image_path_1 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--{self.settingsProfiles_list.currentText()}[WCGX].svg"
            else:
                self.output_image_path_1 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--No-Profile[WCGX].svg"
            with open(f"{self.output_image_path_1}", "w", encoding="utf-8") as f:
                f.write(svg_code)
        ## BOTH
        else:
            # Generate the SVG representation of the word cloud
            svg_code = wordcloud.to_svg()
            # Export the SVG code to a file
            if self.settingsProfiles_list.currentText() != "":
                self.output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--{self.settingsProfiles_list.currentText()}[WCGX].svg"
            else:
                self.output_image_path = rf"{self.destination_path}\{self.font_list.currentItem().text()}--No-Profile[WCGX].svg"
            with open(f"{self.output_image_path}", "w", encoding="utf-8") as f:
                f.write(svg_code)

            # Transform the word cloud image to a numpy array
            wordcloud_image = np.array(wordcloud)
            # Create a PIL Image object from the numpy array
            wordcloud_image = Image.fromarray(wordcloud_image)

            # Export the PIL Image object as a PNG image file
            if self.settingsProfiles_list.currentText() != "":
                self.output_image_path_2 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--{self.settingsProfiles_list.currentText()}[WCGX].png"
            else:
                self.output_image_path_2 = rf"{self.destination_path}\{self.font_list.currentItem().text()}--No-Profile[WCGX].png"
            wordcloud_image.save(self.output_image_path_2)
            os.startfile(
                self.output_image_path_2
            )  # Open the PNG file after generating both formats
        self.stash_last_generated_button.setVisible(True)  # Display Stash button
        self.delete_last_generated_button.setVisible(True)  # Delete Stash button

    def download_selected_icon_fnc(self, button):
        if button == self.gallery.export_fa_png_btn:
            # Get file name and path using a file dialog
            export_path, _ = QFileDialog.getSaveFileName(
                self, "Export Image", "", "PNG (*.png)"
            )
            if export_path:
                self.gallery.export_as_png.save(export_path, quality=100)
        elif button == self.gallery.export_fa_svg_btn:
            # Get file name and path using a file dialog
            export_path, _ = QFileDialog.getSaveFileName(
                self, "Export Image", "", "SVG (*.svg)"
            )
            if export_path:
                # Export the SVG data to an SVG file
                with open(export_path, "w") as file:
                    file.write(self.gallery.export_as_svg)

    def mask_select_button_fnc(self):
        if self.gallery.isVisible():
            self.gallery.close()
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Mask Image",
            "",
            "Image Files (*.png;*.svg;*.jpg;*.jpeg)",
            options=options,
        )
        if file_name:
            self.mask_path = file_name
            self.enable_WordCloud_Generator_Button()

        if self.mask_path:
            if (
                self.mask_path.lower().endswith(".png")
                or self.mask_path.lower().endswith(".jpg")
                or self.mask_path.lower().endswith(".jpeg")
            ):
                # Open Mask Image
                self.mask_image = np.array(Image.open((self.mask_path)))
                try:
                    self.mask_image[(self.mask_image[..., 3] == 0)] = [
                        255,
                        255,
                        255,
                        255,
                    ]  # Replace transparent with white (because white is ignored)
                except:
                    self.mask_image = np.array(Image.open((self.mask_path)))
                self.update_image_dimensions()
                self.mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
                self.fa_mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
            elif self.mask_path.lower().endswith(".svg"):
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
                # Transform QImage to Pillow Image
                pil_image = Image.fromqpixmap(mask_test)

                # Transform Pillow Image to NumPy array
                mask_array = np.array(pil_image)
                try:
                    mask_array[(mask_array[..., 3] == 0)] = [
                        255,
                        255,
                        255,
                        255,
                    ]  # Replace transparent with white
                    self.mask_image = mask_array
                except:
                    self.mask_image = mask_array
                self.update_image_dimensions()
                self.mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
                self.fa_mask_select_button.setStyleSheet(
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
            self.fa_mask_select_button.setStyleSheet(
                """
            QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
            QPushButton{border:2px solid red; background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
            )

    def mask_fallback_fnc(self):
        if self.mask_path and self.gallery.closed == True:
            if (
                self.mask_path.lower().endswith(".png")
                or self.mask_path.lower().endswith(".jpg")
                or self.mask_path.lower().endswith(".jpeg")
            ):
                # Open Mask Image
                self.mask_image = np.array(Image.open((self.mask_path)))
                try:
                    self.mask_image[(self.mask_image[..., 3] == 0)] = [
                        255,
                        255,
                        255,
                        255,
                    ]  # Replace transparent with white
                except:
                    self.mask_image = np.array(Image.open((self.mask_path)))
                self.update_image_dimensions()
                self.mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
            elif self.mask_path.lower().endswith(".svg"):
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
                # Transform QImage to Pillow Image
                pil_image = Image.fromqpixmap(mask_test)

                # Transform Pillow Image to NumPy array
                mask_array = np.array(pil_image)
                try:
                    mask_array[(mask_array[..., 3] == 0)] = [
                        255,
                        255,
                        255,
                        255,
                    ]  # Replace transparent with white
                    self.mask_image = mask_array
                except:
                    self.mask_image = mask_array
                self.update_image_dimensions()
                self.mask_select_button.setStyleSheet(
                    """
                QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
                )
                self.fa_mask_select_button.setStyleSheet(
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
            self.fa_mask_select_button.setStyleSheet(
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
        selected_folder = QFileDialog.getExistingDirectory(
            self, "Select Folder", "", options=options
        )
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

    def update_mask_image(self):
        selected_items = self.gallery.masks_list.selectedItems()
        selected_qimage = None  # Initialize
        filtered_index = -1
        if selected_items:
            selected_index = self.gallery.masks_list.row(
                selected_items[0]
            )  # Get the index of the selected item
            if 0 <= selected_index < len(self.gallery.all_items):
                filtered_index = self.gallery.all_items[
                    selected_index
                ]  # Get the original index from the filtered list
            if 0 <= filtered_index < len(self.gallery.pixmaps):
                selected_pixmap = self.gallery.pixmaps[
                    filtered_index
                ]  # Get the selected pixmap
                selected_qimage = self.gallery.images[
                    filtered_index
                ]  # Get the corresponding QImage
                selected_svg = self.gallery.svg_raw[
                    filtered_index
                ]  # Get the selected svg file
                self.gallery.export_as_png = selected_pixmap
                self.gallery.export_as_svg = selected_svg

            # Now you can set self.mask_image the selected QImage
            self.gallery.mask_image = selected_qimage

            q_image = selected_qimage
            if selected_qimage is not None:
                pil_image = Image.fromqimage(q_image)
                pil_image_as_mask = Image.fromqimage(q_image)

                # Get the image dimensions
                width, height = pil_image.size

                # Update the mask dimensions label
                self.fa_image_size = (width, height)
                self.update_image_dimensions()

                # Set the maximum width and maintain the aspect ratio
                resize_max = (200, 10000)
                pil_image.thumbnail(resize_max, resample=Image.LANCZOS)

                # Transform the resized Pillow Image to a QImage
                resized_qimage = ImageQt(pil_image)

                # Transform the QImage to a QPixmap and set it to self.mask_image_thumbnail
                pixmap = QPixmap.fromImage(resized_qimage)
                self.mask_image_thumbnail.setPixmap(pixmap)

                self.mask_image_thumbnail.setVisible(True)
                # Transform Pillow Image to NumPy array
                mask_array = np.array(pil_image_as_mask)
                try:
                    mask_array[(mask_array[..., 3] == 0)] = [
                        255,
                        255,
                        255,
                        255,
                    ]  # Replace transparent with white
                    self.mask_image = mask_array
                except:
                    self.mask_image = mask_array

    def start_gallery_window(self):
        if not self.gallery.isVisible():
            self.gallery.show()
            self.gallery.closed = False
            self.populate_masks_list_fa_fnc()
            self.mask_select_button.setStyleSheet(
                """
                    QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                    QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
            )
            self.fa_mask_select_button.setStyleSheet(
                """
                    QPushButton:pressed{padding-left: 3px; padding-top: 3px;}
                    QPushButton{background-color:  rgba(100,100,100,150); color: #E6E6FA; border-radius:10px;}"""
            )
        else:
            self.gallery.showNormal()
        self.enable_WordCloud_Generator_Button()

    def filter_fa_images(self):
        filter_text = self.gallery.fa_filter_input.toPlainText()
        for item_index in range(self.gallery.masks_list.count()):
            item = self.gallery.masks_list.item(item_index)
            tooltip = item.toolTip()
            if filter_text not in tooltip:
                item.setHidden(True)
            else:
                item.setHidden(False)
        # self.gallery.masks_list.setCurrentItem(self.gallery.masks_list.item(0))

    def populate_masks_list_fa_fnc(self):
        self.gallery.masks_list.clear()
        for index in self.gallery.all_items:
            item = QListWidgetItem(self.gallery.masks_list)
            item.setIcon(QIcon(self.gallery.pixmaps[index]))
            item.setToolTip(self.gallery.tooltips[index])
        self.gallery.masks_list.setCurrentItem(self.gallery.masks_list.item(0))

    def open_destination_folder_function(self):
        os.startfile(rf"{self.destination_path}")

    def margin_slider_changed(self, value: int):
        self.label_margin_slider.setText(f"{value}")
        self.margin_info_label.setText(f"{value}")

    def scale_slider_changed(self, value: int):
        self.label_scale_slider.setText(f"{value}x")

        if self.mask_path and not self.gallery.isVisible():
            if (
                self.mask_path.lower().endswith(".png")
                or self.mask_path.lower().endswith(".jpg")
                or self.mask_path.lower().endswith(".jpeg")
            ):
                width, height = self.raster_image_size
                self.mask_dimensions_label.setText(
                    f"Mask Dimensions: {value * width}x{value * height}"
                )
            elif self.mask_path.lower().endswith(".svg"):
                width, height = self.svg_image_size
                self.mask_dimensions_label.setText(
                    f"Mask Dimensions: {value * width}x{value * height}"
                )
        elif self.gallery.isVisible():
            width, height = self.fa_image_size
            self.mask_dimensions_label.setText(
                f"Mask Dimensions: {value * width}x{value * height}"
            )

    def prefer_horizontal_slider_changed(self, value: int):
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
        self.label_min_font_size_slider.setText(f"{(value)}")
        self.min_font_size_info_label.setText(f"{(value)}")

    def max_font_size_slider_changed(self, value: int):
        self.label_max_font_size_slider.setText(f"{(value)}")
        self.max_font_size_info_label.setText(f"{(value)}")

    def color_thresh_slider_changed(self, value:int):
        self.color_thresh_slider_lbl.setText(f"{(value)}")
    
    def collocations_thresh_slider_changed(self, value: int):
        self.collocation_thresh_slider_label.setText(f"{(value)}")
        self.collocations_thresh_info_label.setText(f"{value}")

    def font_step_slider_changed(self, value: int):
        self.font_step_indicator_label.setText(f"{(value)}")
        self.fontstep_info_label.setText(f"{(value)}")

    def random_seed_slider_changed(self):
        if self.random_seed_slider.value() != 0:
            self.random_seed_int_lbl.setText(f"{self.random_seed_slider.value()}")
        else:
            self.random_seed_int_lbl.setText("Off")

    ## IMAGE DIMENSIONS INFO
    def update_image_dimensions(self):
        global width
        global height
        self.scale_slider.setValue(1)  # Reset Scale slider
        if self.mask_path:
            if (
                self.mask_path.lower().endswith(".png")
                or self.mask_path.lower().endswith(".jpg")
                or self.mask_path.lower().endswith(".jpeg")
            ):
                try:
                    with Image.open(self.mask_path) as img:
                        width, height = img.size
                        self.mask_dimensions_label.setText(
                            f"Mask Dimensions: {width}x{height}"
                        )
                        self.raster_image_size = (width, height)
                        self.mask_dimensions_label.setStyleSheet("color: green;")
                        resizeMax = (
                            200,
                            10000,
                        )  # Height will be calculated based on original width, so that aspect ratio is maintained
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
            elif self.mask_path.lower().endswith(".svg"):
                try:
                    # Create a QSvgRenderer for the SVG file
                    svg_filename = self.mask_path
                    svg_renderer = QSvgRenderer(svg_filename)

                    # Get the dimensions of the SVG
                    svg_size = svg_renderer.defaultSize()
                    width = str(svg_size.width())
                    height = str(svg_size.height())
                    self.mask_dimensions_label.setText(
                        f"Mask Dimensions: {width}x{height}"
                    )
                    self.svg_image_size = (svg_size.width(), svg_size.height())
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
                    # Transform QImage to Pillow Image
                    pil_image = Image.fromqpixmap(mask_test)
                    resizeMax = (200, 10000)  # Height will be calculated based on original width, so that aspect ratio is maintained
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
            else:
                self.mask_dimensions_label.setText(f"")
                self.mask_image_thumbnail.setText(f"")
                self.mask_image_thumbnail.setVisible(False)

        if self.gallery.isVisible() and not self.gallery.closed:
            width, height = self.fa_image_size
            self.mask_dimensions_label.setText(f"Mask Dimensions: {width}x{height}")
            self.mask_dimensions_label.setStyleSheet("color: green;")
        # Check if WC button needs to be disabled or not
        self.enable_WordCloud_Generator_Button()

    ## ENABLE WORDCLOUD BUTTON##
    def enable_WordCloud_Generator_Button(self):
        if (
            not self.gallery.closed
            and self.destination_path
            and self.word_input.toPlainText() != ""
        ):
            self.WC_GeneratorFrame.setVisible(True)
        elif (
            self.mask_path
            and self.destination_path
            and self.word_input.toPlainText() != ""
            and self.gallery.closed
        ):
            self.WC_GeneratorFrame.setVisible(True)
        else:
            self.WC_GeneratorFrame.setVisible(False)
    def turn_the_page(self, button):
        if button == self.page_forward_btn:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
        if button == self.page_back_btn:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
    ## SELECT FONT and FONT HANDLING
    def apply_selected_font(self, item):
        try:
            font_path = item.data(1001)
            font_id = QFontDatabase.addApplicationFont(font_path)
            font_families = QFontDatabase.applicationFontFamilies(font_id)

            if font_families:
                selected_font = QFont(font_families[0], 15)  # Use the first font family
                self.word_input.setFont(selected_font)
            self.wordcloud_font_path = font_path
        except:
            pass
    # Add currently selected font to Profile Fonts list, so it can be stored in a Settings profile
    def add_font_to_profile_fonts_list(self):
        try:
            profile_font_path = self.font_list.currentItem().data(1001)
            profile_font_name = os.path.basename(profile_font_path)
            profile_font_display_name = profile_font_name.split(".")[0].capitalize()
        
            self.profile_fonts_list.addItem(profile_font_display_name, profile_font_path)
        except:
            pass
    # Delete currently selected font from Profile Fonts list, so it can be stored in a Settings profile
    def delete_font_from_profile_fonts_list(self):
        try:
            selected_profile_font = self.profile_fonts_list.currentText()
            index = self.profile_fonts_list.findText(selected_profile_font)
            if index != -1:
                self.profile_fonts_list.removeItem(index)
        except:
            pass
    
    def apply_selected_profile_font(self):
        if self.profile_fonts_list.currentText():
            try:
                font_path = self.profile_fonts_list.currentData(Qt.UserRole)
                font_id = QFontDatabase.addApplicationFont(font_path)
                font_families = QFontDatabase.applicationFontFamilies(font_id)

                if font_families:
                    selected_font = QFont(font_families[0], 15)  # Use the first font family
                    self.word_input.setFont(selected_font)
                self.wordcloud_font_path = font_path
            except:
                pass
    
    def scan_system_fonts(self):
        self.font_list.clear()
        # Get the directories where fonts are typically located
        system_fonts_location = QStandardPaths.standardLocations(
            QStandardPaths.FontsLocation
        )

        # Initialize a list to store font file paths
        font_file_paths = []

        # Loop through the font directories and list font files
        for font_directory in system_fonts_location:
            font_files = [
                os.path.join(font_directory, file)
                for file in os.listdir(font_directory)
                if file.endswith((".ttf", ".otf"))
            ]
            font_file_paths.extend(font_files)
        for font_path in font_file_paths:
            font_name = os.path.basename(font_path)
            font_name_display = font_name.split(".")[0].capitalize()
            item = QListWidgetItem(font_name_display)
            item.setData(
                1001, font_path
            )  # Using an arbitrary ID (1001) to store font path, so we can access this data
            self.font_list.addItem(item)  # - populate the list with fonts
            self.font_list.setCurrentItem(
                self.font_list.item(0)
            )  # Automatically select the first item

    def filter_fonts_fnc(self):
        filter = self.filter_fonts_input.toPlainText().lower()

        if self.font_list.count() > 0:
            for index in range(self.font_list.count()):
                item = self.font_list.item(index)
                if item is not None:
                    text = item.text()
                if filter not in text.lower():
                    item.setHidden(True)
                else:
                    item.setHidden(False)

        if self.font_list.count() > 0:
            self.font_list.setCurrentItem(self.font_list.item(0))

    def scan_appData_fonts(self):
        self.font_list.clear()
        try:
            # Get the user-specific AppData folder
            appdata_fonts_location = QStandardPaths.writableLocation(
                QStandardPaths.GenericDataLocation
            )
            # Construct the path to the user's fonts directory within AppData
            appdata_fonts_dir = os.path.join(
                appdata_fonts_location, "Microsoft", "Windows", "Fonts"
            )
            # Initialize a list to store font file paths
            font_file_paths = []
            # List font files within the user's AppData fonts directory
            font_files = [
                os.path.join(appdata_fonts_dir, file)
                for file in os.listdir(appdata_fonts_dir)
                if file.endswith((".ttf", ".otf"))
            ]
            font_file_paths.extend(font_files)
            for font_path in font_file_paths:
                font_name = os.path.basename(font_path)
                font_name_display = font_name.split(".")[0].capitalize()
                item = QListWidgetItem(font_name_display)
                item.setData(
                    1001, font_path
                )  # Using an arbitrary ID (1001) to store font path
                self.font_list.addItem(item)  # - populate the list with fonts
                self.font_list.setCurrentItem(
                    self.font_list.item(0)
                )  # Automatically select the first item
        except Exception as e:
            print(e)

    def scan_fonts(self, fontDirectory):
        self.font_list.clear()
        font_files = self.get_font_files(fontDirectory)

        for font_path in font_files:
            try:
                font_name = os.path.basename(font_path)
                font_name_display = font_name.split(".")[0].capitalize()
                item = QListWidgetItem(font_name_display)
                item.setData(
                    1001, font_path
                )  # Using an arbitrary ID (1001) to store font path
                self.font_list.addItem(item)  # - populate the list with fonts
                self.font_list.setCurrentItem(
                    self.font_list.item(0)
                )  # Automatically select the first item
            except:
                pass
        # Disable the Generate WordCloud button if the selected path contains no font files
        if self.font_list.count() == 0:
            self.generate_wordcloud_button.setEnabled(False)
        else:
            self.generate_wordcloud_button.setEnabled(True)

    # Allow users to specify custom font directory
    def select_custom_fonts_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        # initial_directory = userPath  # system_fonts_path
        selected_directory = QFileDialog.getExistingDirectory(
            self, "Select Fonts Directory", options=options
        )

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
        self.scan_system_fonts()

    def load_appData_fonts_fnc(self):
        self.scan_appData_fonts()

    ## RANDOM COLOR PRESETS FUNCTIONS ##
    
    def random_colors_presets_function(self, button):
        if button == self.colp_pink_btn:
            self.red_max.setValue(255)
            self.green_max.setValue(0)
            self.blue_max.setValue(255)
            self.red_min.setValue(255)
            self.green_min.setValue(0)
            self.blue_min.setValue(255)
        if button == self.colp_wpp_btn:
            self.red_max.setValue(89)
            self.green_max.setValue(13)
            self.blue_max.setValue(59)
            self.red_min.setValue(89)
            self.green_min.setValue(13)
            self.blue_min.setValue(59)
        if button == self.colp_14_btn:
            self.red_max.setValue(20)
            self.green_max.setValue(20)
            self.blue_max.setValue(20)
            self.red_min.setValue(20)
            self.green_min.setValue(20)
            self.blue_min.setValue(20)
        if button == self.colp_e6_btn:
            self.red_max.setValue(230)
            self.green_max.setValue(230)
            self.blue_max.setValue(230)
            self.red_min.setValue(230)
            self.green_min.setValue(230)
            self.blue_min.setValue(230)
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
        if self.colormaps_dropdown.currentText() == "Mask Image Colors":
            self.colormap = "gist_ncar"
            self.color_function = None
            return self.colormap
        if self.colormaps_dropdown.currentText() == "Default":
            self.colormap = "gist_ncar"
            self.color_function = None
            return self.colormap
        elif (
            self.colormaps_dropdown.currentText() != "Default"
            and self.colormaps_dropdown.currentText() != "Random Colors"
        ):
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
        elif (
            self.colormaps_dropdown.currentText() != "Default"
            and self.colormaps_dropdown.currentText() != "Random Colors"
            and self.colormaps_dropdown.currentText() != "Gradient"
        ):
            self.colormap = self.colormaps_dropdown.currentText()
            self.color_function = None
            return self.color_function
        elif self.colormaps_dropdown.currentText() == "Random Colors":
            self.colormap = None
            self.color_function = self.random_color_func
            return self.color_function
        elif self.colormaps_dropdown.currentText() == "Gradient":
            self.colormap = None
            self.color_function = self.generate_gradient_color
            return self.color_function

    def check_dropdown_selected_item(self):
        if self.colormaps_dropdown.currentText() == "Random Colors":
            self.RandomColorFrame.setVisible(True)
        else:
            self.RandomColorFrame.setVisible(False)
        if self.colormaps_dropdown.currentText() == "Gradient":
            self.gradient_settings_btn.setVisible(True)
        else:
            self.gradient_settings_btn.setVisible(False)
        if self.colormaps_dropdown.currentText() == "Mask Image Colors":
            self.colorEdgeSliderFrame.setVisible(True)
        else:
            self.colorEdgeSliderFrame.setVisible(False)

    def update_gradient_transparency_indicator_fnc(self, int):
        self.gradient_window.transparency_indicator_lbl.setText(f"{int}")

    def select_first_gradient_color_fnc(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.gradient_window.first_gradient_lbl.setText(color.name())
            self.gradient_window.select_first_color_btn.setStyleSheet(
                f"""
            background-color:{color.name()};
            """
            )

    def select_second_gradient_color_fnc(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.gradient_window.second_gradient_lbl.setText(color.name())
            self.gradient_window.select_second_color_btn.setStyleSheet(
                f"""
            background-color:{color.name()};
            """
            )

    def random_color_func(self, *args, **kwargs):
        # Generate a random color for each trigram
        r, g, b = (
            random.randint(self.red_min.value(), self.red_max.value()),
            random.randint(self.green_min.value(), self.green_max.value()),
            random.randint(self.blue_min.value(), self.blue_max.value()),
        )
        a = 255
        return f"rgba({r}, {g}, {b},{a})"

    def generate_gradient_color(
        self, word, font_size, position, orientation, random_state=None, **kwargs
    ):
        # Define the top-left and bottom-right colors
        top_color_hex = self.gradient_window.first_gradient_lbl.text()  # First color
        bottom_color_hex = (
            self.gradient_window.second_gradient_lbl.text()
        )  # Second color
        # Transform hex colors to RGB tuples
        top_color_rgb = mcolors.hex2color(top_color_hex)
        bottom_color_rgb = mcolors.hex2color(bottom_color_hex)
        # Calculate the linear interpolation based on word position
        x, y = position
        if self.gallery.isVisible():
            width, height = self.fa_image_size
        else:
            if (
                self.mask_path.lower().endswith(".png")
                or self.mask_path.lower().endswith(".jpg")
                or self.mask_path.lower().endswith(".jpeg")
            ):
                width, height = self.raster_image_size
            elif self.mask_path.lower().endswith(".svg"):
                width, height = self.svg_image_size

        transition_point = float(self.gradient_window.gradient_push_slider.value()) / 10

        if self.gradient_window.straight_diagonal_checkbox.isChecked():
            gradient_position = (x / height, y / width)  # - diagonal (left to right)
        elif self.gradient_window.diagonal45_checkbox.isChecked():
            gradient_position = (
                (x + y) / (width + height),
                (x + y) / (width + height),
            )  # 45-degree diagonal

        # Adjust the x-range to extend the first color further across width and height
        r = int(
            np.interp(
                gradient_position[0],
                [0, transition_point],
                [top_color_rgb[0], bottom_color_rgb[0]],
            )
            * 255
        )
        g = int(
            np.interp(
                gradient_position[1],
                [0, transition_point],
                [top_color_rgb[1], bottom_color_rgb[1]],
            )
            * 255
        )
        b = int(
            np.interp(
                gradient_position[0],
                [0, transition_point],
                [top_color_rgb[2], bottom_color_rgb[2]],
            )
            * 255
        )

        # Interpolate the color (for hex to rgb)
        # r = int(np.interp(gradient_position[0], [0, 1], [top_color_rgb[0], bottom_color_rgb[0]]) * 255)
        # g = int(np.interp(gradient_position[1], [0, 1], [top_color_rgb[1], bottom_color_rgb[1]]) * 255)
        # b = int(np.interp(gradient_position[0], [0, 1], [top_color_rgb[2], bottom_color_rgb[2]]) * 255)

        a = self.gradient_window.transparency_slider.value()
        return r, g, b, a

    def show_gradient_window_fnc(self):
        if self.gradient_window.isVisible():
            self.gradient_window.showNormal()
        else:
            self.gradient_window.show()

    def change_tab_based_on_selected_item(self, button):
        ## Collocations
        if (
            button == self.collocationSettings_btn
            or button == self.collocationSettings_btn2
        ):
            self.parameters_window.setCurrentIndex(6)
        ## Font Size
        elif (
            button == self.fontSizeSettings_btn or button == self.fontSizeSettings_btn2
        ):
            self.parameters_window.setCurrentIndex(1)
        ## Repeat
        elif button == self.repeatWords_btn:
            self.parameters_window.setCurrentIndex(0)
        ## Orientation odds
        elif button == self.textOrientationSettings_btn:
            self.parameters_window.setCurrentIndex(4)
        ## Margin
        elif button == self.marginSettings_btn:
            self.parameters_window.setCurrentIndex(3)
        ## Font Step
        elif button == self.fontStepSettings_btn:
            self.parameters_window.setCurrentIndex(2)

    def update_info_labels(self):
        self.repeat_info_label.setText(f"{self.repeat_checkbox.isChecked()}")
        self.collocations_info_label.setText(
            f"{self.collocations_checkbox.isChecked()}"
        )

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
            stashed_file_location = (
                rf"{os.path.join(stash_folder_name, os.path.basename(new_image_name))}"
            )
            os.rename(new_image_name, stashed_file_location)
        elif self.export_format_options.currentText() == "BOTH":
            output_full_path = rf"{self.output_image_path_2}"
            new_image_name = self.random_string_generator(output_full_path)
            # ----- # Take the initially generated random string and rename other file format
            png_name, png_ext = os.path.splitext(rf"{new_image_name}")
            svg_name, svg_ext = os.path.splitext(rf"{self.output_image_path}")
            output_full_path_svg = rf"{png_name}{svg_ext}"
            os.rename(
                self.output_image_path, output_full_path_svg
            )  # rename the actual file on disk
            # transfer newly renamed file to stash folder
            stashed_file_location = rf"{os.path.join(stash_folder_name, os.path.basename(output_full_path_svg))}"
            os.rename(rf"{output_full_path_svg}", rf"{stashed_file_location}")
            # transfer PNG to stash folder
            stashed_file_location_PNG = (
                rf"{os.path.join(stash_folder_name, os.path.basename(new_image_name))}"
            )
            os.rename(new_image_name, stashed_file_location_PNG)
        else:
            output_full_path = rf"{self.output_image_path_1}"
            new_image_name = self.random_string_generator(output_full_path)
            # transfer newly renamed file to stash folder
            stashed_file_location = (
                rf"{os.path.join(stash_folder_name, os.path.basename(new_image_name))}"
            )
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
        self.delete_last_generated_button.setVisible(
            False
        )  # Hide button after deleting
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
        fontAwesome_font_path = resource_path(
            "emojiFonts/Font Awesome 6 Free-Solid-900.otf"
        )
        font_id = QFontDatabase.addApplicationFont(fontAwesome_font_path)
        font_family_fontAwesome = QFontDatabase.applicationFontFamilies(font_id)[0]
        q_font_fontAwesome = QFont(font_family_fontAwesome, 50)
        self.emoji_list.setFont(q_font_fontAwesome)
        for icon_key, icon_info in fontAwesome_data.items():
            if "styles" in icon_info and "solid" in icon_info["styles"]:
                search_terms = icon_info["search"]["terms"]
                icon_unicode = chr(
                    int(icon_info["unicode"], 16)
                )  # Transform hexadecimal to Unicode
                # item_text = f"{icon_unicode} {', '.join(search_terms)}"
                item = QListWidgetItem(icon_unicode)
                self.emoji_list.addItem(item)
                item.setToolTip(", ".join(search_terms))
        self.emoji_list.setSpacing(10)

        self.FilterListFrame.setVisible(False)
        self.unicodeEmojis_filter_input.setVisible(False)
        self.FontAwesome_FilterFrame.setVisible(True)

    def filter_fontAwesome_icons_fnc(self):
        filter_text = self.fontAwesome_filter_input.toPlainText().lower()
        for item_index in range(self.emoji_list.count()):
            item = self.emoji_list.item(item_index)
            tooltip = item.toolTip()
            if filter_text not in tooltip:
                item.setHidden(True)
            else:
                item.setHidden(False)

    def filter_unicodeEmojis_byName_fnc(self):
        filter_text = self.unicodeEmojis_filter_input.toPlainText()
        for item_index in range(self.emoji_list.count()):
            item = self.emoji_list.item(item_index)
            tooltip = item.toolTip()
            if filter_text not in tooltip:
                item.setHidden(True)
            else:
                item.setHidden(False)

    def unicodeEmojiList_fnc(self):
        self.emoji_list.clear()
        self.unicodeEmojis_filter_input.setVisible(True)
        # Set the font family for the listWidget
        unicode_font_path = resource_path("emojiFonts/Segue UI Emoji.ttf")
        font_id = QFontDatabase.addApplicationFont(unicode_font_path)
        font_family_unicode = QFontDatabase.applicationFontFamilies(font_id)[0]
        q_font_unicode = QFont(font_family_unicode, 40)
        self.emoji_list.setFont(q_font_unicode)
        # Populate the list with the filtered emojis from the json
        emoji_edition_filter = ["13.0", "13.1", "14.0", "15.0"]
        selected_emoji_group = self.emoji_filter_list.currentText()

        for emoji, data in emoji_data.items():
            unicode_edition = data["unicode_version"]
            emoji_group = data["group"]
            emoji_name = "".join(data["name"])
            if unicode_edition not in emoji_edition_filter:
                if self.emoji_filter_list.currentText() == "All":
                    item = QListWidgetItem(emoji)
                    self.emoji_list.addItem(item)
                    item.setToolTip(emoji_name)
                elif emoji_group == selected_emoji_group:
                    item = QListWidgetItem(emoji)
                    self.emoji_list.addItem(emoji)
                    item.setToolTip(emoji_name)

        # item.setToolTip(", ".join(emoji_name))
        self.emoji_list.setSpacing(5)
        self.FilterListFrame.setVisible(True)
        self.FontAwesome_FilterFrame.setVisible(False)

    def populateEmojiList(self):
        self.emoji_list.clear()
        self.FontAwesome_FilterFrame.setVisible(False)
        self.unicodeEmojis_filter_input.setVisible(True)
        emoji_edition_filter = ["13.0", "13.1", "14.0", "15.0"]
        selected_emoji_group = self.emoji_filter_list.currentText()

        for emoji, data in emoji_data.items():
            unicode_edition = data["unicode_version"]
            emoji_group = data["group"]
            emoji_name = "".join(data["name"])

            if unicode_edition not in emoji_edition_filter:
                if self.emoji_filter_list.currentText() == "All":
                    item = QListWidgetItem(emoji)
                    self.emoji_list.addItem(item)
                    item.setToolTip(emoji_name)
                elif emoji_group == selected_emoji_group:
                    item = QListWidgetItem(emoji)
                    self.emoji_list.addItem(item)
                    item.setToolTip(emoji_name)

    def insertEmojiOnClick(self, item):
        current_text = self.word_input.toPlainText()
        if current_text != "":
            self.word_input.setText(f"{current_text} {item.text()}")
        else:
            self.word_input.setText(f"{current_text}{item.text()}")

    def custom_regexp(self):
        ## Heterogeneous - GOOD ?
        if self.heterogeneous_checkbox.isChecked():
            regexp = r".+"  # - Any character can be a word or part of a word - Words are in order, due to space character being considered a word

        ## AlphaNumeric - GOOD
        elif self.binary_checkbox.isChecked():
            regexp = r"\b(?:[a-zA-Z]+\d+\w*|\d+\w*)\b"  # - Numbers as a word, or alphanumeric words!

        ## URL - Good, except for emojis as part of word
        elif self.url_checkbox.isChecked():
            regexp = r"\b[\w'/.'-]+\b|[^\w\s]"  # - Includes any punctuation, or character if part of a word, including numbers, word order is randomized
        ## Disorder - GOOD
        elif self.disorder_checkbox.isChecked():
            regexp = r"\S"  # - treats characters as a word(all letters will be placed randomly, not as part of the word)
        return regexp

    def random_state_fnc(self):
        if self.random_seed_slider.value() == 0:
            random_state = None
        else:
            random_state = self.random_seed_slider.value()
        return random_state

    def on_close(self):
        self.gradient_window.close()
        self.error_window.close()
        self.gallery.close()
        self.storeProfile_window.close()
        self.deleteProfile_window.close()

    def on_gallery_close(self):
        # Initialize a separate flag, to check if window is closed or not, because window closed detection is garbage. window.isHidden() is also garbage.
        self.gallery.closed = True
        # Call mask fallback, in case there was already a mask set from file
        self.mask_fallback_fnc()
        if not self.mask_path:
            self.mask_dimensions_label.setText(f"")
            self.mask_image_thumbnail.setText(f"")
            self.mask_image_thumbnail.setVisible(False)
        self.gallery.fa_filter_input.setPlainText("")

    def stopwords_fnc(self):
        if self.stopwords.toPlainText != "":
            stopwords = set()
            text = self.stopwords.toPlainText()
            words = text.split()
            for word in words:
                stopwords.add(word)
        else:
            stopwords = set()
        return stopwords

    def init_wcgx_db(self):
        # Initialize Settings File(db)
        db_file = "wcgx.db"
        if not os.path.isfile(db_file):
            # Create and Connect to the SQLite database
            conn = sqlite3.connect("wcgx.db")
            # Create a cursor object
            cursor = conn.cursor()
            # Create a list of profile fonts and their data - this will stay empty on wcgx.db creation
            profile_fonts_data = []
            for index in range(self.profile_fonts_list.count()):
                try:
                    item_text = self.profile_fonts_list.itemText(index)
                    item_data = self.profile_fonts_list.itemData(index, Qt.UserRole)
                    profile_fonts_data.append((item_text, item_data))
                except:
                    pass
            # Serialize the list data to a string using JSON
            profile_fonts_data_str = json.dumps(profile_fonts_data)
            
            # Settings to be stored in Default profile
            settings_to_insert = [
                ("Min. Font Size", self.min_font_size_slider.value()),
                ("Max. Font Size", self.max_font_size_slider.value()),
                ("Margin", self.margin_slider.value()),
                ("H. Odds", self.prefer_horizontal_slider.value()),
                ("Font Step", self.font_step_slider.value()),
                (
                    "Character Filtering",
                    self.characterFilteringOptionsGroup.checkedButton().objectName(),
                ),
                ("CLC", int(self.collocations_checkbox.isChecked())),
                ("CLC. Thresh", self.collocations_thresh_slider.value()),
                ("Repeat", int(self.repeat_checkbox.isChecked())),
                ("Color Preset", self.colormaps_dropdown.currentText()),
                ("Min Red", self.red_min.value()),
                ("Min Green", self.green_min.value()),
                ("Min Blue", self.blue_min.value()),
                ("Max Red", self.red_max.value()),
                ("Max Green", self.green_max.value()),
                ("Max Blue", self.blue_max.value()),
                ("StopWords", self.stopwords.toPlainText()),
                ("Profile Fonts", profile_fonts_data_str)
            ]
            # Text to be stored in Default profile
            text_to_insert = [
                (
                    "Default",
                    "WCGX - WordCloud Generator X-Treme",
                ),
            ]
            # Create table "Settings"
            cursor.execute(
                """
                CREATE TABLE Settings (
                    Profile TEXT NOT NULL,
                    Key TEXT NOT NULL,
                    Value,
                    PRIMARY KEY (Profile, Key)
                );
                """
            )
            # Create Text
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Text (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Profile TEXT NOT NULL,
                    Value TEXT
                );
                """
            )
            conn.commit()  # Commit the creation of the table

            # Insert Text
            for entry in text_to_insert:
                profile, value = entry
                cursor.execute(
                    """
                    INSERT INTO Text (Profile, Value) VALUES (?, ?);
                    """,
                    (profile, value),
                )
            conn.commit()  # Commit the insert transactions

            ## Insert settings
            for key, value in settings_to_insert:
                cursor.execute(
                    """
                    INSERT INTO Settings (Profile, Key, Value) VALUES ('Default', ?, ?);
                """,
                    (key, value),
                )
            # Commit the transaction
            conn.commit()
            self.refresh_SettingsList_fnc()
            self.refresh_TextSettingsList_fnc()
        else:
            self.refresh_SettingsList_fnc()
            self.refresh_TextSettingsList_fnc()

    def refresh_SettingsList_fnc(self):
        # Connect to the SQLite database
        conn = sqlite3.connect("wcgx.db")
        # Create a cursor object
        cursor = conn.cursor()
        # Populate the settingsProfiles_list QComboBox with profile names
        cursor.execute("SELECT DISTINCT Profile FROM Settings")
        all_profiles = cursor.fetchall()
        # Clear the QComboBox before adding new items
        self.settingsProfiles_list.clear()
        for profile in all_profiles:
            self.settingsProfiles_list.addItem(profile[0])
        # Close the database connection
        conn.close()

    def refresh_TextSettingsList_fnc(self):
        # Connect to the SQLite database
        conn = sqlite3.connect("wcgx.db")
        # Create a cursor object
        cursor = conn.cursor()
        # Populate the settingsProfiles_list QComboBox with profile names
        cursor.execute("SELECT DISTINCT Profile FROM Text")
        all_profiles = cursor.fetchall()
        self.textProfiles_list.clear()
        for profile in all_profiles:
            self.textProfiles_list.addItem(profile[0])
        # Close the database connection
        conn.close()

    def return_SettingsProfiles_fnc(self, profile, key):
        # Connect to the SQLite database
        conn = sqlite3.connect("wcgx.db")
        cursor = conn.cursor()

        # Prepare the SQL query to select the value
        cursor.execute(
            "SELECT Value FROM Settings WHERE Profile=? AND Key=?", (profile, key)
        )

        result = cursor.fetchone()

        # Close the database connection
        conn.close()

        # Return the profile names
        if result:
            if key == "Profile Fonts":
                profile_fonts_data = json.loads(result[0])  # Deserialize the stored JSON string
                return profile_fonts_data
            else:
                return result[0]
        else:
            return None

    def return_TextProfiles_fnc(self, profile):
        conn = sqlite3.connect("wcgx.db")
        cursor = conn.cursor()

        cursor.execute("SELECT Value FROM Text WHERE Profile=?", (profile,))

        result = (
            cursor.fetchone()
        )  # fetchone() since there's only one entry per profile

        conn.close()

        return result[0] if result else None

    def apply_SettingsProfile_fnc(self):
        if self.settingsProfiles_list.currentText():
            destination_folder = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Destination Folder"
            )
            min_font_size = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Min. Font Size"
            )
            max_font_size = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Max. Font Size"
            )
            margin = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Margin"
            )
            horizontal_odds = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "H. Odds"
            )
            font_step = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Font Step"
            )
            char_filtering = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Character Filtering"
            )
            clc = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "CLC"
            )
            clc_thresh = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "CLC. Thresh"
            )
            repeat = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Repeat"
            )
            color_preset = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Color Preset"
            )
            min_red = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Min Red"
            )
            min_green = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Min Green"
            )
            min_blue = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Min Blue"
            )
            max_red = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Max Red"
            )
            max_green = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Max Green"
            )
            max_blue = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Max Blue"
            )
            stopwords = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "StopWords"
            )
            profile_fonts = self.return_SettingsProfiles_fnc(
                self.settingsProfiles_list.currentText(), "Profile Fonts"
            )
            # Apply settings
            self.min_font_size_slider.setValue(min_font_size)
            self.max_font_size_slider.setValue(max_font_size)
            self.margin_slider.setValue(margin)
            self.prefer_horizontal_slider.setValue(horizontal_odds)
            self.font_step_slider.setValue(font_step)
            getattr(self, char_filtering).setChecked(True)
            self.collocations_checkbox.setChecked(clc)
            self.collocations_thresh_slider.setValue(clc_thresh)
            self.repeat_checkbox.setChecked(repeat)
            self.colormaps_dropdown.setCurrentText(color_preset)
            self.red_min.setValue(min_red)
            self.green_min.setValue(min_green)
            self.blue_min.setValue(min_blue)
            self.red_max.setValue(max_red)
            self.green_max.setValue(max_green)
            self.blue_max.setValue(max_blue)
            self.destination_path = destination_folder
            self.stopwords.setText(stopwords)
            # Apply stored profile fonts, if any
            # Clear the existing items in the list
            self.profile_fonts_list.clear()

            # Populate the list with the fetched "Profile Fonts"
            try:
                for item_text, item_data in profile_fonts:
                    self.profile_fonts_list.addItem(item_text, item_data)
            except:
                pass

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
            self.enable_WordCloud_Generator_Button()

    def applyTextProfile_fnc(self):
        profile = self.textProfiles_list.currentText()
        text_entry = self.return_TextProfiles_fnc(profile)
        if text_entry:
            self.word_input.setText(text_entry)

    def storeProfile_fnc(self):
        # Identify the button that was clicked
        button = self.sender()
        self.storeProfile_window.label_x.setVisible(False)
        # Disconnect button from function (if already exists)
        try:
            self.storeProfile_window.okay_store_btn.clicked.disconnect()
        except:
            pass
        if button.objectName() == "storeSettingsProfile_btn":
            self.storeProfile_window.show()
            self.storeProfile_window.okay_store_btn.clicked.connect(
                self.storeSettingsProfileOkAction
            )
        if (
            button.objectName() == "storeTextProfile_btn"
            or button.objectName() == "storeTextProfile_btn2"
        ):
            if self.word_input.toPlainText() != "":
                self.storeProfile_window.show()
                self.storeProfile_window.okay_store_btn.clicked.connect(
                    self.storeTextProfileOkAction
                )
            else:
                self.error_window.error_lbl.setText(
                    f"\n # Error:\nMaybe add some text first, then you can store it."
                )
                self.error_window.show()
                self.error_window.adjustSize()

    def storeSettingsProfileOkAction(self):
        if self.storeProfile_window.profile_name.toPlainText() != "":
            # Connect to the SQLite database
            conn = sqlite3.connect("wcgx.db")
            # Create a cursor object
            cursor = conn.cursor()
            # Create a list of profile fonts and their data
            profile_fonts_data = []
            for index in range(self.profile_fonts_list.count()):
                try:
                    item_text = self.profile_fonts_list.itemText(index)
                    item_data = self.profile_fonts_list.itemData(index, Qt.UserRole)
                    profile_fonts_data.append((item_text, item_data))
                except:
                    pass
            # Serialize the list data to a string using JSON
            profile_fonts_data_str = json.dumps(profile_fonts_data)
            # Settings to be stored in profile
            settings_to_insert = [
                ("Destination Folder", self.destination_path),
                ("Min. Font Size", self.min_font_size_slider.value()),
                ("Max. Font Size", self.max_font_size_slider.value()),
                ("Margin", self.margin_slider.value()),
                ("H. Odds", self.prefer_horizontal_slider.value()),
                ("Font Step", self.font_step_slider.value()),
                (
                    "Character Filtering",
                    self.characterFilteringOptionsGroup.checkedButton().objectName(),
                ),
                ("CLC", int(self.collocations_checkbox.isChecked())),
                ("CLC. Thresh", self.collocations_thresh_slider.value()),
                ("Repeat", int(self.repeat_checkbox.isChecked())),
                ("Color Preset", self.colormaps_dropdown.currentText()),
                ("Min Red", self.red_min.value()),
                ("Min Green", self.green_min.value()),
                ("Min Blue", self.blue_min.value()),
                ("Max Red", self.red_max.value()),
                ("Max Green", self.green_max.value()),
                ("Max Blue", self.blue_max.value()),
                ("StopWords", self.stopwords.toPlainText()),
                ("Profile Fonts", profile_fonts_data_str)
            ]
            # Get the profile name from the user input
            profile_name = (
                self.storeProfile_window.profile_name.toPlainText().strip().capitalize()
            )

            # Insert settings with the user-provided profile name
            for key, value in settings_to_insert:
                cursor.execute(
                    """
                INSERT OR REPLACE INTO Settings (Profile, Key, Value) VALUES (?, ?, ?);
                """,
                    (profile_name, key, value),
                )

            # Commit the transaction
            conn.commit()

            self.storeProfile_window.close()
            # Refresh the settings list
            self.refresh_SettingsList_fnc()
            # Select the stored profile in Setting Profile dropdown
            self.settingsProfiles_list.setCurrentText(profile_name)
        else:
            self.error_window.error_lbl.setText(
                f"\n # Error:\nProfile name cannot be blank"
            )
            self.error_window.show()
            self.error_window.adjustSize()
        self.storeProfile_window.profile_name.setPlainText("")
    
    def storeTextProfileOkAction(self):
        profile_name = (
            self.storeProfile_window.profile_name.toPlainText().strip().capitalize()
        )
        text = self.word_input.toPlainText()

        if profile_name != "":
            # Connect to the database
            conn = sqlite3.connect("wcgx.db")
            cursor = conn.cursor()

            # Check if the profile already exists
            cursor.execute(
                "SELECT COUNT(*) FROM Text WHERE Profile = ?", (profile_name,)
            )
            exists = cursor.fetchone()[0] > 0

            if exists:
                # Update the existing profile's text
                cursor.execute(
                    "UPDATE Text SET Value = ? WHERE Profile = ?", (text, profile_name)
                )
            else:
                # Insert a new profile with the user-provided text
                cursor.execute(
                    "INSERT INTO Text (Profile, Value) VALUES (?, ?)",
                    (profile_name, text),
                )

            conn.commit()  # Commit the transaction
            conn.close()  # Close the database connection
            self.storeProfile_window.close()
            # Refresh the settings list
            self.refresh_TextSettingsList_fnc()
            self.textProfiles_list.setCurrentText(profile_name)
        else:
            self.error_window.error_lbl.setText(
                "\n # Error:\nProfile name cannot be blank"
            )
            self.error_window.show()
            self.error_window.adjustSize()
        self.storeProfile_window.profile_name.setPlainText("")
    
    def update_selected_settings_profile(self):
        self.are_you_sure_window.label_x.setText(f"You are about to update -{self.settingsProfiles_list.currentText()}- Profile with the current settings.\n\nContinue?")
        self.are_you_sure_window.okay_store_btn.clicked.connect(self.update_selected_settings_profile_OK)
        self.are_you_sure_window.cancel_store_btn.clicked.connect(lambda _ : self.are_you_sure_window.close())
        self.are_you_sure_window.show()
    
    def update_selected_settings_profile_OK(self):
        if self.settingsProfiles_list.currentText():
            # Connect to the SQLite database
            conn = sqlite3.connect("wcgx.db")
            # Create a cursor object
            cursor = conn.cursor()
            # Create a list of profile fonts and their data
            profile_fonts_data = []
            for index in range(self.profile_fonts_list.count()):
                try:
                    item_text = self.profile_fonts_list.itemText(index)
                    item_data = self.profile_fonts_list.itemData(index, Qt.UserRole)
                    profile_fonts_data.append((item_text, item_data))
                except:
                    pass
            # Serialize the list data to a string using JSON
            profile_fonts_data_str = json.dumps(profile_fonts_data)
            # Settings to be stored in profile
            settings_to_insert = [
                ("Destination Folder", self.destination_path),
                ("Min. Font Size", self.min_font_size_slider.value()),
                ("Max. Font Size", self.max_font_size_slider.value()),
                ("Margin", self.margin_slider.value()),
                ("H. Odds", self.prefer_horizontal_slider.value()),
                ("Font Step", self.font_step_slider.value()),
                (
                    "Character Filtering",
                    self.characterFilteringOptionsGroup.checkedButton().objectName(),
                ),
                ("CLC", int(self.collocations_checkbox.isChecked())),
                ("CLC. Thresh", self.collocations_thresh_slider.value()),
                ("Repeat", int(self.repeat_checkbox.isChecked())),
                ("Color Preset", self.colormaps_dropdown.currentText()),
                ("Min Red", self.red_min.value()),
                ("Min Green", self.green_min.value()),
                ("Min Blue", self.blue_min.value()),
                ("Max Red", self.red_max.value()),
                ("Max Green", self.green_max.value()),
                ("Max Blue", self.blue_max.value()),
                ("StopWords", self.stopwords.toPlainText()),
                ("Profile Fonts", profile_fonts_data_str)
            ]
            # Get the profile name from the user input
            profile_name = (
                self.settingsProfiles_list.currentText()
            )

            # Insert settings with the user-provided profile name
            for key, value in settings_to_insert:
                cursor.execute(
                    """
                INSERT OR REPLACE INTO Settings (Profile, Key, Value) VALUES (?, ?, ?);
                """,
                    (profile_name, key, value),
                )

            # Commit the transaction
            conn.commit()
        self.are_you_sure_window.okay_store_btn.clicked.disconnect()
        self.are_you_sure_window.cancel_store_btn.clicked.disconnect()
        self.are_you_sure_window.label_x.setText("")
        self.are_you_sure_window.close()

    def cancelSettingsStorage_fnc(self):
        self.storeProfile_window.profile_name.setPlainText("")
        self.storeProfile_window.close()

    def open_fs_window_fnc(self):
        self.fs_window.show()


class DeleteProfileWindow(widget.QDialog, Ui_StoreProfileWindow):
    def __init__(self, wcgx):
        super().__init__()
        self.setupUi(self)
        self.main_window = wcgx

        self.main_window.deleteSettingsProfile_btn.clicked.connect(
            self.initDeleteProfile_fnc
        )
        self.main_window.deleteTextProfile_btn.clicked.connect(
            self.initDeleteProfile_fnc
        )
        self.cancel_store_btn.clicked.connect(self.cancelDeleteProfile_fnc)

    def cancelDeleteProfile_fnc(self):
        self.close()

    def deleteSettingsProfile(self):
        profile_name = self.main_window.settingsProfiles_list.currentText()

        conn = sqlite3.connect("wcgx.db")  # Connect to the database
        cursor = conn.cursor()

        # Delete the profile
        cursor.execute("DELETE FROM Settings WHERE Profile = ?", (profile_name,))
        conn.commit()  # Commit the delete transaction
        conn.close()  # Close the database connection
        self.close()
        # Refresh the settings list
        self.main_window.refresh_SettingsList_fnc()

    def deleteTextProfile(self):
        profile_name = (
            self.main_window.textProfiles_list.currentText()
        )  # Get selected profile name
        conn = sqlite3.connect("wcgx.db")  # Connect to the database
        cursor = conn.cursor()
        # Delete the profile
        cursor.execute("DELETE FROM Text WHERE Profile = ?", (profile_name,))
        conn.commit()  # Commit the delete transaction
        conn.close()  # Close the database connection
        self.close()
        # Refresh the settings list
        self.main_window.refresh_TextSettingsList_fnc()

    def initDeleteProfile_fnc(self):
        button = self.sender()
        self.profile_name.hide()
        self.cancel_store_btn.setText("Cancel")
        self.okay_store_btn.setText("Delete")
        self.okay_store_btn.setStyleSheet("background-color:#141414; color:red;")
        self.cancel_store_btn.setStyleSheet("background-color:#e6e6e6; color:#141414;")
        self.setWindowTitle("Delete Profile")
        self.setStyleSheet("background-color:red;")
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        # Disconnect any existing functions from button
        try:
            self.okay_store_btn.clicked.disconnect()
        except:
            pass
        if (
            button.objectName() == "deleteSettingsProfile_btn"
            and self.main_window.settingsProfiles_list.currentText() is not ""
        ):
            self.okay_store_btn.clicked.connect(self.deleteSettingsProfile)
            self.label_x.setText(
                f'You are about to delete the Settings stored in "{self.main_window.settingsProfiles_list.currentText()}" profile.\nAre you sure?\nThis cannot be undone!\n\n\n'
            )
            self.adjustSize()
            self.show()

        if (
            button.objectName() == "deleteTextProfile_btn"
            and self.main_window.textProfiles_list.currentText() is not ""
        ):
            self.okay_store_btn.clicked.connect(self.deleteTextProfile)
            self.label_x.setText(
                f'You are about to delete the Text stored in "{self.main_window.textProfiles_list.currentText()}" profile.\nAre you sure?\nThis cannot be undone!\n\n\n'
            )
            self.adjustSize()
            self.show()


if __name__ == "__main__":
    app = widget.QApplication(sys.argv)
    window = WCGX()
    window.show()
    sys.exit(app.exec())
