# Class: CanDisturbanceFrameTrigger

> Category: `CANDisturbance` | Type: `notes`

## Description

With a trigger field, it is possible to define which value each bit of each field in a CAN frame must have to fulfill the trigger condition. When the trigger condition is fulfilled, the CAN Disturbance Interface outputs the configured sequence to the bus.

Each field of a CAN/CAN FD frame contains one or multiple bits that can be configured.

If a field has multiple bits, this field is represented by an array in this data type. The bit order of a field with several bits corresponds to the CAN/CAN FD specification.

For example, the Base Identifier field contains 11 bits, and the field is represented by the attribute IDBase of this structure.

The bit represented by ID28 is the first bit that is sent in the Base Identifier field on the bus. To set a defined value for this bit the attribute IDBase must be designated IDBase[10].

This means the Array-Index 0 is the Least Significant Bit (LSB) and the Array-Index 10 is the Most Significant Bit (MSB) in the Base Identifier field.

The table below shows the definition in a common view (expected payload):

A special case is the payload field which is represented by the Payload attribute. This field represents the data bytes of a frame. This field has the following structure.

Payload stream on bus and access via Payload attribute:

The table below shows the payload field bit order:

You can access control information of a CanDisturbanceFrameTrigger object with the following attributes:

| Value | Description |
|---|---|
| 0 | The bit must be dominant |
| 1 | The bit must be recessive |
| -1 | The bit may be dominant or recessive (irrelevant) |

| Point of View | Bit N | ... | Bit 0 |
|---|---|---|---|
| Transmission on bus | MSB | LSB |  |
| Array index | N | 0 |  |

| Point of View | Bit 7 | ... | Bit 0 | ... | Bit 7 | ... | Bit 0 |
|---|---|---|---|---|---|---|---|
| Transmission on bus | Byte0 (MSB) | Byte0 (LSB) | Byte64 (MSB) | Byte64 (LSB) |  |  |  |
| Payload array index | [7] | [0] | [511] | [505] |  |  |  |

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| Trigger start definition |  |  |  |
| TriggerFieldType | The CAN frame field will cause the trigger to start sending the configured sequence.The system variablesysvar::CanDisturbanceInterace::Enums::FieldType contains an enumeration of possible values. | dword | — |
| TriggerFieldOffset | The offset in the CAN frame field is configured by TriggerFieldType. If the offset is outside the trigger field, the offset is set to the maximum number of bits this field contains. If the trigger field EndOfFrame is used, the offset is extended up to 26. The reason is that in this case an IFS or a Bus Idle trigger can also be configured. | dword | — |
| Trigger configuration |  |  |  |
| IDBase | The standard ID or extended ID (28-18) | char[11] | — |
| RemoteBase | RTR bit: standard CAN frame RRS bit: standard CAN FD frame SRR bit: extended CAN/CAN FD frame | char | — |
| IDE | The IDE bit in a CAN/CAN FD frame | char | — |
| IDExtended | The extended ID (17-0) of an extended CAN/CAN FD frame | char[18] | — |
| RemoteExtended | RTR bit: extended CAN frame RRS bit: extended CAN FD frame | char | — |
| FDF | The FDF bit | char | — |
| Reserved | Res bit: standard and extended CAN FD frame R0 bit: extended CAN frame | char | — |
| BRS | The BRS bit for standard and extended CAN FD frame(not usable for CAN frames) | char | — |
| ESI | The ESI bit for standard and extended CAN FD frames(not usable for CAN frames) | char | — |
| DLC | The Data Length Code (DLC) for CAN/CAN FD frames | char[4] | — |
| Payload | The payload data of a CAN/CAN FD frame CAN frames up to 64 bits possibleCAN FD frames up to 512 bits possible | char[512] | — |
| StuffCount | The stuff count field for CAN FD frames. Includes the parity bit.(not usable for CAN frames) | char[4] | — |
| CRC | The CRC value of CAN/CAN FD frames CAN frames up to 15 bitsCAN FD frames DLC < 10 up to 17 bitsCAN FD Frames DLC >= 10 up to 21 bits | char[21] | — |
| CRCDelimiter | The CRC delimiter for CAN / CAN FD frames | char | — |
| AckSlot | The acknowledge slot | char | — |
| AckDelimiter | The acknowledge delimiter | char | — |
| EndOfFrame | The End Of Frame (EOF) | char[7] | — |

| Version 15© Vector Informatik GmbH |
|---|
