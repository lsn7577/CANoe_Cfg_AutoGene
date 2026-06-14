# System Variables CAPL Functions

> Category: `SystemVariables` | Type: `notes`

## Description

Define Variables

General Functions

Return Data of a Variable

Set the Value of a Variable

Structs of System Variables

Variable Filters

sysDefineVariableLongLong

Defines a variable of the Int64 type.

sysGetVariableArraySize

Returns the current array size of a system variable (element) of a generic array type.

Sets the current array size of a system variable (element) of a generic array type.

System Variables | Direct Access to Values from System Variables

| SYSTEM VARIABLES These CAPL functions are supported by Windows and Linux. The functionality under Linux has not been fully tested yet. |
|---|

| Define Variables General Functions Return Data of a Variable | Set the Value of a Variable Structs of System Variables Variable Filters |
|---|---|

| Functions | Short Description |
|---|---|
| sysDefineVariableData | Defines a variable of the data type. |
| sysDefineVariableFloat | Defines a variable of the float type. |
| sysDefineVariableFloatArray | Defines a variable of the float[] type. |
| sysDefineVariableInt | Defines a variable of the int type. |
| sysDefineVariableIntArray | Defines a variable of the int[] type. |
| sysDefineVariableLongLong | Defines a variable of the Int64 type. |
| sysDefineVariableString | Defines a variable of the String (char[]) type. |

| Functions | Short Description |
|---|---|
| sysDefineNamespace | Defines a name space. |
| sysUndefineNamespace | Deletes a name space. |
| sysUndefineVariable | Deletes a variable. |

| Functions | Short Description |
|---|---|
| SysGetOrigTimeNS | Returns the original time stamp of the last update to the variable value. |
| sysGetVariableArrayLength | Returns the length of an array system variable. |
| sysGetVariableArraySize | Returns the current array size of a system variable (element) of a generic array type. |
| sysGetVariableData | Returns the value of a variable of the data type. |
| sysGetVariableDescriptionForValue | Retrieves a description for a value of a system variable of type long or long array. |
| sysGetVariableDWord | Returns the value of a variable of type unsigned 32 bit integer. |
| sysGetVariableFloat | Returns the value of a variable of the float type. |
| sysGetVariableFloatArray | Returns the value of a variable of the float[] type. |
| sysGetVariableInt | Returns the value of a variable of the int type. |
| sysGetVariableLongArray | Returns the value of a variable of the int[] type. |
| sysGetVariableLongLong | Returns the value of a variable of a 64 bit integer type. |
| sysGetVariableMax | Retrieves the maximum of a variable. |
| sysGetVariableMin | Retrieves the minimum of a variable |
| sysGetVariableQWord | Returns the value of a variable of type unsigned 64 bit integer. |
| sysGetVariableString | Returns the value of a variable of the string (char[]) type. |
| sysGetVariableSVType | Gets the type of a system variable encoded as a long integer. |
| sysGetVariableTimeNS | Returns the time stamp of the last update to the variable value. |
| sysGetVariableValueForDescription | Retrieves the value for a value description of a system variable of type long or long array. |
| sysIsVariableTypeSigned | Returns whether the data type of a system variable is signed. |

| Functions | Short Description |
|---|---|
| sysSetAnalysisOnlyVariable | Defines whether the variable shall be used only in the analysis part of CANoe. |
| SysSetVariableArraySize | Sets the current array size of a system variable (element) of a generic array type. |
| sysSetVariableData | Sets the value of a variable of the data type. |
| sysSetVariableDescriptionForValue | Sets a description for a particular value of a system variable of type long or long array. |
| sysSetVariableDWord | Sets the value of a variable of type unsigned 32 bit integer. |
| sysSetVariableFloat | Sets the value of a variable of the float type. |
| sysSetVariableFloatArray | Sets the value of a variable of the float[] type. |
| sysSetVariableInt | Sets the value of a variable of the int type. |
| sysSetVariableLongArray | Sets the value of a variable of the int[] type. |
| sysSetVariableLongLong | Sets the value of a variable of a 64 bit integer type. |
| sysSetVariableQWord | Sets the value of a variable of type unsigned 64bit integer. |
| sysSetVariableString | Sets the value of a variable of the string (char[]) type. |

| Functions | Short Description |
|---|---|
| sysBeginVariableStructUpdate | Starts the update of several elements of a system variable of type struct or generic array. |
| sysEndVariableStructUpdate | Ends the update of several elements of a system variable of type struct or generic array. |
| sysGetVariableMemberPhys | Retrieves the physical value of a specific element of a variable of type struct or generic array. |
| sysSetVariableMemberPhys | Sets the physical value of a specific element of a variable of type struct or generic array. |

| Functions | Short Description |
|---|---|
| sysCreateVariableFilter | Creates a new variable filter behind the node calling the function. |
| sysFilterAddNamespace | Adds a namespace to the variable filter. |
| sysFilterAddVariable | Adds a variable a variable filter. |
| sysFilterRemoveNamespace | Removes a namespace from the variable filter. |
| sysFilterRemoveVariable | Removes a variable from a variable filter. |
| sysSetVariableFilterActive | Activates or deactivates a variable filter. |

| Version 15© Vector Informatik GmbH |
|---|
