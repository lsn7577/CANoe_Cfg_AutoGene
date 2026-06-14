# Main object attributes

> Category: `DBC` | Subcategory: `object_attributes` | Type: `concept`

## General

In this page the attributes of a main object are shown.

If the object is structured (object type ARRAY, RECORD or DEFSTRUCT) the sub object fields are enabled. The number of sub objects in the EDS Window is modified if focus is on the sub number field and the return key is pressed, another object is selected or the file is stored.

Most often all sub objects of an array are equal except the name. It is allowed to describe only a template in the main object. This is made by selecting the check box Compact Storage. All attributes apart from object type and sub number refer to the several sub object (except sub-index 0 and 255). Object type of the sub objects is assumed to be VAR. If the object includes any signal descriptions, they are not stored and cannot be recreated!

For some objects, e.g. object 1000h, there is an additional button right of the default value field. After clicking this button a dialog appears in which a symbolic representation of the default value is shown. If you enter a default value manually a range check is done with the given low and high limits or the allowed value range depending on the object data type. If a range violation is detected, an appropriate warning is displayed in the output window.

If an object has a signal description, you can read the default value and the limits (high and low) from this signal description with the buttons in the section Get signal list attributes and set them for the selected object.

Objects with object type ARRAY or RECORD can be linked to a manufacturer or profile specific data structure. If one of these structures, which are displayed in the Type Definition page of the main window, is edited all objects which are linked to this object are adapted. To use this mechanism the structure has to be selected in the Linked with list, which appears at the location of the data type list.

## Device configuration

This page shows the attributes which are allowed in DCF only. If the object type is DOMAIN the path for the upload and download file can be specified.

## Signals

This page allows the creation of signal descriptions for objects.

In the upper part you can create the list of signals with a maximum number of bits. The maximum is defined by the data type of the selected object. On selection of a signal, the lower part shows the information of that signal. With button [Edit...] you can open the dialog Signal Editor which allows the modification of the signal values. With button [Delete] you can remove the selected signal from the list. If you want to remove all signals, use button [Delete all]. The button [Get Default] in the section Get object attributes reads the default value from the object and set it for the signal.

## Unknown Entries

This page contains entries of the object which are not conform to the EDS specification. The entries are displayed in the INI-file format (name=value). Comments (which start with a semicolon) in an EDS file section are also displayed in this page.
