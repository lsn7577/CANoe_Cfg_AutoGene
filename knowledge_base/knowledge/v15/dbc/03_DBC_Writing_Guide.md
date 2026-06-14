# DBC File Writing Guide (Vector CANoe 15.0)

> 本文档基于 Vector CANoe 15.0 CANeds (DBC Editor) 帮助文档整理，涵盖 DBC (CAN database) 文件的编写、语法、关键字、属性及 v15 新增特性。
> 适用对象：DBC 工程师、CANoe 配置工程师、网络通信设计工程师。
> 生成日期：2026/06/01
> 注: v15 将 DBC 编辑器从 CANdb++ 迁移到 CANeds，并引入了 vCDL (Vector Communication Description Language) 作为 DBC 的超集。

---

## CANeds 概述 (v15)


# CANeds

Start Page

|  | CANeds for CANopen is a powerful tool for generating and modifying CANopen Electronic Data Sheets (EDS) and Device Configuration Files (DCF). Furthermore CANopen Device Descriptions (XDD and XDC) can be created and modified, but not all possibilities of the device description can be used with CANeds. It saves device manufacturers and system integrators from the hard and error-prone job of writing EDS files manually. An intrinsic knowledge of all standard objects and their possible attributes makes it very easy to build-up an EDS, DCF, XDD or XDC. CANeds displays the structure of one of these files as an hierarchical tree (mid pane in the main window). It represents the CANopen object attributes like object type or data type symbolically. The cumbersome translation of the numerous types to their numerical values needed in these files is done automatically. The same is true for setting up the links between the sections of the file. |

| Quick Access New Features (CANopen) Use Cases Create a New EDS Create new Objects Check EDS and DCF Files Scan a Physical Device Create Signal Lists | Quick Access | New Features (CANopen) | Use Cases | Create a New EDS Create new Objects Check EDS and DCF Files Scan a Physical Device Create Signal Lists | Windows - Menus - Key Combinations CANeds Main Window Object Dictionary Database Window EDS Window Attribute Window Key Combinations Tips & Tricks Floating of the Output Window Optimize the column width in the objects overview | Windows - Menus - Key Combinations | CANeds Main Window Object Dictionary Database Window EDS Window Attribute Window Key Combinations | Tips & Tricks | Floating of the Output Window Optimize the column width in the objects overview | Functions Read and write EDS, DCF, XDD and XDC files Modification of EDS and DCF files Check of EDS and DCF files Limited modification of XDD and XDC files Check of XDD and XDC files to the CANopen XML schema Scanning devices with semi-automatic creation of EDS files Notifications: errors, warnings, status | Functions | Read and write EDS, DCF, XDD and XDC files Modification of EDS and DCF files Check of EDS and DCF files Limited modification of XDD and XDC files Check of XDD and XDC files to the CANopen XML schema Scanning devices with semi-automatic creation of EDS files Notifications: errors, warnings, status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Quick Access |
| New Features (CANopen) |
| Use Cases |
| Create a New EDS Create new Objects Check EDS and DCF Files Scan a Physical Device Create Signal Lists |
| Windows - Menus - Key Combinations |
| CANeds Main Window Object Dictionary Database Window EDS Window Attribute Window Key Combinations |
| Tips & Tricks |
| Floating of the Output Window Optimize the column width in the objects overview |
| Functions |
| Read and write EDS, DCF, XDD and XDC files Modification of EDS and DCF files Check of EDS and DCF files Limited modification of XDD and XDC files Check of XDD and XDC files to the CANopen XML schema Scanning devices with semi-automatic creation of EDS files Notifications: errors, warnings, status |

Glossary | File Name Extensions | Copyright/Contact | Typographical Conventions

| Version 15© Vector Informatik GmbH |  |


---

## 文档说明 (Document)

**条目数**: 7

### HID_DOC_CHECK


# Check EDS and DCF Files

CANeds

The application allows to check EDS and DCF file in different ways.

## Check while file is read

When a file is read after a file open command few simple test are done to inform the user if faulty values can not be read.

## Compare objects with database objects

Single objects can be compared with the database. If a value differs the object is marked with the icon .

An object is compared with its database by selecting it in the EDS Window and start command Compare Database. An object is also compared after a value in the attribute window has changed and another object is selected.

All objects are compared with the selected database after a file is read.

## Check a file with CANchkEDS

The command Check EDS starts the big EDS check. All objects are checked according to the Electronic Data Sheet Specification for CANopen (CiA306) and test description for CANopen Devices (Appendix to CiA301 V4.0).

If the check detect an error the corresponding object is marked with the icon .

| Version 15© Vector Informatik GmbH |  |


### HID_DOC_COPYMULTI


# Clone Object

CANeds

Sometimes it is useful to copy one object to more than one new index. This may be achieved by the command Clone Object of the menu Edit or the associated toolbar button or context menu which opens the Clone Object dialog.

In this dialog the index range of new objects can be specified. Start Index (hex) specifies the first index the new object is created with, End Index (hex) specifies the last one. If no end index is set only one copy of the object is created.

| Version 15© Vector Informatik GmbH |  |


### HID_DOC_COPYPASTE


# Copy and Paste

CANeds

With copy & paste it is possible to move objects to another location in the same or another tree view. First one or more objects have to be selected. Then the objects are copied by the command Copy and cut by the command Cut. In both cases the selected tree objects in the EDS or database window are copied to the clipboard.

After selecting a new tree object the command Paste inserts the objects below.

If an object with the same index already exist a dialog to select the further procedure appears at the end of and drag & drop operation.

| Version 15© Vector Informatik GmbH |  |


### HID_DOC_DRAGDROP


# drag & drop

CANeds

With drag & drop it is possible to move objects to another location in the same or another tree view. To drag objects, select them, click the objects and, while holding down the mouse button, move them to the new location. Release the mouse button to drop the objects. A list of child tree objects can be expanded or collapsed while this operation by holding the mouse pointer of the parent tree object.

Performing this operation with the left mouse button copies the selected objects to the new location. Using the right mouse button moves the objects and delete them in their old location. Objects of the database window are always copied.

Drag sources are EDS and database objects. Drop targets are several tree objects in the EDS tree view.

If an object with the same index already exists, a dialog to select the further procedure appears at the end of the drag & drop operation.

| Version 15© Vector Informatik GmbH |  |


### HID_DOC_MULTISELECT


# Multiple Selection

CANeds

While key <Alt> is pressed, multiple objects are selected by click on them with the left mouse button. To select a range of objects click on the first one, press key <Shift>, hold it and click on the last object.

Only objects of the same type may be selected multiple.

| Version 15© Vector Informatik GmbH |  |


### HID_DOC_NEWOBJ


# Create new Objects

CANeds

New objects can be created by several commands of menu Edit, by context menus or by the toolbar.

Possible tree objects are:

| Object type | Description |
| --- | --- |
| Objects | CANopen objects |
| Sub Objects | CANopen sub objects |
| Modules | Allow building of flexible devices which can be extended by modules |
| Name Sections | For compact sub objects it is possible to assign explicit names, if the default names are not useful enough. For this a list of according names can be created. |
| Object Links | In order to ease the implementation of a configuration tool it is possible to group related objects together via an object link. |
| Dynamic Channels | Support of intelligent or programmable devices |
| Tools | Describes some aspects of the usage of the EDS by software packages (specified in CiA405) |
| Sections | Allows additional sections with user-defined entries |

Copy and Paste | Multiple Selection | Copy with offset

| Version 15© Vector Informatik GmbH |  |


### HID_DOC_READWRITE


# Read and write files

CANeds

Command File | Open opens a file. It is to select if the file is an EDS, DCF, XDD or XDC.

The commands File | Save and File | Save As save the active file.

| Version 15© Vector Informatik GmbH |  |


---

## 术语表 (Glossary)

**条目数**: 9

### OHIDP_G_FILEEXTENSIONS


# File Name Extensions

CANeds » Glossary

| Extension | Description |
| --- | --- |
| CODB | CANopen database |
| CHM | Online help file |
| DCF | Device configuration file |
| EDS | Electronic data sheet |
| EXE | Executable program |
| HTML | Hypertext markup language file |
| XDC | CANopen device configuration in XML format |
| XDD | CANopen device description in XML format |
| XML | Extended markup language file |

| Version 15© Vector Informatik GmbH |  |


### OHIDP_G_OBJECT


# Object

CANeds » Glossary

Objects are defined in CiA301 or nodes in a tree view (e.g. in the database window).

| Version 15© Vector Informatik GmbH |  |


### OHID_G_CODB


# CODB

CANeds » Glossary

CANopen profile database which are supplied by the CAN in Automation e.V. in a readable text format.

| Version 15© Vector Informatik GmbH |  |


### OHID_G_DATABASE


# Database

CANeds » Glossary

The tools database is a merge of different CANopen profile databases (CODBs) which are supplied by the CiA® in a human readable text format. Each profile database describes the typical object entries for exactly one device profile.

The profile database files are selected by the command Edit List and are shown in the database window.

| Version 15© Vector Informatik GmbH |  |


### OHID_G_EDS


# EDS

CANeds » Glossary

Electronic Data Sheet in accordance with standardization by CiA301.

| Version 15© Vector Informatik GmbH |  |


### OHID_Glossary


# Glossary

CANeds » Glossary

## C

CANopen

CODB

Context menu

CiA®

## D

Database

## E

EDS

## F

File extensions

## M

Menu Bar

## O

Object

## X

XDC

XDD

| Version 15© Vector Informatik GmbH |  |


### glossary_dcf


# DCF

CANeds » Glossary

Device Configuration File

| Version 15© Vector Informatik GmbH |  |


### glossary_xdc


# XDC

CANeds » Glossary

Device Configuration File

| Version 15© Vector Informatik GmbH |  |


### glossary_xdd


# XDD

CANeds » Glossary

Device Description File

| Version 15© Vector Informatik GmbH |  |


---

## CANeds 帮助

**条目数**: 3

### OHID_Shortcuts


# Key Combinations

CANeds » Key Combinations

| Key(s) | Action (Command) |
| --- | --- |
| <Ctrl>+<N> | New (Menu File) |
| <Ctrl>+<O> | Open (Menu File ) |
| <Ctrl>+<S> | Save (Menu File) |
| <Ctrl>+<X> | Cut (Menu Edit) |
| <Shift>+<DELETE> | Cut (Menu Edit) |
| <Ctrl>+<C> | Copy (Menu Edit) |
| <Ctrl>+<INSERT> | Copy (Menu Edit) |
| <Ctrl>+<V> | Paste (Menu Edit) |
| <Shift>+<INSERT> | Paste (Menu Edit) |
| <DELETE> | Delete (Menu Edit) |
| <Ctrl>+<Z> | Undo Object Attributes (Menu Edit) |
| <Alt>+<BACK> | Undo Object Attributes (Menu Edit) |
| <F8> | Correct Attributes (Menu Edit) |
| <Ctrl>+<F> | Find In Output Window (Menu View) |
| <Ctrl>+<F2> | Edit List (Menu Database) |
| <F3> | Find Next (Menu View) |
| <F4> | Compare Database (Menu Check) |
| <F5> | Check EDS (Menu Check) |
| <F7> | Edit Database Definitions (Menu Check) |
| <F9> | Scan (Menu Network) |
| <F2> | Edit signal (Signal list) |
| <F6> | Next window of object dictionary page (Control menu) |
| <Shift>+<F6> | Previous window of object dictionary page (Control menu) |
| <F1> | Call online help |
| <TAB> | Switch to next input control or window |
| <Shift>+<TAB> | Switch to previous input control or window |
| <Ctrl>+<Page Down> | Switch to next page in the main window |
| <Ctrl>+<Page Up> | Switch to previous page in the main window |

| Version 15© Vector Informatik GmbH |  |


### OHID_TYPOGRAFIE


# Typographical conventions

CANeds » Typographical conventions

On this page we present to you the typographic and symbolic elements of our Help system together with their meanings.

| Element | Short Description |
| --- | --- |
|  | Caution! |
|  | Note |
|  | Example |
|  | Step by Step Procedure |
|  | FAQ |
|  | Introduction |
|  | Basic Knowledge |
|  | Expert Knowledge |
|  | Changes |
|  | Cross Reference |
|  | Definition |
|  | Multimedia Link |
|  | Edit |
|  | Do not edit manually! |
|  | Obsolete Function |
| / | This symbols flags (expandable/closeable) drop-down sections. |
| Typography | Links to a help page or a help pop up window. |
| »CAPL | Links to a glossary entry. |
| Vector Knowledgebase | Links to an external page/application. |
|  | This symbol flags cross references/conceptual links; a window will pop up. |
| CANoe | Notation for product names and trademarks. |
| [OK] | Notation for buttons in dialogs. |
| <F5> | Notation for keys on the computer keyboard. |
| <Ctrl>+<z> | Notation for keys on the computer keyboard that should be pressed simultaneously. |
| Add… File|Save file… | Notation for commands, menu names, dialog names and screen/dialog elements.Here Save file… refers to a command within the File menu. |
| on message <msg id> | Notation for syntax (CAPL, MS-DOS, XML, C#…). |
| on message 0x100 | Notation for sample code (CAPL, MS-DOS, XML, C#…). |

| Version 15© Vector Informatik GmbH |  |


### contact


# Copyright/Contact

CANeds

© Vector Informatik GmbH

|  | Vector Informatik GmbH – Support Our business hours are Monday to Friday from 08:30 am to 5:00 pm (CET): Phone: Fax: E-Mail: KnowledgeBase: Support Page: +49 711 80670 200 +49 711 80670 111 support@vector.com kb.vector.com vector.com/support You can submit your support request in the Vector Customer Portal, via e-mail or telephone or use one of the forms below. Please select your issue type below to submit your issue the Vector support team. Software tool or hardware product issue Hardware repair Embedded software issue Return shipments Other issues | Phone: Fax: E-Mail: KnowledgeBase: Support Page: | +49 711 80670 200 +49 711 80670 111 support@vector.com kb.vector.com vector.com/support | You can submit your support request in the Vector Customer Portal, via e-mail or telephone or use one of the forms below. Please select your issue type below to submit your issue the Vector support team. Software tool or hardware product issue Hardware repair Embedded software issue Return shipments Other issues |  |
| --- | --- | --- | --- | --- | --- |
| Phone: Fax: E-Mail: KnowledgeBase: Support Page: | +49 711 80670 200 +49 711 80670 111 support@vector.com kb.vector.com vector.com/support |
| You can submit your support request in the Vector Customer Portal, via e-mail or telephone or use one of the forms below. Please select your issue type below to submit your issue the Vector support team. Software tool or hardware product 

[...truncated for brevity...]

---

## 对象属性 (Object Attributes)

**条目数**: 11

### HIDD_FV_DYNCHANOBJ


# Dynamic channel segment attributes

CANeds

In case of programmable devices according to CiA302 rsp. CiA405 the description of the dynamic network variable arrays are not written in the EDS. All necessary information are already given by the dynamic channel objects.

Each data type and direction (Input/Output) has its own area, called segment. A segment is a range of indexes in the object dictionary with following values:

| Data Type | Data type of objects in this segment. |
| --- | --- |
| Direction | Distinction between inputs and outputs (necessary for mapping). |
| Start / End Index | Range of indexes. |
| Offset | Offset in the process picture, where the first object of this segment is allocated. Many devices distinguish strictly between different segments in the process picture for different data types. For those devices the offset of the first segment will be 0, the offset of the second segment will be the maximum count of the first segment multiplied by the data type size of the first segment and so forth. Other devices mix different data types in the same segment. For those devices all offset attributes will have the value 0. |
| Bit Address Difference | If the data type of this segment is Boolean, the bit address difference has to be defined (most often 1 or 8). |
| Maximal Number | Maximum number of objects which can be allocated in this segment. |

The capability of the device to manage dynamic variables has to be declared in the Device Information page.

| Ve

[...truncated for brevity...]

### HIDD_FV_MAINOBJ


# Main object attributes

CANeds

## General

In this page the attributes of a main object are shown.

If the object is structured (object type ARRAY, RECORD or DEFSTRUCT) the sub object fields are enabled. The number of sub objects in the EDS Window is modified if focus is on the sub number field and the return key is pressed, another object is selected or the file is stored.

Most often all sub objects of an array are equal except the name. It is allowed to describe only a template in the main object. This is made by selecting the check box Compact Storage. All attributes apart from object type and sub number refer to the several sub object (except sub-index 0 and 255). Object type of the sub objects is assumed to be VAR. If the object includes any signal descriptions, they are not stored and cannot be recreated!

For some objects, e.g. object 1000h, there is an additional button right of the default value field. After clicking this button a dialog appears in which a symbolic representation of the default value is shown. If you enter a default value manually a range check is done with the given low and high limits or the allowed value range depending on the object data type. If a range violation is detected, an appropriate warning is displayed in the output window.

If an object has a signal description, you can read the default value and the limits (high and low) from this signal description with the buttons in the section Get signal list attributes and set them for the s

[...truncated for brevity...]

### HIDD_FV_MODSECTION


# Module attributes

CANeds

A very common way for building flexible devices is using a bus coupler device which can be extended by modules. The base device automatically detects the existence of extension modules. This page defines the attributes of such a module.

The Unknown Entries field contains entries of the object which are not conform to the EDS specification. The entries are displayed in the INI-file format (name=value).

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_NAMESECT


# Name section attributes

CANeds

Most often all sub objects of an array are equal except the name. It is allowed to describe only a template in the main object (check box Compact Storage in the main object has to be activated). The implicit default names of the sub objects are assumed to be xxxn with xxx as the name of the main object and as the decimal sub-index. Sub-index 0 has the name NrOfObjects.

If these default names are not useful enough the name section object can be inserted and in the attribute fields (shown above) the explicit names can be added. To set an explicit name, double click the wanted sub-index or press <Return> and enter a name in the edit field.

The Unknown Entries field contains entries of the object which are not conform to the EDS specification. The entries are displayed in the INI-file format (name=value).

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_OBJLINKS


# Object link attributes

CANeds

In order to ease the implementation of a configuration tool it is possible to group related objects together via links. In the attribute window of the object link object all main objects of the EDS file are displayed. Objects with a check mark are linked.

The Unknown Entries field contains entries of the object which are not conform to the EDS specification. The entries of both fields are displayed in the INI-file format (name=value).

The Unknown linked objects field contains the hexadecimal indexes to non existing linked objects.

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_SUBEXTOBJ


# Sub extension object attributes

CANeds

On this page the attributes of a sub extension object are shown. Sub extension objects that instantiate new sub objects.

There are two additional fields according to the sub object attributes:

| Created per Module | Number of sub objects with this attributes that are created per module or number of bits that are created per module to build a new sub object.. |
| --- | --- |
| Maximum Sub Index | If an array is filled up to the end, the next object may be used to create the remaining sub objects. This value defines the maximum sub index after which the next object is used. If the value is 0 or the entry is missing, the next object can not be used. |

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_SUBOBJ


# Sub object attributes

CANeds

On this page the attributes of a sub object are shown, which are analogue to the attributes of a main object.

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_TOOLOBJ


# Tool attributes

CANeds

To allow the denotation of a device specific tool already by the device manufacturer the EDS may contain a description, which tools are to be used. On creating a DCF from that EDS, this tool description will be copied. For more information see CiA405.

| Attribute | Description |
| --- | --- |
| Name | Symbolic name of the tool |
| Command | Concrete command with command line parameters |
| Make | This switch indicates that the tool has to be called on project changes where some kind of a recompile is required. For example, this Make may be necessary to recompile PLC programs in the event of changes to variable addresses or names. |
| Wait | This switch indicates whether the calling tool should wait for until the called tool is closed before it permits further user actions. For example, this is necessary if the called tool accesses DCF files and might change them! |

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_UNKNOWNSECT


# Unknown section attributes

CANeds

If there are any sections in the EDS file which are not conform to the EDS specification are not mentioned in one of the list sections (e.g. [MandatoryObjects]) these sections are represented by Unknown section objects in the Object Dictionary page of the main window.

Comments (which start with a semicolon) at the beginning of an EDS file are also represented by Unknown section objects.

In the attribute window the section name and all entries of the section are listed using the INI-file format (name=value).

| Version 15© Vector Informatik GmbH |  |


### OHID_WND_ATTRIBUTE


# Attribute Window

CANeds

In the Attribute window the attributes of the selected tree object in the Object Dictionary page are displayed. In most cases it is possible to change attributes.

- Main Object

- Sub Object

- Sub Extension Object

- Module Attributes

- Name Section

- Object Link

- Dynamic Channel

- Tool

- Connected Modules

- Unknown Section

| Version 15© Vector Informatik GmbH |  |


### attributes_conn_modules


# Connected module attributes

CANeds

This page is only available if a DCF is loaded which describes connected modules.

With the button [Add] a new module can insert in the list. The number of the module can be set with a double click on an element of the list.

| Version 15© Vector Informatik GmbH |  |


---

## 信号描述 (Signal Descriptions)

**条目数**: 2

### signal_descriptions_createsignallist


# Create Signal Lists

CANeds » Signal descriptions » Create Signal Lists

You can create a signal list on the Signals page of the selected object.

## Insert signals

With a double mouse click on an entry Free you can define a signal. For this signal, enter the mandatory information as name, start bit and signal length (column Bits) in the appropriate columns. With the tabulator key you can switch between the different columns, with <F2> you can edit the values of them.

In the lower part you can see additional information about the current selected signal, e.g the default value and the limits of the value range.

With the button [Edit...] you can open the dialog Signal Editor to modify the attributes of the current selected signal.

| Version 15© Vector Informatik GmbH |  |


### signal_descriptions_overview


# Overview Signal Descriptions

CANeds » Signal Descriptions

Besides the object attributes the CANopen standard allows the division of the object value (signal group) into several signals. For the signals the length and the starting position (in bits) is set. With CANeds you can define such signal descriptions for object.

This is possible for objects of object type VAR and data type of the UNSIGNED group as well as user-defined data types. Such objects you can separate in ranges and allocate these ranges with signals.

|  | Note The specification of signal descriptions is possible in XML format only. When you save a file you have to consider that you save it in XML format (as XDC or XDD file). Otherwise the information about signals are lost if you save the file in INI format (as EDS or DCF file). |

## Layout of signal lists

The data type of an object defines the size of it. This size is also valid for the signal list. So an object of data type Unsigned32 has a size of 32 bit. These bits you can allocate with signals freely. It is not necessary that you string the signals together and to allocate the whole range of the object. The resulting gaps are filled automatically with empty signals by CANeds.

## Calculation of the object value

The value of an object is represented by the signal list and the values of the individual signals. To calculate the object value, the values of the signals are stringed together.

|  | Example You define four signals A, B, C and D with dif

[...truncated for brevity...]

---

## 操作步骤 (Procedures)

**条目数**: 1

### ohid_creatingneweds


# Create a New EDS

CANeds

For creating a new EDS there are several possibilities.

In any case it should be verified, that the appropriate databases are loaded. See command Database | Edit List.

If a CAN interface card exists, a device may be connected and the EDS may be created semi-automatically with the command Scan. Otherwise every single object has to be created by getting objects from the database or another EDS to the EDS Window or via a dialog.

| Version 15© Vector Informatik GmbH |  |


---

## 选项卡 (Tab Pages)

**条目数**: 6

### HIDD_FV_DEVICEINFO


# Device Information

CANeds

This page contains the settings of the used device. The values of Dynamic Channels and Compact PDO can be set either in the edit field or by using the check boxes.

To get the number of explicit defined PDOs in the EDS button the [Get] is used. Button [Set] sets the number of explicit defined PDOs and deletes unnecessary objects or creates necessary objects. Only those sub objects of the PDO are created which are selected in the Compact PDO field. Existing PDOs are not updated.

|  | Example Creation of an EDS with three RxPDO (sub-index 1, 2 and 5 ) and two TxPDO (sub-indexes 1 and 2 ). Set CompactPDO to 0x13, number of RxPDO to 3, number of TxPDO to 0 and click [Set]. Set CompactPDO to 0x3, number of TxPDO to 2 and click [Set] again. To specify further compact PDOs only the number of RxPDO/TxPDO and value of CompactPDO is set (without clicking [Set]). |

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_DUMMYUSAGE


# Dummy Usage

CANeds

On this page you can select the data types that are allowed for the dummy usage.

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_FILEINFO


# File Information

CANeds

This page allows the modification of several attributes of the EDS file. The values of File version and File revision are integers whereas EDS version value must have format x.y.

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_TYPEDEF


# Type Definitions

CANeds

This page contains manufacturer and device profile specific data types stored in the EDS file.

After selecting a type definition the values of the type can be edited on the right side. The appearance of the edit fields depends on the used object type. New type definitions are added by dint of button [New] and to delete types button [Delete] or key <DEL> is used.

To add new sub indexes to a record type (object type DEFSTRUCT) the question mark in the sub index column has to be double clicked and a data type can be selected. Pressing <DEL> removes the currently selected sub index. For a simple type (object type DEFTYPE) only the name and the length of the type can be defined.

If the check mark Display objects in object dictionary is set all data types are visible in the Object Dictionary page too. To set this attribute on start-up the option Display types in object dictionary view after file is loaded in the EDS page of the option dialog (menu Options | Settings... | EDS) has to be activated.

New Type Definition

| Version 15© Vector Informatik GmbH |  |


### HIDD_FV_UNKNOWNENTRIES


# Unknown Entries

CANeds

This page contains unknown entries of some special sections in the EDS file. Unknown entries found in the file information, device information, comment or dummy usage section are displayed here. To delete an entry select it via mouse and press button <DEL>. It’s not possible to insert new entries.

This page is visible only if there are unknown entries in the EDS file.

| Version 15© Vector Informatik GmbH |  |


### OHID_OBJECT_DICITIONARY


# Object Dictionary

CANeds

This page contains all information regarding to used databases, objects of the EDS file and their attributes. It consists of three different panes. The layout of the window may be stored. Thus the layout is restored on opening of the next file.

The size of the windows can be changed to any size. Position the mouse pointer over the window frame so that an arrow symbol is displayed. Hold the left mouse button pressed and drag the window frame until the desired window size is reached. Release the mouse button.

Use the command Arrange Windows to arrange the width of the three mid panes so that the whole attribute window is shown.

Object Dictionary Overview

| Version 15© Vector Informatik GmbH |  |


---

## 窗口 (Windows)

**条目数**: 15

### AFX_HIDW_STATUS_BAR


# Status Bar

CANeds

The status bar is displayed at the bottom of the application window. To display or hide the status bar, use the command Status Bar in the menu View. The right areas of the status bar indicate which of the following keys are latched down:

| Indicator | Description |
| --- | --- |
| CAP | The Caps Lock key is latched down. |
| NUM | The Num Lock key is latched down. |
| SCRL | The Scroll Lock key is latched down. |

| Version 15© Vector Informatik GmbH |  |


### AFX_HIDW_TOOLBAR


# Toolbar

CANeds

The toolbar is displayed at the top of the application window below the menu bar. The toolbar provides quick mouse access to frequently required commands used in the application. After clicking on symbol the corresponding command is executed. To hide or display the toolbar, choose command Toolbar from menu View.

| Symbol | Command |
| --- | --- |
|  | New (Menu File) |
|  | Open (Menu File) |
|  | Save (Menu File) |
|  | Cut (Menu Edit) |
|  | Copy (Menu Edit) |
|  | Copy Multiple (Menu Edit) |
|  | Paste (Menu Edit) |
|  | New Object (Menu Edit) |
|  | New Sub Object (Menu Edit) |
|  | New Module (Menu Edit) |
|  | New Name Section (Menu Edit) |
|  | New Object Links (Menu Edit) |
|  | New Dynamic Channel Segment (Menu Edit) |
|  | New Tool (Menu Edit) |
|  | New Section (Menu Edit) |
|  | Undo Object Attributes (Menu Edit) |
|  | Edit List (Menu Database) |
|  | File View or Overall View (Menu Database) |
|  | Compare Object (Menu Check) |
|  | Edit Database Definitions (Menu Check) |
|  | Check File (Menu Check) |
|  | Scan (Menu Network) |
|  | Clear Output Window (Menu View) |
|  | Find in output window (Menu View) |
|  | Find Next (Menu View) |
|  | About Vector CANeds... (Menu Help) |
|  | Start context help |

| Version 15© Vector Informatik GmbH |  |


### ConvertToMultiplexedPDODlg


# Convert to Multiplexed PDO

CANeds

If the number of sub objects of a PDO Mapping Parameter object is set to 254 or 255 then this dialog appears. After choosing the wanted MPDO mode and clicking [YES] all existing sub objects except sub object 0 are deleted and the default value of sub object 0 is set to 254 (Destination Address MPDO) or 255 (Source Address MPDO).

| Version 15© Vector Informatik GmbH |  |


### DeleteSubObjDlg


# Compactify subobjects

CANeds

If the sub objects of have to be stored compact (check box Compact Storage is selected in the main object) this dialog appears.

If you click button [Yes], all sub objects are deleted and a name section object is created. The names of the sub objects are shown in the attribute window of this object and can be restored if you deactivate the check box Compact Storage.

Pressing [No] deletes all sub objects without creating other objects.

Pressing [Cancel] will abort the creation of a compact storage. Your sub objects including their signals will be left unmodified.

|  | Caution! By creating a compact storage sub objects with their signals will be deleted. The signal definitions are not stored within the compact storage, so they cannot be re-created! |

| Version 15© Vector Informatik GmbH |  |


### DeviceTypeDlg


# Device Type

CANeds

This dialog allows to set the default value of object 1000h symbolically. First a device profile is selected in the list box. Then additional information is added.

| Version 15© Vector Informatik GmbH |  |


### Dialog_CopyWithOffset


# Copy with offset

CANeds

After clicking [OK] the selected objects are copied to the clipboard whereas the index of the objects is increased by offset of this dialog.

| Version 15© Vector Informatik GmbH |  |


### Dialog_Edit_DatabaseConditions


# Edit Database Conditions

CANeds

When the dialog is opened the variables of the conditions of the current databases are loaded. Variables which are already stored in the EDS file but aren't found in the current selected database are displayed in grey. If there is a value in the column Value then the variable is used in the EDS check. To edit the value you can double click the column or you can press <F2> or <Return>.

By pressing <Del> a variable can be deleted.

| Version 15© Vector Informatik GmbH |  |


### HIDD_CODBLIST


# Selected Databases

CANeds

To show a CANopen database (CODB) in the application the wanted database files have to be added to the database list after clicking button [Add]. In the new dialog one or more files can be selected. By default all new database files are marked by a check mark. Pressing [Ok] shows the database objects of the marked files in the Database Window.

It is possible to mark and unmark files with a click on the check box, by pressing <Enter> or the space bar.

|  | Note Vector delivers some databases together with the tool. For the current release of these databases or additional databases, the CiA® office should be contacted. |

The order of the files in the dialog is important because objects with the same index or sub index, which are contained in different database files, are overwritten. Only the multiple object of the last file appears in the database window. Therefore the files in the list box can be moved by the buttons [Up] and [Down]. If the check box Check if objects are overwritten by a succeeding database is selected, a dialog informs about overwritten objects and in the database window these objects are marked.

In the column Object Shift a value can be set to shift the indexes of database objects in the range from 6000h to 6700h. This is useful for Multiple Device Modules. Objects outside this index range are not shifted (e.g. object 1000h). For more information on Multiple Device Modules see CiA301.

To delete one or more databases the f

[...truncated for brevity...]

### HIDD_DUPLICATE_OBJ_DLG


# Duplicate Object

CANeds

If an object already exists in the target folder of the EDS this dialog appears.

There is one of two possibilities to choose. Either the existing object is left unchanged and the new object is not inserted or the new one replaces the existing object. If there are multiple objects to insert, the chosen operation can be applied to all following objects. Pressing button [Cancel] terminates the whole operation.

A similar dialog appears, if

- a fixed object is inserted into a module and there is already a non fixed object with the same index in the object dictionary

- a sub extension object is inserted into a module and there is a fixed object with the same index in a module

and vice versa.

| Version 15© Vector Informatik GmbH |  |


### HIDD_MSG_FORMVIEW


# Output Window

CANeds

In the output window status, error and warning notifications are shown.

A click with the right mouse button into the output window opens a context menu. Command Clear clears the whole window and command Copy copies the contents to the clipboard.

Via double clicking, an error or warning notification the corresponding object or page is selected and the attribute can be edited. The same result is achieved by selecting the wanted error notification; opening context menu via right mouse click and selecting command Go to Error. The command Help of the context menu shows a more detailed error description.

The commands Find in output window and Find Next of menu View look for a character string in this window.

To give more places to all other windows the output window has the ability to float which means it is no longer docked to the frame window. By double clicking the gripper at the left of the docked window or a click on the quadratic toggle box, the window changes its state from docked to float. If the window is floating a double click on the caption of the window or shifting the window to the edge of the frame window docks the output window to the frame window.

Floating of the Output Window

| Version 15© Vector Informatik GmbH |  |


### OHID_APPLICATION_WINDOW


# CANeds Main Window

CANeds

The main window of CANeds contains a menu bar, a toolbar, a status bar, an output window and a window with different pages to select. These pages contains information about the current file (EDS, DCF, XDD, XDC), objects of the Object Dictionary and the specific data types.

- Object Dictionary

- File Information

- Device Information

- Dummy Usage

- Type Definitions

- Unknown Entries

It is possible to hide the output window, the menu, the toolbar or the status bar to increase the size of the other windows. For this use the menu View.

Context Menu | Key Combinations

| Version 15© Vector Informatik GmbH |  |


### OHID_WND_DATABASE


# Database Window

CANeds

In the database window the objects of the selected database files are displayed in a tree view. The database is updated after the database file list is modified by the command Database | Edit List.

Via command File View and Overall View you can switch the view. In the file view all database files and their objects are displayed. So you can copy objects of a specific profile to the file. In the overall view all objects are displayed. Objects which are found in several files are marked by a d if this is activated in dialog Database List.

Navigating through the tree is described in the EDS Window.

| Version 15© Vector Informatik GmbH |  |


### OHID_WND_EDS


# EDS Window

CANeds

The EDS Window shows the structure of the EDS, DCF, XDD or XDC in a tree view control. It is possible to delete or add several objects. This can be done with a double click, drag and drop, commands of the context menu or commands of the menu Edit. The name and other attributes of the actually selected object are shown in the attribute window pane.

Different objects are displayed with different symbols in the tree:

| Object | Symbol |
| --- | --- |
| Main object (with signal information) | () |
| Sub object (with signal information) | () |
| Object link |  |
| Name list |  |
| Module |  |
| Dynamic channel segment |  |
| Tool |  |
| Section |  |

## Navigation in the EDS window

- Navigation with the cursor keys:

- Navigation with the mouse:

| Version 15© Vector Informatik GmbH |  |


### ObjectToMapDlg


# Object to map

CANeds

This dialog allows to set the default value of a PDO mapping parameter sub object. In the object list all mapable objects are shown with index, data type, and object name.

To map an object, select it in the list and click [OK].

| Version 15© Vector Informatik GmbH |  |


### dlg_signaleditor


# Signal Editor

CANeds » Signal descriptions » Signal Editor

In this dialog you can modify the attributes of the signal that is currently selected. Just as in the signal list you can change the name, the start bit and the length of the signal.

|  | Caution! If you change the signals in a sub object, this will change the signals of all other sub objects of an array too. The signal lists of all objects of an array have to be identical. If the main object is a record, the signal lists of the sub objects can differ. |

The following table provides you an overview of the additional dialog elements which you can use to change the attributes of a signal.

| Dialog element | Description |
| --- | --- |
| Type | data type of the signal |
| Default | default value of the signal, initial value 0 |
| Low Limit | lower limit of the signal value (for signals with more than 64 bit, enter this value in hexadecimal format) |
| High Limit | higher limit of the signal value (for signals with more than 64 bit, enter this value in hexadecimal format) |
| Automatic calculation of limits | activates or deactivates the automatic calculation of the limit values |
| Unit | unit of the signal |
| Factor | used for the conversion of the signal value into a logical value |
| Offset | correction value to calculate the signal value for the generation of databases and the correct display in the Trace Window of CANoe/CANalyzer |

With the button [Get from object] in section Get object attributes you can 

[...truncated for brevity...]

---

## 菜单 (Menus)

**条目数**: 2

### OHID_G_CONTEXTMENU


# Context Menu

CANeds

The tool offers access to certain commands contained in the menu bar via the context menus of the tree objects. The context menus of a tree object contains only commands which are applicable to the selected tree.

To open the context menu of tree object you have to position the mouse pointer on the object and press the right key of the mouse.

| Version 15© Vector Informatik GmbH |  |


### OHID_G_MENUBAR


# Menu Bar

CANeds

The menu bar is located under the title bar of the application window and contains following menus:

- File

- Edit

- View

- Database

- Check

- Network

- Options

- Window

- Help

Additional to the commands contained in the menu bar line certain commands are accessible via the context menus.

| Version 15© Vector Informatik GmbH |  |


---

## 消息 (Messages)

**条目数**: 5

### HID_MSG_GENERAL


# Notifications

CANeds

The notifications are divided into error, warning and status notifications. The notification number indicates the type of notification:

## 0000 - 0999: Notifications of the EDS checker

These notifications are generated if an EDS is checked (see command Check EDS).

- Errors

- Warnings

## 1000 - 1099: Database comparison notifications

These notifications are generated if are compared via command Compare Object or attributes of an object have changed.

## 1100 - 1200: Notifications while an EDS is loaded

These notifications are generated if an EDS file is loaded.

| Version 15© Vector Informatik GmbH |  |


### HIDnotificationDatabase


# Database Comparison

CANeds » Notifications » Database Comparison

| ID | Notification / Description |
| --- | --- |
| warning 1000 | ... differs from selected database (...). An attribute of the object differs from the selected database. In the last brackets the possible correct values are shown. |
| warning 1001 | Number of sub objects is too small (...). The number of sub objects is smaller than needed in the selected database. In the last brackets the possible correct values are shown. |
| warning 1002 | Number of sub objects is too big (...). The number of sub objects is bigger than needed in the selected database. In the last brackets the possible correct values are shown. |
| warning 1003 | … is missing. An object attribute is missing. |
| warning 1004 | No comparison possible because database object is missing. There is no appropriate object in the database. |

| Version 15© Vector Informatik GmbH |  |


### HIDnotificationErrors


# Errors (CANchkEDS)

CANeds » Notifications » Errors (CANchkEDS)

| ID | Notification / Description |
| --- | --- |
| error 1 | Section [...] not found. Section doesn’t exist in the EDS because section name has wrong spelling or doesn’t exist. |
| error 2 | Incorrect brackets in section [...]. Section has no or incorrect enclosing brackets. E.g.: [sectionname) or sectionname] |
| error 3 | Illegal position of section name [...]. Left bracket of a section isn’t in the leftmost column. |
| error 4 | Duplicate section [...]. Two or more sections in the EDS have the same section name. E.g.: [1004ObjectLinks]ObjectLinks=1; 1=1004;[1004ObjectLink] ObjectLinks=1; 1=1007; An error is produced because two identical sections exist. Here the function reading the EDS overwrite value '1004' of the entry with value '1007'. This could produce additional confusing errors. |
| error 5 | Insufficient entries in section [...]. Value in the first entry is bigger than number of following entries. E.g.: [Comments]Lines=2Line1=second comment line ‘Line2’ is missing |
| error 6 | Insufficient sub objects in main section [...]. Number of sub objects in the main object is bigger than number of following sub objects. E.g.: [1004] SubNumber=2...[1004sub0] ... Section [1004sub1] is missing. |
| error 7 | Link [...] related to non-existent object. Linked section related to non-existent object. E.g.: [0001ObjectLinks]... Object [0001] doesn't exist. |
| error 8 | Access type in section [...] contradicts 

[...truncated for brevity...]

### HIDnotificationLoadEDS


# Loading EDS File

CANeds » Notifications » Loading EDS File

| ID | Notification / Description |
| --- | --- |
| warning 1100 | Entry ... is not read because object is not structured. An attribute is not read because the object is not structured. The entry is not lost, it is displayed in the Unknown Entry window. E.g.: [1000]ParameterName=Device TypeObjectType=0x7SubNumber=2 The SubNumber entry is not read because object type is VAR. |
| warning 1101 | Entry ... is not read because object is structured. An attribute is not read because the object is structured. The entry is not lost, it is displayed in the Unknown Entry window. So a deactivated field in the attribute window is not filled out. E.g.: [1003]ParameterName=PredefinedErrorFieldObjectType=0x8DataType=0x0007AccessType=rwPDOMapping=0SubNumber=2 Data type, access type and mapping information are not read because object type is ARRAY. |
| warning 1102 | Entry CompactSubObj is not read because entry SubNumber is bigger or equal null. Entry CompactSubObj is not read because a entry SubNumber is found in the same section which has a number bigger or equal null. The entry is not lost, it is displayed in the Unknown Entry window. E.g.: [1400]...CompactSubObj=2SubNumber=2... |

| Version 15© Vector Informatik GmbH |  |


### HIDnotificationWarnings


# Warnings (CANchkEDS)

CANeds » Notifications » Warnings (CANchkEDS)

| ID | Notification / Description |
| --- | --- |
| warning 1 | Unknown or not used section [...]. After all checks a section is found which has not been checked, because this section is unknown or not used. Section Error Cause [Tools] This section is unknown and produce this warning. [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. | Section | Error Cause | [Tools] | This section is unknown and produce this warning. | [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... | An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. |
| Section | Error Cause |
| [Tools] | This section is unknown and produce this warning. |
| [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... | An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. |
| warning 2 | Redundant sub object [...]. More entries are found than expected. E.g.: SubNumber=2... [1010sub0]... [1010sub1]... [1010sub2]... The last sub-object is redundant and causes the warning. |
| warning 3 | Illegal enumeration in section [...]. Enumeration is not correct. E.g.: [Comme

[...truncated for brevity...]

---

## 提示 (Tips)

**条目数**: 2

### OHID_TIPP_WND_OD_OVERVIEW


# Object Dictionary Overview

CANeds

By selecting the Object Dictionary pageand clicking the tree object Object Dictionary the right window shows all objects of the EDS file.

To get the best view click into the window and then press the key comtination <Ctrl> and <+> of number block. Now all columns are resized so that all text is visible. The same result you achieve with a double click on the divider of the column in the window header.

To sort a single column the header of the column has to be clicked.

Object Dictionary

| Version 15© Vector Informatik GmbH |  |


### OHID_TIPP_WND_OUTPUT_FLOAT


# Floating of the Output Window

CANeds

To give more place to all other windows you can display the output window in float mode.

Click therefor on the quadratic toggle button.

To dock the window again double click the title bar of the window or draw of the window to the edge of the frame window.

Output Window

| Version 15© Vector Informatik GmbH |  |


---

## 弹出框 (Popups)

**条目数**: 6

### CiA301


# CiA301

CANeds » Glossary

Application Layer and Communication Profile(CiA301 V4.02)

See Also

| Version 15© Vector Informatik GmbH |  |


### CiA301Appendix


# Appendix to CiA301

CANeds » Glossary

Test description for CANopen Devices(Appendix to CiA301 V4.0, Revision 2)

See Also

| Version 15© Vector Informatik GmbH |  |


### CiA302


# CiA302

CANeds » Glossary

Framework for CANopen Managers and Programmable CANopen Devices(CiA302 V4.01)

See Also

| Version 15© Vector Informatik GmbH |  |


### CiA306


# CiA306

CANeds » Glossary

Electronic Data Sheet Specification for CANopen(CiA306 V1.0)

See Also

| Version 15© Vector Informatik GmbH |  |


### canopen


# CANopen

CANeds » Glossary

CANopen is a registered community trade mark of CAN in Automation e.V.

| Version 15© Vector Informatik GmbH |  |


### cia


# CiA®

CANeds » Glossary

CAN in Automation e.V.

CiA® is a registered community trade mark of the CAN in Automation e.V.

See Also

| Version 15© Vector Informatik GmbH |  |

