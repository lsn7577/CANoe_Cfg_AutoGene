# ChkConfig_EnablePDULayer

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_EnablePDULayer();
```

## Description

Enables the PDU layer for the current bus context. It affects the next checks that are created after calling this function.

Use this function to enable the PDU layer again after calling ChkConfig_DisablePDULayer.

Default is enabled for a PDU network.

## Return Values

0: Successful

## Availability

| Since Version |
|---|
