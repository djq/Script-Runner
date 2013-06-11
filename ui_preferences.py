# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_preferences.ui'
#
# Created: Mon Jun 10 21:35:08 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PrefsDialog(object):
    def setupUi(self, PrefsDialog):
        PrefsDialog.setObjectName(_fromUtf8("PrefsDialog"))
        PrefsDialog.resize(547, 354)
        self.gridLayout_4 = QtGui.QGridLayout(PrefsDialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtGui.QGroupBox(PrefsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbAutoDisplay = QtGui.QCheckBox(self.groupBox)
        self.cbAutoDisplay.setObjectName(_fromUtf8("cbAutoDisplay"))
        self.gridLayout_2.addWidget(self.cbAutoDisplay, 0, 0, 1, 1)
        self.cbCustomEditor = QtGui.QCheckBox(self.groupBox)
        self.cbCustomEditor.setObjectName(_fromUtf8("cbCustomEditor"))
        self.gridLayout_2.addWidget(self.cbCustomEditor, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.leCustomEditorPath = QtGui.QLineEdit(self.groupBox)
        self.leCustomEditorPath.setMinimumSize(QtCore.QSize(400, 0))
        self.leCustomEditorPath.setObjectName(_fromUtf8("leCustomEditorPath"))
        self.horizontalLayout.addWidget(self.leCustomEditorPath)
        self.tbSetEditorPath = QtGui.QToolButton(self.groupBox)
        self.tbSetEditorPath.setObjectName(_fromUtf8("tbSetEditorPath"))
        self.horizontalLayout.addWidget(self.tbSetEditorPath)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBoxOutput = QtGui.QGroupBox(PrefsDialog)
        self.groupBoxOutput.setObjectName(_fromUtf8("groupBoxOutput"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxOutput)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 433, 58))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.leLogDirectory = QtGui.QLineEdit(self.layoutWidget)
        self.leLogDirectory.setMinimumSize(QtCore.QSize(250, 0))
        self.leLogDirectory.setObjectName(_fromUtf8("leLogDirectory"))
        self.gridLayout.addWidget(self.leLogDirectory, 0, 2, 1, 1)
        self.tbSetLogDirectory = QtGui.QToolButton(self.layoutWidget)
        self.tbSetLogDirectory.setObjectName(_fromUtf8("tbSetLogDirectory"))
        self.gridLayout.addWidget(self.tbSetLogDirectory, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.cbOverwriteLogFile = QtGui.QCheckBox(self.layoutWidget)
        self.cbOverwriteLogFile.setObjectName(_fromUtf8("cbOverwriteLogFile"))
        self.gridLayout.addWidget(self.cbOverwriteLogFile, 1, 1, 1, 2)
        self.layoutWidget1 = QtGui.QWidget(self.groupBoxOutput)
        self.layoutWidget1.setGeometry(QtCore.QRect(8, 40, 352, 80))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.cbShowConsole = QtGui.QCheckBox(self.layoutWidget1)
        self.cbShowConsole.setObjectName(_fromUtf8("cbShowConsole"))
        self.gridLayout_3.addWidget(self.cbShowConsole, 0, 0, 1, 1)
        self.cbClearConsole = QtGui.QCheckBox(self.layoutWidget1)
        self.cbClearConsole.setMinimumSize(QtCore.QSize(350, 0))
        self.cbClearConsole.setObjectName(_fromUtf8("cbClearConsole"))
        self.gridLayout_3.addWidget(self.cbClearConsole, 1, 0, 1, 1)
        self.cbLogToDisk = QtGui.QCheckBox(self.layoutWidget1)
        self.cbLogToDisk.setObjectName(_fromUtf8("cbLogToDisk"))
        self.gridLayout_3.addWidget(self.cbLogToDisk, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxOutput, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PrefsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(PrefsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PrefsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PrefsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PrefsDialog)
        PrefsDialog.setTabOrder(self.cbClearConsole, self.cbLogToDisk)
        PrefsDialog.setTabOrder(self.cbLogToDisk, self.leLogDirectory)
        PrefsDialog.setTabOrder(self.leLogDirectory, self.tbSetLogDirectory)
        PrefsDialog.setTabOrder(self.tbSetLogDirectory, self.buttonBox)

    def retranslateUi(self, PrefsDialog):
        PrefsDialog.setWindowTitle(QtGui.QApplication.translate("PrefsDialog", "Script Runner Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PrefsDialog", "General Options", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoDisplay.setText(QtGui.QApplication.translate("PrefsDialog", "Automatically display info/source when a script is selected from the list", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCustomEditor.setToolTip(QtGui.QApplication.translate("PrefsDialog", "Application to use for editing scripts. If not specified, the system default will be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCustomEditor.setText(QtGui.QApplication.translate("PrefsDialog", "Edit scripts using:", None, QtGui.QApplication.UnicodeUTF8))
        self.leCustomEditorPath.setToolTip(QtGui.QApplication.translate("PrefsDialog", "Full path to your editor application", None, QtGui.QApplication.UnicodeUTF8))
        self.leCustomEditorPath.setPlaceholderText(QtGui.QApplication.translate("PrefsDialog", "Full path to your edtior", None, QtGui.QApplication.UnicodeUTF8))
        self.tbSetEditorPath.setText(QtGui.QApplication.translate("PrefsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxOutput.setTitle(QtGui.QApplication.translate("PrefsDialog", "Output and Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PrefsDialog", "Log directory", None, QtGui.QApplication.UnicodeUTF8))
        self.tbSetLogDirectory.setText(QtGui.QApplication.translate("PrefsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cbOverwriteLogFile.setText(QtGui.QApplication.translate("PrefsDialog", "Overwrite log file each time the script is run", None, QtGui.QApplication.UnicodeUTF8))
        self.cbShowConsole.setText(QtGui.QApplication.translate("PrefsDialog", "Show console at startup", None, QtGui.QApplication.UnicodeUTF8))
        self.cbClearConsole.setText(QtGui.QApplication.translate("PrefsDialog", "Clear console before running a script", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLogToDisk.setText(QtGui.QApplication.translate("PrefsDialog", "Log script output to disk", None, QtGui.QApplication.UnicodeUTF8))

