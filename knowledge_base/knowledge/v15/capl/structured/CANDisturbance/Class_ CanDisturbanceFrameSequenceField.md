# Class: CanDisturbanceFrameSequenceField

> Category: `CANDisturbance` | Type: `notes`

## Description

Each object of CanDisturbanceFrameSequenceField represents one field of a CAN frame in an object of class CanDisturbanceFrameSequence.

Each field of a CAN/CAN FD frame contains one or multiple bits. Each bit is represented by an object of the class CanDisturbanceBitSequence.

If a field has several bits, this field is represented by an array in this data type. The bit order of a field with several bits corresponds to the CAN/CAN FD specification.

For example, the CAN Base Identifier field contains 11 bits. This field is represented by the attribute IDBase of this structure.

The bit represented by ID28 is the first bit that is sent in the Base Identifier field on the bus. For example, to set a dominant value for the ID28 bit, the attribute IDBase of the CanDisturbanceFrameSequence must be called in the following way:

canDisturbanceFrameSequence seq;seq.IDBase.BitSequence[10].SegmentValue[0] = 'd';

This means the array index 0 is the Least Significant Bit (LSB) and the array index 10 is the Most Significant Bit (MSB) in the Base Identifier field.

The table below shows the definition in a common view (expected payload):

—

You can access control information of a CanDisturbanceFrameSequenceField object with the following attributes:

Digital Disturbance

| Point of View | Bit N | ... | Bit 0 |
|---|---|---|---|
| Transmission on bus | MSB | LSB |  |
| Array index | N | 0 |  |

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| BitSequence | Represents the bit sequence used for the field. | CanDisturbanceBitSequence [32] | — |
| FieldLength | Returns the length of the field. | byte | read-only |

| Version 15© Vector Informatik GmbH |
|---|
