# Overview Signal Descriptions

> Category: `DBC` | Subcategory: `signal_descriptions` | Type: `concept`

Besides the object attributes the CANopen standard allows the division of the object value (signal group) into several signals. For the signals the length and the starting position (in bits) is set. With CANeds you can define such signal descriptions for object.

This is possible for objects of object type VAR and data type of the UNSIGNED group as well as user-defined data types. Such objects you can separate in ranges and allocate these ranges with signals.

Note

The specification of signal descriptions is possible in XML format only. When you save a file you have to consider that you save it in XML format (as XDC or XDD file). Otherwise the information about signals are lost if you save the file in INI format (as EDS or DCF file).

| Note The specification of signal descriptions is possible in XML format only. When you save a file you have to consider that you save it in XML format (as XDC or XDD file). Otherwise the information about signals are lost if you save the file in INI format (as EDS or DCF file). |
|---|

## Layout of signal lists

The data type of an object defines the size of it. This size is also valid for the signal list. So an object of data type Unsigned32 has a size of 32 bit. These bits you can allocate with signals freely. It is not necessary that you string the signals together and to allocate the whole range of the object. The resulting gaps are filled automatically with empty signals by CANeds.

## Calculation of the object value

The value of an object is represented by the signal list and the values of the individual signals. To calculate the object value, the values of the signals are stringed together.

Example

You define four signals A, B, C and D with different values and signal lengths for an object 2000h of data type Unsigned32.

Signal A: value 01h,Signal B: value 04h,Signal C: value 19h,Signal D: value 98h

This results in an object value of 01041998h.

If you don't define signal B, the resulting gap is filled with an empty signal. The value of this signal is 0 and the object value would be 01001998h.

| Example You define four signals A, B, C and D with different values and signal lengths for an object 2000h of data type Unsigned32. Signal A: value 01h,Signal B: value 04h,Signal C: value 19h,Signal D: value 98h This results in an object value of 01041998h. |
|---|

| Example If you don't define signal B, the resulting gap is filled with an empty signal. The value of this signal is 0 and the object value would be 01001998h. |
|---|

## Objects and signals

Caution!

Please take care that the signal lists and its signalsare additional information only!

For Vector applications working with files, that are created with CANeds, the object is the reference. So the values of the object are used always!

If the are any differences of the default value or the limit values between object and signals, a warning is display during saving the EDS file.

The following cases may occur:

Create signal lists | Insert signals | Edit signals

| Caution! Please take care that the signal lists and its signalsare additional information only! For Vector applications working with files, that are created with CANeds, the object is the reference. So the values of the object are used always! |
|---|
