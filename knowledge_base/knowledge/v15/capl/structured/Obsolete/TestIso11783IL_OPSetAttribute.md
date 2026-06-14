# TestIso11783IL_OPSetAttribute

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by: Iso11783IL_OPSetAttribute |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long TestIso11783IL_OPSetAttribute( dbNode node, dword objectID, dword attributeID, long value ); |  |  |  |
| long TestIso11783IL_OPSetAttribute( dbNode node, dword objectID, dword attributeID, long value, long options ); |  |  |  |  |
| Function | The function sets an attribute value of an object. The object must exist in the object pool and support the attribute ID. If the Object Pool API is active, the Change Attribute command (175) is sent to the Virtual Terminal. This can be suppress with Bit 0 in options. Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. | Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |
| Note Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous. Further information on site MultiBus Environment. |  |  |  |  |
| Parameters | node Simulation node to apply the function. |  |  |  |
| objectID Object ID of an object in the object pool |  |  |  |  |
| attributeID Attribute ID, see ISO11783-6 |  |  |  |  |
| value New value |  |  |  |  |
| options Options Bit 0 and 1 = 0: send Change Attribute Value command if parameters are valid Bit 0 and 1 = 1: suppress Change Attribute Value command Bit 0 and 1 = 2: force sending Change Attribute Value command even parameters are invalid Bit 0 and 1 = 3: reserved |  |  |  |  |
| Return Values | 0: Function has been executed successfully <0: An error has occurred, see error codes -1108: Value is out of range -1109: Attribute is read only -1110: Object ID not found -1111: Attribute ID not supported |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 | ISO11783 Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
