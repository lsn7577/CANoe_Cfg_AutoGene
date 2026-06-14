# Signal Editor

> Category: `DBC` | Subcategory: `windows` | Type: `concept`

In this dialog you can modify the attributes of the signal that is currently selected. Just as in the signal list you can change the name, the start bit and the length of the signal.

Caution!

If you change the signals in a sub object, this will change the signals of all other sub objects of an array too. The signal lists of all objects of an array have to be identical. If the main object is a record, the signal lists of the sub objects can differ.

The following table provides you an overview of the additional dialog elements which you can use to change the attributes of a signal.

| Caution! If you change the signals in a sub object, this will change the signals of all other sub objects of an array too. The signal lists of all objects of an array have to be identical. If the main object is a record, the signal lists of the sub objects can differ. |
|---|

| Dialog element | Description |
|---|---|
| Type | data type of the signal |
| Default | default value of the signal, initial value 0 |
| Low Limit | lower limit of the signal value (for signals with more than 64 bit, enter this value in hexadecimal format) |
| High Limit | higher limit of the signal value (for signals with more than 64 bit, enter this value in hexadecimal format) |
| Automatic calculation of limits | activates or deactivates the automatic calculation of the limit values |
| Unit | unit of the signal |
| Factor | used for the conversion of the signal value into a logical value |
| Offset | correction value to calculate the signal value for the generation of databases and the correct display in the Trace Window of CANoe/CANalyzer |

### Dialog element

### Description

Type

data type of the signal

Default

default value of the signal, initial value 0

Low Limit

lower limit of the signal value (for signals with more than 64 bit, enter this value in hexadecimal format)

High Limit

higher limit of the signal value (for signals with more than 64 bit, enter this value in hexadecimal format)

Automatic calculation of limits

activates or deactivates the automatic calculation of the limit values

Unit

unit of the signal

Factor

used for the conversion of the signal value into a logical value

Offset

correction value to calculate the signal value for the generation of databases and the correct display in the Trace Window of CANoe/CANalyzer

With the button [Get from object] in section Get object attributes you can read the default value from the object. The calculation of the signal value is done automatically. To enter the value range limits manually, deactivate the check box Automatic calculation of limits.

Note

If the default value of the object contains a phrase in the form of 0x180+$NODEID, this value cannot be read from the object. In this case the button [Get from object] is inactive and the default value is set to a minus sign.

If the check box Automatic calculation of limits is deactivated, you can calculate the possible limit values dependent on the data type of the signal with the button [Calculate limits].

| Note If the default value of the object contains a phrase in the form of 0x180+$NODEID, this value cannot be read from the object. In this case the button [Get from object] is inactive and the default value is set to a minus sign. |
|---|

## Modification of the signal size

If you change the size of a signal (the number of bits), take care that the default value might be invalid. The limit values are influenced by changing the signal size too. In both cases CANeds supports you on adapting the values to the new size of the signal.
