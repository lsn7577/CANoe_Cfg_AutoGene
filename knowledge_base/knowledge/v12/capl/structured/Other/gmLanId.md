# gmLanId

> Category: `Other` | Type: `function`

## Syntax

```c
dword gmLanId (dbMessage aMessage, dword aSourceId)
```

## Description

This function can be used to create a message ID for a GMLAN message. In addition to the message, you must specify the transmission node or its source ID.

The message ID returned can be used, for example, to wait for a specific GMLAN message with the TestWaitForMessage function.

## Return Values

If the message is a GMLAN message, a GMLAN message ID will be returned containing the correct source address and priority. Otherwise, the message ID will be returned.

## Example

```c
dword gmID = 0;
long result = 0;
gmID = gmLanId(Comfort::Console_1, 48);
waitResult = TestWaitForMessage(gmID, 5000);
```

## Availability

| Since Version |
|---|
