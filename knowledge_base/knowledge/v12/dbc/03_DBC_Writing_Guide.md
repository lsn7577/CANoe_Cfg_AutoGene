# DBC File Writing Guide (Vector CANoe 12.0)

> 本文档基于 Vector CANoe 12.0 CANdb++ 帮助文档整理，涵盖 DBC (CAN database) 文件的编写、语法、关键字、属性。
> 适用对象：DBC 工程师、CANoe 配置工程师、网络通信设计工程师。
> 生成日期：2026/06/01
> 注: v12 使用 CANdb++ 作为 DBC 编辑器，与 v15 的 CANeds 存在结构差异。

---

## CANdb++ 概述 (v12)


# CANdb++

Start Page

All information that is processed in a networked bus system, as well as the interrelationships between units of information, are usually managed in a database.

CANdb++ is a data management program which can be used to create and modify these databases.

## New Features with program version 3.0

## Functional features of CANdb++:

- Creating a new CANdb network file (*.dbc)

- Modifying an existing CAN database

- Creating supplemental user-defined attributes for objects of the CAN database

- Defining value tables for signal values and environment variables

- Checking for consistency of the objects in a CAN database and their interrelationships

- Displaying the communication matrix

- Creating variants of an object

- Comparing objects of the same object type

- Exporting a CAN database

- Exporting an object

|  | Note Most CANdb++ dialogs can be changed in size.Exceptions to this are the standard windows dialogs, e.g. File-Open. It is easy to exchange or link data between different windows using the drag & drop feature.This is of special interest if the user has a very large signal list and e.g. would like to add a signal to a node. Currently this cannot be done easily on the left side of the Overview Window, since the user cannot scroll upwards.In such a case it is advisable to open a window with View|List|Signals and to drag the signal from this window to the node, e.g. under Rx Signals on the left side of the Overview Window. For detailed information on the differences in features between the different CANdb++ versions please refer to the table on the following Help page: Overview of CANdb++ program versions. |

Support

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 对象 (Objects)

**条目数**: 10

### OhidCANdb++ObjectNamingRules


# Rules for Naming Objects

CANdb++ » Objects

## Naming of the following objects follows the rules for naming C identifiers:

A C identifier begins with an alpha character or an underline ('_'). It may contain alphanumeric or underline characters. This is important since these names are used in automatically generated code, and this code is compiled by a C compiler or by CAPL.

- Signals, multiplexor signals, multiplexed signals

- Signal groups, multiplexor signal groups, multiplexed signal groups

- Messages

- Nodes/network nodes

- Value tables

- Environment variables (new with CANdb++ 2.7. SP8)

## There are no restrictions in naming the following objects:

- Controllers/ECUs

- Vehicles

- Networks

- Node groups

- Attributes

- Value descriptions within value tables*

|  | Note Names used by other tools, e.g. by CANgen, are also subject to naming rules for C identifiers. If nodes are exported as node-based in DBC files then the controller names are saved as valid C identifiers. In this operation any invalid characters within a name are deleted. Any invalid characters at the beginning of a name are replaced by an underline. During an export of environment variables and networks in DBC files their names are saved as valid C identifiers. In the process any invalid characters within a name are deleted. Any invalid characters at the beginning of a name are replaced by an underline. *Value descriptions within value tables may not content quotation marks ". This will caus

[...truncated for brevity...]

### OhidGECUs


# Control Units (ECUs: Electronic Control Units)

CANdb++ » Objects

Control units are the distributed processing units in the network.

Information is exchanged with other control units via network nodes, which represent the control unit's interface to the CAN bus.

Control units can also contain multiple sub-functions (functional nodes).

Environment variables are assigned to the control unit in the CANdb++ data model.

Several network nodes can be assigned to a control unit, which enables the modeling of gateways.

The name and comment of a control unit cannot be changed while processing, because a CANdb database doesn't support control units as independent objects.

When a database is opened a control unit is installed for every node.

|  | Note Whenever a network node is defined, CANdb automatically defines a ECU with the same name, and a link is installed between the new network node and the ECU. When a network node is designed (installed), this establishes a link to the one network of a DBC database. |

Since a DBC database always contains the data of exactly one network, a new network cannot be installed.

Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGGateway


# Gateway

CANdb++ » Objects

A Gateway is a special control unit, that is used as a connecting element between two or more CAN buses. Information is exchanged between the two buses via the network nodes of the Gateway.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGMessages


# Messages

CANdb++ » Objects

Messages can be transmitted over the CAN bus. A message is defined by the following system parameters:

- Symbolic message name

- Identifier (CAN ID)

- Number of data bytes (DLC Data Length Code)

- Transmission type (not with DBC files)

- Cycle time (if the message is transmitted cyclically) (not with DBC files)

- Network node, that sends the message With CANdb++ version 1.1 several nodes can be assigned to a message as a sender (node). This function is only available with a CANdb++ database (*.MDC file).

- Message Signals

- Comment

In addition, optionally the concrete values of user-defined attributes can be assigned to a message.

Optionally, the concrete values of user-defined attributes can be assigned to a message.

|  | Note The CAN ID of a message within a network must be unique, i.e. each CAN ID may only be used once within a network! |

Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGNetworks


# Network

CANdb++ » Objects

In a network there are usually multiple control units (ECUs) that are connected to one another by their network nodes (NN) and exchange information over the same CAN bus.

Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGNodeGroup


# Node Groups

CANdb++ » Objects

Multiple network nodes can be combined into a node group.

For example, all of the network nodes of a specific manufacturer could be combined into a Node Group.

Furthermore, node groups also permit structuring for variants of networks.

For example, all those network nodes that are used in every vehicle body bus can be used to form one node group. This node group is then linked to all variants of that network.

Network nodes that are not used in every vehicle body bus are then linked individually to the networks.

Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGNodes


# Network Nodes

CANdb++ » Objects

Network nodes are the interfaces of the control unit to a network, over which the control unit outputs information and receives information via the CAN bus.

A network node is defined by the following system parameters:

- Symbolic network node name

- Address

In addition, optionally the concrete values for user-defined attributes may also be assigned to a network node (see also functional network nodes).

|  | Note With CANdb++ version 1.1 several nodes may be assigned to a message as a senders (node). This function is only available with a CANdb++ database (*.MDC file). The address of a network node must be unique within the network, i.e. each network node address may only be used once within a network! Whenever a network node is defined, CANdb automatically defines a ECU with the same name, and a link is installed between the new network node and the ECU. When a network node is designed (installed), this establishes a link to the one network of a DBC database. |

Since a DBC database always contains the data of exactly one network, a new network cannot be installed.

Signals and message signals | Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGObjectTypes


# Object Types

CANdb++ » Objects

The following object types are available in CANdb++ and are shown on the left side of the Overall View Window:

| Table Head | Table Head |
| --- | --- |
|  | Vehicles |
|  | Networks |
|  | Control Units (ECUs) |
|  | Environment Variables |
|  | Node Groups |
|  | Network Nodes |
|  | Messages |
|  | Signals |

After selecting an object type all objects belonging to this object type are displayed on the right side of the Overall View Window.

The user may create as many individual objects as desired for each object type.

The object types are arranged hierarchically in the Overall View Window.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGObjects


# Objects and Object Symbols

CANdb++ » Objects

Instances of Object types are referred to as objects.In the Overall View Window an object symbol appears in front of each object so that the object can be visualized.

| Object Type | Object Icon | Object |
| --- | --- | --- |
| Vehicles |  | vehicle |
| Networks |  | network |
|  | linked network |
| Control Units (ECUs) |  | control unit |
|  | linked control unit |
| Gateways |  | gateway |
| Environment Variables |  | environment variable |
| Node Groups |  | node group |
|  | linked node group |
| Network Nodes |  | network node |
|  | linked network node |
| Messages |  | message |
|  | message that is received or sent by a network node |
| Signal Groups |  | Signal group |
| Packet Signal |  | packet signal |
|  | Sub signal within a packet signal |
| Signals |  | Signal |
|  |  | signal that is not mapped to a message |
|  | Gateway Signal(a signal that is routed over a gateway from one bus (Source Network) to another bus (destination network)).Gateway signals are displayed in the Overview Window under the vehicles object type.See also Gateway Signals. |
|  | message signal (signal that was linked to a message) |
|  | signal that is sent by a network node = Tx Signal |
|  | signal that is received by a network node = Rx Signal |
|  | signal that is received and sent by a network or node = Rx/Tx Signal |
|  | signals that is transmitted in a message from a network node = Mapped Tx Signal |
|  | signal that is received i

[...truncated for brevity...]

### OhidGSignals


# Signals and Message Signals

CANdb++ » Objects

Signals represent the smallest unit of information. A signal is defined by the following system parameters:

- Symbolic signal name

(see also rules for naming objects)

- Signal length The signal length is set in bits.

- Format (Intel or Motorola)

- Value type (data type)

| Data Type | Description |
| --- | --- |
| Signed: | Signed Integer of set length (two's complement)(the most significant bit is the sign (+/-) bit)value range: -2^(SigLength-1) to +2^(SigLength-1)-1 |
| Unsigned: | Unsigned Integer of set length value range: 0 to 2^SigLength-1 |
| IEEE Float: | 32 Bit IEEE Floatvalue range: 3,4 * 10^-38 to 3,4 * 10^38precision: 7 digits |
| IEEE Double: | 64 Bit IEEE Doublevalue range: 1,7 * 10^-308 to 1,7 * 10^308precision: 15 digits |
| In MDC databases the following additional types are available: |
| Boolean | 1-bit signal (unsigned) with the values true and false.A value table with a predefined name is automatically assigned to these signals.Boolean signals have neither a conversion formula nor Min or Max values. |
| ASCII | String (unsigned) with a length entry in characters (8 bits per Char).ASCII signals have neither a conversion formula nor Min or Max values. |
| UNICODE | String (unsigned int) with a length entry in characters (16 bits per Char).UNICODE signals have neither a conversion formula nor Min or Max values. |
| BCD | Binary encoded decimal numbers (unsigned) with a length entered in digits (4 bits p

[...truncated for brevity...]

---

## 菜单 (Menus)

**条目数**: 68

### CANdbMenuEditOverview


# Menu: Edit

CANdb++ » Menu Bar » Edit

Menu: Edit

The Edit menu contains following commands:

| Symbol | Shortcut | Menu | Description | Hint |
| --- | --- | --- | --- | --- |
| — | <Ctrl>+<Z> | Undo | Undoes the last action. | — |
| — | <Ins> | New | Creates a new object, user-defined attribute or value table. The command opens he Object dialog in which the user can define concrete values for system parameters. | — |
|  | <Return> | Edit | Opens an Object dialog in which the user can modify concrete parameter values for the selected object, user-defined attribute or value table. | — |
| — | — | Edit Common Attributes | — | — |
| — | — | Reset to Default | Resets user-defined attributes to their default value. If you edit the default value of an attribute in the right part of the Overview Window, it can be reset with Reset to default. The same command is available in the shortcut menu of the marked attribute. Default values are labeled with *. | — |
|  | <Ctrl>+<C> | Copy | Copies the selected object, user-defined attribute or value table to the clipboard. Afterwards it can be pasted or linked from the clipboard. | — |
|  | <Ctrl>+<V> | Paste | Inserts the contents of the clipboard. | — |
| — | — | Insert Link | Links the object in the clipboard with the selected object. | Possible links are shown in the table on the Data Model help page. |
| — | <Del> | Delete | Deletes the selected object,user-defined attribute, value table or link. When deleting a link only the link is

[...truncated for brevity...]

### ChangeCommonMultiplexAttrDialog


# Edit Common Multiplexor Attributes

CANdb++ » Multiplexor Concept » Edit Common Multiplexor Attributes

Using this function, a common multiplexor signal and the associated common multiplexor values can be defined for selected signals of a message.

Depending on the multiplexor concept used (Standard or Extended Multiplexor Concept), different dialogs will be displayed.

## Standard Multiplexor Concept in DBC Databases

The Edit common multiplexing properties [for Standard Multiplexing] dialog opens when DBC databases are processed for which no extended multiplexing is activated or used.

Select the signals, and then select Edit common multiplexor… in the shortcut menu.

The dialog permits only a single multiplexor value to be specified because only one multiplexor value can be defined for a multiplexed signal.

The dialog can only be opened if no multiplexor signal is selected, because for DBC standard multiplexing only one multiplexor signal per message is allowed.

The multiplexor signal can only be changed when all multiplexed signals of this message have been selected on the right-hand side of the main window (list overview) before the dialog is opened.

## Extended Multiplexor Concept in DBC and MDC Databases

|  | Note This function is only available in DBC and MDC databases if extended multiplexing is activated and supported by the database. For DBC databases the network attributes ProtocolType or BusType must be set as following, see limitations for extended multip

[...truncated for brevity...]

### ChangeCommonMultiplexAttrValDescr


# Dialog: Value Descriptions

CANdb++ » Multiplexor Concept » Edit Common Multiplexor Attributes » Select Multiplexor Value Descriptions

Value descriptions to be used as the multiplexor value can be selected using the Value Descriptions dialog.

Value descriptions for which the check box is already selected after the dialog is started are already used as the common multiplexor value in the Edit common multiplexing properties dialog.

Deactivating the check box removes the corresponding multiplexor value from the list of common multiplexor values.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_ATTRDEF_DIALOG


# Definition (Attribute Definition)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set the values of system parameters for the selected user-defined attribute here.

|  | Note When you enter 0 for both Minimum and Maximum, the Initial Value can be any value (according to the chosen Value Type). |

## [OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes and displays the attribute in the Attribute Definitions Window according to the changed configuration.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_COMMENT_DIALOG


# Comment

CANdb++ » Menu Bar » Edit

Menu: Edit

## Comment

The input box contains the comment.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_COMMONATTRIBUTES_DIALOG


# Edit Common Attributes

CANdb++ » Menu Bar » Edit

Menu: Edit

With this function/command you can edit common attributes of several objects together.

If you mark more than one entry in the window (e.g. several signals), you can edit/change the values of those entries together simultaneously.

## Proceed as follows to make these settings:

- Select the Signals (or Object or Networks or…) Select one of the signals (…) you wish to edit with the left mouse button. Hold the <Shift> key on the keyboard and select additional signals (…) you wish to edit with the left mouse button.

- Start Editing After selecting the signals (…) you should choose the Edit Common Attributes command in the context-/popup-menu (right mouse button) of the active window..

- Now you see a list view of the attributes of the selected signals (…). You can edit all attributes that have a check box on the left side of the attributes name.

- Activate the check box with the left mouse button. Place the mouse pointer in the active line of the Value row and press the left mouse button; this activates the editing function.

- Depending on the kind of attribute you can either enter the value directly (e.g. maximum, minimum) or you can select the value from a list box (e.g. type, access).

- With the [OK] button you accept the changes.With [Cancel] you undo all changes and close the window.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_CONTROLUNITLIST_DIALOG


# Control Unit (ECU)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Control Units

Appearing in the table on this page are all Control Units (ECUs) that are linked to the active/selected object.

[Add…]

Opens the Object Selection Dialog in which the user can select the ECUs with which the object should (also) be linked.

[Delete]

Removes the link between the ECU that was selected in the table and the active object. This action deletes neither the ECU nor the active/selected object!

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_CONTROLUNIT_DIALOG


# Definition (ECU)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected control unit here.

When creating a control unit a recommended concrete value appears in the input box Name. This value can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_DATA_SELECT


# Dialog: Object Selection

CANdb++

Appearing here are the objects that can be selected.The desired object(s) is/are selected by clicking the relevant line(s) in the table. The selected line is shown with a color background (Default: Blue).

|  | Note If you wish to select multiple lines in the table you must hold down the <Ctrl> key while clicking the specific lines. If you wish to select multiple lines in the table which lie directly below one another, you must click the first object and then, while holding down the <Shift> key, click the last object. All lines lying between these two lines are selected as well. To make it easier to view, a subset of the selectable objects can be displayed with the help of the Attribute and Value boxes and the [Selection] button. |

## Attribute list box

Here the user can select the system parameter or user-defined attribute whose concrete value is entered in the Value input box.

## Value input box

The concrete value for the system parameter or user-defined attribute can be input here.

## [Selection]

After clicking this button only those table lines are shown whose concrete values for the parameter or attribute selected in the Attribute list box matches the value in the Value input box.

## [OK]

Adds the specified link(s) and closes the dialog.

## [Cancel]

Aborts the procedure, i.e. the links are not added and the dialog is closed.

## [Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik

[...truncated for brevity...]

### HIDD_ENVVARLIST_DIALOG


# Environment Variables (Control Units (ECUs))

CANdb++ » Menu Bar » Edit

Menu: Edit

## Environment Variables

Appearing in the table on this page are all environment variables that are linked to the active/selected control unit (ECU).

- Name In this column the general symbol and the name of each environment variable is shown.

- Type In this column the Value Type of each environment variable is shown.

- Unit In this column the physical unit of the environment variable is shown.

[Add…]

Opens the Object Selection Dialog in which the user can select environment variables with which the ECU should (also) be linked.

[Delete]

Removes the link between the environment variable that was selected in the table and the ECU. This action deletes neither the environment variable nor the ECU!

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_ENVVAR_DIALOG


# Definition (Environment Variable)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected environment variable here.

When creating an environment variable a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

|  | Note Depending on data types of variables different fields are available. Please have a look on following page environment variable for detailed information. When you enter 0 for both Minimum and Maximum, the Initial Value can be any value (according to the chosen Value Type). |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_GROUP_DIALOG


# Definition (Node Group)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected node group here.

When creating a node group a recommended concrete value appears in the Name input box for this system parameter. This value can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_MESSAGELAYOUT_DIALOG


# Layout (Message)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Layout

Appearing on this page, to help visualize the message contents, is a graphic overview showing the positions of message signals within the message.

The signals can be arranged either

- with the buttons [To Front] and [To Back] or

- You can use the [Arrange] button to arrange the signals automatically.In this case:

- 8-bit signals should not exceed the 1-byte limit, or 16-bit signals the 2-byte limit.

- Signals with 8-16 bits should be arranged on byte limits.

- Signals with < 8 bits should not go past a byte limit and if possible should be arranged at the beginning of a message.

- graphically: You select a signal with the left mouse button, hold the button and move the signal (drag & drop).

With the buttons [Add…] you can add new signals, and with [Delete] you can remove placed signals.

If you activate the Bit Index Inverted option check box, the indexing in the byte will be sequential or inverted. Please refer to the Intel and Motorola format in CANdb++ page for detailed information on bit indexing.

All changes are displayed simultaneously in the Signals Page (e.g. new order of the signals if you rearranged them).

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_MESSAGELIST_DIALOG


# Messages/Tx Messages

CANdb++ » Menu Bar » Edit

Menu: Edit

## Messages/Tx Messages

Appearing in the table on this page are all messages, that were linked with the selected object.

[Add…]

Opens the Object Selection dialog in which the user can select the messages with which the object should also be linked.

[Delete]

Removes the link between the message that was selected in the table and the selected object.

|  | Note This action deletes neither the message nor the selected object! |

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_MESSAGESIGNAL_DIALOG


# Definition (Message Signal)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected message signal here.

When creating a message signal a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_MESSAGE_DIALOG


# Definition (Message)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected message here.

When creating a message a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

## [OK]

Accepts the changes and closes the dialog.

## [Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

## [Accept]

Accepts the changes.

## [Help]

Calls the CANdb++ Help topic for the active dialog.

## ID [...] - only on Definition page

Opens the J1939 Message, the J1587 Settings or the ARINC825 CAN ID dialog, depending on the used database.

Information on the Multiplexor Concept

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_NETWORKLIST_DIALOG


# Networks

CANdb++ » Menu Bar » Edit

Menu: Edit

## Networks

Appearing in the table on this page are all networks, with which the selected object was linked.

[Add…]

Opens the Object Selection dialog in which the user can select the networks with which the object should also be linked.

[Delete]

Removes the link between the network that was selected in the table and the selected object.

|  | Note This action deletes neither the network nor the selected object! |

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_NETWORK_DIALOG


# Definition (Network)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected network here.

When creating a network a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

|  | Note on working with dbc files If the attribute DBName is present in a dbc file, then the name of the network can be changed on the Network dialog (as long as the dbc file is not write-protected). If the attribute is not present, then the network name cannot be changed since a change cannot be saved. When working with mdc files, the attribute has no meaning. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_NODELIST_DIALOG


# Node/Transmitters/Receivers

CANdb++ » Menu Bar » Edit

Menu: Edit

## Node/'Transmitters/'Receivers

Appearing in the table on this page are all network nodes that were linked to the selected object.

[Add]

Opens the Object Selection dialog in which the user can select the network nodes that should also be linked to the object.

[Delete]

Removes the link between the network node that was selected in the table and the selected object.

|  | Note This action deletes neither the network node nor the selected object! |

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_NODE_DIALOG


# Definition (Node)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected network node here.

When creating a network node a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_OBJECT_STATUS_INFO_DIALOG


# Dialog: Object Status

CANdb++ » Menu Bar » Edit

Menu: Edit|Object Status

This dialog contains expanded status information for the selected object.

[Close]

Closes the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_PACKETSIGNAL_LAYOUT_DIALOG


# Layout (Packet)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Layout

Packet signals are only supported by MDC databases.

Appearing on this page, to help visualize the packet signal contents, is a graphic overview showing the positions of subsignals within the packet signal.

The signals can be arranged either

- with the buttons [To Front] and [To Back]

- graphically…by selecting a signal with the left mouse button, hold the button and move the signal (drag & drop).

With the buttons [Add…] you can add new signals, and with [Delete] you can remove placed signals.

If you activate the Bit Index Inverted option check box, the indexing in the byte will be sequential or inverted. Please refer to the Intel and Motorola format in CANdb++ page for detailed information on bit indexing.

All changes are displayed simultaneously in the Packet page (e.g. new order of the signals if you rearranged them).

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_RELATIONDEFINITION_DIALOG


# Definition (Relation)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

Here you can see some basic information about a specific relation.

Usually both linked objects (types) an their names are shown.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

This button is not available.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_RXNODELIST_DIALOG


# Receivers

CANdb++ » Menu Bar » Edit

Menu: Edit

## Receivers

Appearing in the table on this page are all network nodes, that the selected message or selected signal should receive.

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_SIGNALGROUP_DIALOG


# Definition (Signal Group, Multiplexor Signal Group, Multiplexed Signal Group)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected signal group here.

When creating a signal group a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_SIGNALLIST_DIALOG


# Signals (Rx/Tx, Mapped Rx/Tx, Packages)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Signals

Appearing in the table on this page are all signals, that were linked with the selected object.

Depending on the object this are:

- the signals that are transmitted on a message (mapped signals)

- the signals that are transmitted (Tx) or received (Rx) by a node

- the signals that are transmitted on a message (mapped Tx) or received on a message (mapped Rx) by a node

- the signals that are assigned to a packet signal as subsignals

[Add…]

Opens the Object Selection sialog in which the user can select the signals with which the object should also be linked.

[Delete]

Removes the link between the signal that was selected in the table and the selected object.

|  | Note This action deletes neither the signal nor the selected object! |

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_SIGNAL_DIALOG


# Definition (Signal)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected signal here.

When creating a signal a recommended concrete value appears in each of the input boxes for system parameters. These values can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

[Calculate minimum and maximum]

The values for the Minimum and Maximum input boxes are calculated considering the signal length, the value type, the factor and the offset. However, the calculated values can be changed manually at any time.

Signals and message signals

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_TXNODELIST_DIALOG


# Transmitters

CANdb++ » Menu Bar » Edit

Menu: Edit

## Transmitters

Appearing in the table of this page are all senders (network nodes) that are linked to the active or selected message.

- Name In this column the general symbol and the name of each sender are shown.

- Address Shown in this column are the addresses of each sender.

[Add…]

Opens the Object Selection dialog in which the user can select a sender with which the message should (also) be linked.

[Delete]

Removes the link between the sender that was selected in the table and the message. This action deletes neither the sender nor the message!

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_USER_ATTRIBUTE_LIST_DIALOG


# Attributes

CANdb++ » Menu Bar » Edit

Menu: Edit

## Attributes

Appearing in the table on this page are all user-defined attributes available for this object together with the valid attribute values for the object.

The attributes are arranged hierarchically according to the attribute categories defined in the candb.INI configuration file. Attributes that aren't assigned to any category are displayed under No category assigned.

An attribute value can be changed after double clicking the value.

If a * appears after the attribute value, the attribute still has the default value that was assigned when it was created.

As soon as the attribute value of an object is edited, the * will appear no longer – independently of the concrete attribute value assigned. So, edited attribute values are characterized by the absence of the *. If the object is assigned a value that corresponds to the defined default value from the attribute definition, the following message appears:

The value you have entered corresponds to the attribute default.Should the attribute be reset to the default value?[Yes] : The value is reset to the default value, for the object no explicit value will be saved in the database. [No] : The same value is saved in addition to the default value.

If the default value will be changed later, this only has an effect on objects for which no explicit value is saved.

The attribute value can be reset to the default value only by choosing the command button [Reset].

[Re

[...truncated for brevity...]

### HIDD_VALUEDESCRIPTION_DIALOG


# Value Description

CANdb++ » Menu Bar » Edit

Menu: Edit

## Value Description

Appearing in the table on this page are the actual values of the value table.

In the Value column are the values of signals or environment variables, which have been assigned symbolic names in the Description column.

|  | Note Values are only displayed if a value table is assigned to the signal or variable. |

[Add]

Adds a new line to the table.

[Delete]

Deletes the line that was selected in the table.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_VALUETABLE_DIALOG


# Definition (Value Table)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can define the values of system parameters for the selected value table here.

'Name' input box

The name of the value table can be input here.

'Comment' input box

The user can enter a comment on the value table here.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes and displays the value table in the Value Tables Window according to the changed configuration.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_VEHICLELIST_DIALOG


# Vehicles

CANdb++ » Menu Bar » Edit

Menu: Edit

## Vehicles

Appearing in the table on this page are all vehicles, with which the selected object may be linked.

[Add…]

Opens the Object Selection Dialog in which the user can select the vehicles with which the object should also be linked.

[Delete]

Removes the link between the vehicle that was selected in the table and the selected object.

|  | Note This action deletes neither the vehicle nor the selected object! |

[View...]

Opens the editing dialog of the marked object.

|  | Note No changes can be made in editing dialogs that were opened with this button. Their only purpose is to provide quick access to information. |

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_VEHICLE_DIALOG


# Definition (Vehicle)

CANdb++ » Menu Bar » Edit

Menu: Edit

## Definition

The user can set concrete values for system parameters of the selected vehicle here.

When creating a Vehicle the Name input box contains a recommended concrete value for the system parameter. This value can be changed.

[OK]

Accepts the changes and closes the dialog.

[Cancel]

Aborts the procedure, i.e. the changes are not accepted and the dialog is closed.

[Accept]

Accepts the changes.

[Help]

Calls the CANdb++ help topic for the active dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_DEL_MSG


# Deleting a Message

CANdb++ » Menu Bar » Edit

Menu: Edit

You can delete a message in the following manner:

- The Delete command in the Edit menu or in the shortcut menu Deletes the messages without the signals it contains.

- The shortcut menu command for the marked message Delete with signals Deletes the message and all signals that are not contained in any other message.

| Version 3.0.28© Vector Informatik GmbH |  |


### arinc825canIdDlg


# Dialog: ARINC825 CAN ID

CANdb++

This dialog supports you with the definition of the CAN identifier according the specification of ARINC 825.

To use this dialog, the following conditions must be fulfilled:

- The message type must have the value CAN Extended.

- The attribute ProtocolType must have the value ARINC825.

## Open this dialog

On page Definitions of the message dialog click [...] next to the ID field. Information The information of field Add. Info to interpret the CAN identifier are displayed in this dialog too.

## Define CAN identifier

The layout of the CAN identifier is defined dependent on the value of field Logical Communication ChannelLCC. If this value is changed, the current values of other fields may be newly interpreted by means of the new layout (see table below).

The value setting is done via a list or input field. Consider that the input and display of the field values is done in hexadecimal or decimal number format, dependent on the number format that is defined in CANdb++.

The following field names are used for the bit fields of the CAN identifier:

| Bit | Name | LCC Value | Meaning |
| --- | --- | --- | --- |
| 0, 2 | 4, 6 | 1, 3 | 5 | 7 |
| 26..28 | LCC | X | X | X | X | X | Logical communication channel |
| 19..25 | Source FID | X |  |  |  |  | Source function code identifier |
| 19..25 | Client FID |  | X |  |  |  | Client function code identifier |
| 18 | RSD | X |  |  |  |  | Reserved |
| 18 | SMT |  | X |  |  |  | Rervice message ty

[...truncated for brevity...]

### j1587messageDlg


# Dialog: J1587 Properties

CANdb++

In the J1587 Properties dialog you can exactly specify a J1587 parameter.

Per default the type of the parameter is PID. If you set the value Volvo to the network attribute J1587ProprietaryFormat you can select other types.

The PID merges parameter identifier and page, see Display a J1587 PID. Additionally the page is displayed separately. The value is updated automatically if the PID edit field looses focus.

Definition of a J1587 parameter

| Version 3.0.28© Vector Informatik GmbH |  |


### j1939messageDlg


# Dialog: J1939 Message

CANdb++

In the J1939 Message dialog you can exactly specify a J1939 Parameter Group.

You can insert the source and the destination address, the priority and the PGN (Parameter Group number) of the message.

For the source address you can use the values 0..253 (0x0..0xFD) and *. In this case * stands for the zero address that corresponds to the value 254 (0xFE).

The destination address can accept the same values as the source address. Additionally you can use the value All that stands for the global address (255 (0xFF)).

For the priority you can insert the values 1..7.

The valid value range for the PGN is 0x0..0x3FFFF.

|  | Note Please note that the PGN edit field and possibly the destination edit field are updated, if the PGN edit field loses the focus.If the PGN of a specific Parameter Group (PDU1 format) is entered, where the lower byte is greater than zero, this value will be used as destination address and it will be reset to zero in the PGN edit field. In contrast, if the PGN of a non-specific Parameter Group (PDU2 format) is entered, the destination address will be set to All. |

J1939 Basics | J1939 Extended CAN Identifier

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_EXPORT_DBC_NETWORKS_DIALOG


# Dialog: Export CANdb++ Data

CANdb++

Menu: File|Export CANdb++ Data

Displayed here is the list of networks that can be exported to CANdb network files.

|  | Note Both the data of individual networks (nodes, messages and signals) and environment variables (EV) are exported. The EVs are exported to a separate DBC file. EVs are available throughout the network. |

## Networks

All networks contained in the active database are listed in this overview.

## Environment Variables

This field contains the name of the file in which the associated environment variables are saved.

## Export of ECUs and Nodes

Two variants are available for exporting ECUs and nodes:

- Based on the ECUs

Taking the place of a network node is a node with the name of the ECU to which the network node is linked.

|  | Example Assume that two nodes N1 and N2 are linked to a ECU E1. In this case messages that are sent by N1 and N2 would be exported as if they were sent by just one node, that is E1. If a node N3 which is not linked to any ECU sends a message M3, this transmitting relation is not exported. |

- Based on the network nodes

The individual network nodes are exported as such, even if they are not linked to a ECU.

## Other Options

- Use compatible DBC format

If you activate the check box Use compatible DBC format, the attributes for time monitoring GenMsgTimeoutTime, GenSigTimeoutMsg and GenSigTimeoutTime will be generated from the relation attributes.

Generating these attributes allows f

[...truncated for brevity...]

### HID_APP_EXIT


# Exit

CANdb++ » Menu Bar » File » Exit

Menu: File|Exit

Closes the active CAN database and exits CANdb++.

## Shortcuts

| Standard Toolbar |  |
| --- | --- |
| Keyboard | <Alt>+<F4> |

|  | Note In CANdb++ the created or modified objects and links are written directly to the database.It is not necessary to save them explicitly. |

Notes on saving CAN databases

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_CLOSE


# Close

CANdb++ » Menu Bar » File » Close

Menu: File|Close

Closes the active CAN database.

## Shortcuts

| Standard Toolbar |  |
| --- | --- |
| Keyboard | <Ctrl>+<F4> |

|  | Note In CANdb++ the created or modified objects and links are written directly to the database. It is not necessary to save them explicitly. See also: Notes on saving CAN databases The active CAN database is automatically closed when the last window in the CANdb++Program Window is closed. |

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_COMMIT


# Save

CANdb++ » Menu Bar » File » Save

Menu: File|Save

This command is only available if the active database is a CANdb network file!

Commits the changes to the stored CANdb network file.

## Shortcuts

| Standard Toolbar |  |
| --- | --- |
| Keyboard | — |

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_DIFFERENCE


# Difference / Difference to Archive

CANdb++ » Menu Bar » File » Difference / Difference to Archive

Menu: File|Difference / Difference to Archive

## 'Difference' Command

Opens the Compare dialog in which the user can select the CAN database with which the active database should be compared.

After selecting the CAN database and clicking the [Open] button the two databases are compared and the results of the comparison are displayed in the Difference Window.

## 'Difference to Archive…' Command

This function requires an interface to the SourceSafe version management system.

The command opens a password request where you have to enter the correct archive password. After that the Difference to Archive dialog is opened. (see Open from Archive dialog)

After selecting the CAN database and clicking the [Open] button the two databases are compared and the results of the comparison are displayed in the Difference Window.

## Shortcuts

| Difference Toolbar |  |
| --- | --- |
| Keyboard | None |

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_MRU_FILE1


# List of Last Opened CAN Databases

CANdb++ » Menu Bar » File » List of Last Opened CAN Databases

Menu: File|List of Last Opened CAN Databases

Contained in this list are the CAN databases that were last opened with CANdb++.

Clicking a name causes the associated CAN database to be opened.

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_NEW


# Create Database

CANdb++ » Menu Bar » File » Create Database

Menu: File|Create Database

First, the Template dialog is opened. There you decide whether to chose a template for

- a CANdb Network (.dbc) or for

- a CANdb++ Database (.mdc).

See also: Notes on database templates

|  | Note MDC databases can only be created with CANdb++ Admin. |

Next you can select one of the available templates by a doubleclick or by a single click and chosing [OK].

After you have selected a template, the New Database File dialog opens, in which the memory location, file name and file type can be defined for the CAN database to be created.

Notes on file names and text fields:

- The size of text fields in databases is limited.

- Names may contain a maximum of 255 characters.To permit compatibility to DBC databases the names should be a maximum of 32 characters in length.

- All texts/text fields (e.g. comments, signal units, etc.) are limited to a length of 255 characters.

After selecting the memory location, entering the file name, selecting the file type and clicking the [Save] button a new database is automatically set up and is displayed in the Overall View Window.

When the file type CANdb++ database is selected the program automatically assigns the file name extension MDC.When selecting the file type CANdb network the file name extension DBC is automatically assigned.

## Shortcuts

| Standard Toolbar | None |
| --- | --- |
| Keyboard | <Ctrl>+<N> |

|  | Note on Names/Descriptor

[...truncated for brevity...]

### HID_FILE_OPEN


# Open Database

CANdb++ » Menu Bar » File » Open Database

Menu: File|Open Database

Opens the Open dialog in which the file to be opened can be selected.

After selecting the file type and the file to be opened and clicking the [Open] button the file is opened and is displayed in the Overall View Window.

## Shortcuts

| Standard Toolbar |  |
| --- | --- |
| Keyboard | <Ctrl>+<O> |

|  | Note If you choose a CAN database *.mdc in the program version CANdb++ Standard, this file is opened only write protected. Editing a CAN database is only possible with the program version CANdb++ Admin. |

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_SAVE_AS


# Export Into CANdb++ Database

CANdb++ » Menu Bar » File » Export Into CANdb++ Database

Menu: File|Export Into CANdb++ Database

Opens the Export Database Under dialog in which the memory location and file name can be defined for the CAN database to be exported.

Notes on file names and text fields:

- The size of text fields in databases is limited.

- Names may contain a maximum of 255 characters.To permit compatibility to DBC databases the names should be a maximum of 32 characters in length.

- All texts/text fields (e.g. comments, signal units, etc.) are limited to a length of 255 characters.

After selecting the memory location, entering the file name and clicking the [Save] button the entire data contents of the active database are automatically exported to a CANdb++ database.

|  | Note The File name extension MDC is assigned automatically. |

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_SAVE_ASDBC


# Export Into CANdb Network Files

CANdb++ » Menu Bar » File » Export Into CANdb Network Files

Menu: File|Export Into CANdb Network Files

Opens the Export CANdb++ Data dialog in which the memory location and file name can be defined for the CANdb++ networks to be exported.

Notes on file names and text fields:

- The size of text fields in databases is limited.

- Names may contain a maximum of 255 characters.To permit compatibility to DBC databases the names should be a maximum of 32 characters in length.

- All texts/text fields (e.g. comments, signal units, etc.) are limited to a length of 255 characters.

After selecting the memory location, entering the file names and clicking the [OK] button the networks are automatically exported to CANdb network files.

|  | Note The File name extension DBC is assigned automatically. |

Network Protocols for *.dbc Files

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_SAVE_CSV


# Export List of Objects

CANdb++ » Menu Bar » File » Export List of Objects

Menu: File|Export List of Objects

Opens the Export Object List Under dialog, where storage location, file name, and separator of the CSV file can be specified. Objects that are shown in the List view are saved with the displayed attributes in the visible sort sequence.

The separator can either be selected directly in the selection field or freely defined.

The data from the list view is exported as it is displayed on the screen. Hidden columns and the * that identifies a default value will not be saved.The column titles are exported in the first line of the CSV file.

|  | Note on Names/Descriptors and on Zip/Unzip Some Zip programs have problems with certain characters, e.g. umlauts (mutated vowels; ä, ö, ü), "ß", space. These characters are altered during a zip/unzip operation without any feedback/confirmation. This results in configurations that do not work (properly) any longer after unzipping. Please use only names/descriptors that do not contain any of these characters. |

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_FILE_VALIDATE


# Validate

CANdb++ » Menu Bar » File » Validate

Menu: File|Validate

Checks the objects of the CAN database and their interrelationships for consistency and displays the results of the consistency check in a Consistency Check Window.

You can use the Consistency check shortcut menu command of a marked network to perform a consistency check for an individual network.

|  | Note You can specify information for the consistency check in the Settings dialog (Options menu). |

| Version 3.0.28© Vector Informatik GmbH |  |


### ImportAttributeDef


# Import Attribute Definitions

CANdb++ » Menu Bar » File » Import Attribute Definitions

Menu: File|Import Attribute Definitions

Opens the dialog Import Attribute Definitions from where you can choose the database, from which the Attribute Definitions should be take over to the current database.

Information on importing attribute definitions is displayed in the CANdb++ Import - Results Window.

Attribute Definition Window | Database templates

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_CANdb++_Export_compatible_dbc-format_notes-1


# Explanation/addendum for export with the option 'Use compatible DBC format'

CANdb++

## Relations of type 'Node - mapped Rx signals' and 'Control unit - environment variable'

When exporting into compatible DBC format, user-defined attributes for Node - mapped Rx signals and Control unit - environment variable are not exported; that is, this information is lost.(Special case: GenSigTimeoutMsg and GenSigTimeoutTime)

## Relations of type 'Node - Tx message'

The information for relations of type Node - Tx message are not lost on export as long as only one transmitter is defined for a message. In this case the relation attribute is simply converted to a message attribute on export; this message attribute has the same name as the relation attribute.

## Relations of type 'Network - node'

Relations of the type Network - node are exported as node attributes.

Since in each dbc file only one network is managed, the assignment is unambiguous and no information is lost.

## Relations of type 'Control unit - node'

Relations of the type Control unit - node are exported as node attributes.

When exporting on the Basis of network nodes no information is lost as long as only one ECU is assigned to a node.

When exporting on the Basis of ECUs no information is lost as long as only one node is assigned to an ECU.

## Relations of type 'Control unit - environment variable'

The information for relations of the type Control unit - environment variable are lost on export.

## Relations o

[...truncated for brevity...]

### OHID_CANdb++_Export_compatible_dbc-format_notes-1_special_case


# Special Case: GenSigTimeoutMsg and GenSigTimeoutTime

CANdb++

GenSigTimeoutMsg and GenSigTimeoutTime are attribute definitions for the object type Node - mapped Rx signal and serve to describe relations between nodes and mapped signals.

Since these relations cannot be saved in compatible DBC format, they are converted accordingly on export.

On conversion, for each Node - mapped Rx signal relation, a signal attribute is generated. The name of the signal attribute is made up of the prefix GenSigTimeoutMsg_ (or GenSigTimeoutTime_) and the name of the node that is attached to this prefix.

The value of the respective signal attribute corresponds to the value of the relation.

|  | Example for the relation between a node MotorDiagnosis and a mapped signal Diagnostics the signal attributes GenSigTimeoutMsg_MotorDiagnose and GenSigTimeoutTime_MotorDiagnose are generated. The attributes for the signal Diagnostics have the values of the relation. Additional mapped Rx signals that are received by the node MotorDiagnosis also have the attributes GenSigTimeoutMsg_MotorDiagnose and GenSigTimeoutTime_MotorDiagnose after the export, however with the value that corresponds to their relation to the node MotorDiagnosis. Before export (from mdc database): Node: Mapped Rx Signal (message): GenSigTimeoutTime: MotorDiagnosis Diagnostics (DiagnosticData) 100 Status (DiagnosticData) 50 ErrorCode (DiagnosticData) 0 After the export in compatible dbc database: Signal (message): GenSigTimeoutMsg_

[...truncated for brevity...]

### OHID_CANdb_menu_file_script_execute


# Execute Script

CANdb++ » Menu Bar » File » Execute Script

Menu: File|Execute Script

Opens the Execute Script dialog, where you can select the script, that has to be executed.

After selecting the file and clicking [Open] the script will be executed.

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_FILE_SAVE


# Save As

CANdb++ » Menu Bar » File » Save As

Menu: File|Save As

This command is only available if the active database is a CANdb network file!

Opens the Export Database Under dialog. Here you can define the name the opened CANdb Network File should be saved with.

|  | Note on Names/Descriptors and on Zip/Unzip Some Zip programs have problems with certain characters, e.g. umlauts (mutated vowels; ä, ö, ü), "ß", space. These characters are altered during a zip/unzip operation without any feedback/confirmation. This results in configurations that do not work (properly) any longer after unzipping. Please use only names/descriptors that do not contain any of these characters. |

| Version 3.0.28© Vector Informatik GmbH |  |


### NetworkDesigner_Menu_View


# Menu: View

CANdb++ » Menu Bar » View

Menu: View

The View menu contains the following commands:

| Icon | Shortcut | Menu | Description |
| --- | --- | --- | --- |
|  | — | Overview | This opens an Overall View menu which contains a summary of the contents of the active CAN database. |
| — | — | List – Vehicles | Shows all vehicles in a List Window. |
| — | — | List – Networks | Shows all networks in a List Window. |
| — | — | List – Control Units | Shows all control units (ECUs) in a List Window. |
| — | — | List – Environment Variables | Shows all environment variables in a List Window. |
| — | — | List – Nodes | Shows all network nodes in a List Window. |
| — | — | List – Messages | Shows all messages in a List Window. |
| — | — | List – Signals | Shows all signals in a List Window. |
|  | — | Attribute Definitions | Opens an Attribute Definitions Window with a list of the user-defined attributes. New user-defined attributes can be added and existing attributes can be edited in this window. |
|  | — | Value Tables | Opens a Value Tables Window with a list of the user-defined value tables in which individual signal values or environment variable values can be assigned symbolic names. |
| — | — | Communication Matrix | Opens a Communication Matrix Window with the communication matrix of the active CAN database. You can choose between the following views: All networks Single networkIn the following dialog you can choose the network that will be displayed. |
| — | — | J19

[...truncated for brevity...]

### OhidGMainMenuBar


# Menu Bar

CANdb++ » Menu Bar

The menu bar is located beneath the Title Bar of the CANdb++ Program Window and contains the following menus:

- File

- Edit

- View

- Options

- Window

- Help

Besides the commands contained in the menus of the Main Menu Bar, CANdb++ offers access to additional executable commands in the shortcut menus of the objects.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidMenuFile


# Menu: File

CANdb++ » Menu Bar » File

Menu: File

The File menu contains the following commands:

- Create Database...

- Open Database...

- Close

- Save (only available for DBC databases)

- Save as… (only available for DBC databases)

- Export

- Export|Into CANdb Network Files...

- Export List of Objects...

- Import Attribute Definitions...

- Consistency Check

- Execute Script…

- Plug-Ins (Specific modules must be installed.)

- Exit

Located above the Exit command is the List of last opened CAN databases.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidMenuHelp


# Menu: Help

CANdb++ » Menu Bar » Help

Menu: Help

The Help menu contains the following commands:

| Icon | Shortcut | Menu | Description |
| --- | --- | --- | --- |
| — | <F1> | CANdb++ Help | Calls CANdb++ help. |
| — | — | Using Help | Calls a help containing information on using and optimizing help. As an alternative to this command you can also open this help topic by pressing the <F1> key while CANdb++ help is active. |
| — | — | About CANdb++ | The following information about CANdb++ is displayed here: Version number Copyright |

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidMenuOptions


# Menu: Options

CANdb++ » Menu Bar » Options

Menu: Options

The Options menu contains the following commands:

- Settings...

- Customize...

- Toolbar

- Status Bar

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidMenuWindow


# Menu: Window

CANdb++ » Menu Bar » File

Menu: Window

The Window menu contains the following commands:

| Icon | Shortcut | Menu | Description | Hint |
| --- | --- | --- | --- | --- |
|  | — | Cascade | Arranges the opened windows so that they overlap, whereby the title bars of the individual windows remain visible. | — |
|  | — | Tile Horizontal | Arranges the opened windows so that they lie above one another. | — |
|  | — | Tile Vertical | Arranges the opened windows so that they are side-by-side. | — |
| — | — | Arrange Symbols | Arranges the icons of minimized windows along the lower border of the CANdb++ Program Window. | This command has no effect on the sizes and positions of windows that are not minimized. |
| — | — | Located beneath the commands is the List of opened windows. | Contained in this list are all opened windows. A window can be activated by clicking its name.Appearing in front of the name of the active window is a . | — |

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_CHECKOPTIONS_DIALOG


# Consistency Check

CANdb++ » Menu Bar » Options » Settings » Consistency Check

Menu: Options|Settings|Consistency Check

On this page you define the content of the output of a consistency check. You can change these settings even after performing a consistency check and directly apply the changes to the Output/Result Window.

## Importance

Here you can control the quantity of information by selecting the kind of information you want to see. You can choose:

- Info

- Warnings

- Error

## Object Types

Now you can select the object types you want to include in the consistency check (in the Results Window respectively).

- Signals

- Messages

- Nodes/ECUs

- Networks

- Other

## Type

In this section you specify which type of information you want to be shown in the Results Window.

- Values

- Rx/Tx Relation

- Signal arrangement

- Missing connections

- Compatibility

- System messages

- Manufacturer-specific

- Value range violations

- Unmapped objects (Overall view)

## Special Checks

- DLC of messagesWhen this option check box is activated the DLCs of messages are checked.In the default setting validation is activated, i.e. the check box is marked.

- Lengths of signalsWhen this option check box is activated signal lengths are validated.In the default setting validation is enabled, i.e. the check box is activated.

Consistency Check Window

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_DISPLAYOPTIONS_DIALOG


# Display

CANdb++ » Menu Bar » Options » Settings » Display

Menu: Options|Settings|Display

Here the user can set the numbering format and the message identifiers that should be used.

## Number format

Here the user can set the numbering format for message identifiers (CAN IDs) and for the addresses of network nodes.

## Message Identifiers

Here the identifier type for messages can be set.

|  | Example If Name is selected, only the symbolic names of messages are displayed in the Overall View Window. |

## Number Format for Attributes

With this check boxes you can define that

- Int-Attributes shall always be interpreted and displayed decimal (or not) and

- Hex-Attributes shall always be interpreted and displayed hexadecimal (or not).

## Sorting of Signals in Message Dialog

With these option buttons you can chose, whether the signals are displayed

- in ascending alphabetical order of their names or

- ordered by their starting position (Offset).

## Message names:

Four modes are available to you for representing message names:

- Name

- Name [ID]

- ID

- ID [Name]

## Display Format for Signal Start Bit

On the page Intel and Motorola formats in CANdb++ you will find detailed information about the two formats.

For the Motorola format there are four options:

- Motorola Forward LSB

- Motorola Backward

- Motorola Sequential

- Motorola Forward MSB

For the Intel format there are two options:

- Intel Standard

- Intel Sequential

## Bit Index Inverted

If you ac

[...truncated for brevity...]

### HIDD_DLG_SETTINGS


# Defaults

CANdb++ » Menu Bar » Options » Settings » Defaults

Menu: Options|Settings|Defaults

On this page, you can make settings in order to influence the values that are used when creating a new object (signal or message).

If in one of the byte order for signals / value for signals / type for messages selection boxes the value default is selected, then upon creation of a new object, the pre-set default value (in the default selection field) is used for this object.

If in the selection box last value is used, then upon creation of a new object, the value is used that was set for the last new object.

|  | Example A new signal is created. The setting for new signals is, e.g. Value: Default with standard value Unsigned Byte order: Last value In this case, the dialog in which the new signal object is displayed for editing is pre-occupied with the default value Unsigned for the value type. In addition, the byte order for the signal is set according to a previously newly-created signal. |

|  | Note If the pre-set default value (for the default setting) or the last-used value (for the last value setting) cannot be used (because, e.g. the setting is not available in the loaded database), then a more sensible default value delivered by the system is used. |

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_ETCOPTIONS_DIALOG


# Edit

CANdb++ » Menu Bar » Options » Settings » Edit

Menu: Options|Settings|Edit

To permit modeling of Transport Protocols (TP) it may be necessary to override the length restrictions for signals and messages.

Option check boxes can be used to activate/deactivate validation of the DLCs of messages and the lengths of signals. The configured settings are automatically saved to the registered database.

## Messages

- Automatic DLC adaptation When this check box is activated DLCs are automatically adapted when messages are created/defined.When message signals are added or deleted the DLC of the affected message is automatically readjusted.

- Report different byte order during consistency check If this check box is activated, the system will report during a consistency check if a message contains signals > 1 bit both in Intel and Motorola format.

## Signals

- Automatic Min-Max calculation If this check box is activated the minimum and maximum values of signals are calculated automatically as soon the length, the value type, the factor or the offset of a signal is changed in the list view.

- The automatically calculated values may be adjusted manually at any time.

- This function has no effect for signals with minimum and maximum value = 0.

- Signals >= 8/16 must fall on 1-byte or 2-byte limitsActivating this check box specifies that 8-bit or 16-bit signals must lie directly on a 1-byte or 2-byte limit and must not exceed the respective limit.The consistency check will

[...truncated for brevity...]

### HIDD_SETTINGS_LONG_NAMES


# Long Names

CANdb++ » Menu Bar » Options » Settings » Long Names

Menu: Options|Settings|Long Names

The Limit to ... characters entry box can be used to specify how many characters should be allowed for the naming of signals, messages, nodes environment variables or value descriptions and accepted upon validation of a name.

- The symbolic names of the objects signals, messages, nodes and environment variables may have a length up to 128 characters.

- The identifiers of value descriptions may have a length up to 255 characters.

|  | Note on Compatibility When saving to DBC files, symbolic names of the objects mentioned above will be saved as before with up to 32 characters. For symbolic names of the objects mentioned above with more than 32 characters a unique short name 32 characters in length is generated from the (long) symbolic name. These short symbolic names are used by older tools that do not support long symbolic names. The long name itself is saved in an attribute generated by CANdb++: SystemSignalLongSymbol for signal names SystemMessageLongSymbol for message names SystemNodeLongSymbol for node names SystemEnvVarLongSymbol for environment variable names If the names of several objects of the same object type (e.g. signals or messages) are identical for the first 32 characters, a unique 32-character name is created upon saving by using the first 27 characters and adding a suffix (e.g. '_0000'). |

|  | Do not edit manually! The SystemXX attributes generated in 

[...truncated for brevity...]

### HID_PREFERENCES_OPTIONS


# Settings

CANdb++ » Menu Bar » Options » Settings

Menu: Options|Settings

Opens the Settings dialog.

On the Display page of this dialog you can define which numbering format and which message identifiers should be used.

On the Edit page of this dialog you can activate the automatic DLC adaptation of messages and the automatic Min-Max calculation of signals.

On the Consistency Check page of this dialog you define the output of the information of a consistency check. You also can change these settings after a consistency check and directly apply to the shown Result Window.

On the Default page of this dialog you can make settings to influence values that are used to create a new object (signal or message).

On the Long Names page you can specify the settings pertaining to the allowed length of object names.

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_VIEW_STATUS_BAR


# Status Bar

CANdb++ » Menu Bar » Options » Status Bar

Menu: Options|Status Bar

Shows or hides the Status bar.

When the status bar is shown a appears in front of this command in the menu.

| Version 3.0.28© Vector Informatik GmbH |  |


### HID_VIEW_TOOLBAR


# Toolbar

CANdb++ » Menu Bar » Options » Toolbar

Menu: Options|Toolbar

Shows or hides the Toolbar of the CANdb++ Program window.

When the toolbar is shown a appears in front of this command in the menu.

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 操作步骤 (Procedures)

**条目数**: 18

### CANdb++VariantHandling


# Notes on the handling of variants

CANdb++

## Basics

In CANdb++ databases all variants of a vehicle platform must be maintained. This includes the vehicle variants itself, as well as the variants of networks and ECUs linked to the vehicle. Sometimes even the communication nodes and the messages have several variants.

## Creation and structure of variants

In the first step, the variants of all the objects mentioned above have to be stored in the database (see Creating variants or copies of an object). Second, the interconnections between the variants of the same object must be stored in the database and made visible at the user interface.

|  | Example For a specific platform a variant Sedan and a variant Convertible exist. The sedan has four doors, the convertible only two. The convertible has an ECU controlling the roof top which is not used in the sedan. This may be described by the following variant tree: Sedan LeftFrontDoor_ECU RightFrontDoor_ECU LeftRearDoor_ECU RightRearDoor_ECU Convertible LeftFrontDoor_ECU RightFrontDoor_ECU RoofTop_ECU |

## Relations and structures in CANdb++ databases

CANdb++ databases stores a set of basic objects (e.g. signals, messages, network nodes, networks, ECUs and vehicles). The objects are related to each other in very defined ways:

- Signals…are mapped on messages and will be transmitted and received by nodes.

- Messages…are transmitted/received by nodes

- Network nodes…are connected to networks and are realized in ECUs

- Net

[...truncated for brevity...]

### CompareObjects


# Comparing Objects

CANdb++

To determine whether objects differ and which differences exist between the objects, objects of the same object type may be compared.

Proceed as follows to compare the objects:

- On the right side of the Overall View Window or in the List Window select the objects that you wish to compare.Independent of the sequence in which the objects are selected, the object that was created first is always utilized as the comparison object. The other object is then utilized as the reference object.

- Choose the Edit|Compare command. The results of the comparison are displayed in the Difference Window.

|  | Note Hold down the <Ctrl> key to select multiple objects. |

| Version 3.0.28© Vector Informatik GmbH |  |


### ConsistencyCheck


# Consistency Check of a CAN Database

CANdb++

To determine whether the objects of a CAN database and their interrelationships are consistent, an automatic consistency check may be performed with CANdb++.

Proceed as follows to perform a consistency check:

Choose the File|Validate command to start the automatic consistency check.The results of the consistency check are displayed in a Consistency Check Window.

| Version 3.0.28© Vector Informatik GmbH |  |


### CreateAReport


# Creating a Report

CANdb++

Executable reports establish which information (layout) will be displayed and presented in a report to be created at a later time. To permit the creation of reports, the 'Crystal Reports' software from the 'Seagate' or Crystal Decisions company must be installed.

|  | Caution! Crystal Reports is not included with the CANdb++ or CANdb++ Admin product! |

Proceed as follows to create an executable report:

- Create an executable report with the Crystal Report Designer and save it in the CANdb++ Reports directory (Default: C:\Programs\CANdb++\Reports). As the database assign to the report the MS Access file Report.MDB that exists in the directory. To avoid dependencies to fixed paths for the report you can define the database path as a relative path. This involves opening the Define Path dialog by the Database|Define path command.

- Select the database fields for the report from the database. Define the sorting order and the groupings of data.

- Define the positions and layouts of the individual fields.

- Save the report in the CANdb++ Reports directory (Default: C:\Programs\CANdb++\Reports). Reports can be generated with this report. (Generating a report)

## Notes on Reports

Essentially both CANdb++ reports (RPT) and executable reports (EXE) may be used for report generation.

### CANdb++ Reports (*.rpt)

- These reports may only be called up and executed within CANdb++.

- Supplemental parameters may be passed to these reports when they are

[...truncated for brevity...]

### CreateAnObjectVariant


# Creating Variants or Copies of an Object

CANdb++

Proceed as follows to create a variant or a copy of an object:

- Select the object of which a variant or copy is to be created.

- Copy the selected object to the Clipboard using the Edit|Copy command.As an alternative to this you could also use the Copy command from the selected object's shortcut menu.

- If you wish to insert the variant or copy in an active List Window continue with step 4.If you wish to insert the variant or copy in the Overall View Window select the object type of the previously copied object.

- Paste the copy of the object from the clipboard using the Edit|Paste command to create the variant.

- Modify the variant or the copy of the object (if necessary).

|  | Caution! After creating a variant or copy of an object, this variant or copy is completely independent of the source object!Modifications of the source objects are not mirrored in the variant or copy.If necessary, the variants or copies have to be modified manually. |

Objects of the same object type can be compared to determine if they are different and which differences exist (Comparing objects).

Notes on the handling of variants

| Version 3.0.28© Vector Informatik GmbH |  |


### CreateCANdbNetworkFile


# Creating a CANdb Network File

CANdb++

With CANdb++ databases can also be created in the form of CANdb network files with the file name extension DBC whose format is compatible with the CANdb Editor (CAN Database Editor).

Proceed as follows to create a CANdb network file:

- Choose the File|Create Database command to create a new CANdb network file and have it displayed in the Overall View Window.

- Create all necessary objects.

- Add all necessary links.

- Check for consistency of the database.

|  | Note Use the File|Commit Changes command to save a CANdb network file. |

|  | Note on Names/Descriptors and on Zip/Unzip Some Zip programs have problems with certain characters, e.g. umlauts (mutated vowels; ä, ö, ü), "ß", space. These characters are altered during a zip/unzip operation without any feedback/confirmation. This results in configurations that do not work (properly) any longer after unzipping. Please use only names/descriptors that do not contain any of these characters. |

| Version 3.0.28© Vector Informatik GmbH |  |


### CreateLink


# Adding a Link

CANdb++

Proceed as follows to add a link:

- Select the object you wish to link.

- Copy the selected object to the Clipboard with the Edit|Copy command.

- Select the object to which the object just copied should be linked.

- Add the new link with the Edit|Insert Connection command. The link is added.

As an alternative to this you could also add a link by

- Show the structure level of the object to which a link should be made.

- Select the object you wish to link.

- While holding down the mouse button drag the selected object to the object to which you wish to link it.

- When the mouse pointer is located above the object to which you wish to link the selected object, release the mouse button. The link is then added.

|  | When the mouse pointer assumes this form linking is possible. |
| --- | --- |
|  | When the mouse pointer assumes this form linking cannot take place. |

The object symbols of linked objects are identified by the linking symbol .

| Version 3.0.28© Vector Informatik GmbH |  |


### CreateNewObject


# Creating an Object

CANdb++

Proceed as follows to create an object in the Overall View Window:

- On the left side of the Overall View Window select the object type of the new object you wish to create.

- Choose the Edit|New commandThis opens the Object dialog. Appearing in each of the input boxes of the Object dialog are recommendations for the concrete values of system parameters.

- Change the values in the Object dialog (if necessary) and click the [OK] button.The newly created object than appears on the right side of the Overall View Window.

Proceed as follows to create an object in a List Window:

- Choose the Edit|New commandThis opens the Object dialog. In each of the input boxes of the Object dialog are recommendations for the concrete values of system parameters.

- Change the values in the Object dialog (if necessary) and click the [OK] button.The newly created object appears in the List Window.

|  | Note In a List Window only those objects can be created whose object type is represented in the List Window. |

| Version 3.0.28© Vector Informatik GmbH |  |


### CreateSignalGroup


# Creating a Signal Group

CANdb++

Proceed as follows to create a signal group in the Overall View Window:

- Select the message on which the signals to be combined in a group are to be transferred.

- Choose the New Signal Group command from the selected object's shortcut menu. The new signal group appears in the left area of the Overall View Window.

Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### DefineUserDefinedAttributes


# Creating User-Defined Attributes

CANdb++

Besides system parameters, that must be defined when creating an object, user-defined attributes can also be assigned to the object. The values of the user-defined attributes appear, as do the values of system parameters, in the columns in the right area of the Overall View Window or in the relevant List Windows.

Proceed as follows to create a user-defined attribute:

- Activate the Attribute Definitions Window. If the Attribute Definitions Window is not yet opened, open it with the View|Attribute Definitions command.

- Choose the Edit|New command. he Attribute Definition Object dialog is opened. Appearing in each of the input boxes are recommendations for the concrete values of system parameters.

- Change the values in the Object dialog (if necessary) and click the [OK] button.The newly created attribute appears in the Attribute Definitions Window.

|  | Note The value in the Default input box is assigned to each object as default value of the user-defined attribute. Objects that have still the default value of the user-defined attribute are marked in the right area of the overview window with a * behind the attribute value. |

user-defined attributes at object relations | Attributes of type File

| Version 3.0.28© Vector Informatik GmbH |  |


### DefineValueTables


# Defining Value Tables

CANdb++

Value tables can be used to assign symbolic names to the values of signals and environment variables.

Proceed as follows to define a value table:

- Activate the Value Tables Window. If the Value Tables Window is not opened yet, open it with the View|Value Tables command.

- Choose the Edit|New command.The Value Table object dialog is opened.Appearing in each of the input boxes are recommendations for the concrete values of system parameters.

- Change the values in the object dialog (if necessary) and click the [OK] button.The newly created value table appears in the Value Tables Window.

|  | Note The value table name defined by the user must not begin with the prefix VtSig_ resp. VtEv_. These prefixes are used internally. |

| Version 3.0.28© Vector Informatik GmbH |  |


### DeleteALink


# Deleting a Link

CANdb++

Proceed as follows to delete a link:

- Select the link to be deleted.

- Delete the link by choosing the Edit|Delete command.As an alternative to this you could also choose the Remove command from the selected link's shortcut menu.

|  | Note When deleting a link only the link is removed. The original object remains preserved. |

| Version 3.0.28© Vector Informatik GmbH |  |


### DeleteObjects


# Deleting an Object, Attribute or Value Table

CANdb++

Proceed as follows to delete an object, attribute or value table:

- Select the object, attribute or value table to be deleted.

- Delete the object, attribute or value table by choosing the Edit|Delete commandAs an alternative to this you could also choose the Delete command from the selected object's shortcut menu.

| Version 3.0.28© Vector Informatik GmbH |  |


### ExportDatabase


# Exporting a CAN Database

CANdb++

Proceed as follows to export a CAN database:

- Open the database that you wish to export. Use the File|Open File command to open a database that was saved in a folder which is accessible to you.If you are using CANdb++ Admin you may also open a database that was saved in the Version Administration archive. To do this use the File|Open from Archive command.The opened database is displayed in the Overall View Window.

- Choose the File|Export - Into CANdb++ Database command to export the latest total data set to a CANdb++ database or the File|Export – Into CANdb Network Files command to export the latest total data set to CANdb network files.

| Version 3.0.28© Vector Informatik GmbH |  |


### ExportObjects


# Exporting Objects

CANdb++

Objects of the following object types can be exported separately:

- Vehicles

- Networks

- Control Units

With an Export the object, including all objects linked to this object, are written to a new CAN database that only contains information relevant to this object.

Proceed as follows to export an object:

- Select the object to be exported.

- Choose the Export command from the selected object's shortcut menu.

- Make all necessary entries and confirm them.The object is then exported.

| Version 3.0.28© Vector Informatik GmbH |  |


### HintsSavingCANDatabases


# Notes on Saving CAN Databases

CANdb++

In CANdb++ the created or modified objects and links are written directly to the CANdb++ database. It is not necessary to save CANdb++ databases explicitly.

Use the File|Commit Changes command to save a CANdb network file.

Use the File|Export – Into CANdb++ Database command to save a CANdb++ database under a different name.

The CANdb++ Admin program version provides you with Version Administration for CAN databases with direct access to CAN databases that were saved in MS Visual Source Safe.

| Version 3.0.28© Vector Informatik GmbH |  |


### ModifyObjects


# Modifying an Object, Attribute or Value Table

CANdb++

Proceed as follows to modify an object, attribute or value table:

- Select the object, attribute or value table to be modified.

- Open the Object Dialog.To do this use the Edit|Edit command As an alternative to this you could also double click the object to be modified directly or choose the Edit command from the selected object's shortcut menu.

- Make the desired changes and click the [OK] button.

The parameters of an object or attribute can also be edited directly in the table on the right side of the Overall View Window or in the List Window. To do this, please proceed as follows:

- Activate the table cell containing the object parameter or attribute to be modified by clicking it.The relevant table line gets a color background (Default: Blue). The activated cell gets a background with a different color (Default: Light gray).

- Activate Editing mode for the activated cell by pressing the <F2> key or by clicking the cell again.The cell is framed and gets a color background (Default: Blue), and if applicable the list of possible parameters is shown.

- Modify the parameter by entering a different value or by selecting a different option from the list shown.

- Press the <Esc> key if you wish to abort the procedure, i.e. if you wish to leave the parameter value unchanged.Press the < ¿ Return> key if you wish to accept the changed value.

|  | Note You can move the cell selection within the table using the arrow c

[...truncated for brevity...]

### NetworkDesignerModifiyDatabase


# Modifying a CAN Database

CANdb++

Proceed as follows to modify a CAN database:

- Open the database you wish to modify. Use the File|Open File command to open a database that was saved in a folder which is accessible to you.If you are using CANdb++ Admin you can also open a database that was saved in the Version Administration archive. To do this, use the File|Open from ArchiveThe opened database is displayed in the Overall View Window.

- If necessary modify the existing objects.

- If necessary delete any objects that are no longer needed.

- Create all necessary new objects.

- Create all necessary object variants.

- Add all necessary new links.

- Delete any links that are no longer needed.

- Check for consistency of the database.

|  | Note With CANdb++ databases, the created or modified objects and links are written directly to the database. It is not necessary to save them explicitly. CANdb network databases have to be stored using the File|Commit Changes command. |

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 工具栏 (Toolbars)

**条目数**: 2

### DifferenceToolbar


# Difference Toolbar

CANdb++

The icons arranged on the Difference toolbar permit quick access to commands needed in this window. The toolbar is located directly beneath the title bar of the Difference Window.

When an icon is clicked the associated command is executed.

| Icon | Command |
| --- | --- |
|  | Compares the selected object of the database to be compared with the object in the reference database or the selected link of the comparison object with the link of the reference object. |
|  | Shows the previous comparison level |
|  | Assigns the value of the selected parameter of the reference object to the same parameter of the comparison object. |

| Version 3.0.28© Vector Informatik GmbH |  |


### StandardToolbar


# Toolbar

Start Page » Toolbar

CANdb++

The icons arranged on the toolbar permit quick access to frequently needed commands. The toolbar is located beneath the menu bar in the CANdb++ Program Window.

When an icon is clicked the corresponding command is executed.

The toolbar of the CANdb++ Program Window can be shown/hidden by the Options|Toolbar command.

| Icon | Command |
| --- | --- |
|  | File|Open file command |
|  | File|Commit Changes command |
|  | Edit|Copy command |
|  | Edit|Paste command |
|  | Edit|Edit command |
|  | Edit|Object status command |
|  | Edit|Compare command |
|  | View|Overview command |
|  | View|Attribute Definitions command |
|  | View|Value Tables command |
|  | Window|Cascade command |
|  | Window|Tile Horizontal command |
|  | Window|Tile Vertical command |

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 窗口 (Windows)

**条目数**: 13

### AttributeDefinitionWindow


# Attribute Definitions Window

CANdb++

The Attribute Definitions Window contains the list of user-defined attributes.

New user-defined attributes can be added and existing attributes can be edited here.

Attribute definitions of a CANdb database contain no column information. For this reason with DBC files the column can not be changed.

|  | Note When you enter 0 for both Minimum and Maximum, the Initial Value can be any value (according to the chosen Value Type). |

| Version 3.0.28© Vector Informatik GmbH |  |


### CheckResultWindow


# Consistency Check Window

CANdb++

Displayed in the Consistency Check Window are the results of the consistency check for the objectsof a CAN database and their interrelationships.

The icon at the beginning of each line visualizes the object status.

You can open the Consistency check – results display dialog with the Configure display shortcut menu command. In this dialog you can specify what information will be displayed in the Consistency Check Window:

- Importance of messages

- Object types

- Type of error

By way of information for you, the window title indicates how many messages are displayed in the Consistency Check Window, for example 4 of 6 displayed.

|  | Note Detailed information on the object status of objects can be taken from the Note and Explanation columns in the table of the Consistency Check Window or from the Object Status dialog. (To open the Object Status dialog choose the Edit|Object Status command.) When the Consistency Check Window is opened it is automatically updated whenever the CAN database if modified. |

Configuring the consistency check

| Version 3.0.28© Vector Informatik GmbH |  |


### CommunicationMatrixWindow


# Communication Matrix Window

CANdb++

In a communication matrix the interrelationships between signals,messages and the network nodes are shown in table form.

- The Communication Matrix Window contains the communication matrix of the active CAN database in table format.

- The signals are laid out by lines, and the network nodes are laid out by columns.

- Shown in the table cells are the messages in which the signal is transmitted or received by the specific network node.

- Table fields with signal names have gray backgrounds.

- Transmitted messages are shown as follows (e.g. <Tx> EngineData):

- Message name in blue font

- <Tx> in front of the message name

- Received messages are not marked in any way and are displayed by using a black font.

|  | Note If the Communication Matrix Window is opened, it is automatically updated whenever the CAN database is modified. |

| Version 3.0.28© Vector Informatik GmbH |  |


### DifferenceWindow


# Difference Window

CANdb++

In Difference Window the results of a comparison are displayed in the form of a table.

The title bar of the Difference Window for object comparison includes the label Object Difference as well as the names of the comparison object and the reference object.

The title bar of the Difference Window for database comparison includes the label Difference.

The Comparison column shows icons to visualize the results of the comparison results.

|  | Note The Difference Window has its own toolbar. If a Difference Window is opened it is automatically updated whenever the CAN database is modified. |

Import data in Difference Window | Comparison of Networks

| Version 3.0.28© Vector Informatik GmbH |  |


### ExportDifferenceDialog


# Comparison of Networks

CANdb++

To document the changes of two versions of a network that are being compared, mark the desired network in the Difference Window and select the context menu command Export change index… in the shortcut menu.

The Export change index for network dialog appears.

You can specify the following items in this dialog:

- Destination file

- Destination type (currently only CSV format is possible)

- Delimiter

- Display of Include node changesIf this check box is activated, differences between defined nodes in the two databases will be displayed in the *.csv file (see in the example under Nodes)

- Display of Include message changesIf this check box is activated, differences between defined messages in the two databases will be displayed in the *.csv file (see in the example under Messages)

Whether nodes are added or deleted in the databases is always displayed!

|  | Example Example of a CSV file: Database: test1.mdc Reference: test2.mdc Network Difference Attribute Database Value Reference Value Body added VC_Bus_Bo - + Power Train removed VC_Bus_PT + - Nodes Difference Attribute Database Value Reference Value Display changed NodelayerModules Yes* No DriverControl Mapped Tx Signal added GearSelect - + Messages Difference Attribute Database Value Reference Value DiagnosticData changed GenMsgDiData Yes* No | Database: test1.mdc | Reference: test2.mdc | Network | Difference | Attribute | Database Value | Reference Value | Body | added | VC_Bus_Bo 

[...truncated for brevity...]

### ListWindow


# List Window

CANdb++

The List Window contains a table-based summary of all objects of an object type or all objects that are linked to the selected object (for example all signals mapped on a message).

The displayed information corresponds to the information of the object list of the Overall View Window.

Analogous to the methods used in the Overall View Window, the objects shown in the List Window can be edited and new objects can be added.

|  | Note If a List Window is opened, it is automatically updated whenever the displayed object type or object is modified. |

| Version 3.0.28© Vector Informatik GmbH |  |


### OverviewWindow


# Overall View Window

CANdb++

The Overall View Window contains a summary of the contents of the active CAN database and is subdivided vertically.

Displayed in the left area is a hierarchical overview of the available object types and objects. The hierarchies show the connection (relation) between the objects. The right area contains the list of objects which are assigned or connected with the object type or the object in the left area.

For every object in the list name and attribute are displayed in table form.

If connections (relations) between objects are shown in the list, the names of the connected basic objects, the attributes of the connections and additionally the attributes of the connected basic object are displayed.

If for example in the hierarchic view a concrete message is selected, in the object list the signals connected with this message ( on the message mapped signals) are listed. Here the name of the connected signal, the message name, the signal position in the data field of the message ( start bit) and the attributes of the connected signal (length, value type, …) are displayed in columns.

In the vehicles object hierarchy for some objects or relations you get the following additional information:

- Networks which are connected with ECUsIf an ECU is connected with two networks (as gateway) the names of both networks are listed. For more than two networks <<more>> is displayed.

- ECUs which are connected with the nodes of a network

- Networks which

[...truncated for brevity...]

### OverviewWindowChangeWidth


# Overall View Window: Changing the Widths of Areas

CANdb++

The widths of areas in the Overall View Window can be changed as follows:

- Position the mouse pointer above the border between the two areas. When the mouse pointer is located above a border it assumes the following form:

- Drag the border.

Overall View Window: Showing/Hiding Structure Levels

| Version 3.0.28© Vector Informatik GmbH |  |


### ProgramWindow


# CANdb++ Program Window

CANdb++

The following elements are arranged in the CANdb++ Program Window:

- Title bar

- Main menu bar

- Toolbar and Version Administration toolbar (the Version Administration toolbar is only available in the CANdb++ Admin program version!)

- Working area with various windows

- Status bar

| Version 3.0.28© Vector Informatik GmbH |  |


### ShowHideStructureLevels


# Overall View Window: Showing/Hiding Structure Levels

CANdb++

Showing structure levels in the left area of the Overall View Window:

- Click the icon in front of the object type or object. The subordinate structural level is shown.

As an alternative you could also show the structure level by double clicking the name of the object type.

Hiding structure levels in the left area of the Overall View Window:

- Click the icon in front of the object type or object. The subordinate structure level is hidden.

As an alternative to this you could also hide the structure level by double clicking the object type.

Overall View Window: Changing the Widths of Areas

| Version 3.0.28© Vector Informatik GmbH |  |


### ValueTableWindow


# Value Tables Window

CANdb++

The Value Tables Window contains the list of user-defined value tables.New user-defined value tables can be added and existing value tables can be edited here.

| Version 3.0.28© Vector Informatik GmbH |  |


### WindowImportDataDiff


# Importing Data in Difference Window

CANdb++

From the Difference Window's shortcut menu the user can define the type of acceptance of objects, links or hierarchies:

- Accept attribute value

This takes an individual attribute value for an object from the reference database and accepts it into the active database.

- Accept object/link

For objects that only exist in the reference the menu command Accept object/link is provided in the shortcut menu.

This takes an individual object from the reference database and transfers it to the active database. Subobjects are not accepted in this operation.

If the selected object is a link between two objects, that link is transferred to the active database. Even if the target object of this link does not exist yet, it is still accepted into the active database.

- Accept object hierarchy

This imports a complete object hierarchy (objects and links) from the reference database into the active database.

If objects to be imported already exist in the database, a dialog opens in which you can choose:

- Whether you only wish to have the listed object overwritten, or

- Whether you wish to have all duplicate objects overwritten (by selecting the Apply to all objects option).

|  | Example If a network does not exist in the target database you can transfer it to your target database… …as a Network or …as a Network hierarchy With the Accept object/link function only the selected network object is transferred. Network nodes, messages and 

[...truncated for brevity...]

### WindowJ1939CommunicationMatrix


# J1939 Communication Matrix Window

CANdb++

Menu: View|J1939 Communication Matrix

The J1939 Communication Matrix Window shows the communication matrix for the currently active CAN database and displays the relationships between the J1939 Parameter Groups and the network nodes in the form of a table.

The first column shows all of the network nodes, as well as the Tx messages transmitted by the individual nodes. The other columns represent the nodes in the network. When a node receives a message, this is indicated by an x in the column for that node.

If you select a J1939 Parameter Group, the status bar shows the message and node name along with the Parameter Group (PGN), the transmitter address (SA), the recipient address (DA) and the priority (Prio).

When the J1939 Communication Matrix Window is open, it is updated automatically each time the CAN database is modified.

## Adding New Parameter Groups

You can add Parameter Groups to a node in the J1939 Communication Matrix Window via drag & drop or copy & paste, and can delete them again as well. When you add a Parameter Group it is duplicated, because the transmitter address is adapted and the CAN ID of the message therefore changes. The name of the duplicated Parameter Group contains the suffix _xxxx, where xxxx is a 4-digit number that is incremented with each duplication.

If you drag a Tx Parameter Group onto a node while pressing the <Shift> key, the message is not duplicated. Instead, the Tx message is removed fr

[...truncated for brevity...]

---

## 弹出框 (Popups)

**条目数**: 19

### PopupBusType


## BusType

The attribute BusType (object type: network; value type: string) will always be generated, if not existing in the loaded mdc data base.

In this case the attribute is filled with the name of the network protocol. For example the attribute is filled with LIN, if the exported network use the LIN protocol.

| Version 3.0.28© Vector Informatik GmbH |  |


### PopupLinInitValue


## LinInitValue

The attribute LinInitValue (object type: signal; value type: integer) will be generated, if:

- it is not defined in the mdc data base

- the exported network use the LIN protocol

In this case the attribute value is initialized for every signal with the initial value of the signal (provided that the initial value is different to the default value of the attribute).

| Version 3.0.28© Vector Informatik GmbH |  |


### PopupLinProtocolType


## LinProtocolType

The attribute LinProtocolType (object type: network; value type: enum; value range: LDF, DBC) will be generated if:

- it is not defined in the mdc data base and

- the exported network contains at least one message of the type LIN

In this case the attribute value is set to DBC.

| Version 3.0.28© Vector Informatik GmbH |  |


### PopupLinSpeedDefinition


## LinSpeedDefinition

The attribute LinSpeedDefinition (object type: network; value type: float) will be generated, if:

- it is not defined in the mdc data base

- the exported network uses the LIN protocol

If the baud rate of the network isn't 0, this value is taken to set attribute LinSpeedDefinition to a suitable value.

If for example the baud rate of the exported network is 9600 Baud the LinSpeedDefinition is initialized with 9.6, because the content of LinSpeedDefinition is given in kBaud.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupBaudRate


## Baud Rate

The attribute Baud Rate (object type: network; value type: integer) will be generated, if

- it is not defined in the mdc data base and

- the exported network use the FlexRay protocol

If the baud rate of the network isn't 0, the attribute BaudRate is initialized with this value.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupCANdbDatabases


## CANdb++ Database

All information that is processed in a networked CAN bus system, as well as the interrelationships between different units of information, can be stored in a CANdb++ database.

CANdb++ databases have the file name extension MDC and can be created and modified with the CANdb++ Editor.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupCANdbNetworkFile


## CANdb Network File

All information necessary to describe the network is stored in a CANdb network file.

CANdb network files have the file name extension DBC and can be created with either the CANdb Editor (CAN Database Editor) or the CANdb++ Editor.

|  | Note The object types Vehicle and Control Unit (ECU) are not available for CANdb network files, since the DBC format does not support these object types. |

| Version 3.0.28© Vector Informatik GmbH |  |


### popupCompareResultVisualisation


## Icons to visualize the comparison result

|  | Comparison and reference objects or databases agree, i.e. there are no differences.(Text color of these lines: Black) |
| --- | --- |
|  | The objects are equal but they are defined more than once.(This may occur e.g. if a signal with the same name exists more than once in a (dbc) file). |
| Difference | Comparison and reference objects or databases exhibit differences.(Text color of these lines: Red) |
| Missing | The object does not exist in one of the compared databases or one of the compared objects does not have the link (In this case a '-' appears in the Comparison or Reference column).(Text color of these lines: Blue) |

| Version 3.0.28© Vector Informatik GmbH |  |


### popupCurrentArchive


## Active Archive

The active archive refers to the Version Administration archive whose configuration file SRCSAFE.INI is entered in the Archive path input box of the Create Version page (Settings dialog).

Use the Options|Settings command to open the Settings dialog.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupCycleSend


## Cycle Type and Transmission Type

Making the setting PropsFromUserAttrs=1 in the CANdb.INI file causes user-defined attribute definitions to be used.The cycle time and transmission type of the messages are determined from the user-defined attributes GenMsgSendType and GenSigSendType, GenMsgCycleTime and GenSigCycleTime of the Vector Tool Chain and cannot be edited.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupDragging


## Dragging

In MS Windows the following procedure is referred to as Dragging:

- With the Mouse pointer point to the element that should be dragged.

- Move the element while holding the mouse button down.

- Release the mouse button when the desired position has been reached.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupObjectStatusVisualisation


## Icons to Visualize the Object Status

|  | There is a unit of information for this object. |
| --- | --- |
|  | There are multiple units of information for this object. |
|  | There is a warning for this object. |
|  | There are multiple warnings for this object. |
|  | There is an error message for this object. |
|  | There are multiple error messages for this object. |

| Version 3.0.28© Vector Informatik GmbH |  |


### popupOptimalColumnWidth


## Optimum Column Width for Tables

The optimal column width is understood to be the column width necessary to display the entire column contents.

If necessary the portion of the column header that cannot be displayed any longer is replaced by '…'.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupStatusBar


## Status Bar

The status bar is located along the lower edge of a window.

When the Mouse pointer is located above an icon in the CANdb++ Program window or a command is selected, a brief description of the specific command appears in the status bar.

The fields on the right side of the status bar provide information on the states of the toggle keys:

| Abbreviation | Description |
| --- | --- |
| UF | This activates <Caps Lock> (Caps Lock LED lights up). |
| NUM | The <Num> key is activated (Num Lock LED lights up). |
| RF | The <Scroll> key is activated (Scroll Lock LED lights up). |

|  | Note The status bar of the CANdb++Program window can be shown/hidden by the Options|Status Bar command. |

| Version 3.0.28© Vector Informatik GmbH |  |


### popupSystemAttribute


## System Attributes (System Parameters)

The following system attributes, which can be replaced by user-defined attributes, are available:

| System Attribute | For Object Type | Key Name | Attribute Name |
| --- | --- | --- | --- |
| Tx Method | message | AttrMsgSendType | GenMsgSendType |
| Cycle Time | message | AttrMsgCycleTime | GenMsgCycleTime |
| Initial Value | signal | AttrSigInitialStartValue | GenSigStartValue |
| Address | node | AttrNodeAddress | NmStationAddress |
| Protocol | network | AttrBusType | BusType |

| Version 3.0.28© Vector Informatik GmbH |  |


### popupSystemParameter


## System Parameters

System parameters are parameters that are absolutely necessary to define an object, attribute or value table.

The concrete values of system parameters may be modified on the Definition page of the Object dialog.

Besides system parameters, user-defined attributes may also be assigned to objects and value tables.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupSystemProtocol


## The following values of the system attribute 'Protocol' are predefined in CANdb++:

- CAN

- LIN

- MOST

- FlexRay

| Version 3.0.28© Vector Informatik GmbH |  |


### popupSystemSymbol


## System Icon

CANdb++ System icon

If you click the System icon the System menu is opened.

If you double click the System icon the window is closed.

| Version 3.0.28© Vector Informatik GmbH |  |


### popupSzenario


## Scenario

Scenarios add messages to the amount of analyzed messages.

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 提示 (Tips)

**条目数**: 10

### TipActivateDialog


# Activating a Dialog

CANdb++ » Tips

Proceed as follows to activate a dialog:

Click anywhere within the dialog to be activated.The selected dialog is then activated and is placed in the foreground.

|  | Note The title bar of an active dialog is highlighted in MS Windows by a specific color (default is blue). |

| Version 3.0.28© Vector Informatik GmbH |  |


### TipActivateWindow


# Activating a Window

CANdb++ » Tips

Proceed as follows to activate a window:

Click anywhere within the window to be activated. As an alternative to this you could also use the Window|List of opened windows command to activate a window located in the background.The selected window is activated and is placed in the foreground.

|  | Note The title bar of an active dialog is highlighted in MS Windows by a specific color (default is blue). |

| Version 3.0.28© Vector Informatik GmbH |  |


### TipChangeColumnWidth


# Changing the Column Width in Tables

CANdb++ » Tips

Proceed as follows to change the column width in tables that are displayed in dialogs or windows:

Position the mouse pointer in the column header above the border adjacent to the column whose width you wish to change. When the mouse pointer is located above the border it assumes the following form:

Drag the border. If necessary the portion of the column contents that cannot be displayed any longer is automatically replaced by '…'.

Proceed as follows to set the optimum column width:

Position the mouse pointer in the column header above the border on the right side of the column whose width you wish to change. When the mouse pointer is located above the border it assumes the following form:

Double click the border. The optimum column width is then configured automatically.

Configuration of list views

| Version 3.0.28© Vector Informatik GmbH |  |


### TipChangeWindowSize


# Changing the Window Size

CANdb++ » Tips

The size of the CANdb++ Program Window and the CANdb++ windows can be changed.

## Proceed as follows to change the size of a window:

- Activate the window whose size you wish to change.

- Position the mouse pointer above the window frame of the active window. When the mouse pointer is located above the window frame it assumes the following forms:

- Drag the window frame until the desired size is reached.

## Proceed as follows to maximize a window:

- Activate the window you wish to maximize.

- Click the Maximize icon of the active window.As an alternative to this you could also double click the window's title bar.The window is then maximized.

## Proceed as follows to minimize a window:

- Activate the window you wish to minimize.

- Click the Minimize icon of the active window.The window is then minimized.

| Version 3.0.28© Vector Informatik GmbH |  |


### TipCloseDialog


# Closing a Dialog

CANdb++ » Tips

If you wish to have changes you made in the active dialog accepted, you must close the dialog by clicking the [OK] button.

If you do not wish to have the changes accepted you must close the dialog in the following manner:

- Press the [Cancel] or [Close] button

- Click the Close icon

- Press the <Esc> key

| Version 3.0.28© Vector Informatik GmbH |  |


### TipCloseWindow


# Closing a Window

CANdb++ » Tips

If a window is no longer needed, it can be closed.

Proceed as follows to close a window:

1. Activate the window you wish to close.

2. Click the Close icon of the active window.

As an alternative to this you could also double click the window's system icon or simultaneously press the <Ctrl> and <F4> keys.The window is then closed.

|  | Note When the last window in the CANdb++ program qindow is closed, the active CAN database is automatically closed. |

| Version 3.0.28© Vector Informatik GmbH |  |


### TipHelpForActiveDialog


# Help for the Active Dialog

CANdb++ » Tips

CANdb++ help is context-sensitive.

The help topic for the active dialog can be called as follows:

- Pressing the key <F1>

- Choosing the command button [Help]

Some dialogs contain a help icon besides the close icon in the title bar.

After clicking the help icon direct help is activated and the mouse pointer assumes the following form:

If you click an element of the dialog with this mouse pointer, the help topic for this dialog element will appear.

| Version 3.0.28© Vector Informatik GmbH |  |


### TipMoveWindows


# Moving a Window or Dialog

CANdb++ » Tips

The position of the CANdb++ Program Window can be changed, as can the positions of all CANdb++ windows and dialogs.

Proceed as follows to move a window or a dialog:

- Activate the window or dialog that you wish to move.

- Position the mouse pointer to the title bar of the active window or dialog.

- Drag the title bar until the desired position is reached.

| Version 3.0.28© Vector Informatik GmbH |  |


### TipSortATable


# Sorting a Table

CANdb++ » Tips

When opening a window the lines in a table are generally shown in the sequence in which they were created.

To sort the lines of a table according to a specific column, you only need to click on that column header. Clicking again on the same column header sorts the lines in descending order.

For example, if signals are displayed in a table and you click the Name column header, then the signals are shown sorted by name.

| Version 3.0.28© Vector Informatik GmbH |  |


### TipTableSearch


# Searching in a Table

CANdb++ » Tips

In the object lists an object can be found by name by entering the first characters of the name while no edit control is visible.

This behavior in CANdb++ is the same as in the Windows Explorer.

Sorting a table

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 故障排除 (Troubleshooting)

**条目数**: 3

### DatabaseInvalidName


# Notification: 'Invalid CANdb Symbol'

CANdb++ » Troubleshooting

## Possible cause:

An invalid name was entered in the Name input box.

Valid names must satisfy the following requirements:

- The name must begin with an alpha character.

- The name may only contain letters, numbers.

- The name may not contain any spaces, special characters or punctuation marks.

## Action:

Correct the name and click the [OK] button.

| Version 3.0.28© Vector Informatik GmbH |  |


### DatabaseWriteProtection


# Notification: Database is write protected. No changes can be made.

CANdb++ » Troubleshooting

## Possible cause:

The active database file was given write protection on the file system level.

## Action:

Remove the write protection. To do this, for example, you could open the MS Windows Explorer and change the properties of the database file.

|  | Note If you are utilizing Version Administration, please follow the instructions given below. |

## Possible cause:

The active CAN database was versioned in Version Administration and has not been reserved again yet.

## Action:

Reserve the CAN databaseVersion Management|Reserve command

## Possible cause:

Shown in the Overall View Window is the write-protected, temporary copy of a version of a CAN database stored in Version Administration.

|  | Note The write protection of this copy cannot be removed by reserving! This protects data that have already been versioned from being changed. |

## Action:

Open the current version of the CAN database with the File|Open file... command and reserve the CAN database with the Version Management|Reserve command.As an alternative to this you could also use the File|Open from archive... to command reserve the current version of the CAN database.

| Version 3.0.28© Vector Informatik GmbH |  |


### VehicleCannotBeCreated


# Notification: No vehicle can be established. Vehicles not supported by the basic database schema!

CANdb++ » Troubleshooting

## Possible cause:

An attempt was made to create a Vehicle in a CANdb network file.

Vehicles cannot be created in CANdb network files!

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 通用说明 (General)

**条目数**: 41

### Bsp_Standard_Attributdef


# Using Standard Attribute Definitions

CANdb++

Excerpt from the CANdb.INI file for using permanently defined system attributes of CANdb++:

…

[Attribute_Settings]

// Read Vector tool chain attributes from user-defined attributes

// 0 = read from standard tables (default)

// 1 = read from user-defined attributes

PropsFromUserAttrs=0

// Name of user-defined attribute for message transmit types

AttrMsgSendType=GenMsgSendType// attribute name for Attribute Tx method

…

Using user-defined attribute definitions | Attribute mapping - Assigning user-defined attributes | Vector Tool Chain attributes

| Version 3.0.28© Vector Informatik GmbH |  |


### Bsp_userdef_Attributdef


# Using User-Defined Attribute Definitions

CANdb++

Excerpt from the CANdb.INI file for using user-defined attribute definitions instead of the system attributes:

…

[Attribute_Settings]

// Read Vector Tool Chain attributes from user-defined attributes

// 0 = read from standard tables (default)

// 1 = read from user-defined attributes

PropsFromUserAttrs=1

// Name of user-defined attribute for message transmit types

AttrMsgSendType=GenMsgSendType// attribute name for Attribute Tx method

…

In the Attribute Definitions Window user-defined attribute definitions can be displayed. In the Attribute Definition dialog they can be edited.

In this example, the value range of the Tx method was extended with newTxmethod.

Using standard attribute definitions | Attribute mapping - Assigning user-defined attributes | Vector tool chain attributes

| Version 3.0.28© Vector Informatik GmbH |  |


### CANFD


# CAN FD Support

CANdb++ » CAN FD Support

Generally you can handle CAN FD message like a normal CAN message with the following differences:

- A CAN FD message can only be defined within a CAN FD bus (bus type can be set by using the Protocol attribute at the bus object):You can either open an existing CAN network file and set the Protocol attribute to CAN FD (bus object dialog) or you create an new network file using the CAN_FD Template.DBC template.

- The DLC of a CAN FD message (in contrast to a CAN message) can be up to 64 bytes in size. The following sizes are allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48 and 64 bytes.

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_ATTRCATEGORIES_DIALOG


# Configuring the Visibility of User-Defined Attribute Categories

CANdb++

- All attributes may be assigned to user-defined attribute categories.

This serves to limit the columns in the list to certain categories of the Vector Tool Chain (e.g. attributes for the Interaction Layer, for Transport Protocols, etc.)

- Attribute categories are defined and attributes are assigned to categories in the INI file.

- The attributes of categories may be shown or hidden using a dialog menu command.

This only affects the List Views, not visibility in the dialog's attribute lists.

The CANdb.INI file already contains some prepared attribute categories for the Vector Tool Chain, e.g.

- Interaction Layer

- Network Management

- Transport Protocol

- Diagnostics

- CANoe

## Sample excerpt from CANdb.INI

[AttributeCategory5]

Name=CANoe

Attribute1=NodeLayerModules

Attribute2=CANoeDrift

Attribute3=CANoeJitterMin

Attribute4=CANoeJitterMax

Attribute5=CANoeStartDelay

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_CUSTOMIZECOLUMNS_DIALOG


# Configuration of List Views

CANdb++

To improve the display List Views can now be configured:

- Columns can be hidden or shown in the List Views.

- The order of the columns can be changed, this can also be done by drag & drop.

- Visibility and order can be changed in a configuration dialog.

- Column widths can be configured to optimal or minimum values from items in the shortcut menu for the column headers.

|  | Note These functions are available for the column located under the mouse pointer or for all columns. These functions are available from the specific shortcut menu (right mouse button). |

Configuring the visibility of user-defined attribute categories | Changing the column width in tables

| Version 3.0.28© Vector Informatik GmbH |  |


### HIDD_GATEWAYSIGNAL_DIALOG


# 'Gateway Signals' Dialog

CANdb++

You can create and manage gateway signals in this dialog.

To do this, select one of the following objects from the Overview Window (tree view) on the left side:

- A Vehicle ,

- an ECU or the

- Gateway Signal object type

Now you can call the dialog by the Gateway Signal… command in the shortcut menu (right mouse button).

## Procedure for Creating Gateway Signals

- In the Gateway box define which ECU should assume the gateway function.

- Select the source network and the target network.

- Select the receiving node (Rx node) and the transmitting node (Tx node).

- Select the source signal and one or more target signals.

An incoming signal can be routed simultaneously to different outgoing signals of the Tx node.

- Press the [Define] button

The newly created gateway signal is now shown in the Overview List located in the lower section of the dialog.

Target signals that are already being used are shown in gray in the list of target signals, and they cannot be selected any more, since a target signal may be associated to a maximum of one source signal.

## Procedure for Deleting Gateway Connections

- Select a gateway signal in the Overview List located in the lower section of the dialog.

- Press the [Remove] button.

The connection between the source signal and the target signal has now been removed, and the target signal can be selected again for new connections.

## Notes on Gateway Signals

- If the Gateway Signals Dialog of a

[...truncated for brevity...]

### HID_functional_nodes


# Functional Nodes

CANdb++

A control device may contain a number of sub-functions. These functional network nodes are logically linked with the network.

|  | Example The two functional nodes Window raiser and Door locking can be included in a control device as sub-functions, but they can also be kept in separate control devices. |

|  | Note To make it possible to use functional nodes of this type in different control units, their communication behavior (message attributes, message layout, signal attributes, etc.) must be identical in all control devices that contain these functional nodes. When exporting to a CANdb network file you can specify whether the individual network nodes or the control device associated with them should be exported. |

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_CANDB_INI


# Settings in CANdb.ini

CANdb++

The file CANdb.ini is located in the directory EXEC32 of your CANdb++ installation.

The following settings for CANdb++ can be made in CANdb.ini:

- Root directory for generated CAN drivers(section [CAN_Driver], line 'RootDir=')

- The display of the signals and environment variables in the tree view of the Overview Window can be modified. The display in the main view remains unaffected by this.(section [GUI_Settings], line 'DisplayDeepestTreeHierarchy=')

- The Mapping of the attributes of the Vector CAN tools tool chain can be set.(section [Attribute_Settings], line 'PropsFromUserAttrs=')

- The Provider entry can be modified.([CANdbPrv] section, 'StoreEcuNameWithNode=' entry)Excerpt from CANdb.ini[CANdbPrv]//Store the ECU name as name of the nodes in DBC databases// 1 = store ECU name (default)// 0 = store node nameStoreEcuNameWithNode=1(See also Notes on working with DBC databases)

- MaxSignalShortNameLenThe MaxSignalShortNameLen entry defines the maximum length of (short) names of signals.The default value conforms to the maximum length of short names (32 characters).Likewise MaxMsgShortNameLenlimits the length of message names while MaxNodeShortNameLenlimits the length of node names.

## Proceed as follows to configure these settings:

- Use an ASCII editor to open the file CANdb.ini.

- If you want to set the root directory for generated CAN drivers, enter the desired root directory in the line RootDir= of the section [CAN_Driver].(W

[...truncated for brevity...]

### OHID_CANdb++_Database_DBC_Notes


# Notes on Working with DBC Databases

CANdb++

## Expansions for DBC databases

- DBC databases support multiple senders of a message.

- DBC databases support the definition and saving of user-defined attributes at the following relations:

- Tx relation between nodes and messages(Object type: Node – Tx message)

- Rx relation between nodes and mapped signals(Object type: Node – Mapped Rx signal)

- Access relation between nodes (ECUs) and environment variables(Object type: Controller – Environment variable)

## Exporting MDC databases to DBC databases

When exportng MDC databases or subsets (networks, ECUs) of MDC databases, it is possible to level out the attributes at the Tx relation between nodes and messages. The purpose of this is to permit compatibility with older versions of Vector Tools.The Export dialog has a means of activating the leveling out.The attributes defined in the MDC databases for ECUs and the relations defined between ECUs and nodes are assigned to the network nodes when exporting to DBC databases.

When exporting MDC databases or subsets (networks, ECUs) of MDC databases the user may indicate how the nodes/ECUs should be exported.In the MDC data model there is a separation between an ECU and a network node. A network node describes a controller's communication layer (e.g. the Tx and Rx messages and signals on a bus). A ECU represents a controller with one or more network nodes.

This modeling capability can also be utilized for functional nodes. Thi

[...truncated for brevity...]

### OHID_CANdb++_Database_Templates


# Database Templates

CANdb++

When creating a new database templates provide a rough framework of predefined attributes such as bus type and other parameters. This involves taking bus-typical values and special features into consideration.

## Templates for CANdb networks (DBC files)

- EmptyTemplate A completely empty CAN network is created without predefined attributes.

- CANoeTemplate A network is created which already contains a set of predefined CANoe specific attributes.The BusType attribute is created and set to the default value CAN.The attributes CANoeDrift, CANoeJitterMax, CANoeJitterMin, CANoeStartDelay, ECU and NodeLayerModules are explained in Vector Tool Chain Attributes.

- CANTemplate A network is created with the BusType attribute.The default value for BusType is CAN.

- FlexRayTemplate A network is created which contains a set of predefined FlexRay specific attributes.The default value for BusType is FlexRay.

- MOSTTemplate A network is created which already contains a set of predefined MOST-specific attributes.The default value for BusType is MOST.

- CAPLgen_IL_Basic Template A network is created which already contains a basic set of attributes for the usage of the CANoe CAPL Generator.The default value for BusType is CAN. The attributes of the CAPL Generator are explained in the CANoe online help.

- Vector_IL_Basic Template A network is created which already contains a basic set of attributes for the usage of the CANoe CAPL Generator for the Vector i

[...truncated for brevity...]

### OHID_CANdb++_Multiplex_Concepts


# Information on the Multiplexor Concept

CANdb++

The concepts for defining multiplexor signals differ in MDC and DBC databases. A definition of multiplexed signals is described here.

| MDC Databases |
| --- |
| Standard Multiplexor Concept in MDC Databases |
| The relationships between multiplexed signals, multiplexor signals and messages are defined by means of different types of signal groups. All multiplexed signals which are sent based on a multiplexor signal are incorporated into a multiplexor group. In the dialog for the multiplexor group the specific signal that transmits the multiplex value must be defined in the Multiplexor list box. Since the multiplex value defines which multiplex group should be transmitted in the message, a multiplex group must exist for each multiplex value, and a different multiplex value must be assigned to each multiplex group. That is, the same multiplex value may not be assigned to two multiplex groups. The multiplex groups are incorporated into a Multiplexor Group. Several multiplexor groups may be set up in one message. This yields the following two-stage group hierarchy: Message Multiplexor Group(s) (one for each multiplexor signal) Multiplex Groups (one for each multiplex value) Multiplexed signals A multiplexor signal is assigned to this multiplexor group. Then in this multiplexor group a multiplex group is created for all concrete values of the multiplexor signal. Signals are then assigned to the multiplex groups; these signals th

[...truncated for brevity...]

### OHID_CANdb++_export_notes


# Exporting Networks and ECUs

CANdb++

Since a node may be implemented in different ECUs in different vehicles, a vehicle-oriented export of data must occur here. Otherwise all of the networks for all of the ECUs in which the node is used will be exported.

With networks only those ECUs which are also needed by the nodes connected to the network may be exported to DBC databases.

This may be done by the Export function at the network that is assigned to a vehicle, or at a ECU assigned to the vehicle (Vehicle–Networks or Vehicle–ECUs).

Export CANdb++ Data dialog | Notes on working with DBC databases | Exporting a CAN database | Import CANdb++ data | XML export | Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_CANdb++_export_xml


# XML Export

CANdb++

Networks may be exported in files that have XML format. Using XML Export you can provide network data to other tools and systems.

## Data Structure

With this export the following objects are written to the file in their hierarchies:

- Selected network

- …nodes linked to the network

- …messages sent by a node

- …signals mapped to a message

- …names of the nodes which receive a signal

|  | Note With objects the system-defined and user-defined attributes are exported to the file. XML files cannot be imported into CANdb databases. |

Export CANdb++ data dialog | Notes on exporting networks and ECUs | Notes on working with DBC databases | Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_CANdb++_signal_gateway


# Gateway Signals

CANdb++

Signals which are routed from one network to another are called gateway signals.

Gateway signals are either automatically recognized and created by CANdb++, or they can be created in a special dialog.

How does CANdb++ automatically detect gateway signals?

Automatically generated gateway signals cannot be defined directly; they are recognized as such by CANdb++ if they satisfy the following conditions:

- The signal is received by a Gateway ECU of the source network (via a Rx node of the ECU).

- The signal is sent by the same Gateway ECU onto the target network (via a Tx node of the ECU).

- The source signal and target signal are identical.

How can automatically generated gateway signals be deleted?

- Automatically created gateway signals cannot be deleted directly,since they are not defined in the database. As soon as the necessary conditions for an automatically generated gateway signal cease to exist, the signal is removed from the list of gateway signals.

How can a user create a new gateway signal?

- New gateway signals can be created in the Gateway Signals dialog.To open this dialog unfold/expand a vehicle in the object hierarchy and select the Gateway signals command in the shortcut menu of a gateway signal.

- First, you select the topology. Second, you define which signals should be made into gateway signals.

Where are gateway signals displayed?

- Gateway signals are shown in the Overview Window below the Vehicle and Gateway Sign

[...truncated for brevity...]

### OHID_CANdb_attribute_mapping


# Attribute Mapping – Assigning User-Defined Attributes

CANdb++

User-defined attributes can be edited and read by several programs of the Vector CAN tools tool chain.

While exchanging (importing) data, mapping assigns the contents of user-defined attributes to predefined fields (attributes) of the relevant program(s) of the Vector CAN tools tool chain.

Therefore valid types and valid value ranges of user-defined attributes are predefined (see user-defined attributes).

Settings for mapping functionality may be configured in the CANdb.INI file under the [Attribute_Settings] section. You can select whether user-defined attributes should be assigned (imported) or the attributes of the standard table should be used. Furthermore you determine which user-defined attribute will be assigned to which predefined attribute.

Using standard attribute definitions | Using user-defined attribute definitions

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_CANdb_attribute_value_type_file


# Attributes of Type 'File'

CANdb++

New with program version CANdb++ 1.1 is the value type File for user-defined attributes.

- This means that not only numbers (integer, float,…) but also large (binary) objects like files can be assigned to attributes.

- The value type File is available for objects and relations.(See also User-defined attributes at object relations)

- If type File is selected, the edit fields Default, Minimum and Maximum are not available.

- If type File is selected, the value of the attribute is the name of the assigned file.

|  | Example The value in the Default input box is assigned to each object as the default value for the user-defined attribute. Objects still having the default value of the user-defined attribute are characterized by an * after the attribute value in the right area of the Overall View Window. |

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_CANdb_format_intel_motorola


# Intel and Motorola Formats in CANdb++

CANdb++ » Intel and Motorola Formats in CANdb++

In CAN databases signals can be defined with a byte order for either Motorola or Intel processors. The individual signals within a message may also have different byte orders.

## Byte order for Motorola processors (Big Endian)

## Byte order for Intel processors (Little Endian)

## Bit significance (Bit Order)

Within a byte the significance of bits is the same in both formats:

msb: most significant bit; lsb: least significant bit

## General

In the CANdb++ Editor the position and length of a signal are shown in Intel or Motorola Forward format. The following table describes the start position, direction of signals and the type of bit indication in the various representations:

## Bit Indication

The bits of a message have following indices:

(1) Bit indexing in the byte from the right to the left

Transmitting a message with 8 byte length on the bus, bit 7 (most significant bit of byte 0) will be transmitted first, followed by bit 6. Bit 56 (least significant bit of byte 7) will be transmitted at last.

(2) Bit indexing in the byte from the left to the right – inverted or sequential bit indexing

Transmitting a message with 8 byte length on the bus, bit 0 (most significant bit of byte 0) will be transmitted first, followed by bit 1. Bit 63 (least significant bit of byte 7) will be transmitted at last.

## Message Layout

In the following representation of the CANdb++ Editor the byte

[...truncated for brevity...]

### OHID_CANdb_object_relation_attribute_user


# User-Defined Attributes at Object Relations

CANdb++

New with program version CANdb++ 1.1 are user-defined attributes for relations between objects.

Not only can attributes be assigned to objects of type network; they can also be assigned to relations between different objects of a network.

### The following relations are available:

- Vehicle – Network

- Vehicle – Control Unit (ECU)

- Network – Node

- Control Unit – Node

- Control Unit – Environment Variable

- Node – Tx Message

- Node – Tx Signal

- Node – Rx Signal

- Node – Mapped Rx Signal

- Message – Signal

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_Glossar


# Glossary

CANdb++

Active archive Application WindowArchive, active Attribute Definition WindowAttributes, user-defined

CANdb++CANdb++ Program WindowCANdb++ database CANdb Network File Communication MatrixCommunication Matrix WindowConsistency Check WindowControl Unit

Data model DBC Difference WindowDifference toolbar

ECUElectronic Control UnitsExtension (File name extension) Environment variables

F File name extension

Gateway

List Window

Main menu bar MDC Menu barMessageMessage signalMouse pointerMultiplexing

Network file Network nodeNetworkNode group

ObjectObject symbolsOverall View WindowObject types

shortcut menu Program Window

SignalSignal groupSignal multiplexingStatus bar System icon System parameters

Title bar

Toolbars Toolbar of the CANdb++ program windowVersion Administration toolbarDifference toolbar

User-defined attributes

Value tables Value Tables WindowVersion Administration toolbarVehicle

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_Protocol_dbc


# Network Protocols for *.dbc Files

CANdb++

With the attribute BusType in *.mdc databases the network protocol for *.dbc files is defined. The attribute can be edited in the Overview Window (select Networks).

During the export of a network from a *.mdc database into a *.dbc file the protocol of the network is transferred to the BusType attribute of the *.dbc file. During the import this attribute value is mapped to the system attribute Protocol and is displayed in the column Protocol of the Overview Window.

If an unknown network protocol or no value is assigned to the attribute, in the Protocol column is displayed Unspecified.

If the attribute BusType is not found in the *.dbc file, the protocol automatically gets the standard protocol CAN.

|  | Example If the attribute BusType of a *.mdc database is assigned to LIN, during the import of the exported *.dbc file, LIN is automatically assigned to the protocol. |

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_Shortcuts


# Key Combinations

CANdb++ » Key Combinations

| Key | Command/Action |
| --- | --- |
| <Ctrl>+<O> | Opens a CAN database.File|Open File... command |
| <Ctrl>+<N> | Creates a new CAN database.File|Create Database... command |
| <Ctrl>+<Z> | Undoes the last action.Edit|Undo command |
| <Ctrl>+<C> | Copies the selected object to the Clipboard.Edit|Copy command |
| <Ctrl>+<V> | Pastes the contents of the clipboard.Edit|Paste command |
| <Ins> | Creates a new object, attribute or value table.Edit|New command |
| <Del> | Deletes the selected object, attribute or value table.Edit|Delete command |
| <Esc> | Closes the active dialog without accepting the changes.Corresponds to activation of the [Cancel] or [Close] button. |
| <F1> | Calls CANdb++ Help for the active dialog or the selected command. |
| <F1> (when CANdb++ help is active) | Calls a help text containing information on the use and adaptation of Help.Help|Using Help command |
| <F2> | Activates editing mode for the activated cell in a table. |
| <F10> | Activates the menu bar |
| <Ctrl>+<F4> | Closes the active window. |
| <Alt>+<F4> | Closes the active CAN database and exits CANdb++.File|Exit command |
| <Alt>+Spacebar | Opens the System menu of the CANdb++ Program Window.As an alternative the system menu may also be opened by double clicking the system icon. |
| <Ctrl>+<B> | Shows the previous comparison level. |

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_Signal_Multiplexing


# Signal Multiplexing

CANdb++

With signal multiplexing different signals can be transmitted on identical data bytes in a message depending on a multiplex value.

The signal that contains the multiplex value is referred to as the Multiplexor Signal (Mode signal).

The signals that are transmitted depending on the multiplex value are referred to as Multiplexed (mode-dependent) Signals (Signal_S1, ...., Signal_S6 in the example).

In the MDC Standard multiplexor concept the multiplexed signals to be transmitted together must each be incorporated into a Multiplex Group (e.g.: Signal_S1 and Signal_S2 in the example).

|  | Example If the multiplex value is equal to 0 the signals Signal_S1 and Signal_S2 are transmitted; if it is equal to 1 the signals Signal_S3 and Signal_S4; and if it is equal to 2 the signals Signal_S5 and Signal_S6 are transmitted. |

Information on the multiplexor concept

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_TYPOGRAFIE


# Typographic Conventions

CANdb++

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

| Version 3.0.28© Vector Informatik GmbH |  |


### OHID_VECTOR_INI


# Settings in VECTOR.ini

CANdb++

The file VECTOR.ini is located in the directory EXEC32 of your CANdb++ installation.

The following settings for CANdb++ can be made in VECTOR.ini:

Proceed as follows to change the language for menus and dialogs:

- Use an ASCII editor to open the file VECTOR.ini.

- Replace the language code number in the line Country= of the section [Language] with the code number of the desired language.

The available languages are listed in the command lines (indicated by // ) of the section [Language].

|  | Example The following setting causes menus and dialogs to appear in English: [Language]Country=01 |

- Store the file VECTOR.ini and close the editor.

If CANdb++ was opened during editing, you have to exit CANdb++ and open it again to work with the new language setting.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidCANdbProgramVersions


# Overview of CANdb++ Program Versions

CANdb++

The following CANdb++ program versions are available:

- CANdb++

- CANdb++ Admin

The functional features of the program versions are shown in the following table:

| Function | Program version |
| --- | --- |
| CANdb++ | CANdb++ Admin |
| Create and modify CANdb++ databases (*.mdc) | — | X |
| Create and modify CANdb network files (*.dbc) | X | X |
| Create and modify user-defined attributes | X | X |
| Create and modify value tables | X | X |
| Display the communication matrix | X | X |
| Create variants of an object | X | X |
| Consistency check of a CAN database | X | X |
| Create and modify objects of the Vehicles object type | — | X |
| Compare objects | X | X |
| Compare CAN databases | — | X |
| Import objects | — | X |
| Import attributes | X | X |
| Export objects and CAN databases | X | X |
| Version administration for CAN databases and objects | — | X |
| Generate reports | — | X |
| Timing analysis to estimate the bus load | — | X |

## Legend

| Function available | X |
| --- | --- |
| Function unavailable | — |

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidDataModel


# CANdb++ Data Model

CANdb++

To model the communications structure of a CAN bus system in a vehicle there are various object types to choose from in the CANdb++ Overall View Window.

The CANdb++ data model provides more comprehensive modeling options than the CANdb data model. Differences between CANdb and CANdb++ data models

By adding a link, a connection (Relation) can be established between two objects of different object types in the CANdb++ data model. For example, linking a signal to a message can define that the message is assigned to this signal.

Please refer to the table below for possible links.

|  | Note A Gateway is a special control unit that is used as a connecting element between two or more CAN buses. |

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidDifferenceDataModel


# Differences Between CANdb and CANdb++ Data Models

CANdb++

The following object types that are not part of the CANdb data model were introduced as new object types in the CANdb++ data model:

- Vehicles

- Control Units

- Node Groups

- Signal Groups

The following object types, which are included in both the CANdb and CANdb++ data models, are defined differently in the CANdb++ data model relative to the CANdb data model:

- Signals

In the CANdb++ data model signals are autonomous objects. signals can be defined independently of messages in CANdb++, e.g. signals may even be created before the messages are created. (see signal based modeling).A signal is assigned to a message by linking the signal to the message, whereby the position of the signal within the message is then defined. A signal can also be linked to multiple messages; for example, this can be done in the modeling of network variants.

- Messages

In the CANdb++ data model the supplemental system parameters Tx Method and Cycle Time are used to define a message.

- Network nodes

In the CANdb data model the network nodes assume the role of the control units in a real network. In the CANdb++ data model this role is assumed by the objects of the new control units object type.

- Environment variables

In the CANdb++ data model environment variables are assigned to the control units.When exporting into CANdb network files the environment variables are exported to a separate network file.

- Value tables

In the 

[...truncated for brevity...]

### OhidGEnvironmentVariables


# Environment Variables

CANdb++

Input and output variables of network nodes, such as switch position, sensor signals and actuator signals.

In the CANdb++ data model environment variables are assigned to the control unit.

Environment variables are defined by the following system parameters:

- Symbolic name of the environment variable

- Value type (data type) of the environment variable Integer – Signed 32 Bit IntegerString – ASCII StringFloat – 64 Bit FloatData – Byte field of a specified length (the length is set in the Length attribute).

- Access rights Defines the rights that Electronic Control Units (ECU's) have when they access environment variables.

| Unrestricted: | All ECU's have read and write access. |
| --- | --- |
| Read: | The assigned ECU's can read the environment variable.(The environment variable represents a sensor.) |
| Write: | The assigned ECU's can write to the environment variable.(The environment variable represents an actuator.) |
| Read/Write: | The assigned ECU's can read from and write to environment variables. |

- Unit Unit of the physical quantity of the environment variable.

- Initial Value (only available for environment variables of value type Integer or Float) Initial value of the environment variables at the start of a simulation or measurement.Note:When you enter '0' for both Minimum and Maximum, the Initial Value can be any value (according to the chosen Value Type).

- Minimum and Maximum (only available for environment variable

[...truncated for brevity...]

### OhidGFileNameExtensions


# File Name Extension

CANdb++

The file name extension refers to the three characters following the dot after the file name.

| File Type | Description |
| --- | --- |
| CNT | Table of contents for help files |
| DBC | CANdb network file (Data Base for CAN) |
| DLL | Runtime library (Dynamic Link Library) |
| EXE | Executable program |
| HLP | Help file |
| INI | File with configuration settings |
| MDC | CANdb++ CAN database |
| RPT | Crystal Report |
| TXT | ASCII Text File |

Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGMouseOperator


# Mouse Pointer

CANdb++

To help visualize possible actions the mouse pointer assumes the following forms:

| Mouse Pointer Explanation |
| --- |
|  | Standard mouse pointer |
|  | When the mouse pointer assumes this form a link can be established with this object.(Creating a link) |
|  | When the mouse pointer assumes this form a link cannot be established with this object. |
|  | When the mouse pointer assumes this form it is located over a border between two table columns.(Changing the column width in tables) |
|  | When the mouse pointer assumes this form the border between the two areas of the Overall View Window is activated.(Changing the widths of Overall View Window areas) |
|  | When the mouse pointer assumes this form the width of the active window can be changed by Dragging the window frame. |
|  | When the mouse pointer assumes this form the height of the active window can be changed by Dragging the window frame. |
| , | When the mouse pointer assumes one of these forms the size of the active window can be changed by Dragging the window frame. |
|  | When the mouse pointer assumes this form it is located in an input box. After clicking in the input box the user can make entries in this box. |
|  | When the mouse pointer assumes this form direct help is activated.After clicking an element the help for this element appears. |

|  | Note Please note that actual mouse pointer forms may deviate from those shown here if a different mouse pointer configuration has been

[...truncated for brevity...]

### OhidGShortcutMenu


# Context Menu

CANdb++

Besides the commands contained in the menus of the Main menu bar, CANdb++ offers access to additional executable commands in the context menus of the objects.

The context menu of an object only contains those commands that can be applied to the selected object.

To open an object's context menu you must position the mouse pointer above the object and then press the right mouse button once.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGSignalGroups


# Signal Groups

CANdb++

Multiple message signals can be combined into a signal group.

|  | Note A signal group may only contain message signals that are transmitted by the same message. |

Creating signal groups| Packet signals | Rules for naming objects

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGTitleBar


# Title Bar

CANdb++

The title bar is located along the upper edge of a window or dialog.

A window or dialog can be moved by Dragging the title bar.

The title bar of the active window or dialog is highlighted by a special color in MS Windows (default color is blue).

The title bar may contain the following icons:

|  | CANdb++ System Icon |
| --- | --- |
|  | Minimize Icon(Clicking this icon minimizes the window) |
|  | Maximize Icon(Clicking this icon maximizes the window) |
|  | Restore Icon(Clicking this icon restores the previous window size) |
|  | Help Icon(Clicking this icon calls direct help) |
|  | Close Icon(compare Closing a window) |

Besides these icons the title bar of the CANdb++ Program window also contains the name of the application and the name of the active database or active window.

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGToolChainIntegration


# Integration in the Vector Tool Chain

CANdb++

CANdb++ is a central tool in the Vector CAN tools tool chain, and it can be started directly from Vector CAN tools such as CANalyzer, CANoe, CANape and CANscope. This provides the Vector CAN tools with direct access to communication-relevant data via CANdb++.

Communication-relevant data are defined, modified and managed entirely in CANdb++; the Vector CAN tools only read-access these data (see also Attribute mapping).

The communication-relevant data must exist in the form of CANdb network files so that the Vector CAN tools can access them.

To also permit the use of data from CANdb++ databases CANdb++ provides the option of data export. CANdb++ databases can be exported into one or more CANdb network files.

The following options are available for export:

- Export of the entire CANdb++ database

- Export of information relevant to an individual object (Export is only possible for vehicles, networks and control units)

| Version 3.0.28© Vector Informatik GmbH |  |


### OhidGUserDefinedAttributes


# User-Defined Attributes

CANdb++

Besides system parameters, user-defined attributes may also be assigned to objects and value tables.

The values of user-defined attributes appear together with the values of the system parameters in the columns on the right side of the Overall View Window and/or in the relevant List Windows.

Attribute definitions of a CANdb database contain no column information. For this reason with DBC files the column cannot be changed.

see also: Attribut Mapping – Assigning User-Defined Attribute

Attributes are defined by the following parameters:

- Object Type Type of the object (signal, message, network node, etc.) or relation (message-signal, etc.), for which the attribute is defined.

- Value Type (data type) of the attribute

| Value Type | Short Description |
| --- | --- |
| Integer | 32 Bit Signed Integer |
| Float | 64 Bit Double Precision Float |
| String | ASCII String |
| Enumeration | This is an enumeration.Valid values are defined in the Value Range.Each line in the Value Range defines a valid enumeration value. |
| Hex | 32 Bit Unsigned IntegerThe value is always displayed in hexadecimal format. |
| File | Here a binary file can be stored in an attribute.This type is only available for MDC databases. |

- Default value Attributes use this value for objects for which no values are set.This parameter is not available with value type File.Note:When you enter 0 for both Minimum and Maximum, the default value can be any value (according t

[...truncated for brevity...]

### OhidGValueTables


# Value Tables

CANdb++

Value tables can be used to assign symbolic names to the values of signals or environment variables.

## Value Description within a Value Table

- Value numerical value (raw value) of the signal or the environment variable to which the value description is assigned

- Value description textual description of the value

|  | Example For example, a value table can be used to assign the symbolic names red, yellow and green to the concrete values 1, 2 and 3 of the Colors signal. |

The Value Tables Window contains the list of user-defined value tables.

## Usage in CANdb Network Files (DBC Files)

In CANdb network files (DBC files) value tables are not stored as separate objects, but as part of signals or environment variables.

If you assign a value table to a signal/an environment variable, this value table will be copied and stored together with the signal/environment variable. This copy gets an automatically generated name (name prefix VtSig_ or VtEv_ + signal name or variable name). With that name the value table will be displayed (after reopening the DBC file) in the Value Table Window.

It is no longer comprehensible which value tables were used originally, because it is not possible to store this information in the DBC format. For this reason changes you make to one value table will not affect any other value tables that used this as template. If you want this, you have to maintain these changes manually for each separate value table.

|  | Note 

[...truncated for brevity...]

### Ohid_CANdbComparisonCANdb


# CANdb++ in Comparison to CANdb

CANdb++

CANdb++ offers significantly expanded functionality compared to CANdb:

- The tree view on the left side of the Overview Window offers a hierarchical overview of the available objects and object types.

- On the right side of the Overview Window and in the List Windows is a table-format overview of objects for the selected object type.

- The values of system parameters and user-defined attributes can be edited directly in the tables of the Overview or List Windows. (Modifying these values)

- CANdb++ databases can be created and modified.

- The CANdb++ data model provides more comprehensive modeling options than the CANdb data model.

- When modifying a CANdb++ database explicit saving is not necessary, since each change is immediately saved in the database. (Notes on saving CAN databases)

- Interconnections (relations) between two objects of different object types can be produced by Adding a link.By linking a signal to a message, for example, the user can define the message in which this signal should be transmitted.

- The automatic consistency check can be used to determine whether the objects of a CAN database and their interrelationships are consistent.

- With CANdb++ Admin and MS Visual Source Safe Version administration for CAN databases and objects can be performed.

## Notes on file names and text fields:

- The text field size is limited in databases.

- Names may contain a maximum of 255 characters.To permit compatibi

[...truncated for brevity...]

### Support


# Vector | Support

CANdb++ » Vector | Support

|  | Vector Informatik GmbH – Support Our business hours are Monday to Friday from 9:00 am to 5:00 pm (CET): Phone: Fax: E-Mail: Online Report Form: +49.711.80670.200 +49.711.80670.111 support@vector.com https://vector.com/support/ | Phone: Fax: E-Mail: Online Report Form: | +49.711.80670.200 +49.711.80670.111 support@vector.com https://vector.com/support/ |  |
| --- | --- | --- | --- | --- |
| Phone: Fax: E-Mail: Online Report Form: | +49.711.80670.200 +49.711.80670.111 support@vector.com https://vector.com/support/ |

|  | International Subsidiaries Depending on your location or language you may select the corresponding phone or e-mail support contact under https://vector.com/support/. |  |

| Version 3.0.28© Vector Informatik GmbH |  |


### VectorAttributes


# Vector Tool Chain Attributes

CANdb++ » Vector Tool Chain Attributes

This document explains the CANdb attributes (user-defined attributes only) that are used in the Vector CAN tools. The documentation of the attributes is ordered according to the application domains of the attributes. These application domains are:

- General

general attributes, which cannot be ordered to any application domain.

- Interaction Layer

attributes describing the transmit and receive behavior of messages and signals.

- Transport Protocol and Diagnostics

attributes for the configuration and the behavior of the ISO/DIS transport protocol for CAN and the diagnostics of ECUs.

- Network Management

attributes for the configuration and the behavior of the OSEK network management of a CAN network.

- Tool specific

attributes used for the configuration of Vector tools (e.g. CANoe).

This collection does not cover all attributes that may be used in CAN databases since the user may add arbitrary attributes to the databases.

## General Attributes

| Manufacturer |
| --- |
| Object Type: | Network |
| Value Type: | String |
| Unit: |  |
| Default Value: | '' |
| Valid Values: |  |
| Description: | Specifies the OEM. |

| VersionYear, VersionMonth, VersionWeek, VersionDay |
| --- |
| Object Type: | Network |
| Value Type: | Int |
| Unit: |  |
| Default Value: | 0 for VersionYear 1 for VersionMonth, VersionWeek and VersionDay |
| Valid Values: | 0...99 for VersionYear 0...12 for VersionMonth 0...52 f

[...truncated for brevity...]

### candbdialogexportecus


# Dialog: Export ECUs

CANdb++

The Export ECUs dialog is opened by clicking on the ECUs node in the hierarchy tree of the Overview Window. The dialog is opened in the shortcut menu by selecting Export ECUs….

Use the dialog to export the electronic control units of a database to a dbc file. One dbc file is created for each electronic control unit.

The dbc file names use the following naming convention:

File name = <electronic control unit name> + '_' + <appendix>

## […]

Opens a dialog for selecting the directory in which the dbc file should be exported.

## Overwrite existing files

The Overwrite existing files option specifies whether dbc files that may already exist should be overwritten by files of the same name.

## Appendix

The Appendix can be used to annotate the exported files (e.g. 'Db_from_1-1-2006'). Only numbers, letters and the characters '_' and '-' can be used for the appendix.

## Include TP messages

When you select Include TP messages the following objects will be exported in addition to the selected ECUs:

- Network Attributes

- TP messages and their signals

TP messages are messages that have at least one of the following message attributes set to Yes:

- DiagState,

- DiagResponse or

- DiagRequest

- Further ECUs (without their communication data) that either

- send TP messages to the selected ECU or

- receive TP messages from the selected ECU.

## Export of ECUs and nodes

Two variants are available for exporting ECUs and nodes:

- Based on the

[...truncated for brevity...]

### ohidp_g_nodelayer_dll


# Embedding Modeling Libraries

CANdb++ » Embedding Modeling Libraries

If you would like to embed a modeling library (DLL file) in CANoe, go forward as follows:

- Insert the attribute NodelayerModules to the attribute list of CANdb++ for the node object with type String.

- Insert the name of the modeling library as attribute value.Either you can insert the name in the attribute definition, then all nodes have the modeling libraries by default.Or you can insert the modeling library name individual for every node in the CANdb++ node view.

- In the Simulation Setup please check, if the modeling library is assigned to the specific node. Therefore select the node and choose the shortcut menu Configuration...|Components.

- Please check the Nodelayer Environment setting via the menu path Configuration...|Options...|Measurement|General. under Compatibility.

- Modelling DLLs (MATLAB, osCAN Library) can be assigned to a node directly in the Simulation Setup using shortcut menu Configuration...|Components. Then these DLLs are assigned to all busses where the node belongs to.

- A DLL shall be defined either in the database or directly in the node (Simulation Setup), but not both at the same time.

Vector tool chain attributes | Search sequence modeling library

| Version 3.0.28© Vector Informatik GmbH |  |


---

## 新特性 (NewFeatures)

**条目数**: 2

### CANdb_NewFeatures_30


# New Features in Version 3.0

CANdb++ » New Features » Version 3.0

## New Features 3.0 SP26

- Page Layout in Message dialog displays at once up to 64 Bytes.

- Optimization of the calculation of minimum values and maximum values in the Signal dialog.

- Correction of a crash when copying nodes in a read-only database.

- When exporting CSV signals, the minimum values and maximum values are exported with full precision.

- For a Mapped Rx signal of a node, the assigned value table is displayed in the dialog in addition to the overview.

- For user-defined attributes with the type hex it is now possible to define the min/max/default values also in the range 0xF0000000 to 0xFFFFFFFFFF.

## New Features 3.0 SP22

- Improved messages layout presentation and handling.

- Improved operating with min/max/init values of signals on their low/high valid limit.

- Support for default values during XML export.

- Improved display of consistence check results for value tables.

## New Features 3.0 SP20

- Settings|Long NamesdialogLong names can be used for signals, messages, nodes and environment variables.Symbolic names with a length of up to 128 characters can be used.

- Value tablesdisplayed forsignalsIf a value table is assigned to a signal, this is indicated in the Overview Window by the fact that the signal item can be expanded.

- Extended Multiplexor concept for DBC databases The extended multiplexor concept allows you to define several multiplexor signals in a single message.

[...truncated for brevity...]

### OHID_CANdb_new_features


# New Features

CANdb++

## New features with version 2.7

- In the object lists of the Overall View Window all relevant attributes of the displayed objects are shown. If relations between objects are displayed in the lists the attributes of the basic objects are shown too. With this the fast overview of the objects increases.Different colors indicate, whether the value of the attribute is defined on the relation or on the basic object. In addition it is shown, whether the value can be changed or not.(See also: List Window)

- The shown objects in the List views can be exported to CSV (Character Separated Values) files. The objects are saved with the displayed attributes in the visible sort sequence. This enables an easy exchange of the object information with other programs (e.g. Microsoft Excel).

- Special attributes of the Vector tool chain (e.g. bus type) are generated automatically on the export of databases. With this the use of the communication matrices in the Vector tools will be more convenient.

- On the Defaults page (Options | Settings) you can make settings in order to influence values that are used to define new objects (signal or message).

- Since CANdb++ 2.7 SP8 SAE-J1939 protocol will be supported by an extended J1939 database format. Now the identifier of a message contains the complete 29 bit CAN identifier inclusive the priority, transmitter an receiver address.A plug-in makes the handling of Parameter Groups and the definition of communication relatio

[...truncated for brevity...]
