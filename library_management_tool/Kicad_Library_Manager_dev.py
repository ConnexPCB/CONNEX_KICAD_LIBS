from PyQt5 import QtCore, QtGui, QtWidgets # Imports PyQt5 widgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_stackedWidget(object):

    def setupUi(self, stackedWidget):
	
		# stackedWidget definition #
		
        stackedWidget.setObjectName(_fromUtf8("stackedWidget")) 											# Defines the object name of the application as "stackedWidget"
        stackedWidget.setFixedSize(550, 275)	 																	# Sets the size of the application
        self.stackedWidget = stackedWidget																	# Passes the stackedWidget object to be an attribute of the Ui_stackedWidget class
		
		# Defines the size policy of the stackedWidget #
		
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stackedWidget.sizePolicy().hasHeightForWidth())
        stackedWidget.setSizePolicy(sizePolicy)
		
		# Home page layout of the stackedWidget #
		
        self.homePage = QtWidgets.QWidget()																		# Defines a QWidget
        self.homePage.setObjectName(_fromUtf8("homePage"))														# Sets the object name of this QWidget to be "homePage"
		
        self.gridLayout_2 = QtWidgets.QGridLayout(self.homePage)													# Defines a QGridLayout for the "homePage" QWidget
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))													# Sets the object name of this QGridLayout to be "gridLayout_2"

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)	        # Defines the size policy of the QComboBox - Horizontal size is Expanding, Vertical size is Fixed		
        
        self.hp_lblTitle = QtWidgets.QLabel(self.homePage)															# Defines a QLabel object for the "homePage" QWidget
        self.hp_lblTitle.setObjectName(_fromUtf8("hp_lblTitle"))													# Sets the object name of this QLabel to be named "hp_lblTitle"		
        self.hp_lblTitle.setSizePolicy(sizePolicy)                                                                  # Sets "sizePolicy" to be associated with "hp_lblTitle"
        font = QtGui.QFont()																						# Defines a font to be associated with the "hp_lblTitle"
        font.setPointSize(11)																							# Sets the font size
        font.setBold(True)																								# Sets the font to be classified as bold
        font.setWeight(75)																								# Sets the font weight
        self.hp_lblTitle.setFont(font)																					# Sets "font" to be associated with "hp_lblTitle"
        self.gridLayout_2.addWidget(self.hp_lblTitle, 0, 1, 1, 3, QtCore.Qt.AlignHCenter)							# Adds the QLabel to the homePage window with a center horizontal align
		
        self.hp_compSelect = QtWidgets.QComboBox(self.homePage)														# Defines a QComboBox object for the "homePage" QWidget
        self.hp_compSelect.setObjectName(_fromUtf8("hp_compSelect"))												# Sets the object name of this QComboBox to be "hp_compSelect"									
        sizePolicy.setHeightForWidth(self.hp_compSelect.sizePolicy().hasHeightForWidth())
        self.hp_compSelect.setFixedWidth(160)																        # Sets the width of the QComboBox
        self.hp_compSelect.addItem(_fromUtf8("Select Component"))													# Adds an item to the QComboBox - "Select Component"
        self.hp_compSelect.addItem(_fromUtf8("Resistor"))															# Adds an item to the QComboBox - "Resistor"
        self.hp_compSelect.addItem(_fromUtf8("Capacitor"))															# Adds an item to the QComboBox - "Capacitor"
        self.hp_compSelect.addItem(_fromUtf8("Inductor"))															# Adds an item to the QComboBox - "Inductor"
        self.gridLayout_2.addWidget(self.hp_compSelect, 0, 0, 1, 1)													# Adds the QComboBox to the homePage window
        self.hp_compSelect.currentIndexChanged.connect(self.windowChange)											# Connects the "hp_compSelect"	QComboBox to the windowChange function if the QComboBoxs selection is changed

        self.hp_lblSchDir = QtWidgets.QLabel(self.homePage)													        # Defines a QLabel object for the "homePage" QWidget
        self.hp_lblSchDir.setObjectName(_fromUtf8("hp_lblSchDir"))													# Sets the object name of the QLabel to be "hp_lblSchDir"
        self.hp_lblSchDir.setSizePolicy(sizePolicy)                                                                 # Sets "sizePolicy" to be associated with "hp_lblSchDir"
        font = QtGui.QFont()																						# Defines a font to be associated with the "hp_lblSchDir"
        font.setPointSize(10)																							# Sets the font size
        font.setBold(True)																								# Sets the font to be classified as bold
        font.setWeight(75)																								# Sets the font weight	
        self.hp_lblSchDir.setFont(font)																					# Sets the "font" to be associated with the "hp_lblSchDir" QLabel
        self.gridLayout_2.addWidget(self.hp_lblSchDir, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)							# Adds the QLabel to the homePage window with a center horizontal align

        self.hp_leSchDir = QtWidgets.QLineEdit(self.homePage)												        # Defines a QLineEdit object for the "homePage" QWidget
        self.hp_leSchDir.setObjectName(_fromUtf8("hp_leSchDir"))														# Sets the object name of the QLineEdit to be "hp_leSchDir"
        self.hp_leSchDir.setFixedWidth(250)																				# Sets the width of the QLineEdit
        self.gridLayout_2.addWidget(self.hp_leSchDir, 2, 1, 1, 2, QtCore.Qt.AlignHCenter)							# Adds the QLabel to the homePage window with a center horizontal align
        self.hp_leSchDir.textChanged.connect(self.SchLib)													    # Connects the "hp_leSchDir" QLineEdit to the SchLib function when the QLine edit gets modified

        self.hp_btnSchDir = QtWidgets.QPushButton(self.homePage)													# Defines a QPushButton for the "homePage" QWidget
        self.hp_btnSchDir.setObjectName(_fromUtf8("hp_btnSchDir"))											        # Sets the object name of this QPushButton to be "hp_btnSchDir"
        self.hp_btnSchDir.setFixedWidth(50)                                                                         # Sets the width of the QPushButton
        icon = QtGui.QIcon('file_select_icon.png')                                                                  # Defines an icon to be associated with the "hp_btnSchDir" and provides the reference image file location for the icon
        self.hp_btnSchDir.setIcon(icon)                                                                                 # Sets "icon" to be associated with "hp_btnSchDir"
        self.gridLayout_2.addWidget(self.hp_btnSchDir, 2, 3, 1, 1)												    # Adds the QPushButton to the homePage window
        self.hp_btnSchDir.clicked.connect(self.SchDir)                                                              # Connects the "hp_btnSchDir" QPushButton to the SchDir function if the QPushButton is clicked

        self.hp_lblFpDir = QtWidgets.QLabel(self.homePage)													        # Defines a QLabel object for the "homePage" QWidget
        self.hp_lblFpDir.setObjectName(_fromUtf8("hp_lblFpDir"))													# Sets the object name of the QLabel to be "hp_lblFpDir"
        font = QtGui.QFont()																						# Defines a font to be associated with the "hp_lblFpDir"
        font.setPointSize(10)																							# Sets the font size
        font.setBold(True)																								# Sets the font to be classified as bold
        font.setWeight(75)																								# Sets the font weight	
        self.hp_lblFpDir.setFont(font)																					# Sets the "font" to be associated with the "hp_lblFpDir" QLabel
        self.gridLayout_2.addWidget(self.hp_lblFpDir, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)							# Adds the QLabel to the homePage window with a center horizontal align

        self.hp_leFpDir = QtWidgets.QLineEdit(self.homePage)												        # Defines a QLineEdit object for the "homePage" QWidget
        self.hp_leFpDir.setObjectName(_fromUtf8("hp_leFpDir"))														# Sets the object name of the QLineEdit to be "hp_leFpDir"
        self.hp_leFpDir.setFixedWidth(250)																				# Sets the width of the QLineEdit
        self.gridLayout_2.addWidget(self.hp_leFpDir, 3, 1, 1, 2, QtCore.Qt.AlignHCenter)							# Adds the QLabel to the homePage window with a center horizontal align

        self.hp_btnFpDir = QtWidgets.QPushButton(self.homePage)													# Defines a QPushButton for the "homePage" QWidget
        self.hp_btnFpDir.setObjectName(_fromUtf8("hp_btnFpDir"))											        # Sets the object name of this QPushButton to be "hp_btnFpDir"
        self.hp_btnFpDir.setFixedWidth(50)                                                                         # Sets the width of the QPushButton
        icon = QtGui.QIcon('file_select_icon.png')                                                                  # Defines an icon to be associated with the "hp_btnFpDir" and provides the reference image file location for the icon
        self.hp_btnFpDir.setIcon(icon)                                                                                 # Sets "icon" to be associated with "hp_btnFpDir"
        self.gridLayout_2.addWidget(self.hp_btnFpDir, 3, 3, 1, 1)												    # Adds the QPushButton to the homePage window
        self.hp_btnFpDir.clicked.connect(self.FpDir)                                                              # Connects the "hp_btnFpDir" QPushButton to the FpDir function if the QPushButton is clicked

        spacerItem2 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)			# Defines a QSpacerItem with a size of 20 x 120, a fixed Horizontal length, and minimized Vertical length
        self.gridLayout_2.addItem(spacerItem2, 4, 2, 1, 1)															# Adds the QSpacerItem to the homePage window
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)			# Defines a QSpacerItem with a size of 40 x 20, a fixed Horizontal length, and minimized Vertical length
        self.gridLayout_2.addItem(spacerItem4, 2, 3, 1, 1)															# Adds the QSpacerItem to the homePage window
        spacerItem = QtWidgets.QSpacerItem(275, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)				# Defines a QSpacerItem with a size of 40 x 20, a fixed Horizontal length, and minimized Vertical length
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)															# Adds the QSpacerItem to the homePage window

        stackedWidget.addWidget(self.homePage)																	#Adds the "homePage" QWidget to the application
		
		# Resistor form layout of the application #
		
        self.resForm = QtWidgets.QWidget()																		# Defines a QWidget
        self.resForm.setObjectName(_fromUtf8("resForm"))														# Sets the object name of this QWidget to be "resForm"
		
        self.gridLayout = QtWidgets.QGridLayout(self.resForm)														# Defines a QGridLayout for the "resForm" QWidget
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))														# Sets the object name of this QGridLayout to be "gridLayout"

        self.res_lblTitle = QtWidgets.QLabel(self.resForm)															# Defines a QLabel object for the "resForm" QWidget
        self.res_lblTitle.setObjectName(_fromUtf8("res_lblTitle"))													# Sets the object name of this QLabel to be "res_lblTitle"
        font = QtGui.QFont()																						# Defines a font to be associated with the "res_lblTitle"
        font.setPointSize(11)																							# Sets the font size
        font.setBold(True)																								# Sets the font to be classified as bold
        font.setWeight(75)																								# Sets the font weight											
        self.res_lblTitle.setFont(font)																					# Sets the "font" to be associated with "res_lblTitle"
        self.gridLayout.addWidget(self.res_lblTitle, 0, 3, 1, 2, QtCore.Qt.AlignHCenter)							# Adds the QLabelto the resForm window with a center horizontal align		
		
        self.res_btnAddField = QtWidgets.QPushButton(self.resForm)													# Defines a QPushButton for the "resForm" QWidget
        self.res_btnAddField.setObjectName(_fromUtf8("res_btnAddField"))											# Sets the object name of this QPushButton to be "res_btnAddField"
        self.gridLayout.addWidget(self.res_btnAddField, 0, 2, 1, 1)													# Adds the QPushButton to the resForm window
		
        self.res_compSelect = QtWidgets.QComboBox(self.resForm)														# Defines a QComboBox object for the "resForm" QWidget
        self.res_compSelect.setObjectName(_fromUtf8("res_compSelect"))												# Sets the object name of this QWidget to be "res_compSelect"
        self.res_compSelect.addItem(_fromUtf8("Home"))																# Adds an item to the QComboBox - "Home"
        self.res_compSelect.addItem(_fromUtf8("Resistor"))															# Adds an item to the QComboBox - "Resistor"
        self.res_compSelect.addItem(_fromUtf8("Capacitor"))															# Adds an item to the QComboBox - "Capacitor"
        self.res_compSelect.addItem(_fromUtf8("Inductor"))															# Adds an item to the QComboBox - "Inductor"
        self.gridLayout.addWidget(self.res_compSelect, 0, 0, 1, 1)													# Adds the QComboBox to the resForm window
        self.res_compSelect.currentIndexChanged.connect(self.windowChange)											# Connects the "res_compSelect"	QComboBox to the windowChange function if the QComboBoxs selection is changed		
		
        self.res_libSelect = QtWidgets.QComboBox(self.resForm)														# Defines a QComboBox object for the "resForm" QWidget
        self.res_libSelect.setObjectName(_fromUtf8("res_libSelect"))												# Sets the object name of this QWidget to be "res_libSelect"
        self.gridLayout.addWidget(self.res_libSelect, 2, 0, 1, 3)													# Adds the QComboBox to the resForm window
   
        self.res_scrollArea = QtWidgets.QScrollArea(self.resForm)													# Defines a QScrollArea for the "resForm" QWidget
        self.res_scrollArea.setObjectName(_fromUtf8("res_scrollArea"))												# Sets the object name for this QScrollArea to be "res_scrollArea"
        self.res_scrollArea.setWidgetResizable(True)																# Sets the QScrollArea to be resizeable
		
        self.res_scrollAreaWidget = QtWidgets.QWidget()																	# Defines a QWidget within the QScrollArea
        self.res_scrollAreaWidget.setObjectName(_fromUtf8("res_scrollAreaWidget"))										# Sets the object name of this QWidget to be "res_scrollAreaWidget"
        self.res_scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 529, 154))												# Sets the size of this of this QWidget to be a 529 x 154 rectangle
		
        self.formLayout_2 = QtWidgets.QFormLayout(self.res_scrollAreaWidget)												# Defines a QFormLayout for the "res_scrollAreaWidget" QWidget
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))															# Sets the object name of the QFormLayout to be "formLayout_2"
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)										# Sets the field growth policy to allow any non-fixed fields to grow indefinitely
		
        self.res_lblPartName = QtWidgets.QLabel(self.res_scrollAreaWidget)													# Defines a QLabel object for the "res_scrollAreaWidget" QWidget
        self.res_lblPartName.setObjectName(_fromUtf8("res_lblPartName"))													# Sets the object name of the QLabel to be "res_lblPartName"
        font = QtGui.QFont()																								# Defines a font to be associated with the "res_lblPartName"
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight	
        self.res_lblPartName.setFont(font)																						# Sets the "font" to be associated with the "res_lblTitle" QLabel
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.res_lblPartName)									# Adds the QLabel to the resScrollArea portion of the resForm window
		
        self.res_lblFootprint = QtWidgets.QLabel(self.res_scrollAreaWidget)													# Defines a QLabel object for the "res_scrollAreaWidget" QWidget
        self.res_lblFootprint.setObjectName(_fromUtf8("res_lblFootprint"))													# Sets the object name of the QLabel to be "res_lblFootprint"
        font = QtGui.QFont()																								# Defines a font to be associated with the "res_lblFootprint" QLabel
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.res_lblFootprint.setFont(font)																						# Sets the "font" to be associated with the "res_lblFootprint" QLabel
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.res_lblFootprint)									# Adds the QLabel to the resScrollArea portion of the resForm window		
		
        self.res_lblCompValue = QtWidgets.QLabel(self.res_scrollAreaWidget)													# Defines a QLabel object for the "res_scrollAreaWidget" QWidget
        self.res_lblCompValue.setObjectName(_fromUtf8("res_lblCompValue"))													# Sets the object name of the QLabel to be "res_lblCompValue"
        font = QtGui.QFont()																								# Defines a font to be associated with the "res_lblCompValue" QLabel
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.res_lblCompValue.setFont(font)																						# Sets the "font" to be associated with the "res_lblCompValue" QLabel
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.res_lblCompValue)									# Adds the QLabel to the resScrollArea portion of the resForm window

        self.res_lblDescription = QtWidgets.QLabel(self.res_scrollAreaWidget)												# Defines a QLabel object for the "res_scrollAreaWidget" QWidget	
        self.res_lblDescription.setObjectName(_fromUtf8("res_lblDescription"))												# Sets the object name of the QLabel to be "res_lblDescription"
        font = QtGui.QFont()																								# Defines a font to be associated with the "res_lblDescription" QLabel
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold				
        font.setWeight(75)																										# Sets the font weight
        self.res_lblDescription.setFont(font)																					# Sets the "font" to be associated with the "res_lblDescription" QLabel
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.res_lblDescription)								# Adds the QLabel to the resScrollArea portion of the resForm window		
		
        self.res_lePartName = QtWidgets.QLineEdit(self.res_scrollAreaWidget)												# Defines a QLineEdit object for the "res_scrollAreaWidget" QWidget
        self.res_lePartName.setObjectName(_fromUtf8("res_lePartName"))														# Sets the object name of the QLineEdit to be "res_lePartName"
        self.res_lePartName.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.res_lePartName)									# Adds the QLineEdit to the resScrollArea portion of the resForm window
		
        self.res_leFootprint = QtWidgets.QLineEdit(self.res_scrollAreaWidget)												# Defines a QLineEdit object for the "res_scrollAreaWidget" QWidget
        self.res_leFootprint.setObjectName(_fromUtf8("res_leFootprint"))													# Sets the object name of the QLineEdit to be "res_leFootprint"
        self.res_leFootprint.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.res_leFootprint)									# Adds the QLineEdit to the resScrollArea portion of the resForm window	
		
        self.res_leCompValue = QtWidgets.QLineEdit(self.res_scrollAreaWidget)												# Defines a QLineEdit object for the "res_scrollAreaWidget" QWidget
        self.res_leCompValue.setObjectName(_fromUtf8("res_leCompValue"))													# Sets the object name of the QLineEdit to be "res_leCompValue"
        self.res_leCompValue.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.res_leCompValue)									# Adds the QLineEdit to the resScrollArea portion of the resForm window	
		
        self.res_leDescription = QtWidgets.QLineEdit(self.res_scrollAreaWidget)												# Defines a QLineEdit object for the "res_scrollAreaWidget" QWidget
        self.res_leDescription.setObjectName(_fromUtf8("res_leDescription"))												# Sets the object name of the QLineEdit to be "res_leDescription"
        self.res_leDescription.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.res_leDescription)									# Adds the QLineEdit to the resScrollArea portion of the resForm window
		
        self.res_scrollArea.setWidget(self.res_scrollAreaWidget)														# Sets the "res_scrollAreaWidget" to be placed inside the "res_scrollArea" QScrollArea
        self.gridLayout.addWidget(self.res_scrollArea, 1, 0, 1, 5)													# Adds the QScrollArea to the resForm window

        self.res_btnBox = QtWidgets.QDialogButtonBox(self.resForm)													# Defines a QDialogButtonBox for the "resForm" QWidget
        self.res_btnBox.setObjectName(_fromUtf8("res_btnBox"))														# Sets the object name of this QDialogButtonBox to be "res_btnBox"
        self.res_btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)					# Sets the buttons of the QDialogButtonBox to be "Cancel" and "Ok"
        self.gridLayout.addWidget(self.res_btnBox, 2, 4, 1, 1)														# Adds the QDialogButtonBox to the resForm window
        self.res_btnBox.accepted.connect(self.submitForm)															# Connects the "res_btnBox"	QDialogButtonBox to the submitForm function if the "Ok" button is clicked
        self.res_btnBox.rejected.connect(self.exitApplication)														# Connects the "res_btnBox"	QDialogButtonBox to the exitApplication function if the "Cancel" button is clicked		

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)			# Defines a QSpacerItem with a size of 120 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)															# Adds the QSpacerItem to the resForm window			
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)				# Defines a QSpacerItem with a size of 70 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)															# Adds the QSpacerItem to the resForm window		
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)				# Defines a QSpacerItem with a size of 40 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)															# Adds the QSpacerItem to the resForm window		
		
        stackedWidget.addWidget(self.resForm)																	# Adds the "resForm" QWidget to the application
		
		# Capacitor form layout of the application #
		
        self.capForm = QtWidgets.QWidget()																		# Defines a QWidget
        self.capForm.setObjectName(_fromUtf8("capForm"))														# Sets the object name of this QWidget to be "capForm"
		
        self.gridLayout_3 = QtWidgets.QGridLayout(self.capForm)														# Defines a QGridLayout for the "capForm" QWidget
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))													# Sets the object name of this QGridLayout to be "gridLayout_3"
		
        self.cap_lblTitle = QtWidgets.QLabel(self.capForm)															# Defines a QLabel object for the "capForm" QWidget
        self.cap_lblTitle.setObjectName(_fromUtf8("cap_lblTitle"))													# Sets the object name of this QLabel to be "cap_lblTitle"
        font = QtGui.QFont()																						# Defines a font to be associated with the "cap_lblTitle"
        font.setPointSize(11)																							# Sets the font size
        font.setBold(True)																								# Sets the font to be classified as bold
        font.setWeight(75)																								# Sets the font weight
        self.cap_lblTitle.setFont(font)																					# Sets the "font" to be associated with "cap_lblTitle"
        self.gridLayout_3.addWidget(self.cap_lblTitle, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)							# Adds the QLabel to capForm window with a center horizontal align
		
        self.cap_btnAddField = QtWidgets.QPushButton(self.capForm)													# Defines a QPushButton for the "capForm" QWidget
        self.cap_btnAddField.setObjectName(_fromUtf8("cap_btnAddField"))											# Sets the object name of this QPushButton to be "cap_btnAddField"
        self.gridLayout_3.addWidget(self.cap_btnAddField, 0, 2, 1, 1)												# Adds the QPushButton to the capForm window
		
        self.cap_compSelect = QtWidgets.QComboBox(self.capForm)														# Defines a QComboBox object for the "capForm" QWidget
        self.cap_compSelect.setObjectName(_fromUtf8("cap_compSelect"))												# Sets the object name of this QWidget to be "cap_compSelect"
        self.cap_compSelect.addItem(_fromUtf8("Home"))																# Adds an item to the QComboBox - "Home"
        self.cap_compSelect.addItem(_fromUtf8("Resistor"))															# Adds an item to the QComboBox - "Resistor"
        self.cap_compSelect.addItem(_fromUtf8("Capacitor"))															# Adds an item to the QComboBox - "Capacitor"
        self.cap_compSelect.addItem(_fromUtf8("Inductor"))															# Adds an item to the QComboBox - "Inductor"	
        self.gridLayout_3.addWidget(self.cap_compSelect, 0, 0, 1, 1)												# Adds the QComboBox to the capForm window
        self.cap_compSelect.currentIndexChanged.connect(self.windowChange)											# Connects the "cap_compSelect"	QComboBox to the windowChange function if the QComboBoxs selection is changed	
		
        self.cap_libSelect = QtWidgets.QComboBox(self.capForm)														# Defines a QComboBox object for the "capForm" QWidget
        self.cap_libSelect.setObjectName(_fromUtf8("cap_libSelect"))												# Sets the object name of this QWidget to be "cap_libSelect"
        self.gridLayout_3.addWidget(self.cap_libSelect, 2, 0, 1, 3)													# Adds the QComboBox to the capForm window        
        
        self.cap_scrollArea = QtWidgets.QScrollArea(self.capForm)													# Defines a QScrollArea for the "capForm" QWidget
        self.cap_scrollArea.setObjectName(_fromUtf8("cap_scrollArea"))												# Sets the object name for this QScrollArea to be "cap_scrollArea"
        self.cap_scrollArea.setWidgetResizable(True)																# Sets the QScrollArea to be resizeable
		
        self.cap_scrollAreaWidget = QtWidgets.QWidget()																	# Defines a QWidget within the QScrollArea
        self.cap_scrollAreaWidget.setObjectName(_fromUtf8("cap_scrollAreaWidget"))										# Sets the object name of this QWidget to be "cap_scrollAreaWidget"
        self.cap_scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 529, 154))												# Sets the size of this of this QWidget to be a 529 x 154 rectangle
		
        self.formLayout_3 = QtWidgets.QFormLayout(self.cap_scrollAreaWidget)												# Defines a QFormLayout for the "cap_scrollAreaWidget" QWidget
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))															# Sets the object name of the QFormLayout to be "formLayout_3"
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)										# Sets the field growth policy to allow any non-fixed fields to grow indefinitely
		
        self.cap_lblPartName = QtWidgets.QLabel(self.cap_scrollAreaWidget)													# Defines a QLabel object for the "cap_scrollAreaWidget" QWidget
        self.cap_lblPartName.setObjectName(_fromUtf8("cap_lblPartName"))													# Sets the object name of the QLabel to be "cap_lblPartName"
        font = QtGui.QFont()																								# Defines a font to be associated with the "cap_lblPartName"
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.cap_lblPartName.setFont(font)																						# Sets the "font" to be associated with "cap_lblPartName"
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cap_lblPartName)									# Adds the QLabel to the capScrollArea portion of the capForm window
		
        self.cap_lblFootprint = QtWidgets.QLabel(self.cap_scrollAreaWidget)													# Defines a QLabel object for the "cap_scrollAreaWidget" QWidget
        self.cap_lblFootprint.setObjectName(_fromUtf8("cap_lblFootprint"))													# Sets the object name of the QLabel to be "cap_lblFootprint"
        font = QtGui.QFont()																								# Defines a font to be associated with the "cap_lblFootprint"
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.cap_lblFootprint.setFont(font)																						# Sets the "font" to be associated with "cap_lblFootprint"
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cap_lblFootprint)									# Adds the QLabel to the capScrollArea portion of the capForm window
		
        self.cap_lblCompValue = QtWidgets.QLabel(self.cap_scrollAreaWidget)													# Defines a QLabel object for the "cap_scrollAreaWidget" QWidget
        self.cap_lblCompValue.setObjectName(_fromUtf8("cap_lblCompValue"))													# Sets the object name of the QLabel to be "cap_lblCompValue"
        font = QtGui.QFont()																								# Defines a font to be associated with the "cap_lblCompValue"
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.cap_lblCompValue.setFont(font)																						# Sets the "font" to be associated with "cap_lblCompValue"
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cap_lblCompValue)									# Adds the QLabel to the capScrollArea of the capForm window
		
        self.cap_lblDecription = QtWidgets.QLabel(self.cap_scrollAreaWidget)												# Defines a QLabel object for the "cap_scrollAreaWidget" QWidget
        self.cap_lblDecription.setObjectName(_fromUtf8("cap_lblDecription"))												# Sets the object name of the QLabel to be "cap_lblDecription"
        font = QtGui.QFont()																								# Defines a font to be associated with the "cap_lblDecription"
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.cap_lblDecription.setFont(font)																					# Sets the "font" to be associated with "cap_lblDecription"
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.cap_lblDecription)									# Adds the QLabel to the capScrollArea portion of the capForm window		
		
        self.cap_lePartName = QtWidgets.QLineEdit(self.cap_scrollAreaWidget)												# Defines a QLineEdit object for the "cap_scrollAreaWidget" QWidget
        self.cap_lePartName.setObjectName(_fromUtf8("cap_lePartName"))														# Sets the object name of the QLineEdit to be "cap_lePartName"
        self.cap_lePartName.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cap_lePartName)									# Adds the QLineEdit to the capScrollArea portion of the capForm window
		
        self.cap_leFootprint = QtWidgets.QLineEdit(self.cap_scrollAreaWidget)												# Defines a QLineEdit object for the "cap_scrollAreaWidget" QWidget
        self.cap_leFootprint.setObjectName(_fromUtf8("cap_leFootprint"))													# Sets the object name of the QLineEdit to be "cap_leFootprint"
        self.cap_leFootprint.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cap_leFootprint)									# Adds the QLineEdit to the capScrollArea portion of the capForm window
		
        self.cap_leCompValue = QtWidgets.QLineEdit(self.cap_scrollAreaWidget)												# Defines a QLineEdit object for the "cap_scrollAreaWidget" QWidget
        self.cap_leCompValue.setObjectName(_fromUtf8("cap_leCompValue"))													# Sets the object name of the QLineEdit to be "cap_leFootprint"
        self.cap_leCompValue.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cap_leCompValue)									# Adds the QLineEdit to the capScrollArea portion of the capForm window
		
        self.cap_leDescription = QtWidgets.QLineEdit(self.cap_scrollAreaWidget)												# Defines a QLineEdit object for the "cap_scrollAreaWidget" QWidget
        self.cap_leDescription.setObjectName(_fromUtf8("cap_leDescription"))												# Sets the object name of the QLineEdit to be "cap_leDescription"
        self.cap_leDescription.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cap_leDescription)									# Adds the QLineEdit to the capScrollArea portion of the capForm window
		
        self.cap_scrollArea.setWidget(self.cap_scrollAreaWidget)														# Sets the "cap_scrollAreaWidget" to be placed inside the "cap_scrollArea" QScrollArea
        self.gridLayout_3.addWidget(self.cap_scrollArea, 1, 0, 1, 4)												# Adds the QScrollArea to the capForm window
		
        self.cap_btnBox = QtWidgets.QDialogButtonBox(self.capForm)													# Defines a QDialogButtonBox for the "capForm" QWidget
        self.cap_btnBox.setObjectName(_fromUtf8("cap_btnBox"))														# Sets the object name of this QDialogButtonBox to be "cap_btnBox"
        self.cap_btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)					# Sets the buttons of the QDialogButtonBox to be "Cancel" and "Ok"
        self.gridLayout_3.addWidget(self.cap_btnBox, 2, 3, 1, 1)													# Adds the QDialogButtonBox to the capForm window
        self.cap_btnBox.accepted.connect(self.submitForm)															# Connects the "cap_btnBox"	QDialogButtonBox to the submitForm function if the "Ok" button is clicked
        self.cap_btnBox.rejected.connect(self.exitApplication)														# Connects the "cap_btnBox"	QDialogButtonBox to the exitApplication function if the "Cancel" button is clicked
		
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)			# Defines a QSpacerItem with a size of 120 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout_3.addItem(spacerItem8, 2, 2, 1, 1)															# Adds the QSpacerItem to the capForm window
        spacerItem9 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)				# Defines a QSpacerItem with a size of 70 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout_3.addItem(spacerItem9, 2, 0, 1, 1)															# Adds the QSpacerItem to the capForm window
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)			# Defines a QSpacerItem with a size of 40 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout_3.addItem(spacerItem10, 0, 1, 1, 1)															# Adds the QSpacerItem to the capForm window
		
        stackedWidget.addWidget(self.capForm)																	# Adds the "capForm" QWidget to the application

		# Inductor form layout of the application #
		
        self.indForm = QtWidgets.QWidget()																		# Defines a QWidget
        self.indForm.setObjectName(_fromUtf8("indForm"))														# Sets the object name of this QWidget to be "indForm"
		
        self.gridLayout = QtWidgets.QGridLayout(self.indForm)														# Defines a QGridLayout for the "indForm" QWidget
        self.gridLayout.setObjectName(_fromUtf8("ind_gridLayout"))													# Sets the object name of this QGridLayout to be "ind_gridLayout"

        self.ind_lblTitle = QtWidgets.QLabel(self.indForm)															# Defines a QLabel object for the "indForm" QWidget
        self.ind_lblTitle.setObjectName(_fromUtf8("ind_lblTitle"))													# Sets the object name of this QLabel to be "ind_lblTitle"
        font = QtGui.QFont()																						# Defines a font to be associated with the "ind_lblTitle"
        font.setPointSize(11)																							# Sets the font size
        font.setBold(True)																								# Sets the font to be classified as bold
        font.setWeight(75)																								# Sets the font weight											
        self.ind_lblTitle.setFont(font)																					# Sets the "font" to be associated with "ind_lblTitle"
        self.gridLayout.addWidget(self.ind_lblTitle, 0, 3, 1, 2, QtCore.Qt.AlignHCenter)							# Adds the QLabelto the indForm window with a center horizontal align		
		
        self.ind_btnAddField = QtWidgets.QPushButton(self.indForm)													# Defines a QPushButton for the "indForm" QWidget
        self.ind_btnAddField.setObjectName(_fromUtf8("ind_btnAddField"))											# Sets the object name of this QPushButton to be "res_btnAddField"
        self.gridLayout.addWidget(self.ind_btnAddField, 0, 2, 1, 1)													# Adds the QPushButton to the indForm window
		
        self.ind_compSelect = QtWidgets.QComboBox(self.indForm)														# Defines a QComboBox object for the "indForm" QWidget
        self.ind_compSelect.setObjectName(_fromUtf8("ind_compSelect"))												# Sets the object name of this QWidget to be "ind_compSelect"
        self.ind_compSelect.addItem(_fromUtf8("Home"))																# Adds an item to the QComboBox - "Home"
        self.ind_compSelect.addItem(_fromUtf8("Resistor"))															# Adds an item to the QComboBox - "Resistor"
        self.ind_compSelect.addItem(_fromUtf8("Capacitor"))															# Adds an item to the QComboBox - "Capacitor"
        self.ind_compSelect.addItem(_fromUtf8("Inductor"))															# Adds an item to the QComboBox - "Inductor"
        self.gridLayout.addWidget(self.ind_compSelect, 0, 0, 1, 1)													# Adds the QComboBox to the indForm window
        self.ind_compSelect.currentIndexChanged.connect(self.windowChange)											# Connects the "ind_compSelect"	QComboBox to the windowChange function if the QComboBoxs selection is changed		
		
        self.ind_libSelect = QtWidgets.QComboBox(self.indForm)														# Defines a QComboBox object for the "indForm" QWidget
        self.ind_libSelect.setObjectName(_fromUtf8("ind_libSelect"))												# Sets the object name of this QWidget to be "ind_libSelect"
        self.gridLayout.addWidget(self.ind_libSelect, 2, 0, 1, 3)													# Adds the QComboBox to the indForm window
        
        self.ind_scrollArea = QtWidgets.QScrollArea(self.indForm)													# Defines a QScrollArea for the "indForm" QWidget
        self.ind_scrollArea.setObjectName(_fromUtf8("ind_scrollArea"))												# Sets the object name for this QScrollArea to be "ind_scrollArea"
        self.ind_scrollArea.setWidgetResizable(True)																# Sets the QScrollArea to be resizeable
		
        self.ind_scrollAreaWidget = QtWidgets.QWidget()																	# Defines a QWidget within the QScrollArea
        self.ind_scrollAreaWidget.setObjectName(_fromUtf8("ind_scrollAreaWidget"))										# Sets the object name of this QWidget to be "ind_scrollAreaWidget"
        self.ind_scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 529, 154))												# Sets the size of this of this QWidget to be a 529 x 154 rectangle
		
        self.ind_SAW_formLayout = QtWidgets.QFormLayout(self.ind_scrollAreaWidget)												# Defines a QFormLayout for the "ind_scrollAreaWidget" QWidget
        self.ind_SAW_formLayout.setObjectName(_fromUtf8("ind_SAW_formLayout"))													# Sets the object name of the QFormLayout to be "ind_SAW_formLayout"
        self.ind_SAW_formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)									# Sets the field growth policy to allow any non-fixed fields to grow indefinitely
		
        self.ind_lblPartName = QtWidgets.QLabel(self.ind_scrollAreaWidget)													# Defines a QLabel object for the "ind_scrollAreaWidget" QWidget
        self.ind_lblPartName.setObjectName(_fromUtf8("ind_lblPartName"))													# Sets the object name of the QLabel to be "ind_lblPartName"
        font = QtGui.QFont()																								# Defines a font to be associated with the "ind_lblPartName"
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight	
        self.ind_lblPartName.setFont(font)																						# Sets the "font" to be associated with the "res_lblTitle" QLabel
        self.ind_SAW_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ind_lblPartName)								# Adds the QLabel to the indScrollArea portion of the indForm window
		
        self.ind_lblFootprint = QtWidgets.QLabel(self.ind_scrollAreaWidget)													# Defines a QLabel object for the "ind_scrollAreaWidget" QWidget
        self.ind_lblFootprint.setObjectName(_fromUtf8("ind_lblFootprint"))													# Sets the object name of the QLabel to be "ind_lblFootprint"
        font = QtGui.QFont()																								# Defines a font to be associated with the "ind_lblFootprint" QLabel
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.ind_lblFootprint.setFont(font)																						# Sets the "font" to be associated with the "ind_lblFootprint" QLabel
        self.ind_SAW_formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ind_lblFootprint)							# Adds the QLabel to the indScrollArea portion of the indForm window		
		
        self.ind_lblCompValue = QtWidgets.QLabel(self.ind_scrollAreaWidget)													# Defines a QLabel object for the "ind_scrollAreaWidget" QWidget
        self.ind_lblCompValue.setObjectName(_fromUtf8("ind_lblCompValue"))													# Sets the object name of the QLabel to be "ind_lblCompValue"
        font = QtGui.QFont()																								# Defines a font to be associated with the "ind_lblCompValue" QLabel
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold
        font.setWeight(75)																										# Sets the font weight
        self.ind_lblCompValue.setFont(font)																						# Sets the "font" to be associated with the "ind_lblCompValue" QLabel
        self.ind_SAW_formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ind_lblCompValue)							# Adds the QLabel to the indScrollArea portion of the indForm window

        self.ind_lblDescription = QtWidgets.QLabel(self.ind_scrollAreaWidget)												# Defines a QLabel object for the "ind_scrollAreaWidget" QWidget	
        self.ind_lblDescription.setObjectName(_fromUtf8("ind_lblDescription"))												# Sets the object name of the QLabel to be "ind_lblDescription"
        font = QtGui.QFont()																								# Defines a font to be associated with the "ind_lblDescription" QLabel
        font.setPointSize(10)																									# Sets the font size
        font.setBold(True)																										# Sets the font to be classified as bold				
        font.setWeight(75)																										# Sets the font weight
        self.ind_lblDescription.setFont(font)																					# Sets the "font" to be associated with the "ind_lblDescription" QLabel
        self.ind_SAW_formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ind_lblDescription)							# Adds the QLabel to the indScrollArea portion of the indForm window		
		
        self.ind_lePartName = QtWidgets.QLineEdit(self.ind_scrollAreaWidget)												# Defines a QLineEdit object for the "ind_scrollAreaWidget" QWidget
        self.ind_lePartName.setObjectName(_fromUtf8("ind_lePartName"))														# Sets the object name of the QLineEdit to be "ind_lePartName"
        self.ind_lePartName.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.ind_SAW_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ind_lePartName)								# Adds the QLineEdit to the indScrollArea portion of the indForm window
		
        self.ind_leFootprint = QtWidgets.QLineEdit(self.ind_scrollAreaWidget)												# Defines a QLineEdit object for the "ind_scrollAreaWidget" QWidget
        self.ind_leFootprint.setObjectName(_fromUtf8("ind_leFootprint"))													# Sets the object name of the QLineEdit to be "ind_leFootprint"
        self.ind_leFootprint.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.ind_SAW_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ind_leFootprint)								# Adds the QLineEdit to the indScrollArea portion of the indForm window	
		
        self.ind_leCompValue = QtWidgets.QLineEdit(self.ind_scrollAreaWidget)												# Defines a QLineEdit object for the "ind_scrollAreaWidget" QWidget
        self.ind_leCompValue.setObjectName(_fromUtf8("ind_leCompValue"))													# Sets the object name of the QLineEdit to be "ind_leCompValue"
        self.ind_leCompValue.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.ind_SAW_formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ind_leCompValue)								# Adds the QLineEdit to the indScrollArea portion of the indForm window	
		
        self.ind_leDescription = QtWidgets.QLineEdit(self.ind_scrollAreaWidget)												# Defines a QLineEdit object for the "ind_scrollAreaWidget" QWidget
        self.ind_leDescription.setObjectName(_fromUtf8("ind_leDescription"))												# Sets the object name of the QLineEdit to be "ind_leDescription"
        self.ind_leDescription.setFixedWidth(200)																				# Sets the width of the QLineEdit
        self.ind_SAW_formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ind_leDescription)							# Adds the QLineEdit to the indScrollArea portion of the indForm window
		
        self.ind_scrollArea.setWidget(self.ind_scrollAreaWidget)														# Sets the "ind_scrollAreaWidget" to be placed inside the "ind_scrollArea" QScrollArea
        self.gridLayout.addWidget(self.ind_scrollArea, 1, 0, 1, 5)													# Adds the QScrollArea to the indForm window

        self.ind_btnBox = QtWidgets.QDialogButtonBox(self.indForm)													# Defines a QDialogButtonBox for the "indForm" QWidget
        self.ind_btnBox.setObjectName(_fromUtf8("ind_btnBox"))														# Sets the object name of this QDialogButtonBox to be "ind_btnBox"
        self.ind_btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)					# Sets the buttons of the QDialogButtonBox to be "Cancel" and "Ok"
        self.gridLayout.addWidget(self.ind_btnBox, 2, 4, 1, 1)														# Adds the QDialogButtonBox to the indForm window
        self.ind_btnBox.accepted.connect(self.submitForm)															# Connects the "ind_btnBox"	QDialogButtonBox to the submitForm function if the "Ok" button is clicked
        self.ind_btnBox.rejected.connect(self.exitApplication)														# Connects the "ind_btnBox"	QDialogButtonBox to the exitApplication function if the "Cancel" button is clicked

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)			# Defines a QSpacerItem with a size of 120 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)															# Adds the QSpacerItem to the indForm window			
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)				# Defines a QSpacerItem with a size of 70 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)															# Adds the QSpacerItem to the indForm window		
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)				# Defines a QSpacerItem with a size of 40 x 20, a fixed Horizontal length, and a minimized Vertical length
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)															# Adds the QSpacerItem to the indForm window		
		
        stackedWidget.addWidget(self.indForm)																	# Adds the "indForm" QWidget to the application
		
        self.retranslateUi(stackedWidget)																	# Calls the retranslateUi function
        stackedWidget.setCurrentIndex(0)																	# Sets the stackedWidget to start by displaying the homePage window
        QtCore.QMetaObject.connectSlotsByName(stackedWidget)												

    def retranslateUi(self, stackedWidget):
		
        stackedWidget.setWindowTitle(_translate("stackedWidget", "Connex", None))								# Defines the text for the applications title bar
		
		# Text definitions for the home page layout #
		
        self.hp_lblTitle.setText(_translate("stackedWidget", "Kicad Library Manager", None)) 					# Defines the text for the "hp_lblTitle" QLabel
        self.hp_lblSchDir.setText(_translate("stackedWidget", "Schematic Directory:", None)) 					# Defines the text for the "hp_lblSchDir" QLabel
        self.hp_lblFpDir.setText(_translate("stackedWidget", "Footprint Directory:", None)) 					# Defines the text for the "hp_lblFpDir" QLabel				
		
        self.hp_compSelect.setItemText(0, _translate("stackedWidget", "Select Component", None))				# Defines the text for the "hp_compSelect" QComboBox Item 0
        self.hp_compSelect.setItemText(1, _translate("stackedWidget", "Resistor", None))						# Defines the text for the "hp_compSelect" QComboBox Item 1
        self.hp_compSelect.setItemText(2, _translate("stackedWidget", "Capacitor", None))						# Defines the text for the "hp_compSelect" QComboBox Item 2
        self.hp_compSelect.setItemText(3, _translate("stackedWidget", "Inductor", None))						# Defines the text for the "hp_compSelect" QComboBox Item 3
		
		# Text definitions for the resistor form layout #
		
        self.res_lblTitle.setText(_translate("stackedWidget", "Resistor Creation Form", None))					# Defines the text for the "res_lblTitle" QLabel		
		
        self.res_btnAddField.setText(_translate("stackedWidget", "Add Field", None))							# Defines the text for the "res_btnAddField" QPushButton
		
        self.res_compSelect.setItemText(0, _translate("stackedWidget", "Home", None))							# Defines the text for the "res_compSelect" QComboBox Item 0	
        self.res_compSelect.setItemText(1, _translate("stackedWidget", "Resistor", None))						# Defines the text for the "res_compSelect" QComboBox Item 1
        self.res_compSelect.setItemText(2, _translate("stackedWidget", "Capacitor", None))						# Defines the text for the "res_compSelect" QComboBox Item 2
        self.res_compSelect.setItemText(3, _translate("stackedWidget", "Inductor", None))						# Defines the text for the "res_compSelect" QComboBox Item 3
		
        self.res_lblPartName.setText(_translate("stackedWidget", "Part Name (Value)", None))					# Defines the text for the "res_lblPartName" QLabel
        self.res_lblFootprint.setText(_translate("stackedWidget", "Footprint", None))							# Defines the text for the "res_lblFootprint" QLabel
        self.res_lblCompValue.setText(_translate("stackedWidget", "Component Value", None))						# Defines the text for the "res_lblCompValue" QLabel
        self.res_lblDescription.setText(_translate("stackedWidget", "Description", None))						# Defines the text for the "res_lblDescription" QLabel
		
		# Text definitions for the capacitor form layout #
		
        self.cap_lblTitle.setText(_translate("stackedWidget", "Capacitor Creation Form", None))					# Defines the text for the "cap_lblTitle" QLabel		
		
        self.cap_btnAddField.setText(_translate("stackedWidget", "Add Field", None))							# Defines the text for the "cap_btnAddField" QPushButton		
		
        self.cap_compSelect.setItemText(0, _translate("stackedWidget", "Home", None))							# Defines the text for the "cap_compSelect" QComboBox Item 0
        self.cap_compSelect.setItemText(1, _translate("stackedWidget", "Resistor", None))						# Defines the text for the "cap_compSelect" QComboBox Item 1
        self.cap_compSelect.setItemText(2, _translate("stackedWidget", "Capacitor", None))						# Defines the text for the "cap_compSelect" QComboBox Item 2
        self.cap_compSelect.setItemText(3, _translate("stackedWidget", "Inductor", None))						# Defines the text for the "cap_compSelect" QComboBox Item 3
		
        self.cap_lblPartName.setText(_translate("stackedWidget", "Part Name (Value)", None))					# Defines the text for the "cap_lblPartName" QLabel
        self.cap_lblFootprint.setText(_translate("stackedWidget", "Footprint", None))							# Defines the text for the "cap_lblFootprint" QLabel
        self.cap_lblCompValue.setText(_translate("stackedWidget", "Component Value", None))						# Defines the text for the "cap_lblCompValue" QLabel
        self.cap_lblDecription.setText(_translate("stackedWidget", "Description", None))						# Defines the text for the "cap_lblDecription" QLabel
		
		# Text definitions for the inductor form layout #
		
        self.ind_lblTitle.setText(_translate("stackedWidget", "Inductor Creation Form", None))					# Defines the text for the "ind_lblTitle" QLabel		
		
        self.ind_btnAddField.setText(_translate("stackedWidget", "Add Field", None))							# Defines the text for the "ind_btnAddField" QPushButton		
		
        self.ind_compSelect.setItemText(0, _translate("stackedWidget", "Home", None))							# Defines the text for the "ind_compSelect" QComboBox Item 0
        self.ind_compSelect.setItemText(1, _translate("stackedWidget", "Resistor", None))						# Defines the text for the "ind_compSelect" QComboBox Item 1
        self.ind_compSelect.setItemText(2, _translate("stackedWidget", "Capacitor", None))						# Defines the text for the "ind_compSelect" QComboBox Item 2
        self.ind_compSelect.setItemText(3, _translate("stackedWidget", "Inductor", None))						# Defines the text for the "ind_compSelect" QComboBox Item 3
		
        self.ind_lblPartName.setText(_translate("stackedWidget", "Part Name (Value)", None))					# Defines the text for the "ind_lblPartName" QLabel
        self.ind_lblFootprint.setText(_translate("stackedWidget", "Footprint", None))							# Defines the text for the "ind_lblFootprint" QLabel
        self.ind_lblCompValue.setText(_translate("stackedWidget", "Component Value", None))						# Defines the text for the "ind_lblCompValue" QLabel
        self.ind_lblDescription.setText(_translate("stackedWidget", "Description", None))						# Defines the text for the "ind_lblDescription" QLabel
		
    def windowChange(self, stackedWidget):  
        
        if(self.stackedWidget.currentIndex() == 0):																# If the current active page is the homePage perform the following:
            self.stackedWidget.setCurrentIndex(self.hp_compSelect.currentIndex())									# Set the active page to the selected page from the "hp_compSelect" QComboBox - This is done by changing the stackedWidget's index
            if(self.hp_compSelect.currentIndex() == 1):																# If the current selected page from the "hp_compSelect" QComboBox is the resForm perform the following:
                self.res_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "res_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "hp_compSelect" QComboBox
            elif(self.hp_compSelect.currentIndex() == 2):															# If the current selected page from the "hp_compSelect" QComboBox is the capForm perform the following:
                self.cap_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "cap_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "hp_compSelect" QComboBox
            elif(self.hp_compSelect.currentIndex() == 3):															# If the current selected page from the "hp_compSelect" QComboBox is the indForm perform the following:
                self.ind_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "ind_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "hp_compSelect" QComboBox
        elif(self.stackedWidget.currentIndex() == 1):															# If the current active page is the resForm perform the following:
            self.stackedWidget.setCurrentIndex(self.res_compSelect.currentIndex())									# Set the active page to the selected page from the "res_compSelect" QComboBox - This is done by changing the stackedWidget's index
            if(self.res_compSelect.currentIndex() == 0):															# If the current selected page from the "res_compSelect" QComboBox is the homePage perform the following:
                self.hp_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "hp_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "res_compSelect" QComboBox
            elif(self.res_compSelect.currentIndex() == 2):															# If the current selected page from the "res_compSelect" QComboBox is the capForm perform the following:
                self.cap_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "cap_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "res_compSelect" QComboBox
            elif(self.res_compSelect.currentIndex() == 3):															# If the current selected page from the "res_compSelect" QComboBox is the indForm perform the following:
                self.ind_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "ind_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "res_compSelect" QComboBox
        elif(self.stackedWidget.currentIndex() == 2):															# If the current active page is the capForm perform the following:
            self.stackedWidget.setCurrentIndex(self.cap_compSelect.currentIndex())									# Set the active page to the selected page from the "cap_compSelect" QComboBox - This is done by changing the stackedWidget's index
            if(self.cap_compSelect.currentIndex() == 0):															# If the current selected page from the "cap_compSelect" QComboBox is the homePage perform the following:
                self.hp_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "hp_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "cap_compSelect" QComboBox
            elif(self.cap_compSelect.currentIndex() == 1):															# If the current selected page from the "cap_compSelect" QComboBox is the resForm perform the following:
                self.res_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "res_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "cap_compSelect" QComboBox
            elif(self.cap_compSelect.currentIndex() == 3):															# If the current selected page from the "cap_compSelect" QComboBox is the indForm perform the following:
                self.ind_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "ind_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "cap_compSelect" QComboBox
        elif(self.stackedWidget.currentIndex() == 3):															# If the current active page is the indForm perform the following:
            self.stackedWidget.setCurrentIndex(self.ind_compSelect.currentIndex())									# Set the active page to the selected page from the "ind_compSelect" QComboBox - This is done by changing the stackedWidget's index
            if(self.ind_compSelect.currentIndex() == 0):															# If the current selected page from the "ind_compSelect" QComboBox is the homePage perform the following:
                self.hp_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "hp_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "ind_compSelect" QComboBox
            elif(self.ind_compSelect.currentIndex() == 1):															# If the current selected page from the "ind_compSelect" QComboBox is the resForm perform the following:
                self.res_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "res_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "ind_compSelect" QComboBox
            elif(self.ind_compSelect.currentIndex() == 2):															# If the current selected page from the "ind_compSelect" QComboBox is the capForm perform the following:
                self.cap_compSelect.setCurrentIndex(self.stackedWidget.currentIndex())									# Set the "cap_compSelect" QComboBox's index to be the index of the stackedWidget - This was just set by the selection of the "ind_compSelect" QComboBox

    def SchDir(self):
        
        self.hp_fdSchDirText = QtWidgets.QFileDialog.getExistingDirectory(self.stackedWidget, 'Select a folder:', 'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)    # Defines and opens a QFileDialog which prompts the user to select a directory and then sets that directory to the "hp_fdSchDirText" string
        self.hp_leSchDir.setText(self.hp_fdSchDirText)                                                                                                   # Sets the "hp_leSchDir" QLineEdit's text to be the "hp_fdSchDirText" string

    def FpDir(self):

        self.hp_fdFpDir = QtWidgets.QFileDialog.getExistingDirectory(self.stackedWidget, 'Select a folder:', 'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)    # Defines and opens a QFileDialog which prompts the user to select a directory and then sets that directory to the "hp_fdFpDir" string
        self.hp_leFpDir.setText(self.hp_fdFpDir)   

    def SchLib(self):
        
        hp_fdSchDir = QtCore.QDir(self.hp_fdSchDirText)
        filters = ["*.lib"]
        hp_fdSchDir.setNameFilters(filters)
        libraries = hp_fdSchDir.entryList()
        for files in libraries:
            self.res_libSelect.addItem(files)																   # Adds an item to the QComboBox - "Home"            
            self.cap_libSelect.addItem(files)																   # Adds an item to the QComboBox - "Home"
            self.ind_libSelect.addItem(files)																   # Adds an item to the QComboBox - "Home"
            
    def submitForm(self):

         if(self.stackedWidget.currentIndex() == 1):
             file = self.hp_leSchDir.text() + "/" + self.res_libSelect.currentText()
             f = open(file, "w")
             L = self.res_lePartName.text() + "\n" + "newline added"
             f.write(L)
             f.close()
        
             f = open(file, "r+")
             print (f.read())
             f.close()
             #print ("Resistor Part Name:", self.res_lePartName.text())
             #print ("Resistor Footprint:", self.res_leFootprint.text())
             #print ("Resistor Value:", self.res_leCompValue.text())
             #print ("Resistor Description:", self.res_leDescription.text())
         elif(self.stackedWidget.currentIndex() == 2):
             print ("Capacitor Part Name:", self.cap_lePartName.text())
             print ("Capacitor Footprint:", self.cap_leFootprint.text())
             print ("Capacitor Value:", self.cap_leCompValue.text())
             print ("Capacitor Description:", self.cap_leDescription.text())
         elif(self.stackedWidget.currentIndex() == 3):
             print ("Inductor Part Name:", self.ind_lePartName.text())
             print ("Inductor Footprint:", self.ind_leFootprint.text())
             print ("Inductor Value:", self.ind_leCompValue.text())
             print ("Inductor Description:", self.ind_leDescription.text())     

    def exitApplication(self):
        
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 															# Define a QT application with sys.argv param
    stackedWidget = QtWidgets.QStackedWidget() 														# Define a QT stacked widget
    ui = Ui_stackedWidget() 																		# Call the "ui_stackedWidget()" class
    ui.setupUi(stackedWidget) 																		# Call the setupUi function within the Ui_stackedWidget class
    stackedWidget.show()																			# Start the application
    sys.exit(app.exec_())
    print ("test")