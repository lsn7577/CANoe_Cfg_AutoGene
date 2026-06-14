# linDeactivateResps

> Category: `LIN` | Type: `function`

## Syntax

```c
long linDeactivateResps(); // form 1
```

## Description

This function deactivates frame responses for all frames published by the calling Slave node. The frame responses can be deactivated individually using the function linSetRespCounter().

With form 2 you can deactivate the Slave responses of the selected Slave node (nodeName). If the parameter nodeName is not set or an empty string is given, the Slave responses of the node invoking this function will be deactivated.

If the configurable_frames list for the targeted Slave node is not complete, the function will not work correctly.

## Return Values

Number of deactivated frame responses or -1 on failure.

## Availability

| Since Version |
|---|
