# getChecksum

> Category: `Obsolete` | Type: `function`

## Syntax

```c
int getChecksum(linFrame msg)
```

## Description

Returns the currently set checksum of a LIN frame or LIN checksum error.

In the case of a LIN frame, the correct value derived from the message data is returned by default, even after the message data has been modified. The user can, however set a deviating value with setManualChecksum to generate checksum errors on the LIN bus. This value is then constant and will not be affected by changes in the message data. To turn off this behavior for a given message, the user must call resetManualChecksum.

## Return Values

Calculated checksum.

## Availability

| Up to Version |
|---|
