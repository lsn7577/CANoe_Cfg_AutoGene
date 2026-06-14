# ISO11783 TC IL Functional Properties

> Category: `ISO11783` | Type: `notes`

## Description

These properties describe the functional properties of a real Task Controller that is simulated with the TC IL.

tcVersion

Version of the Task Controller according to ISO11783-10.

0..4

4

Yes

bootTime

Maximum number of seconds from a power cycle to transmission of first Task Controller Status message.

0..255

255

availableMemory

If the object pool size in a Request Object-pool Transfer message of a client is bigger than this value then the Request Object-pool Transfer Response message of the Task Controller contains the status value 1 (There is not enough memory available). Otherwise the status value is 0 (There may be enough memory).

0.. 4294967295

100000

options

Bit 0: Supports TC-BAS

Bit 1: Supports TC-GEO without position based control

Bit 2: Supports TC-GEO with position based control

Bit 3: Supports Peer Control

Bit 4: Supports TC-SC (Section Control)

Bit 5-15: Reserved

This value is send with the Version message

0..FFFFh

65535

numberOfBooms

Maximum number of section control booms that is supported for Section Control.

This value is send with the Version message.

numberOfSections

Maximum number of sections that is supported for Section Control.

numberOfControlChannels

Maximum number of individual control channels that is supported for position based control.

enablePassiveMode

Enables (1) or disables (0) the passive mode of the Task Controller.

If property enableAutoDetection is not set then the Task Controller is monitored that has the same node address as defined in the database.

0..1

0

enableAutoDetection

Enables or disables the auto detection of the Task Controller address. If enabled then the Task Controller that registers first on the bus with an Address Claimed message is monitored.

This property has only impact if passive mode is enabled.

autoDetectionFunctionInstance

If value is not -1 the auto detected Task Controller must have this Function Instance.

This property has only impact if passive mode is enabled and property enableAutoDetection is set.

0..31, -1

-1

| Property Value | Description | Value Range | Initial Value | IL must be stopped (TCIL_ControlStop) |
|---|---|---|---|---|
| tcVersion | Version of the Task Controller according to ISO11783-10. | 0..4 | 4 | Yes |
| bootTime | Maximum number of seconds from a power cycle to transmission of first Task Controller Status message. | 0..255 | 255 | Yes |
| availableMemory | If the object pool size in a Request Object-pool Transfer message of a client is bigger than this value then the Request Object-pool Transfer Response message of the Task Controller contains the status value 1 (There is not enough memory available). Otherwise the status value is 0 (There may be enough memory). | 0.. 4294967295 | 100000 | Yes |
| options | Bit 0: Supports TC-BAS Bit 1: Supports TC-GEO without position based control Bit 2: Supports TC-GEO with position based control Bit 3: Supports Peer Control Bit 4: Supports TC-SC (Section Control) Bit 5-15: Reserved This value is send with the Version message | 0..FFFFh | 65535 | Yes |
| numberOfBooms | Maximum number of section control booms that is supported for Section Control. This value is send with the Version message. | 0..255 | 255 | Yes |
| numberOfSections | Maximum number of sections that is supported for Section Control. This value is send with the Version message. | 0..255 | 255 | Yes |
| numberOfControlChannels | Maximum number of individual control channels that is supported for position based control. This value is send with the Version message. | 0..255 | 255 | Yes |
| enablePassiveMode | Enables (1) or disables (0) the passive mode of the Task Controller. If property enableAutoDetection is not set then the Task Controller is monitored that has the same node address as defined in the database. | 0..1 | 0 | Yes |
| enableAutoDetection | Enables or disables the auto detection of the Task Controller address. If enabled then the Task Controller that registers first on the bus with an Address Claimed message is monitored. This property has only impact if passive mode is enabled. | 0..1 | 0 | Yes |
| autoDetectionFunctionInstance | If value is not -1 the auto detected Task Controller must have this Function Instance. This property has only impact if passive mode is enabled and property enableAutoDetection is set. | 0..31, -1 | -1 | Yes |

| Version 15© Vector Informatik GmbH |
|---|
