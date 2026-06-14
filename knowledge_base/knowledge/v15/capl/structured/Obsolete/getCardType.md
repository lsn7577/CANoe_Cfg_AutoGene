# getCardType

> Category: `Obsolete` | Type: `notes`

| Deprecated Function |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long getCardType(); |  |  |  |
| Function | Determines the type of CAN platform being used. Is needed e.g. to program the BTR / OCR values. |  |  |  |
| Parameters | — |  |  |  |
| Return Values | 17: for Vector drivers |  |  |  |
| For other manufacturer other values will be returned. |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1 | CAN | • | • |  |
| Example ...switch(getCardType()) {case 6: setOcr(0,0x02); break;case ...default: write("Unknown driver %d", getCardType()); break;}... |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
