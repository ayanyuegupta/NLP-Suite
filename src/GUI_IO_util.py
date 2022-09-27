import sys
# import GUI_util
# import IO_libraries_util
# if not IO_libraries_util.install_all_packages(GUI_util.window,"GUI_IO_util", ['tkinter', 'os']):
#     sys.exit(0)

import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

import config_util
import IO_libraries_util

# import IO_internet_util
# import webbrowser

NLP_Suite_website_name = 'NLP Suite GitHub'
# HELP messages

introduction_main = "Welcome to this Python 3 script.\nFor brief general information about this script, click on the \"Read Me\" button.\nFor brief information on specific lines click on any of the \"?HELP\" buttons.\nFor longer information on various aspects of the script, click on the \"Open TIPS files\" button and select the pdf help file to view.\nAfter selecting an option, click on \"RUN\" (the RUN button is disabled until all I/O information has been entered).   Click on \"CLOSE\" to exit."
# msg_fileButtonDisabled="\n\nIf the Select INPUT file button is greyed out because you previously selected an INPUT directory but you now wish to use a file as input, click on the Select INPUT directory button and press ESCape to make all INPUT options available."
# msg_dirButtonDisabled="\n\nIf the Select INPUT directory button is greyed out because you previously selected an INPUT file but you now wish to use a directory as input, click on the Select INPUT file button and press ESCape to make all INPUT options available."
msg_openExplorer="\n\nA small button appears next to the select directory button. Click on the button to open Windows Explorer on the directory displayed, if one is displayed, or on the directory where the NLP script is saved."
msg_openFile="\n\nA small button appears next to the select file button. Click on the button to open the file, if one has been selected, as a check that you selected the correct file." # + msg_fileButtonDisabled
msg_Esc="\n\nPress the ESCape button to clear any previously selected options and start fresh."

msg_IO_config="The default or GUI-specific config files are 2-columns csv files with the 4 I/O labels - Input filename with path, Input files directory, Input files secondary directory, Output files directory - in the first column and the file or directory path in the second column.\n\nThe fields Input filename with path and Input files directory are MUTUALLY EXCLUSIVE. YOU CAN ONLY HAVE ONE OR THE OTHER BUT NOT BOTH.\n\nA couple of scripts in the NLP Suite require two input directories (e.g., for source and target files, as in social_science_researh_main and file_classifier_main)\n\nCONFIG FILES ARE STORED IN THE SUBDIRECTORY config OF THE MAIN NLP SUITE DIRECTORY."

msg_IO_setup="Please, using the dropdown menu, select the type of INPUT/OUTPUT configuration you wish to use in this GUI: Default I/O configuration or GUI-specific I/O configuration.\n\nEach option will allow you to select and INPUT file or directory where the files(s) to be used in input are stored and an OUTPUT directory where files produced by the NLP tools will be saved (csv, txt, html, kml, jpg).\n\n   The default configuration is the I/O option used for all GUIs as default;\n   the GUI-specific I/O configuration is an alternative I/O option only used in a specific GUI.\n\nYou can click on the display area and scroll to visualize the current configuration. You can also click on the 'Setup INPUT/OUTPUT configuration' button to get a better view of the available options.\n\nClick on the small buttons to the right of the I/O display area to open the input file, the input directory, the output directory displayed, and the config file where these options are saved. "+msg_IO_config
msg_CoreNLP="Please, select the directory where you downloaded the Stanford CoreNLP software.\n\nYou can download Stanford CoreNLP from https://stanfordnlp.github.io/CoreNLP/download.html\n\nYou can place the Stanford CoreNLP folder anywhere on your machine. But... on some machines CoreNLP will not run unless the folder is inside the NLP folder.\n\nIf you suspect that CoreNLP may have given faulty results for some sentences, you can test those sentences directly on the Stanford CoreNLP website at https://corenlp.run\n\nYOU MUST BE CONNECTED TO THE INTERNET TO RUN CoreNLP."
msg_WordNet="Please, select the directory where you downloaded the WordNet lexicon database.\n\nYou can download WordNet from https://wordnet.princeton.edu/download/current-version."
msg_Mallet="Please, select the directory where you downloaded the MALLET topic modeling software."
msg_CoNLL="Please, select a csv CoNLL table that you would like to analyze.\n\nA CoNLL table is a file generated by the Python script StanfordCoreNLP.py. The CoreNLP script parses a set of text documents using the Stanford CoreNLP parser, providing a dependency tree for each sentence of the documents. In a CoNLL table, each token is labeled with a part-of-speech tag (POSTAG), a Dependency Relation tag (DEPREL), its dependency relation within the corresponding dependency tree, and other useful information." + msg_openFile
msg_corpusData="Please, select the directory where you store your TXT corpus to be analyzed. ALL TXT FILES PRESENT IN THE DIRECTORY WILL BE PARSED. NON TXT FILES WILL BE IGNORED. MOVE ANY TXT FILES YOU DO NOT WISH TO PROCESS TO A DIFFERENT DIRECTORY."  + msg_openExplorer # + msg_dirButtonDisabled
msg_anyData="Please, select the directory where you store the files to be analyzed. ALL FILES OF A SELECTED EXTENSION TYPE (pdf, docx, txt, csv, conll), PRESENT IN THE DIRECTORY WILL BE PROCESSED. ALL OTHER FILE TYPES WILL BE IGNORED."  + msg_openExplorer # + msg_dirButtonDisabled
msg_anyFile="Please, select the file to be analyzed (of any type: pdf, docx, txt, csv, conll)."  + msg_openFile
msg_txtFile="Please, select the TXT file to be analyzed." + msg_openFile # + msg_fileButtonDisabled
msg_csvFile="Please, select the csv file to be analyzed." + msg_openFile # + msg_fileButtonDisabled
msg_csv_txtFile="Please, select either a CSV file or a TXT file to be analyzed." + msg_openFile # + msg_fileButtonDisabled
msg_txt_htmlFile="Please, select either a TXT file or an html file to be analyzed." + msg_openFile # + msg_fileButtonDisabled
msg_outputDirectory="Please, select the directory where the script will save all OUTPUT files of any type (txt, csv, png, html)."  + msg_openExplorer
msg_outputFilename="Please, enter the OUTPUT file name. THE SELECT OUTPUT BUTTON IS DISABLED UNTIL A SEARCHED TOKEN HAS BEEN ENTERED.\n\nThe search result will be saved as a separated csv file with the file path and name entered. \n\nThe same information will be displayed in the command line."
msg_openOutputFiles="Please, tick the checkbox to open automatically (or not open) output csv file(s), including any Excel charts.\n\nIn the NLP Suite, all CSV FILES that contain information on web links or files with their path will encode this information as hyperlinks. If you click on the hyperlink, it will automatically open the file or take you to a website. IF YOU ARE A MAC USER, YOU MUST OPEN ALL CSV FILES WITH EXCEL, RATHER THAN NUMBERS, OR THE HYPERLINK WILL BE BARRED AND DISPLAYED AS A RED TRIANGLE.\n\nEXCEL HOVER-OVER EFFECT.  Most Excel charts have been programmed for hover-over effects, whereby when you pass the cursor over a point on the chart (hover over) some releveant information will be displayed (e.g., the sentence at that particular point).\n\nEXCEL EMPTY CHART AREA.  If the hover-over chart area is empty, with no chart displayed, enlarge the chart area by dragging any of its corners or by moving the zoom slide bar on the bottomg right-hand corner of Excel.\n\nEXCEL ENABLE MACROS.  The hover-over effect is achieved using VBA macros (Virtual Basic for Applications, Windows programming language). If Excel warns you that you need to enable macros, while at the same time warning you that macros may contain viruses, do the following: open an Excel workbook; click on File; slide cursor all the way down on the left-hand banner to Options; click on Trust Center; then on Trust Center Settings; then Macro Settings; Click on Enable all macros, then OK. The message will never appear again."
msg_multipleDocsCoNLL="\n\nFOR CONLL FILES THAT INCLUDE MULTIPLE DOCUMENTS, THE EXCEL CHARTS PROVIDE OVERALL FREQUENCIES ACROSS ALL DOCUMENTS. FOR SPECIFIC DOCUMENT ANALYSES, PLEASE USE THE GENERAL EXCEL OUTPUT FILE."

# location of this src python file
#one folder UP, the NLP folder
#subdirectory of script directory where config files are saved
#subdirectory of script directory where lib files are saved
#subdirectory of script directory where Google maps lib files are saved
#subdirectory of script directory where Excel lib files are saved
#subdirectory of script directory where lib files are saved
#subdirectory of script directory where lib files are saved
#subdirectory of script directory where lib files are saved
#subdirectory of script directory where gender names are saved
#global TIPSPath
#subdirectory of script directory where reminders file is saved

scriptPath = os.path.dirname(os.path.abspath(__file__))
NLPPath=os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir)
configPath = os.path.join(NLPPath,'config')
libPath = os.path.join(NLPPath,'lib')
image_libPath = os.path.join(NLPPath,'lib'+os.sep+'images')
Google_heatmaps_libPath = os.path.join(NLPPath,'lib'+os.sep+'sampleHeatmap')
Excel_charts_libPath = os.path.join(NLPPath,'lib'+os.sep+'sampleCharts')
sampleData_libPath = os.path.join(NLPPath,'lib'+os.sep+'sampleData')
sentiment_libPath = os.path.join(NLPPath,'lib'+os.sep+'sentimentLib')
concreteness_libPath = os.path.join(NLPPath,'lib'+os.sep+'concretenessLib')
CoreNLP_enhanced_dependencies_libPath = os.path.join(NLPPath,'lib'+os.sep+'CoreNLP_enhanced_dependencies')
wordLists_libPath = os.path.join(NLPPath,'lib'+os.sep+'wordLists')
namesGender_libPath = os.path.join(NLPPath, 'lib'+os.sep+'namesGender')
GISLocations_libPath = os.path.join(NLPPath,'lib'+os.sep+'GIS')
TIPSPath = os.path.join(NLPPath,'TIPS')
videosPath = os.path.join(NLPPath,'videos')
remindersPath = os.path.join(NLPPath, 'reminders')

# The function places and displays a message for each ? HELP button in the GUIs
def place_help_button(window,x_coordinate,y_coordinate,text_title,text_info):
    help_button = tk.Button(window, text='? HELP', command=lambda: display_help_button_info(text_title, text_info))
    # place widget with hover-over info
    y_multiplier_integer = placeWidget(window, x_coordinate,
                                                   y_coordinate,
                                                   help_button, False, False, False, False, 90,
                                                   help_button_x_coordinate,
                                                   "Press the ?HELP button to get information about what you can do on this line of the GUI.\n"
                                                   "Press the Read Me button to get general information about what the algorithms behind this GUI are meant to do.")

    # y_multiplier_integer = placeWidget(window,x_coordinate,y_coordinate,help_button,False,False,True)
    return y_multiplier_integer

# The function displays the info for any bottom (e.g., ? HELP and ReadMe) in the GUIs
def display_help_button_info(text_title,text_info):
    mb.showinfo(title=text_title, message=text_info)

def display_widget_info(window, e, x_coordinate, y_coordinate, x_coordinate_hover_over, text_info):
    # background = 'red' sets the whole widget in red
    # TODO Must left justify rather than center the info displayed
    display_window_lb = tk.Label(window, anchor='w', text=text_info, name='display_window_lb',
                                 foreground='blue')
    display_window_lb.place(anchor='w', x=x_coordinate_hover_over, y=y_coordinate)

def delete_display_widget_lb(window, e, text_info):
    if text_info != '':
        window.nametowidget('display_window_lb').place_forget()

# https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# called by place_widget which is called in every GUI
def hover_over_widget(window, x_coordinate, y_coordinate, widget_name, no_hover_over_widget=False,
                    whole_widget_red=False, x_coordinate_hover_over= 90, text_info=''):
    if no_hover_over_widget:
        return
    # hover-over effect
    # background = 'red' sets the whole widget in red
    # background='#F0F0F0' sets the widget in grey
    # foreground='red' (or any color) sets the color of a widget wording to a selected color
    # activeforeground='red' it sets to red the wording in the currently active widget wordings

    # 'label' in str(widget_name)
    # 'text' in str(widget_name)
    # 'entry' in str(widget_name)
    # 'checkbutton' in str(widget_name)
    # 'combobox' in str(widget_name) is the ttk menu object
    # 'scale' in str(widget_name)

# --------------------------------------------------------------------

    # on colors available in tkinter

    #   https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix

# --------------------------------------------------------------------

    # scale, text, and combobox widgets do not have a label and code would break below
    # wording is the wording of the text value displayed in a widget (e.g, RUN, CLOSE,
    #   or, for a menu, the item currently displayed in the menu, e.g., mm/dd/yyyy for a date menu)
    if 'scale' in str(widget_name) or \
        'text' in str(widget_name) or \
        'combobox' in str(widget_name):
        wording = ''
    else:
        wording = widget_name.cget('text')

    # colors: get the original colors because must reset widget to the original color upon leaving at the end
    if widget_name.cget('background')!='#F0F0F0' and widget_name.cget('background')!='red' : # light grey
        background_color = '#F0F0F0'
    else:
        background_color = widget_name.cget('background')

    if widget_name.cget('foreground')!='black' and widget_name.cget('foreground')!='red':
        foreground_color = 'black'
    else:
        foreground_color = widget_name.cget('foreground')

    original_foreground_color = foreground_color
    if foreground_color == 'black':
        change_foreground_color = 'red'
    else:
        change_foreground_color = 'black'

    if wording != '':
        original_foreground_color = widget_name.cget('foreground')
        original_background_color = widget_name.cget('background')
    else:
        original_background_color = widget_name.cget('background')

    # optionmenu widgets with no item displayed, i.e., ='', are set to red
    if 'optionmenu' in str(widget_name):
        if wording == '':
            background_color = 'red'

    # # the background_color is always set to red if the parameter is true
    # # all buttons are also turned red unless disabled
    if (whole_widget_red or ('button' in str(widget_name))) and (widget_name.cget('state') == 'normal'):
        background_color = 'red'
        change_foreground_color = 'black'

    # TODO unfortunately widget_name.cget('state') is measured when it is placed on the GUI
    #   any change to the widget state because of user's actions in the GUI
    #   will not be reflected in the colors displayed
    #   thus, if a checkbutton is normal when placed on the GUI and displayed in red when hovering over
    #       it will always be displayed in red, and not in sea green, if user's actions disables the widget
    # labels and disabled widgets are set to green to distinguish them from all other widgets
    if 'label' in str(widget_name) or widget_name.cget('state') == 'disabled':
        background_color = 'light sea green'
        # the next command does not seem to work as it does not display the wording of the widget
        change_foreground_color = 'black'


# Enter the widget ----------------------------------------------------------

# no text info available to be displayed ------------------------------------------------------
    if text_info == '': # no text info to be displayed
        if 'optionmenu' in str(widget_name):
            # print('widget_name','wording',wording,widget_name,'state',widget_name.cget('state') == 'disabled')
            widget_name.bind('<Enter>', lambda e: e.widget.config(background=background_color,
                    activeforeground=change_foreground_color, foreground=change_foreground_color))
        else:
            widget_name.bind('<Enter>', lambda e: e.widget.config(background=background_color,
                    foreground=change_foreground_color))

# text info available -------------------------------------------------------------------------
    else: # there is text info to be displayed
        # these are the y coordinates where the text info is displayed
        # move up the display if the ino contains line breaks
        # there should not be more than 2 line breaks
        number_of_lines = text_info.count('\n')
        if number_of_lines == 0:
            y_coordinate = y_coordinate - 20
        elif number_of_lines == 1:
            y_coordinate = y_coordinate - 25
        elif number_of_lines == 2:
            y_coordinate = y_coordinate - 30

        # combobox is the ttk menu object; the regular config breaks
        # https://stackoverflow.com/questions/71733010/ttkcombobox-foreground-color-change-doesnt-work-properly-whats-wrong
        color = widget_name.cget('background')
        # for ttk combox objects
        #   from tkinter import ttk
        #   print(ttk.Style().lookup('TButton', 'background'))
        if 'combobox' in str(widget_name):
            # TODO the widget should be turned red but it is in blue
            widget_name.bind('<Enter>',
                 lambda e: (e.widget.config(ttk.Style().map(
                        'Red.TCombobox',
                        foreground=[('readonly', 'red')],
                        selectforeground=[('readonly', 'red')])),
                            display_widget_info(window, e, x_coordinate,
                                                y_coordinate,
                                                x_coordinate_hover_over,
                                                text_info)))
        elif 'optionmenu' in str(widget_name):
            # activeforeground sems to available only for optionmenu
            widget_name.bind('<Enter>',
                 lambda e: (e.widget.config(background=background_color, activeforeground=change_foreground_color, foreground=change_foreground_color),
                            display_widget_info(window, e, x_coordinate,
                                                y_coordinate,
                                                x_coordinate_hover_over,
                                                text_info)))
        else:
            widget_name.bind('<Enter>',
                 lambda e: (e.widget.config(background=background_color, foreground=change_foreground_color),
                            display_widget_info(window, e, x_coordinate,
                                                y_coordinate,
                                                x_coordinate_hover_over,
                                                text_info)))

# Leave the widget ----------------------------------------------------------
    # TODO does not work
    # https://stackoverflow.com/questions/69549437/combobox-foreground-color-setting-is-lost-when-navigating-out-through-tab-key
    # if "combobox" in str(widget_name):
    #     if label != "":
    #         widget_name.bind('<Leave>',
    #                     lambda e: ttk.Style().map("myCombobox.TCombobox",
    #                         selectforeground=[('readonly', 'red')],
    #                         foreground=[('readonly', 'red')]),
    #                     lambda e: delete_display_widget_lb(window, e, text_info))
    widget_name.bind('<Leave>',
                     # upon leaving you must resume/reset the original colors of the widget
                     #  as set in original_background_color and original_foreground_color
                     lambda e: (e.widget.config(background=original_background_color, foreground=original_foreground_color),
                                   delete_display_widget_lb(window, e, text_info)))


# when a widget has hover-over effects, the parameter no_hover_over_widget is set to False
# widget_name is the name of the widget that needs to be placed in any of the GUI scripts as defined by tk.
def placeWidget(window,x_coordinate,y_multiplier_integer,widget_name,sameY=False, no_hover_over_widget=False, whole_widget_red=False, centerX=False, basic_y_coordinate=90, x_coordinate_hover_over = 90, text_info=''):
    # print("widget_name",widget_name,"text_info",text_info)
    #basic_y_coordinate = 90
    y_step = 40 #the line-by-line increment on the GUI
    if centerX:
        widget_name.place(relx=0.5, anchor=tk.CENTER, y=basic_y_coordinate + y_step*y_multiplier_integer)
    else:
        widget_name.place(x=x_coordinate, y=basic_y_coordinate + y_step*y_multiplier_integer)
    # use the following command to change the color of any label to any value
    # widget_name.config(foreground='red')

    # when a widget has hover-over effects, the parameter no_hover_over_widget is set to False
    hover_over_widget(window,x_coordinate, basic_y_coordinate + y_step*y_multiplier_integer,widget_name, no_hover_over_widget, whole_widget_red, x_coordinate_hover_over, text_info)

    if sameY==False:
        y_multiplier_integer = y_multiplier_integer+1
    return y_multiplier_integer

if sys.platform == 'darwin': #Mac OS
    about_button_x_coordinate = 330 # get_labels_x_coordinate() + 100
    release_history_button_x_coordinate = 510 # get_labels_x_coordinate() + 100
    team_button_x_coordinate = 690 # get_labels_x_coordinate() + 100
    cite_button_x_coordinate = 870 # get_labels_x_coordinate() + 100

    help_button_x_coordinate = 70
    labels_x_coordinate = 150  # start point of all labels in the second column (first column after ? HELP)
    labels_x_indented_coordinate = 160
    select_file_directory_button_width=23
    open_file_directory_button_width = 1
    IO_button_name_width=1
    open_file_directory_coordinate = 400
    entry_box_x_coordinate = 470 #start point of all labels in the third column (second column after ? HELP); where IO filename, dir, etc. are displayed
    read_button_x_coordinate = 70
    watch_videos_x_coordinate = 200
    open_TIPS_x_coordinate = 370
    open_reminders_x_coordinate = 570
    open_setup_x_coordinate = 770
    run_button_x_coordinate = 940
    close_button_x_coordinate = 1070

    open_IO_config_button = 650
    open_NLP_package_language_config_button = 650
    open_setup_software_button = 650

    open_file_button_brief = 700
    open_inputDir_button_brief = 740
    open_outputDir_button_brief = 780
    open_config_file_button_brief = 820

    # special internal GUI specific values MAC
    # SVO_main Mac
    SVO_1st_column = 120
    open_S_dictionary = 260
    lemmatize_S = 320
    SVO_2nd_column = 520# filter & dictionary options for Verbs
    open_V_dictionary = 640
    lemmatize_V = 700
    SVO_3rd_column = 920 # filter & dictionary options for Objects
    open_O_dictionary = 1050
    lemmatize_O = 1110

    SVO_2nd_column_top = 400
    SVO_3rd_column_top = 800

    dictionary_S_width=60
    dictionary_V_width=60
    dictionary_O_width=60

    # Mac NLP_setup_package_language_main
    language_widget_with=50
    plus_column = 982
    reset_column = 1035
    show_column = 1115

    # CoNLL_table_analyzer_main
    combobox_position = 210
    combobox_width = 40

else: #windows and anything else
    about_button_x_coordinate = 230 # get_labels_x_coordinate() + 100
    release_history_button_x_coordinate = 400 # get_labels_x_coordinate() + 100
    team_button_x_coordinate = 570 # get_labels_x_coordinate() + 100
    cite_button_x_coordinate = 740 # get_labels_x_coordinate() + 100
    help_button_x_coordinate = 70
    help_button_x_coordinate = 50
    labels_x_coordinate = 120  # start point of all labels in the second column (first column after ? HELP)
    labels_x_indented_coordinate = 140
    select_file_directory_button_width=30
    IO_button_name_width=30
    open_file_directory_button_width = 3
    open_file_directory_coordinate = 350
    entry_box_x_coordinate = 400 #start point of all labels in the third column (second column after ? HELP)
    read_button_x_coordinate = 50
    watch_videos_x_coordinate = 170
    open_TIPS_x_coordinate = 350
    open_reminders_x_coordinate = 550
    open_setup_x_coordinate = 750
    run_button_x_coordinate = 940
    close_button_x_coordinate = 1050

    open_IO_config_button = 820
    open_NLP_package_language_config_button = 820
    open_setup_software_button = 820

    open_file_button_brief = 760
    open_inputDir_button_brief = 800
    open_outputDir_button_brief = 840
    open_config_file_button_brief = 880

    # special internal GUI specific values WINDOWS

    # Windows NLP_setup_package_language_main
    language_widget_with=70
    plus_column = 920
    reset_column = 960
    show_column = 1020

    # SVO_main Windows
    SVO_1st_column = 120
    open_S_dictionary = 260
    lemmatize_S = 320
    SVO_2nd_column = 520# filter & dictionary options for Verbs
    open_V_dictionary = 640
    lemmatize_V = 700
    SVO_3rd_column = 920 # filter & dictionary options for Objects
    open_O_dictionary = 1050
    lemmatize_O = 1110

    SVO_2nd_column_top = 400
    SVO_3rd_column_top = 800

    dictionary_S_width=60
    dictionary_V_width=60
    dictionary_O_width=60

    # CoNLL_table_analyzer_main
    combobox_position = 200
    combobox_width = 50

basic_y_coordinate = 90
y_step = 40 #the line-by-line increment on the GUI

def get_GUI_width(size_type=1):
    if sys.platform == 'darwin':  # Mac OS
        if size_type == 1: # for now we have one basic size
            return 1400
        if size_type == 2:
            return 1400
        if size_type == 3:
            return 1400
        if size_type == 4:
            return 1400
    elif sys.platform == 'win32': # for now we have two basic sizes
        if size_type == 1:
            return 1200 # increased from 1100 to account for the new SETUP widget on the last line of any GUI
        if size_type == 2:
                return 1200
        elif size_type==3:
            return 1300
        elif size_type==4:
            return 1300

def get_basic_y_coordinate():
    return basic_y_coordinate
def get_y_step():
    return y_step
def get_help_button_x_coordinate():
    return help_button_x_coordinate

def get_labels_x_coordinate():
    return labels_x_coordinate

def get_labels_x_indented_coordinate():
    return labels_x_indented_coordinate

def get_entry_box_x_coordinate():
    return entry_box_x_coordinate

def get_open_file_directory_coordinate():
    return open_file_directory_coordinate

def about():
    url = "https://github.com/NLP-Suite/NLP-Suite/wiki/About"
    IO_libraries_util.open_url(NLP_Suite_website_name, url)
    # check internet connection
    # if not IO_internet_util.check_internet_availability_warning("Check on GitHub what the NLP Suite is all about"):
    #     return
    # webbrowser.open_new_tab("https://github.com/NLP-Suite/NLP-Suite/wiki/About")

def release_history():
    url = "https://github.com/NLP-Suite/NLP-Suite/wiki/NLP-Suite-Release-History"
    IO_libraries_util.open_url(NLP_Suite_website_name, url)
    # check internet connection
    # if not IO_internet_util.check_internet_availability_warning("Check on GitHub the NLP Suite release history"):
    #     return
    # webbrowser.open_new_tab("https://github.com/NLP-Suite/NLP-Suite/wiki/NLP-Suite-Release-History")

# The function displays the contributors to the development of the NLP Suite
def list_team():
    url = 'https://github.com/NLP-Suite/NLP-Suite/wiki/The-NLP-Suite-Team'
    IO_libraries_util.open_url(NLP_Suite_website_name, url)
    # check internet connection
    # if not IO_internet_util.check_internet_availability_warning("Check on GitHub the NLP Suite team"):
    #     return
    # webbrowser.open_new_tab("https://github.com/NLP-Suite/NLP-Suite/wiki/The-NLP-Suite-Team")

def cite_NLP():
    url = "https://github.com/NLP-Suite/NLP-Suite/wiki/About#How-to-Cite-the-NLP-Suite"
    IO_libraries_util.open_url(NLP_Suite_website_name, url)
    #
    # # check internet connection
    # if not IO_internet_util.check_internet_availability_warning("Check on GitHub the NLP Suite newest release version"):
    #     return
    # webbrowser.open_new_tab("https://github.com/NLP-Suite/NLP-Suite/wiki/About#How-to-Cite-the-NLP-Suite")

def GUI_settings(IO_setup_display_brief,GUI_width,GUI_height_brief,GUI_height_full,y_multiplier_integer,y_multiplier_integer_add,increment):
    # the GUIs are all setup to run with a brief I/O display or full display (with filename, inputDir, outputDir)
    #   just change the next statement to True or False IO_setup_display_brief=True
    # GUI_height height of GUI with full I/O display

    if IO_setup_display_brief:
        GUI_height = GUI_height_brief # - 40
        y_multiplier_integer = y_multiplier_integer  # IO BRIEF display
        increment = 0  # used in the display of HELP messages
    else:  # full display
        # GUI CHANGES add following lines to every special GUI
        # +3 is the number of lines starting at 1 of IO widgets
        # y_multiplier_integer=GUI_util.y_multiplier_integer+2
        GUI_height = GUI_height_full
        y_multiplier_integer = y_multiplier_integer + y_multiplier_integer_add  # IO FULL display
        increment = increment
    GUI_size = str(GUI_width) + 'x' + str(GUI_height)
    return GUI_size, y_multiplier_integer, increment

from tkinter import Toplevel
def Dialog2Display(title: str):
    Dialog2 = Toplevel(height=1000, width=1000)

# creating popup message box in tkinter
# buttonType='OK displays an OK button
# buttonType='Yes-No' displays Yes/ and No buttons
# buttonType='Yes-No-Cancel' displays Yes, No, and Cancel buttons
def message_box_widget(window, message_title, message_text, buttonType='OK', timeout=2000):
    global ys_no_button
    ys_no_button  = "NOTHING"
    # timeout = 6000 # testing
    # top_message = tk.Toplevel(window)
    message_title = 'Reminder: ' + message_title
    top_message = tk.Toplevel()
    top_message.title(message_title)
    # windowHeight=len(message_text)
    # print("windowHeight",windowHeight)
    # TODO can the window size (windowSize) be made dynamic,
    #   i.e. change windowHeight with the size of message_text passed?
    # windowHeight = 200
    # for count, line in enumerate(message_text):
    #     pass
    # print('Total Lines', count + 1,"message_text",message_text)
    # # count each \n
    windowHeight = 200
    count = sum(buffer.count('\n') for buffer in message_text)
    count = count + 1
    print('Total lines:', count + 1)
    if count == 1:
        windowHeight = 100
    elif count > 1 and count <4:
        windowHeight = 120
    elif count > 2 and count < 5:
        windowHeight = 140
    elif count > 3 and count <6:
        windowHeight = 200
    elif count > 4 and count < 7:
        windowHeight = 220
    elif count > 5 and count < 8:
        windowHeight = 230
    else:
        windowHeight = 250
    # windowHeight = int(200 + (count * 2))
    # windowSize = '400x' + str(windowHeight)  # +str(windowHeight)
    windowWidth = 500
    windowSize = str(windowWidth) + 'x' + str(windowHeight)
    top_message.geometry(windowSize)

    mbox = tk.Message(top_message, text=message_text, padx=10, pady=10, width=windowWidth-10)
    top_message.attributes('-topmost', 'true')
    mbox.pack()  # put the widget on the window

    # # timer
    # mbox.after(timeout, top_message.destroy)
    # mbox.pack() # put the widget on the window
    # TODO can we either have an OK button or Yes No Cancel buttons and return the selection?

    def wait_for_answer(top_message,button_type, timeout, mbox):
        global ys_no_button
        # mbox.pack() # put the widget on the window
        if button_type=='Yes':
            # mb.showwarning(title="Yes",message='I pressed YES')
            # timer
            # timeout = 6000  # testing
            ys_no_button = "Happy to tell you that  pressed YES!!!!!!!!!!!!!!!!"
            # return ys_no_button
            # mbox.after(timeout, top_message.destroy)
        elif button_type=='No':
            # mb.showwarning(title="No",message='I pressed NO')
            ys_no_button  = "NOTHING to tell you that  pressed NO!!!!!!!!!!!!!!!!"


    # buttonType = 'Yes-No' # testing
    if buttonType=='OK':
        button = tk.Button(top_message, text="OK", command=top_message.destroy)
        button.pack() # put the widget on the window
        # timer
        mbox.after(timeout, top_message.destroy)
    # TODO top_message.destroy must be changed to selecting the value and returning it
    elif buttonType=='Yes-No':
        # mbox.pack() # put the widget on the window
        Yes = tk.Button(top_message, text="Yes", command=lambda: wait_for_answer(top_message,'Yes', timeout, mbox))
        No = tk.Button(top_message, text="No", command=lambda: wait_for_answer(top_message,'No', timeout, mbox))
        Yes.place(x=10, y=windowHeight-40)
        No.place(x=50, y=windowHeight-40)
        # # timer
        # timeout = 6000  # testing
        mbox.after(timeout, top_message.destroy)
        if "Happy" in ys_no_button:
            print("HAPPY")
            top_message.destroy
        # mb.showwarning(title="Answer", message=ys_no_button )
        #
        # # TODO must place Yes No widgets on the same line
        # Yes = tk.Button(top_message, text="Yes", command=top_message.destroy)
        # Yes.pack()
        # No = tk.Button(top_message, text="No", command=top_message.destroy)
        # No.pack()
        return # TODO must return the selected option yes, no
    # TODO this needs to be completed
    elif buttonType=='Yes-No-Cancel':
        # TODO must place Yes No Cancel widgets on the same line
        Yes = tk.Button(top_message, text="Yes", command=top_message.destroy) # top_message.destroy must be changed
        Yes.pack() # put the widget on the window
        No = tk.Button(top_message, text="No", command=top_message.destroy)
        No.pack() # put the widget on the window
        Cancel = tk.Button(top_message, text="Cancel", command=top_message.destroy)
        Cancel.pack() # put the widget on the window
        return # TODO must return the selected option yes, no, or cancel

    top_message.wait_window()
    if window != '':  # set to '' in NLP_setup_update_util since the GUI.window has already been closed
        window.focus_force()

# creating popup menu in tkinter
def dropdown_menu_widget(window,textCaption, menu_values, default_value, callback):

    class App():
        def __init__(self,master):
            top = self.top = Toplevel()
            top.wm_title(textCaption)
            top.focus_force()
            self.menuButton = ttk.Combobox(top, width=len(textCaption)+30)
            self.menuButton['values'] = menu_values
            self.menuButton.pack() # put the widget on the window

            self.menuButton.grid(row=0, column=1) # , sticky=W)
            self.callback = callback

            ok_button = tk.Button(self.top, text='OK', command=self.get_value)
            ok_button.grid(row=0, column=1)

        def get_value(self):
            val = self.menuButton.get()
            self.top.destroy()
            callback(val)

    App(window)

# modified dropdown_menu_widget that will stay open without command=lambda:
def dropdown_menu_widget2(window,textCaption, menu_values, default_value, callback):
    def get_value():
        global val
        val = menuButton.get()
        top.destroy()
        callback(val)
        # top.update()

    top = Toplevel()
    top.wm_title(textCaption)
    top.focus_force()
    menuButton = ttk.Combobox(top, width=len(textCaption)+30)
    menuButton['values'] = menu_values
    menuButton.pack() # put the widget on the window

    menuButton.grid(row=0, column=1) # , sticky=W)
    callback = callback

    ok_button = tk.Button(top, text='OK', command=get_value)
    ok_button.grid(row=0, column=1)

    window.wait_window(top)

    return val

def slider_widget(window,textCaption, lower_bound, upper_bound, default_value):
    top = tk.Toplevel(window)
    l = tk.Label(top, text= textCaption)
    l.pack() # put the widget on the window
    s = tk.Scale(top, from_= lower_bound, to=upper_bound, orient=tk.HORIZONTAL)
    s.set(default_value)
    s.pack() # put the widget on the window

    def get_value():
        global val
        val = s.get()
        top.destroy()
        top.update()

    def _delete_window():
        mb.showwarning(title = "Invalid Operation", message = "Please click OK to save your choice of parameter.")

    top.protocol("WM_DELETE_WINDOW", _delete_window)

    tk.Button(top, text='OK', command=lambda: get_value()).pack()
    window.wait_window(top)
    return val

# TODO
# 2 widgets max for now; should allow more, dynamically
# return a list; see comment at end of function
def enter_value_widget(masterTitle,textCaption,numberOfWidgets=1,defaultValue='',textCaption2='',defaultValue2=''):
    value1=defaultValue
    value2=defaultValue2

    # TODO should not restrict to 2; should have a loop
    if numberOfWidgets==2:
        # TODO should have a list and break it up assigning values in a loop
        value2=defaultValue2
    master = tk.Tk()
    master.focus_force()

    tk.Label(master,width=len(textCaption),text=textCaption).grid(row=0)
    # TODO should not restrict to 2; should have a loop
    if numberOfWidgets==2:
        tk.Label(master, width=len(textCaption2),text=textCaption2).grid(row=1)

    master.title(masterTitle)
    # the width in tk.Entry determines the overall width of the widget;
    #   MUST be entered
    #   + 30 to add room for - [] and X in a widget window
    e1 = tk.Entry(master,width=len(masterTitle)+30)
    e1.focus_force()

    # TODO 2 could be a larger number; should have a loop
    if numberOfWidgets==2:
        e2 = tk.Entry(master,width=len(masterTitle)+30)

    e1.grid(row=0, column=1)
    # TODO 2 could be a larger number; should have a loop
    if numberOfWidgets==2:
        e2.grid(row=1, column=1)

    e1.insert(len(textCaption), defaultValue) # display a default value
    # TODO 2 could be a larger number; should have a loop
    if numberOfWidgets==2:
        e2.insert(len(textCaption2), defaultValue2) # display a default value

    tk.Button(master,
              text='OK',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    master.mainloop()
    value1=str(e1.get())
    # TODO 2 could be a larger number; should have a loop
    if numberOfWidgets==2:
        value2=str(e2.get())
    master.destroy()
    # convert to list; value1 is checked for length in calling function
    #   so do not convert if empty or its length will be the length of ['']
    # if value1!='':
    #     value1=list(value1.split(" "))
    return value1, value2


