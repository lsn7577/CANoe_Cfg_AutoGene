# Device Information

> Category: `DBC` | Subcategory: `tab_pages` | Type: `concept`

This page contains the settings of the used device. The values of Dynamic Channels and Compact PDO can be set either in the edit field or by using the check boxes.

To get the number of explicit defined PDOs in the EDS button the [Get] is used. Button [Set] sets the number of explicit defined PDOs and deletes unnecessary objects or creates necessary objects. Only those sub objects of the PDO are created which are selected in the Compact PDO field. Existing PDOs are not updated.

Example

Creation of an EDS with three RxPDO (sub-index 1, 2 and 5 ) and two TxPDO (sub-indexes 1 and 2 ).

| Example Creation of an EDS with three RxPDO (sub-index 1, 2 and 5 ) and two TxPDO (sub-indexes 1 and 2 ). Set CompactPDO to 0x13, number of RxPDO to 3, number of TxPDO to 0 and click [Set]. Set CompactPDO to 0x3, number of TxPDO to 2 and click [Set] again. To specify further compact PDOs only the number of RxPDO/TxPDO and value of CompactPDO is set (without clicking [Set]). |
|---|
