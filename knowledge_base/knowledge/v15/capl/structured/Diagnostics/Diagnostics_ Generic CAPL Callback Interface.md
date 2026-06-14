# Diagnostics: Generic CAPL Callback Interface

> Category: `Diagnostics` | Type: `notes`

## Description

With CANoe 5.1 SP2 an updated CAPL callback interface is available that makes no assumptions of the used transport protocol and supports connection oriented and segmented transmissions easier.

It is now possible, with two (ECU simulations) or three functions (test simulations or test modules) to extensively configure the TP layer. To do this, the DiagGetCommParameter function was introduced, which makes set parameters for a diagnostic description accessible in CAPL programs, whereby the parameter qualifiers are identical for all CDDS and manufacturers.

Diagnostics: Connection of the Communication Layer

| Version 15© Vector Informatik GmbH |
|---|
