#!/usr/bin/env python

#
# Generated Thu Jun 27 15:36:16 2024 by generateDS.py version 2.35.15.
# Python 3.8.10 (default, Nov 22 2023, 10:22:35)  [GCC 9.4.0]
#
# Command line options:
#   ('-o', 'egais/egais.py')
#   ('-s', 'egais/egaissubs.py')
#   ('--use-old-simpletype-validators', '')
#   ('--external-encoding', 'utf-8')
#   ('--silence', '')
#
# Command line arguments:
#   ./xsd/WB_DOC_SINGLE_01.xsd
#
# Command line:
#   /root/.local/share/virtualenvs/egais-rBIiM-38/bin/generateDS.py -o "egais/egais.py" -s "egais/egaissubs.py" --use-old-simpletype-validators --external-encoding="utf-8" --silence ./xsd/WB_DOC_SINGLE_01.xsd
#
# Current working directory (os.getcwd()):
#   egais
#

import os
import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = 'utf-8'
SaveElementTreeNode = True

#
# Data representation classes
#


class DocumentsSub(supermod.Documents):
    def __init__(self, Version='1.0', Owner=None, Document=None, **kwargs_):
        super(DocumentsSub, self).__init__(Version, Owner, Document,  **kwargs_)
supermod.Documents.subclass = DocumentsSub
# end class DocumentsSub


class DocBodySub(supermod.DocBody):
    def __init__(self, WayBill=None, Ticket=None, WayBillAct=None, ConfirmTicket=None, TTNInformBReg=None, ActInventory=None, ActChargeOn=None, ActInventoryInformBReg=None, QueryAP=None, QuerySSP=None, QuerySP=None, QueryClients=None, QueryClientVersion=None, QueryRests=None, QueryFormBHistory=None, QueryResendDoc=None, QueryFormA=None, QueryFormB=None, ActWriteOff=None, RepProducedProduct=None, RepImportedProduct=None, ReplySSP=None, ReplySpirit=None, ReplyClient=None, ReplyAP=None, ReplyRests=None, ReplyFormA=None, ReplyFormB=None, ReplyHistFormB=None, ReplyClientVersion=None, QueryRejectRepProduced=None, QueryRejectRepImported=None, ReplySSP_v2=None, ReplySpirit_v2=None, ReplyClient_v2=None, ReplyAP_v2=None, ReplyAP_v3=None, ReplyRests_v2=None, ReplyForm1=None, ReplyForm2=None, ReplyHistForm2=None, WayBill_v2=None, WayBillAct_v2=None, ActChargeOn_v2=None, ActInventoryInformF2Reg=None, TTNInformF2Reg=None, QueryAP_v2=None, QueryAP_v3=None, QuerySSP_v2=None, QuerySP_v2=None, QueryClients_v2=None, QueryRests_v2=None, QueryFormF1=None, QueryFormF2=None, ActWriteOff_v2=None, TransferFromShop=None, TransferToShop=None, QueryForm2History=None, RepInformF1Reg=None, ReplyNoAnswerTTN=None, QueryNATTN=None, QueryRestsShop_v2=None, ReplyRestsShop_v2=None, Asiiu=None, AsiiuTime=None, ActChargeOnShop_v2=None, ActWriteOffShop_v2=None, InfoVersionTTN=None, QueryBarcode=None, ReplyBarcode=None, RequestRepealWB=None, ConfirmRepealWB=None, RequestRepealACO=None, RequestRepealAWO=None, QueryRests_Mini=None, QueryRestsShop_Mini=None, ReplyRests_Mini=None, ReplyRestsShop_Mini=None, RequestAddFProducer=None, RequestAddProducts=None, QueryHistoryRestShop=None, QueryWriteOffCheque=None, ReplyHistoryShop=None, ReplyWriteOffCheque=None, AscpNav=None, AsiiuSign=None, AsiiuTimeSign=None, WayBill_v3=None, ActWriteOff_v3=None, WayBillAct_v3=None, RepProducedProduct_v3=None, RepImportedProduct_v3=None, QueryRestBCode=None, ReplyRestBCode=None, ActFixBarCode=None, ActUnFixBarCode=None, QueryParentHistForm2=None, ReplyParentHistForm2=None, TTNHistoryF2Reg=None, CarrierNotice=None, CarrierNotice_v4=None, ClaimIssueFSM=None, RequestManufacturerFSM=None, TTNShipmentFSM=None, TTNIssueFSM=None, RejectionNoticeFSM=None, ReturnNoticeFSM=None, RecheckNotificationsFSM=None, QueryPlaceOfBusiness=None, ReplyPlaceOfBusiness=None, QueryGenerationOpenKey=None, ReplyGenerationOpenKey=None, InvoiceIssueAM=None, InvoiceExportFSM=None, InvoicePlannedImport=None, NotificationsBeginningTurnover=None, ChequeV3=None, RepProducedProduct_v4=None, RepImportedProduct_v4=None, ReportDestructionAMFSM=None, RequestRepealIPI=None, RequestRepealEFSM=None, RequestRepealIAM=None, TTNShipmentReturnFSM=None, TTNIssueReturnFSM=None, ReferenceOfDeficiencies=None, ManufacturingNoticeFSM=None, WayBill_v4=None, WayBillAct_v4=None, Route=None, CancelRoute=None, DebtAbsence=None, RequestAdjustmentData=None, ActReceiptOnlineOrder=None, ActConfirmOnlineOrder=None, ActCancelOnlineOrder=None, RequestBalanceTransfer=None, RequestManufacturerFSMforCheck=None, TicketRMCheck=None, FrapClaims=None, FrapClaimsCor=None, ApplicationLicenses=None, RepProducedProduct_v5=None, ReturnNotificationsFSM=None, TTNInternalMoveFSM=None, ActWriteOff_v4=None, ChequeV4=None, RepProducedProduct_v6=None, RepImportedProduct_v5=None, **kwargs_):
        super(DocBodySub, self).__init__(WayBill, Ticket, WayBillAct, ConfirmTicket, TTNInformBReg, ActInventory, ActChargeOn, ActInventoryInformBReg, QueryAP, QuerySSP, QuerySP, QueryClients, QueryClientVersion, QueryRests, QueryFormBHistory, QueryResendDoc, QueryFormA, QueryFormB, ActWriteOff, RepProducedProduct, RepImportedProduct, ReplySSP, ReplySpirit, ReplyClient, ReplyAP, ReplyRests, ReplyFormA, ReplyFormB, ReplyHistFormB, ReplyClientVersion, QueryRejectRepProduced, QueryRejectRepImported, ReplySSP_v2, ReplySpirit_v2, ReplyClient_v2, ReplyAP_v2, ReplyAP_v3, ReplyRests_v2, ReplyForm1, ReplyForm2, ReplyHistForm2, WayBill_v2, WayBillAct_v2, ActChargeOn_v2, ActInventoryInformF2Reg, TTNInformF2Reg, QueryAP_v2, QueryAP_v3, QuerySSP_v2, QuerySP_v2, QueryClients_v2, QueryRests_v2, QueryFormF1, QueryFormF2, ActWriteOff_v2, TransferFromShop, TransferToShop, QueryForm2History, RepInformF1Reg, ReplyNoAnswerTTN, QueryNATTN, QueryRestsShop_v2, ReplyRestsShop_v2, Asiiu, AsiiuTime, ActChargeOnShop_v2, ActWriteOffShop_v2, InfoVersionTTN, QueryBarcode, ReplyBarcode, RequestRepealWB, ConfirmRepealWB, RequestRepealACO, RequestRepealAWO, QueryRests_Mini, QueryRestsShop_Mini, ReplyRests_Mini, ReplyRestsShop_Mini, RequestAddFProducer, RequestAddProducts, QueryHistoryRestShop, QueryWriteOffCheque, ReplyHistoryShop, ReplyWriteOffCheque, AscpNav, AsiiuSign, AsiiuTimeSign, WayBill_v3, ActWriteOff_v3, WayBillAct_v3, RepProducedProduct_v3, RepImportedProduct_v3, QueryRestBCode, ReplyRestBCode, ActFixBarCode, ActUnFixBarCode, QueryParentHistForm2, ReplyParentHistForm2, TTNHistoryF2Reg, CarrierNotice, CarrierNotice_v4, ClaimIssueFSM, RequestManufacturerFSM, TTNShipmentFSM, TTNIssueFSM, RejectionNoticeFSM, ReturnNoticeFSM, RecheckNotificationsFSM, QueryPlaceOfBusiness, ReplyPlaceOfBusiness, QueryGenerationOpenKey, ReplyGenerationOpenKey, InvoiceIssueAM, InvoiceExportFSM, InvoicePlannedImport, NotificationsBeginningTurnover, ChequeV3, RepProducedProduct_v4, RepImportedProduct_v4, ReportDestructionAMFSM, RequestRepealIPI, RequestRepealEFSM, RequestRepealIAM, TTNShipmentReturnFSM, TTNIssueReturnFSM, ReferenceOfDeficiencies, ManufacturingNoticeFSM, WayBill_v4, WayBillAct_v4, Route, CancelRoute, DebtAbsence, RequestAdjustmentData, ActReceiptOnlineOrder, ActConfirmOnlineOrder, ActCancelOnlineOrder, RequestBalanceTransfer, RequestManufacturerFSMforCheck, TicketRMCheck, FrapClaims, FrapClaimsCor, ApplicationLicenses, RepProducedProduct_v5, ReturnNotificationsFSM, TTNInternalMoveFSM, ActWriteOff_v4, ChequeV4, RepProducedProduct_v6, RepImportedProduct_v5,  **kwargs_)
supermod.DocBody.subclass = DocBodySub
# end class DocBodySub


class SenderInfoSub(supermod.SenderInfo):
    def __init__(self, FSRAR_ID=None, **kwargs_):
        super(SenderInfoSub, self).__init__(FSRAR_ID,  **kwargs_)
supermod.SenderInfo.subclass = SenderInfoSub
# end class SenderInfoSub


class MarkCodeInfoTypeSub(supermod.MarkCodeInfoType):
    def __init__(self, MarkCode=None, **kwargs_):
        super(MarkCodeInfoTypeSub, self).__init__(MarkCode,  **kwargs_)
supermod.MarkCodeInfoType.subclass = MarkCodeInfoTypeSub
# end class MarkCodeInfoTypeSub


class AMCforDocTypeSub(supermod.AMCforDocType):
    def __init__(self, amc=None, ms=None, **kwargs_):
        super(AMCforDocTypeSub, self).__init__(amc, ms,  **kwargs_)
supermod.AMCforDocType.subclass = AMCforDocTypeSub
# end class AMCforDocTypeSub


class boxtypeSub(supermod.boxtype):
    def __init__(self, bl=None, boxnum=None, **kwargs_):
        super(boxtypeSub, self).__init__(bl, boxnum,  **kwargs_)
supermod.boxtype.subclass = boxtypeSub
# end class boxtypeSub


class bktypeSub(supermod.bktype):
    def __init__(self, bk=None, **kwargs_):
        super(bktypeSub, self).__init__(bk,  **kwargs_)
supermod.bktype.subclass = bktypeSub
# end class bktypeSub


class boxamcTypeSub(supermod.boxamcType):
    def __init__(self, boxnumber=None, amclist=None, **kwargs_):
        super(boxamcTypeSub, self).__init__(boxnumber, amclist,  **kwargs_)
supermod.boxamcType.subclass = boxamcTypeSub
# end class boxamcTypeSub


class MarkInfoTypeBCSub(supermod.MarkInfoTypeBC):
    def __init__(self, boxpos=None, **kwargs_):
        super(MarkInfoTypeBCSub, self).__init__(boxpos,  **kwargs_)
supermod.MarkInfoTypeBC.subclass = MarkInfoTypeBCSub
# end class MarkInfoTypeBCSub


class InformF2TypeItemBCSub(supermod.InformF2TypeItemBC):
    def __init__(self, F2RegId='FIRSTSHIPMENT', MarkInfo=None, **kwargs_):
        super(InformF2TypeItemBCSub, self).__init__(F2RegId, MarkInfo,  **kwargs_)
supermod.InformF2TypeItemBC.subclass = InformF2TypeItemBCSub
# end class InformF2TypeItemBCSub


class OrganizationsTypeSub(supermod.OrganizationsType):
    def __init__(self, Organization=None, **kwargs_):
        super(OrganizationsTypeSub, self).__init__(Organization,  **kwargs_)
supermod.OrganizationsType.subclass = OrganizationsTypeSub
# end class OrganizationsTypeSub


class OrgInfoSub(supermod.OrgInfo):
    def __init__(self, Identity=None, ClientRegId=None, FullName=None, ShortName=None, INN=None, KPP=None, UNP=None, RNN=None, address=None, **kwargs_):
        super(OrgInfoSub, self).__init__(Identity, ClientRegId, FullName, ShortName, INN, KPP, UNP, RNN, address,  **kwargs_)
supermod.OrgInfo.subclass = OrgInfoSub
# end class OrgInfoSub


class OrgInfoExSub(supermod.OrgInfoEx):
    def __init__(self, Identity=None, ClientRegId=None, FullName=None, ShortName=None, INN=None, KPP=None, UNP=None, RNN=None, address=None, addresslist=None, State=None, **kwargs_):
        super(OrgInfoExSub, self).__init__(Identity, ClientRegId, FullName, ShortName, INN, KPP, UNP, RNN, address, addresslist, State,  **kwargs_)
supermod.OrgInfoEx.subclass = OrgInfoExSub
# end class OrgInfoExSub


class OrgItemTypeSub(supermod.OrgItemType):
    def __init__(self, ID=None, **kwargs_):
        super(OrgItemTypeSub, self).__init__(ID,  **kwargs_)
supermod.OrgItemType.subclass = OrgItemTypeSub
# end class OrgItemTypeSub


class OrgAddressTypeSub(supermod.OrgAddressType):
    def __init__(self, Country=None, Index=None, RegionCode=None, area=None, city=None, place=None, street=None, house=None, building=None, liter=None, description=None, **kwargs_):
        super(OrgAddressTypeSub, self).__init__(Country, Index, RegionCode, area, city, place, street, house, building, liter, description,  **kwargs_)
supermod.OrgAddressType.subclass = OrgAddressTypeSub
# end class OrgAddressTypeSub


class OrgLicenseTypeSub(supermod.OrgLicenseType):
    def __init__(self, number=None, datefrom=None, dateto=None, orgdistribute=None, **kwargs_):
        super(OrgLicenseTypeSub, self).__init__(number, datefrom, dateto, orgdistribute,  **kwargs_)
supermod.OrgLicenseType.subclass = OrgLicenseTypeSub
# end class OrgLicenseTypeSub


class ProductContractTypeSub(supermod.ProductContractType):
    def __init__(self, number=None, date=None, Supplier=None, Contragent=None, **kwargs_):
        super(ProductContractTypeSub, self).__init__(number, date, Supplier, Contragent,  **kwargs_)
supermod.ProductContractType.subclass = ProductContractTypeSub
# end class ProductContractTypeSub


class ProductsTypeSub(supermod.ProductsType):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsTypeSub, self).__init__(Product,  **kwargs_)
supermod.ProductsType.subclass = ProductsTypeSub
# end class ProductsTypeSub


class ProductInfoSub(supermod.ProductInfo):
    def __init__(self, Identity=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, Producer=None, Importer=None, ProductVCode=None, **kwargs_):
        super(ProductInfoSub, self).__init__(Identity, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, Producer, Importer, ProductVCode,  **kwargs_)
supermod.ProductInfo.subclass = ProductInfoSub
# end class ProductInfoSub


class InformATypeSub(supermod.InformAType):
    def __init__(self, RegId=None, **kwargs_):
        super(InformATypeSub, self).__init__(RegId,  **kwargs_)
supermod.InformAType.subclass = InformATypeSub
# end class InformATypeSub


class InformBTypeSub(supermod.InformBType):
    def __init__(self, InformBItem=None, **kwargs_):
        super(InformBTypeSub, self).__init__(InformBItem,  **kwargs_)
supermod.InformBType.subclass = InformBTypeSub
# end class InformBTypeSub


class InformBTypeItemSub(supermod.InformBTypeItem):
    def __init__(self, BRegId=None, MarkInfo=None, **kwargs_):
        super(InformBTypeItemSub, self).__init__(BRegId, MarkInfo,  **kwargs_)
supermod.InformBTypeItem.subclass = InformBTypeItemSub
# end class InformBTypeItemSub


class MarkInfoTypeSub(supermod.MarkInfoType):
    def __init__(self, Type=None, Ranges=None, **kwargs_):
        super(MarkInfoTypeSub, self).__init__(Type, Ranges,  **kwargs_)
supermod.MarkInfoType.subclass = MarkInfoTypeSub
# end class MarkInfoTypeSub


class WayBillTypeSub(supermod.WayBillType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillType.subclass = WayBillTypeSub
# end class WayBillTypeSub


class PositionTypeSub(supermod.PositionType):
    def __init__(self, Product=None, Pack_ID=None, Quantity=None, Price=None, Party=None, Identity=None, InformA=None, InformB=None, **kwargs_):
        super(PositionTypeSub, self).__init__(Product, Pack_ID, Quantity, Price, Party, Identity, InformA, InformB,  **kwargs_)
supermod.PositionType.subclass = PositionTypeSub
# end class PositionTypeSub


class TransportTypeSub(supermod.TransportType):
    def __init__(self, TRAN_TYPE=None, TRAN_COMPANY=None, TRAN_CAR=None, TRAN_TRAILER=None, TRAN_CUSTOMER=None, TRAN_DRIVER=None, TRAN_LOADPOINT=None, TRAN_UNLOADPOINT=None, TRAN_REDIRECT=None, TRAN_FORWARDER=None, **kwargs_):
        super(TransportTypeSub, self).__init__(TRAN_TYPE, TRAN_COMPANY, TRAN_CAR, TRAN_TRAILER, TRAN_CUSTOMER, TRAN_DRIVER, TRAN_LOADPOINT, TRAN_UNLOADPOINT, TRAN_REDIRECT, TRAN_FORWARDER,  **kwargs_)
supermod.TransportType.subclass = TransportTypeSub
# end class TransportTypeSub


class TicketTypeSub(supermod.TicketType):
    def __init__(self, TicketDate=None, Identity=None, DocId=None, TransportId=None, RegID=None, DocHash=None, DocType=None, Result=None, OperationResult=None, **kwargs_):
        super(TicketTypeSub, self).__init__(TicketDate, Identity, DocId, TransportId, RegID, DocHash, DocType, Result, OperationResult,  **kwargs_)
supermod.TicketType.subclass = TicketTypeSub
# end class TicketTypeSub


class OperationResultTypeSub(supermod.OperationResultType):
    def __init__(self, OperationName=None, OperationResult=None, OperationComment=None, OperationDate=None, **kwargs_):
        super(OperationResultTypeSub, self).__init__(OperationName, OperationResult, OperationComment, OperationDate,  **kwargs_)
supermod.OperationResultType.subclass = OperationResultTypeSub
# end class OperationResultTypeSub


class TicketResultTypeSub(supermod.TicketResultType):
    def __init__(self, Conclusion=None, ConclusionDate=None, Comments=None, **kwargs_):
        super(TicketResultTypeSub, self).__init__(Conclusion, ConclusionDate, Comments,  **kwargs_)
supermod.TicketResultType.subclass = TicketResultTypeSub
# end class TicketResultTypeSub


class WayBillActTypeSub(supermod.WayBillActType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillActTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillActType.subclass = WayBillActTypeSub
# end class WayBillActTypeSub


class PositionType2Sub(supermod.PositionType2):
    def __init__(self, Identity=None, InformBRegId=None, RealQuantity=None, **kwargs_):
        super(PositionType2Sub, self).__init__(Identity, InformBRegId, RealQuantity,  **kwargs_)
supermod.PositionType2.subclass = PositionType2Sub
# end class PositionType2Sub


class ConfirmTicketTypeSub(supermod.ConfirmTicketType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(ConfirmTicketTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.ConfirmTicketType.subclass = ConfirmTicketTypeSub
# end class ConfirmTicketTypeSub


class ActInventoryTypeSub(supermod.ActInventoryType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActInventoryTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActInventoryType.subclass = ActInventoryTypeSub
# end class ActInventoryTypeSub


class ActInventoryPositionTypeSub(supermod.ActInventoryPositionType):
    def __init__(self, Identity=None, Product=None, Quantity=None, InformA=None, InformB=None, **kwargs_):
        super(ActInventoryPositionTypeSub, self).__init__(Identity, Product, Quantity, InformA, InformB,  **kwargs_)
supermod.ActInventoryPositionType.subclass = ActInventoryPositionTypeSub
# end class ActInventoryPositionTypeSub


class InformBTypeRegItemSub(supermod.InformBTypeRegItem):
    def __init__(self, Identity=None, TTNNumber=None, TTNDate=None, Quantity=None, **kwargs_):
        super(InformBTypeRegItemSub, self).__init__(Identity, TTNNumber, TTNDate, Quantity,  **kwargs_)
supermod.InformBTypeRegItem.subclass = InformBTypeRegItemSub
# end class InformBTypeRegItemSub


class InformARegTypeSub(supermod.InformARegType):
    def __init__(self, Quantity=None, BottlingDate=None, TTNNumber=None, TTNDate=None, EGAISFixNumber=None, EGAISFixDate=None, **kwargs_):
        super(InformARegTypeSub, self).__init__(Quantity, BottlingDate, TTNNumber, TTNDate, EGAISFixNumber, EGAISFixDate,  **kwargs_)
supermod.InformARegType.subclass = InformARegTypeSub
# end class InformARegTypeSub


class ActChargeOnTypeSub(supermod.ActChargeOnType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActChargeOnTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActChargeOnType.subclass = ActChargeOnTypeSub
# end class ActChargeOnTypeSub


class ActChargeOnPositionTypeSub(supermod.ActChargeOnPositionType):
    def __init__(self, Identity=None, Product=None, Quantity=None, InformAB=None, MarkCodeInfo=None, **kwargs_):
        super(ActChargeOnPositionTypeSub, self).__init__(Identity, Product, Quantity, InformAB, MarkCodeInfo,  **kwargs_)
supermod.ActChargeOnPositionType.subclass = ActChargeOnPositionTypeSub
# end class ActChargeOnPositionTypeSub


class MarkCodeInfoType4Sub(supermod.MarkCodeInfoType4):
    def __init__(self, MarkCode=None, **kwargs_):
        super(MarkCodeInfoType4Sub, self).__init__(MarkCode,  **kwargs_)
supermod.MarkCodeInfoType4.subclass = MarkCodeInfoType4Sub
# end class MarkCodeInfoType4Sub


class InformABKeyTypeSub(supermod.InformABKeyType):
    def __init__(self, FormA=None, LastFormB=None, **kwargs_):
        super(InformABKeyTypeSub, self).__init__(FormA, LastFormB,  **kwargs_)
supermod.InformABKeyType.subclass = InformABKeyTypeSub
# end class InformABKeyTypeSub


class InformABRegTypeSub(supermod.InformABRegType):
    def __init__(self, InformA=None, **kwargs_):
        super(InformABRegTypeSub, self).__init__(InformA,  **kwargs_)
supermod.InformABRegType.subclass = InformABRegTypeSub
# end class InformABRegTypeSub


class ActInventoryInformBRegSub(supermod.ActInventoryInformBReg):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(ActInventoryInformBRegSub, self).__init__(Header, Content,  **kwargs_)
supermod.ActInventoryInformBReg.subclass = ActInventoryInformBRegSub
# end class ActInventoryInformBRegSub


class InformInvPositionTypeSub(supermod.InformInvPositionType):
    def __init__(self, Identity=None, InformARegId=None, InformB=None, **kwargs_):
        super(InformInvPositionTypeSub, self).__init__(Identity, InformARegId, InformB,  **kwargs_)
supermod.InformInvPositionType.subclass = InformInvPositionTypeSub
# end class InformInvPositionTypeSub


class InformInvBRegItemSub(supermod.InformInvBRegItem):
    def __init__(self, Identity=None, BRegId=None, MarkInfo=None, **kwargs_):
        super(InformInvBRegItemSub, self).__init__(Identity, BRegId, MarkInfo,  **kwargs_)
supermod.InformInvBRegItem.subclass = InformInvBRegItemSub
# end class InformInvBRegItemSub


class QueryParametersSub(supermod.QueryParameters):
    def __init__(self, Parameters=None, **kwargs_):
        super(QueryParametersSub, self).__init__(Parameters,  **kwargs_)
supermod.QueryParameters.subclass = QueryParametersSub
# end class QueryParametersSub


class ParameterSub(supermod.Parameter):
    def __init__(self, Name=None, Value=None, **kwargs_):
        super(ParameterSub, self).__init__(Name, Value,  **kwargs_)
supermod.Parameter.subclass = ParameterSub
# end class ParameterSub


class QueryFormABSub(supermod.QueryFormAB):
    def __init__(self, FormRegId=None, **kwargs_):
        super(QueryFormABSub, self).__init__(FormRegId,  **kwargs_)
supermod.QueryFormAB.subclass = QueryFormABSub
# end class QueryFormABSub


class WayBillInformBRegTypeSub(supermod.WayBillInformBRegType):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(WayBillInformBRegTypeSub, self).__init__(Header, Content,  **kwargs_)
supermod.WayBillInformBRegType.subclass = WayBillInformBRegTypeSub
# end class WayBillInformBRegTypeSub


class InformBPositionTypeSub(supermod.InformBPositionType):
    def __init__(self, Identity=None, InformBRegId=None, **kwargs_):
        super(InformBPositionTypeSub, self).__init__(Identity, InformBRegId,  **kwargs_)
supermod.InformBPositionType.subclass = InformBPositionTypeSub
# end class InformBPositionTypeSub


class ActWriteOffTypeSub(supermod.ActWriteOffType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActWriteOffTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActWriteOffType.subclass = ActWriteOffTypeSub
# end class ActWriteOffTypeSub


class ActWriteOffPositionTypeSub(supermod.ActWriteOffPositionType):
    def __init__(self, Identity=None, Quantity=None, InformB=None, **kwargs_):
        super(ActWriteOffPositionTypeSub, self).__init__(Identity, Quantity, InformB,  **kwargs_)
supermod.ActWriteOffPositionType.subclass = ActWriteOffPositionTypeSub
# end class ActWriteOffPositionTypeSub


class RepProducedTypeSub(supermod.RepProducedType):
    def __init__(self, Identity=None, Header=None, Content=None, ContentResource=None, **kwargs_):
        super(RepProducedTypeSub, self).__init__(Identity, Header, Content, ContentResource,  **kwargs_)
supermod.RepProducedType.subclass = RepProducedTypeSub
# end class RepProducedTypeSub


class PositionType6Sub(supermod.PositionType6):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType6Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType6.subclass = PositionType6Sub
# end class PositionType6Sub


class UsedResourceTypeSub(supermod.UsedResourceType):
    def __init__(self, IdentityRes=None, Product=None, RegForm2=None, Quantity=None, **kwargs_):
        super(UsedResourceTypeSub, self).__init__(IdentityRes, Product, RegForm2, Quantity,  **kwargs_)
supermod.UsedResourceType.subclass = UsedResourceTypeSub
# end class UsedResourceTypeSub


class OrganizationsType7Sub(supermod.OrganizationsType7):
    def __init__(self, Organization=None, **kwargs_):
        super(OrganizationsType7Sub, self).__init__(Organization,  **kwargs_)
supermod.OrganizationsType7.subclass = OrganizationsType7Sub
# end class OrganizationsType7Sub


class OrgInfoEx_v2Sub(supermod.OrgInfoEx_v2):
    def __init__(self, Identity=None, OrgInfoV2=None, addresslist=None, State=None, VersionWB=None, isLicense=None, **kwargs_):
        super(OrgInfoEx_v2Sub, self).__init__(Identity, OrgInfoV2, addresslist, State, VersionWB, isLicense,  **kwargs_)
supermod.OrgInfoEx_v2.subclass = OrgInfoEx_v2Sub
# end class OrgInfoEx_v2Sub


class OrgItemType8Sub(supermod.OrgItemType8):
    def __init__(self, ID=None, **kwargs_):
        super(OrgItemType8Sub, self).__init__(ID,  **kwargs_)
supermod.OrgItemType8.subclass = OrgItemType8Sub
# end class OrgItemType8Sub


class OrgAddressType9Sub(supermod.OrgAddressType9):
    def __init__(self, Country=None, Index=None, RegionCode=None, area=None, city=None, place=None, street=None, house=None, building=None, liter=None, description=None, **kwargs_):
        super(OrgAddressType9Sub, self).__init__(Country, Index, RegionCode, area, city, place, street, house, building, liter, description,  **kwargs_)
supermod.OrgAddressType9.subclass = OrgAddressType9Sub
# end class OrgAddressType9Sub


class ProductContractType10Sub(supermod.ProductContractType10):
    def __init__(self, number=None, date=None, Supplier=None, Contragent=None, **kwargs_):
        super(ProductContractType10Sub, self).__init__(number, date, Supplier, Contragent,  **kwargs_)
supermod.ProductContractType10.subclass = ProductContractType10Sub
# end class ProductContractType10Sub


class OrgInfo_v2Sub(supermod.OrgInfo_v2):
    def __init__(self, UL=None, FL=None, FO=None, TS=None, **kwargs_):
        super(OrgInfo_v2Sub, self).__init__(UL, FL, FO, TS,  **kwargs_)
supermod.OrgInfo_v2.subclass = OrgInfo_v2Sub
# end class OrgInfo_v2Sub


class OrgInfoReply_v2Sub(supermod.OrgInfoReply_v2):
    def __init__(self, UL=None, FL=None, FO=None, TS=None, **kwargs_):
        super(OrgInfoReply_v2Sub, self).__init__(UL, FL, FO, TS,  **kwargs_)
supermod.OrgInfoReply_v2.subclass = OrgInfoReply_v2Sub
# end class OrgInfoReply_v2Sub


class OrgInfoRus_v2Sub(supermod.OrgInfoRus_v2):
    def __init__(self, UL=None, FL=None, TR=None, **kwargs_):
        super(OrgInfoRus_v2Sub, self).__init__(UL, FL, TR,  **kwargs_)
supermod.OrgInfoRus_v2.subclass = OrgInfoRus_v2Sub
# end class OrgInfoRus_v2Sub


class OrgInfoRus_v2_ClaimFrapSub(supermod.OrgInfoRus_v2_ClaimFrap):
    def __init__(self, UL=None, FL=None, **kwargs_):
        super(OrgInfoRus_v2_ClaimFrapSub, self).__init__(UL, FL,  **kwargs_)
supermod.OrgInfoRus_v2_ClaimFrap.subclass = OrgInfoRus_v2_ClaimFrapSub
# end class OrgInfoRus_v2_ClaimFrapSub


class OrgInfoRus_ClaimIssueSub(supermod.OrgInfoRus_ClaimIssue):
    def __init__(self, UL=None, FL=None, **kwargs_):
        super(OrgInfoRus_ClaimIssueSub, self).__init__(UL, FL,  **kwargs_)
supermod.OrgInfoRus_ClaimIssue.subclass = OrgInfoRus_ClaimIssueSub
# end class OrgInfoRus_ClaimIssueSub


class OrgInfoRusReply_v2Sub(supermod.OrgInfoRusReply_v2):
    def __init__(self, UL=None, FL=None, **kwargs_):
        super(OrgInfoRusReply_v2Sub, self).__init__(UL, FL,  **kwargs_)
supermod.OrgInfoRusReply_v2.subclass = OrgInfoRusReply_v2Sub
# end class OrgInfoRusReply_v2Sub


class OrgInfoForeign_v2Sub(supermod.OrgInfoForeign_v2):
    def __init__(self, FO=None, TS=None, **kwargs_):
        super(OrgInfoForeign_v2Sub, self).__init__(FO, TS,  **kwargs_)
supermod.OrgInfoForeign_v2.subclass = OrgInfoForeign_v2Sub
# end class OrgInfoForeign_v2Sub


class OrgInfoForeignReply_v2Sub(supermod.OrgInfoForeignReply_v2):
    def __init__(self, FO=None, TS=None, **kwargs_):
        super(OrgInfoForeignReply_v2Sub, self).__init__(FO, TS,  **kwargs_)
supermod.OrgInfoForeignReply_v2.subclass = OrgInfoForeignReply_v2Sub
# end class OrgInfoForeignReply_v2Sub


class ULTypeSub(supermod.ULType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, INN=None, KPP=None, address=None, **kwargs_):
        super(ULTypeSub, self).__init__(ClientRegId, FullName, ShortName, INN, KPP, address,  **kwargs_)
supermod.ULType.subclass = ULTypeSub
# end class ULTypeSub


class ULType_ClaimIssueSub(supermod.ULType_ClaimIssue):
    def __init__(self, ClientRegId=None, FullName=None, INN=None, KPP=None, address_ur=None, address=None, **kwargs_):
        super(ULType_ClaimIssueSub, self).__init__(ClientRegId, FullName, INN, KPP, address_ur, address,  **kwargs_)
supermod.ULType_ClaimIssue.subclass = ULType_ClaimIssueSub
# end class ULType_ClaimIssueSub


class ULReplyTypeSub(supermod.ULReplyType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, INN=None, KPP=None, address=None, **kwargs_):
        super(ULReplyTypeSub, self).__init__(ClientRegId, FullName, ShortName, INN, KPP, address,  **kwargs_)
supermod.ULReplyType.subclass = ULReplyTypeSub
# end class ULReplyTypeSub


class FLTypeSub(supermod.FLType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, INN=None, address=None, **kwargs_):
        super(FLTypeSub, self).__init__(ClientRegId, FullName, ShortName, INN, address,  **kwargs_)
supermod.FLType.subclass = FLTypeSub
# end class FLTypeSub


class FLType_ClaimIssueSub(supermod.FLType_ClaimIssue):
    def __init__(self, ClientRegId=None, FullName=None, INN=None, address_ur=None, address=None, **kwargs_):
        super(FLType_ClaimIssueSub, self).__init__(ClientRegId, FullName, INN, address_ur, address,  **kwargs_)
supermod.FLType_ClaimIssue.subclass = FLType_ClaimIssueSub
# end class FLType_ClaimIssueSub


class FLReplyTypeSub(supermod.FLReplyType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, INN=None, address=None, **kwargs_):
        super(FLReplyTypeSub, self).__init__(ClientRegId, FullName, ShortName, INN, address,  **kwargs_)
supermod.FLReplyType.subclass = FLReplyTypeSub
# end class FLReplyTypeSub


class FOTypeSub(supermod.FOType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, address=None, **kwargs_):
        super(FOTypeSub, self).__init__(ClientRegId, FullName, ShortName, address,  **kwargs_)
supermod.FOType.subclass = FOTypeSub
# end class FOTypeSub


class TSTypeSub(supermod.TSType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, TSNUM=None, address=None, **kwargs_):
        super(TSTypeSub, self).__init__(ClientRegId, FullName, ShortName, TSNUM, address,  **kwargs_)
supermod.TSType.subclass = TSTypeSub
# end class TSTypeSub


class TRTypeSub(supermod.TRType):
    def __init__(self, ClientRegId=None, address=None, **kwargs_):
        super(TRTypeSub, self).__init__(ClientRegId, address,  **kwargs_)
supermod.TRType.subclass = TRTypeSub
# end class TRTypeSub


class TSReplyTypeSub(supermod.TSReplyType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, TSNUM=None, address=None, **kwargs_):
        super(TSReplyTypeSub, self).__init__(ClientRegId, FullName, ShortName, TSNUM, address,  **kwargs_)
supermod.TSReplyType.subclass = TSReplyTypeSub
# end class TSReplyTypeSub


class OrgAddressTypeULFLSub(supermod.OrgAddressTypeULFL):
    def __init__(self, Country=None, RegionCode=None, description=None, **kwargs_):
        super(OrgAddressTypeULFLSub, self).__init__(Country, RegionCode, description,  **kwargs_)
supermod.OrgAddressTypeULFL.subclass = OrgAddressTypeULFLSub
# end class OrgAddressTypeULFLSub


class OrgUrAddressTypeULFLSub(supermod.OrgUrAddressTypeULFL):
    def __init__(self, Country=None, RegionCode=None, description=None, **kwargs_):
        super(OrgUrAddressTypeULFLSub, self).__init__(Country, RegionCode, description,  **kwargs_)
supermod.OrgUrAddressTypeULFL.subclass = OrgUrAddressTypeULFLSub
# end class OrgUrAddressTypeULFLSub


class OrgAddressTypeULFLReplySub(supermod.OrgAddressTypeULFLReply):
    def __init__(self, Country=None, RegionCode=None, description=None, **kwargs_):
        super(OrgAddressTypeULFLReplySub, self).__init__(Country, RegionCode, description,  **kwargs_)
supermod.OrgAddressTypeULFLReply.subclass = OrgAddressTypeULFLReplySub
# end class OrgAddressTypeULFLReplySub


class OrgAddressTypeFOTSSub(supermod.OrgAddressTypeFOTS):
    def __init__(self, Country=None, description=None, **kwargs_):
        super(OrgAddressTypeFOTSSub, self).__init__(Country, description,  **kwargs_)
supermod.OrgAddressTypeFOTS.subclass = OrgAddressTypeFOTSSub
# end class OrgAddressTypeFOTSSub


class OrgAddressTypeTRSub(supermod.OrgAddressTypeTR):
    def __init__(self, description=None, **kwargs_):
        super(OrgAddressTypeTRSub, self).__init__(description,  **kwargs_)
supermod.OrgAddressTypeTR.subclass = OrgAddressTypeTRSub
# end class OrgAddressTypeTRSub


class ReplyPlaceOfBusinessTypeSub(supermod.ReplyPlaceOfBusinessType):
    def __init__(self, ClientRegId=None, INN=None, KPP=None, RegNumberTS=None, address=None, **kwargs_):
        super(ReplyPlaceOfBusinessTypeSub, self).__init__(ClientRegId, INN, KPP, RegNumberTS, address,  **kwargs_)
supermod.ReplyPlaceOfBusinessType.subclass = ReplyPlaceOfBusinessTypeSub
# end class ReplyPlaceOfBusinessTypeSub


class ProductsType_v2Sub(supermod.ProductsType_v2):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType_v2Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType_v2.subclass = ProductsType_v2Sub
# end class ProductsType_v2Sub


class MarkInfoType15Sub(supermod.MarkInfoType15):
    def __init__(self, Type=None, Ranges=None, **kwargs_):
        super(MarkInfoType15Sub, self).__init__(Type, Ranges,  **kwargs_)
supermod.MarkInfoType15.subclass = MarkInfoType15Sub
# end class MarkInfoType15Sub


class ProductInfoTest_v2Sub(supermod.ProductInfoTest_v2):
    def __init__(self, Domestic=None, Foreign=None, **kwargs_):
        super(ProductInfoTest_v2Sub, self).__init__(Domestic, Foreign,  **kwargs_)
supermod.ProductInfoTest_v2.subclass = ProductInfoTest_v2Sub
# end class ProductInfoTest_v2Sub


class ProductInfo_v2Sub(supermod.ProductInfo_v2):
    def __init__(self, UnitType=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, Producer=None, ProductVCode=None, **kwargs_):
        super(ProductInfo_v2Sub, self).__init__(UnitType, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, Producer, ProductVCode,  **kwargs_)
supermod.ProductInfo_v2.subclass = ProductInfo_v2Sub
# end class ProductInfo_v2Sub


class ProductInfoReply_v2Sub(supermod.ProductInfoReply_v2):
    def __init__(self, UnitType=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, Producer=None, ProductVCode=None, **kwargs_):
        super(ProductInfoReply_v2Sub, self).__init__(UnitType, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, Producer, ProductVCode,  **kwargs_)
supermod.ProductInfoReply_v2.subclass = ProductInfoReply_v2Sub
# end class ProductInfoReply_v2Sub


class ProductInfoReply_v3Sub(supermod.ProductInfoReply_v3):
    def __init__(self, UnitType=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, Producer=None, ProductVCode=None, Package_Type_Code=None, **kwargs_):
        super(ProductInfoReply_v3Sub, self).__init__(UnitType, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, Producer, ProductVCode, Package_Type_Code,  **kwargs_)
supermod.ProductInfoReply_v3.subclass = ProductInfoReply_v3Sub
# end class ProductInfoReply_v3Sub


class ProductInfoRus_v2Sub(supermod.ProductInfoRus_v2):
    def __init__(self, UnitType=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, Producer=None, ProductVCode=None, **kwargs_):
        super(ProductInfoRus_v2Sub, self).__init__(UnitType, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, Producer, ProductVCode,  **kwargs_)
supermod.ProductInfoRus_v2.subclass = ProductInfoRus_v2Sub
# end class ProductInfoRus_v2Sub


class ProductInfoForeign_v2Sub(supermod.ProductInfoForeign_v2):
    def __init__(self, UnitType=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, Producer=None, Importer=None, ProductVCode=None, **kwargs_):
        super(ProductInfoForeign_v2Sub, self).__init__(UnitType, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, Producer, Importer, ProductVCode,  **kwargs_)
supermod.ProductInfoForeign_v2.subclass = ProductInfoForeign_v2Sub
# end class ProductInfoForeign_v2Sub


class ProductInfoAsiiu_v2Sub(supermod.ProductInfoAsiiu_v2):
    def __init__(self, UnitType=None, Type=None, FullName=None, ShortName=None, AlcCode=None, Capacity=None, AlcVolume=None, ProductVCode=None, **kwargs_):
        super(ProductInfoAsiiu_v2Sub, self).__init__(UnitType, Type, FullName, ShortName, AlcCode, Capacity, AlcVolume, ProductVCode,  **kwargs_)
supermod.ProductInfoAsiiu_v2.subclass = ProductInfoAsiiu_v2Sub
# end class ProductInfoAsiiu_v2Sub


class InformF1TypeSub(supermod.InformF1Type):
    def __init__(self, RegId=None, MarkInfo=None, **kwargs_):
        super(InformF1TypeSub, self).__init__(RegId, MarkInfo,  **kwargs_)
supermod.InformF1Type.subclass = InformF1TypeSub
# end class InformF1TypeSub


class InformF2TypeSub(supermod.InformF2Type):
    def __init__(self, InformF2Item=None, **kwargs_):
        super(InformF2TypeSub, self).__init__(InformF2Item,  **kwargs_)
supermod.InformF2Type.subclass = InformF2TypeSub
# end class InformF2TypeSub


class InformF2TypeItemSub(supermod.InformF2TypeItem):
    def __init__(self, F2RegId='FIRSTSHIPMENT', MarkInfo=None, **kwargs_):
        super(InformF2TypeItemSub, self).__init__(F2RegId, MarkInfo,  **kwargs_)
supermod.InformF2TypeItem.subclass = InformF2TypeItemSub
# end class InformF2TypeItemSub


class RepImportedTypeSub(supermod.RepImportedType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RepImportedTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RepImportedType.subclass = RepImportedTypeSub
# end class RepImportedTypeSub


class PositionType20Sub(supermod.PositionType20):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType20Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType20.subclass = PositionType20Sub
# end class PositionType20Sub


class ReplySSPSub(supermod.ReplySSP):
    def __init__(self, Products=None, **kwargs_):
        super(ReplySSPSub, self).__init__(Products,  **kwargs_)
supermod.ReplySSP.subclass = ReplySSPSub
# end class ReplySSPSub


class ReplySpiritSub(supermod.ReplySpirit):
    def __init__(self, Products=None, **kwargs_):
        super(ReplySpiritSub, self).__init__(Products,  **kwargs_)
supermod.ReplySpirit.subclass = ReplySpiritSub
# end class ReplySpiritSub


class ReplyClientSub(supermod.ReplyClient):
    def __init__(self, Clients=None, **kwargs_):
        super(ReplyClientSub, self).__init__(Clients,  **kwargs_)
supermod.ReplyClient.subclass = ReplyClientSub
# end class ReplyClientSub


class ReplyAPSub(supermod.ReplyAP):
    def __init__(self, Products=None, **kwargs_):
        super(ReplyAPSub, self).__init__(Products,  **kwargs_)
supermod.ReplyAP.subclass = ReplyAPSub
# end class ReplyAPSub


class ReplyRestsSub(supermod.ReplyRests):
    def __init__(self, RestsDate=None, Products=None, **kwargs_):
        super(ReplyRestsSub, self).__init__(RestsDate, Products,  **kwargs_)
supermod.ReplyRests.subclass = ReplyRestsSub
# end class ReplyRestsSub


class StockPositionTypeSub(supermod.StockPositionType):
    def __init__(self, Product=None, Quantity=None, InformARegId=None, InformBRegId=None, **kwargs_):
        super(StockPositionTypeSub, self).__init__(Product, Quantity, InformARegId, InformBRegId,  **kwargs_)
supermod.StockPositionType.subclass = StockPositionTypeSub
# end class StockPositionTypeSub


class ReplyFormASub(supermod.ReplyFormA):
    def __init__(self, InformARegId=None, TTNNumber=None, TTNDate=None, Shipper=None, Consignee=None, ShippingDate=None, Product=None, BottlingDate=None, Quantity=None, EGAISNumber=None, EGAISDate=None, MarkInfo=None, **kwargs_):
        super(ReplyFormASub, self).__init__(InformARegId, TTNNumber, TTNDate, Shipper, Consignee, ShippingDate, Product, BottlingDate, Quantity, EGAISNumber, EGAISDate, MarkInfo,  **kwargs_)
supermod.ReplyFormA.subclass = ReplyFormASub
# end class ReplyFormASub


class ReplyFormBSub(supermod.ReplyFormB):
    def __init__(self, InformBRegId=None, TTNNumber=None, TTNDate=None, Shipper=None, Consignee=None, ShippingDate=None, Product=None, Quantity=None, ExciseRate=None, MarkInfo=None, **kwargs_):
        super(ReplyFormBSub, self).__init__(InformBRegId, TTNNumber, TTNDate, Shipper, Consignee, ShippingDate, Product, Quantity, ExciseRate, MarkInfo,  **kwargs_)
supermod.ReplyFormB.subclass = ReplyFormBSub
# end class ReplyFormBSub


class ReplyHistFormBSub(supermod.ReplyHistFormB):
    def __init__(self, InformBRegId=None, HistFormBDate=None, HistoryB=None, **kwargs_):
        super(ReplyHistFormBSub, self).__init__(InformBRegId, HistFormBDate, HistoryB,  **kwargs_)
supermod.ReplyHistFormB.subclass = ReplyHistFormBSub
# end class ReplyHistFormBSub


class OperationBTypeSub(supermod.OperationBType):
    def __init__(self, DocType=None, DocId=None, Operation=None, Quantity=None, OperDate=None, **kwargs_):
        super(OperationBTypeSub, self).__init__(DocType, DocId, Operation, Quantity, OperDate,  **kwargs_)
supermod.OperationBType.subclass = OperationBTypeSub
# end class OperationBTypeSub


class ReplyClientVersionSub(supermod.ReplyClientVersion):
    def __init__(self, VersionDate=None, Client=None, **kwargs_):
        super(ReplyClientVersionSub, self).__init__(VersionDate, Client,  **kwargs_)
supermod.ReplyClientVersion.subclass = ReplyClientVersionSub
# end class ReplyClientVersionSub


class QueryRejectRepProducedSub(supermod.QueryRejectRepProduced):
    def __init__(self, RegId=None, **kwargs_):
        super(QueryRejectRepProducedSub, self).__init__(RegId,  **kwargs_)
supermod.QueryRejectRepProduced.subclass = QueryRejectRepProducedSub
# end class QueryRejectRepProducedSub


class QueryRejectRepImportedSub(supermod.QueryRejectRepImported):
    def __init__(self, RegId=None, **kwargs_):
        super(QueryRejectRepImportedSub, self).__init__(RegId,  **kwargs_)
supermod.QueryRejectRepImported.subclass = QueryRejectRepImportedSub
# end class QueryRejectRepImportedSub


class ReplySSP_v2Sub(supermod.ReplySSP_v2):
    def __init__(self, Products=None, **kwargs_):
        super(ReplySSP_v2Sub, self).__init__(Products,  **kwargs_)
supermod.ReplySSP_v2.subclass = ReplySSP_v2Sub
# end class ReplySSP_v2Sub


class ReplySpirit_v2Sub(supermod.ReplySpirit_v2):
    def __init__(self, Products=None, **kwargs_):
        super(ReplySpirit_v2Sub, self).__init__(Products,  **kwargs_)
supermod.ReplySpirit_v2.subclass = ReplySpirit_v2Sub
# end class ReplySpirit_v2Sub


class ReplyClient_v2Sub(supermod.ReplyClient_v2):
    def __init__(self, Clients=None, **kwargs_):
        super(ReplyClient_v2Sub, self).__init__(Clients,  **kwargs_)
supermod.ReplyClient_v2.subclass = ReplyClient_v2Sub
# end class ReplyClient_v2Sub


class ReplyAP_v2Sub(supermod.ReplyAP_v2):
    def __init__(self, Products=None, **kwargs_):
        super(ReplyAP_v2Sub, self).__init__(Products,  **kwargs_)
supermod.ReplyAP_v2.subclass = ReplyAP_v2Sub
# end class ReplyAP_v2Sub


class ReplyAP_v3Sub(supermod.ReplyAP_v3):
    def __init__(self, Products=None, **kwargs_):
        super(ReplyAP_v3Sub, self).__init__(Products,  **kwargs_)
supermod.ReplyAP_v3.subclass = ReplyAP_v3Sub
# end class ReplyAP_v3Sub


class ReplyRests_v2Sub(supermod.ReplyRests_v2):
    def __init__(self, RestsDate=None, Products=None, **kwargs_):
        super(ReplyRests_v2Sub, self).__init__(RestsDate, Products,  **kwargs_)
supermod.ReplyRests_v2.subclass = ReplyRests_v2Sub
# end class ReplyRests_v2Sub


class StockPositionType21Sub(supermod.StockPositionType21):
    def __init__(self, Product=None, Quantity=None, InformF1RegId=None, InformF2RegId=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, **kwargs_):
        super(StockPositionType21Sub, self).__init__(Product, Quantity, InformF1RegId, InformF2RegId, alcPercent, alcPercentMin, alcPercentMax,  **kwargs_)
supermod.StockPositionType21.subclass = StockPositionType21Sub
# end class StockPositionType21Sub


class ReplyForm1Sub(supermod.ReplyForm1):
    def __init__(self, InformF1RegId=None, OriginalClient=None, OriginalDocNumber=None, OriginalDocDate=None, Product=None, BottlingDate=None, Quantity=None, EGAISNumber=None, EGAISDate=None, GTDNUMBER=None, GTDDate=None, MarkInfo=None, **kwargs_):
        super(ReplyForm1Sub, self).__init__(InformF1RegId, OriginalClient, OriginalDocNumber, OriginalDocDate, Product, BottlingDate, Quantity, EGAISNumber, EGAISDate, GTDNUMBER, GTDDate, MarkInfo,  **kwargs_)
supermod.ReplyForm1.subclass = ReplyForm1Sub
# end class ReplyForm1Sub


class ReplyForm2Sub(supermod.ReplyForm2):
    def __init__(self, InformF2RegId=None, TTNNumber=None, TTNDate=None, Shipper=None, Consignee=None, ShippingDate=None, Product=None, Quantity=None, ExciseRate=None, MarkInfo=None, **kwargs_):
        super(ReplyForm2Sub, self).__init__(InformF2RegId, TTNNumber, TTNDate, Shipper, Consignee, ShippingDate, Product, Quantity, ExciseRate, MarkInfo,  **kwargs_)
supermod.ReplyForm2.subclass = ReplyForm2Sub
# end class ReplyForm2Sub


class ReplyHistForm2Sub(supermod.ReplyHistForm2):
    def __init__(self, InformF2RegId=None, HistForm2Date=None, HistoryF2=None, **kwargs_):
        super(ReplyHistForm2Sub, self).__init__(InformF2RegId, HistForm2Date, HistoryF2,  **kwargs_)
supermod.ReplyHistForm2.subclass = ReplyHistForm2Sub
# end class ReplyHistForm2Sub


class OperationBType22Sub(supermod.OperationBType22):
    def __init__(self, DocType=None, DocId=None, Operation=None, Quantity=None, OperDate=None, **kwargs_):
        super(OperationBType22Sub, self).__init__(DocType, DocId, Operation, Quantity, OperDate,  **kwargs_)
supermod.OperationBType22.subclass = OperationBType22Sub
# end class OperationBType22Sub


class WayBillType_v2Sub(supermod.WayBillType_v2):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillType_v2Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillType_v2.subclass = WayBillType_v2Sub
# end class WayBillType_v2Sub


class PositionType23Sub(supermod.PositionType23):
    def __init__(self, Product=None, Pack_ID=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Price=None, Party=None, Identity=None, InformF1=None, InformF2=None, **kwargs_):
        super(PositionType23Sub, self).__init__(Product, Pack_ID, Quantity, alcPercent, alcPercentMin, alcPercentMax, Price, Party, Identity, InformF1, InformF2,  **kwargs_)
supermod.PositionType23.subclass = PositionType23Sub
# end class PositionType23Sub


class TransportType24Sub(supermod.TransportType24):
    def __init__(self, TRAN_TYPE=None, TRAN_COMPANY=None, TRAN_CAR=None, TRAN_TRAILER=None, TRAN_CUSTOMER=None, TRAN_DRIVER=None, TRAN_LOADPOINT=None, TRAN_UNLOADPOINT=None, TRAN_REDIRECT=None, TRAN_FORWARDER=None, **kwargs_):
        super(TransportType24Sub, self).__init__(TRAN_TYPE, TRAN_COMPANY, TRAN_CAR, TRAN_TRAILER, TRAN_CUSTOMER, TRAN_DRIVER, TRAN_LOADPOINT, TRAN_UNLOADPOINT, TRAN_REDIRECT, TRAN_FORWARDER,  **kwargs_)
supermod.TransportType24.subclass = TransportType24Sub
# end class TransportType24Sub


class WayBillActType_v2Sub(supermod.WayBillActType_v2):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillActType_v2Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillActType_v2.subclass = WayBillActType_v2Sub
# end class WayBillActType_v2Sub


class PositionType27Sub(supermod.PositionType27):
    def __init__(self, Identity=None, InformF2RegId=None, RealQuantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, **kwargs_):
        super(PositionType27Sub, self).__init__(Identity, InformF2RegId, RealQuantity, alcPercent, alcPercentMin, alcPercentMax,  **kwargs_)
supermod.PositionType27.subclass = PositionType27Sub
# end class PositionType27Sub


class ActChargeOnType_v2Sub(supermod.ActChargeOnType_v2):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActChargeOnType_v2Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActChargeOnType_v2.subclass = ActChargeOnType_v2Sub
# end class ActChargeOnType_v2Sub


class ActChargeOnPositionType29Sub(supermod.ActChargeOnPositionType29):
    def __init__(self, Identity=None, Product=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, InformF1F2=None, MarkCodeInfo=None, **kwargs_):
        super(ActChargeOnPositionType29Sub, self).__init__(Identity, Product, Quantity, alcPercent, alcPercentMin, alcPercentMax, InformF1F2, MarkCodeInfo,  **kwargs_)
supermod.ActChargeOnPositionType29.subclass = ActChargeOnPositionType29Sub
# end class ActChargeOnPositionType29Sub


class InformF1F2RegTypeSub(supermod.InformF1F2RegType):
    def __init__(self, InformF1=None, **kwargs_):
        super(InformF1F2RegTypeSub, self).__init__(InformF1,  **kwargs_)
supermod.InformF1F2RegType.subclass = InformF1F2RegTypeSub
# end class InformF1F2RegTypeSub


class InformF2TypeRegItemSub(supermod.InformF2TypeRegItem):
    def __init__(self, Identity=None, TTNNumber=None, TTNDate=None, Quantity=None, **kwargs_):
        super(InformF2TypeRegItemSub, self).__init__(Identity, TTNNumber, TTNDate, Quantity,  **kwargs_)
supermod.InformF2TypeRegItem.subclass = InformF2TypeRegItemSub
# end class InformF2TypeRegItemSub


class InformF1RegTypeSub(supermod.InformF1RegType):
    def __init__(self, Quantity=None, BottlingDate=None, TTNNumber=None, TTNDate=None, EGAISFixNumber=None, EGAISFixDate=None, **kwargs_):
        super(InformF1RegTypeSub, self).__init__(Quantity, BottlingDate, TTNNumber, TTNDate, EGAISFixNumber, EGAISFixDate,  **kwargs_)
supermod.InformF1RegType.subclass = InformF1RegTypeSub
# end class InformF1RegTypeSub


class ActInventoryInformF2RegSub(supermod.ActInventoryInformF2Reg):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(ActInventoryInformF2RegSub, self).__init__(Header, Content,  **kwargs_)
supermod.ActInventoryInformF2Reg.subclass = ActInventoryInformF2RegSub
# end class ActInventoryInformF2RegSub


class InformInvPositionType30Sub(supermod.InformInvPositionType30):
    def __init__(self, Identity=None, InformF1RegId=None, InformF2=None, **kwargs_):
        super(InformInvPositionType30Sub, self).__init__(Identity, InformF1RegId, InformF2,  **kwargs_)
supermod.InformInvPositionType30.subclass = InformInvPositionType30Sub
# end class InformInvPositionType30Sub


class InformInvF2RegItemSub(supermod.InformInvF2RegItem):
    def __init__(self, Identity=None, F2RegId=None, MarkInfo=None, **kwargs_):
        super(InformInvF2RegItemSub, self).__init__(Identity, F2RegId, MarkInfo,  **kwargs_)
supermod.InformInvF2RegItem.subclass = InformInvF2RegItemSub
# end class InformInvF2RegItemSub


class QueryFormF1F2Sub(supermod.QueryFormF1F2):
    def __init__(self, FormRegId=None, **kwargs_):
        super(QueryFormF1F2Sub, self).__init__(FormRegId,  **kwargs_)
supermod.QueryFormF1F2.subclass = QueryFormF1F2Sub
# end class QueryFormF1F2Sub


class WayBillInformF2RegTypeSub(supermod.WayBillInformF2RegType):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(WayBillInformF2RegTypeSub, self).__init__(Header, Content,  **kwargs_)
supermod.WayBillInformF2RegType.subclass = WayBillInformF2RegTypeSub
# end class WayBillInformF2RegTypeSub


class InformF2PositionTypeSub(supermod.InformF2PositionType):
    def __init__(self, Identity=None, InformF2RegId=None, BottlingDate=None, **kwargs_):
        super(InformF2PositionTypeSub, self).__init__(Identity, InformF2RegId, BottlingDate,  **kwargs_)
supermod.InformF2PositionType.subclass = InformF2PositionTypeSub
# end class InformF2PositionTypeSub


class ActWriteOffType_v2Sub(supermod.ActWriteOffType_v2):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActWriteOffType_v2Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActWriteOffType_v2.subclass = ActWriteOffType_v2Sub
# end class ActWriteOffType_v2Sub


class ActWriteOffPositionType31Sub(supermod.ActWriteOffPositionType31):
    def __init__(self, Identity=None, Quantity=None, InformF1F2=None, MarkCodeInfo=None, **kwargs_):
        super(ActWriteOffPositionType31Sub, self).__init__(Identity, Quantity, InformF1F2, MarkCodeInfo,  **kwargs_)
supermod.ActWriteOffPositionType31.subclass = ActWriteOffPositionType31Sub
# end class ActWriteOffPositionType31Sub


class InformF1F2Sub(supermod.InformF1F2):
    def __init__(self, InformF2=None, InformF1=None, **kwargs_):
        super(InformF1F2Sub, self).__init__(InformF2, InformF1,  **kwargs_)
supermod.InformF1F2.subclass = InformF1F2Sub
# end class InformF1F2Sub


class TransferFromShopTypeSub(supermod.TransferFromShopType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(TransferFromShopTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.TransferFromShopType.subclass = TransferFromShopTypeSub
# end class TransferFromShopTypeSub


class TransferFromShopPositionTypeSub(supermod.TransferFromShopPositionType):
    def __init__(self, Identity=None, ProductCode=None, Quantity=None, InformF2=None, **kwargs_):
        super(TransferFromShopPositionTypeSub, self).__init__(Identity, ProductCode, Quantity, InformF2,  **kwargs_)
supermod.TransferFromShopPositionType.subclass = TransferFromShopPositionTypeSub
# end class TransferFromShopPositionTypeSub


class TransferToShopTypeSub(supermod.TransferToShopType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(TransferToShopTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.TransferToShopType.subclass = TransferToShopTypeSub
# end class TransferToShopTypeSub


class TransferToShopPositionTypeSub(supermod.TransferToShopPositionType):
    def __init__(self, Identity=None, ProductCode=None, Quantity=None, InformF2=None, **kwargs_):
        super(TransferToShopPositionTypeSub, self).__init__(Identity, ProductCode, Quantity, InformF2,  **kwargs_)
supermod.TransferToShopPositionType.subclass = TransferToShopPositionTypeSub
# end class TransferToShopPositionTypeSub


class RepPIInformF1RegTypeSub(supermod.RepPIInformF1RegType):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(RepPIInformF1RegTypeSub, self).__init__(Header, Content,  **kwargs_)
supermod.RepPIInformF1RegType.subclass = RepPIInformF1RegTypeSub
# end class RepPIInformF1RegTypeSub


class InformF1PositionTypeSub(supermod.InformF1PositionType):
    def __init__(self, Identity=None, InformF1RegId=None, InformF2RegId=None, **kwargs_):
        super(InformF1PositionTypeSub, self).__init__(Identity, InformF1RegId, InformF2RegId,  **kwargs_)
supermod.InformF1PositionType.subclass = InformF1PositionTypeSub
# end class InformF1PositionTypeSub


class NoAnswerTTNSub(supermod.NoAnswerTTN):
    def __init__(self, Consignee=None, ReplyDate=None, ttnlist=None, **kwargs_):
        super(NoAnswerTTNSub, self).__init__(Consignee, ReplyDate, ttnlist,  **kwargs_)
supermod.NoAnswerTTN.subclass = NoAnswerTTNSub
# end class NoAnswerTTNSub


class NoAnswerTypeSub(supermod.NoAnswerType):
    def __init__(self, WbRegID=None, ttnNumber=None, ttnDate=None, Shipper=None, **kwargs_):
        super(NoAnswerTypeSub, self).__init__(WbRegID, ttnNumber, ttnDate, Shipper,  **kwargs_)
supermod.NoAnswerType.subclass = NoAnswerTypeSub
# end class NoAnswerTypeSub


class ReplyRestsShop_v2Sub(supermod.ReplyRestsShop_v2):
    def __init__(self, RestsDate=None, Products=None, **kwargs_):
        super(ReplyRestsShop_v2Sub, self).__init__(RestsDate, Products,  **kwargs_)
supermod.ReplyRestsShop_v2.subclass = ReplyRestsShop_v2Sub
# end class ReplyRestsShop_v2Sub


class ShopPositionTypeSub(supermod.ShopPositionType):
    def __init__(self, Product=None, Quantity=None, **kwargs_):
        super(ShopPositionTypeSub, self).__init__(Product, Quantity,  **kwargs_)
supermod.ShopPositionType.subclass = ShopPositionTypeSub
# end class ShopPositionTypeSub


class AsiiuSub(supermod.Asiiu):
    def __init__(self, Sensor=None, Producer=None, Data=None, **kwargs_):
        super(AsiiuSub, self).__init__(Sensor, Producer, Data,  **kwargs_)
supermod.Asiiu.subclass = AsiiuSub
# end class AsiiuSub


class DataTypeSub(supermod.DataType):
    def __init__(self, Product=None, StartDate=None, EndDate=None, VbsStart=None, VbsEnd=None, AStart=None, AEnd=None, PercentAlc=None, BottleCountStart=None, BottleCountEnd=None, Temperature=None, Mode=None, Crotonaldehyd=None, Toluene=None, **kwargs_):
        super(DataTypeSub, self).__init__(Product, StartDate, EndDate, VbsStart, VbsEnd, AStart, AEnd, PercentAlc, BottleCountStart, BottleCountEnd, Temperature, Mode, Crotonaldehyd, Toluene,  **kwargs_)
supermod.DataType.subclass = DataTypeSub
# end class DataTypeSub


class AsiiuTimeSub(supermod.AsiiuTime):
    def __init__(self, Sensor=None, Producer=None, Data=None, **kwargs_):
        super(AsiiuTimeSub, self).__init__(Sensor, Producer, Data,  **kwargs_)
supermod.AsiiuTime.subclass = AsiiuTimeSub
# end class AsiiuTimeSub


class DataType32Sub(supermod.DataType32):
    def __init__(self, Product=None, ControlDate=None, VbsControl=None, AControl=None, PercentAlc=None, BottleCountControl=None, Temperature=None, Mode=None, Crotonaldehyd=None, Toluene=None, **kwargs_):
        super(DataType32Sub, self).__init__(Product, ControlDate, VbsControl, AControl, PercentAlc, BottleCountControl, Temperature, Mode, Crotonaldehyd, Toluene,  **kwargs_)
supermod.DataType32.subclass = DataType32Sub
# end class DataType32Sub


class ActChargeOnShopType_v2Sub(supermod.ActChargeOnShopType_v2):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActChargeOnShopType_v2Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActChargeOnShopType_v2.subclass = ActChargeOnShopType_v2Sub
# end class ActChargeOnShopType_v2Sub


class ActChargeOnShopPositionTypeSub(supermod.ActChargeOnShopPositionType):
    def __init__(self, Identity=None, Product=None, Quantity=None, **kwargs_):
        super(ActChargeOnShopPositionTypeSub, self).__init__(Identity, Product, Quantity,  **kwargs_)
supermod.ActChargeOnShopPositionType.subclass = ActChargeOnShopPositionTypeSub
# end class ActChargeOnShopPositionTypeSub


class ActWriteOffShopType_v2Sub(supermod.ActWriteOffShopType_v2):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActWriteOffShopType_v2Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActWriteOffShopType_v2.subclass = ActWriteOffShopType_v2Sub
# end class ActWriteOffShopType_v2Sub


class ActWriteOffShopPositionTypeSub(supermod.ActWriteOffShopPositionType):
    def __init__(self, Identity=None, Product=None, Quantity=None, SumSale=None, MarkCodeInfo=None, **kwargs_):
        super(ActWriteOffShopPositionTypeSub, self).__init__(Identity, Product, Quantity, SumSale, MarkCodeInfo,  **kwargs_)
supermod.ActWriteOffShopPositionType.subclass = ActWriteOffShopPositionTypeSub
# end class ActWriteOffShopPositionTypeSub


class InfoVersionTTNSub(supermod.InfoVersionTTN):
    def __init__(self, ClientId=None, WBTypeUsed=None, **kwargs_):
        super(InfoVersionTTNSub, self).__init__(ClientId, WBTypeUsed,  **kwargs_)
supermod.InfoVersionTTN.subclass = InfoVersionTTNSub
# end class InfoVersionTTNSub


class QueryBarcodeSub(supermod.QueryBarcode):
    def __init__(self, QueryNumber=None, Date=None, Marks=None, **kwargs_):
        super(QueryBarcodeSub, self).__init__(QueryNumber, Date, Marks,  **kwargs_)
supermod.QueryBarcode.subclass = QueryBarcodeSub
# end class QueryBarcodeSub


class MarkTypeSub(supermod.MarkType):
    def __init__(self, Identity=None, Type=None, Rank=None, Number=None, **kwargs_):
        super(MarkTypeSub, self).__init__(Identity, Type, Rank, Number,  **kwargs_)
supermod.MarkType.subclass = MarkTypeSub
# end class MarkTypeSub


class ReplyBarcodeSub(supermod.ReplyBarcode):
    def __init__(self, QueryNumber=None, Date=None, Marks=None, **kwargs_):
        super(ReplyBarcodeSub, self).__init__(QueryNumber, Date, Marks,  **kwargs_)
supermod.ReplyBarcode.subclass = ReplyBarcodeSub
# end class ReplyBarcodeSub


class BarcodeTypeSub(supermod.BarcodeType):
    def __init__(self, Identity=None, Type=None, Rank=None, Number=None, Barcode=None, **kwargs_):
        super(BarcodeTypeSub, self).__init__(Identity, Type, Rank, Number, Barcode,  **kwargs_)
supermod.BarcodeType.subclass = BarcodeTypeSub
# end class BarcodeTypeSub


class RequestRepealWBSub(supermod.RequestRepealWB):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, WBRegId=None, **kwargs_):
        super(RequestRepealWBSub, self).__init__(ClientId, RequestNumber, RequestDate, WBRegId,  **kwargs_)
supermod.RequestRepealWB.subclass = RequestRepealWBSub
# end class RequestRepealWBSub


class ConfirmRepealWBSub(supermod.ConfirmRepealWB):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(ConfirmRepealWBSub, self).__init__(Identity, Header,  **kwargs_)
supermod.ConfirmRepealWB.subclass = ConfirmRepealWBSub
# end class ConfirmRepealWBSub


class RequestRepealACOSub(supermod.RequestRepealACO):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, ACORegId=None, **kwargs_):
        super(RequestRepealACOSub, self).__init__(ClientId, RequestNumber, RequestDate, ACORegId,  **kwargs_)
supermod.RequestRepealACO.subclass = RequestRepealACOSub
# end class RequestRepealACOSub


class RequestRepealAWOSub(supermod.RequestRepealAWO):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, AWORegId=None, **kwargs_):
        super(RequestRepealAWOSub, self).__init__(ClientId, RequestNumber, RequestDate, AWORegId,  **kwargs_)
supermod.RequestRepealAWO.subclass = RequestRepealAWOSub
# end class RequestRepealAWOSub


class ReplyRests_MiniSub(supermod.ReplyRests_Mini):
    def __init__(self, RestsDate=None, Products=None, **kwargs_):
        super(ReplyRests_MiniSub, self).__init__(RestsDate, Products,  **kwargs_)
supermod.ReplyRests_Mini.subclass = ReplyRests_MiniSub
# end class ReplyRests_MiniSub


class StockPositionType35Sub(supermod.StockPositionType35):
    def __init__(self, AlcCode=None, Quantity=None, Inform1RegId=None, Inform2RegId=None, **kwargs_):
        super(StockPositionType35Sub, self).__init__(AlcCode, Quantity, Inform1RegId, Inform2RegId,  **kwargs_)
supermod.StockPositionType35.subclass = StockPositionType35Sub
# end class StockPositionType35Sub


class ReplyRestsShop_MiniSub(supermod.ReplyRestsShop_Mini):
    def __init__(self, RestsDate=None, Products=None, **kwargs_):
        super(ReplyRestsShop_MiniSub, self).__init__(RestsDate, Products,  **kwargs_)
supermod.ReplyRestsShop_Mini.subclass = ReplyRestsShop_MiniSub
# end class ReplyRestsShop_MiniSub


class ShopPositionType36Sub(supermod.ShopPositionType36):
    def __init__(self, AlcCode=None, Quantity=None, **kwargs_):
        super(ShopPositionType36Sub, self).__init__(AlcCode, Quantity,  **kwargs_)
supermod.ShopPositionType36.subclass = ShopPositionType36Sub
# end class ShopPositionType36Sub


class RequestAddProductsSub(supermod.RequestAddProducts):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, Content=None, **kwargs_):
        super(RequestAddProductsSub, self).__init__(ClientId, RequestNumber, RequestDate, Content,  **kwargs_)
supermod.RequestAddProducts.subclass = RequestAddProductsSub
# end class RequestAddProductsSub


class RequestAddSSPPositionTypeSub(supermod.RequestAddSSPPositionType):
    def __init__(self, Producer=None, Type=None, VidCode=None, CountryCode=None, FullName=None, ShortName=None, Unpacked_Flag=None, Capacity=None, PERCENT_ALC=None, PERCENT_ALC_min=None, PERCENT_ALC_max=None, FRAPID=None, Brand=None, PackageType=None, **kwargs_):
        super(RequestAddSSPPositionTypeSub, self).__init__(Producer, Type, VidCode, CountryCode, FullName, ShortName, Unpacked_Flag, Capacity, PERCENT_ALC, PERCENT_ALC_min, PERCENT_ALC_max, FRAPID, Brand, PackageType,  **kwargs_)
supermod.RequestAddSSPPositionType.subclass = RequestAddSSPPositionTypeSub
# end class RequestAddSSPPositionTypeSub


class RequestAddFProducerSub(supermod.RequestAddFProducer):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, Content=None, **kwargs_):
        super(RequestAddFProducerSub, self).__init__(ClientId, RequestNumber, RequestDate, Content,  **kwargs_)
supermod.RequestAddFProducer.subclass = RequestAddFProducerSub
# end class RequestAddFProducerSub


class OrgInfoForeignAddTypeSub(supermod.OrgInfoForeignAddType):
    def __init__(self, FO=None, TS=None, **kwargs_):
        super(OrgInfoForeignAddTypeSub, self).__init__(FO, TS,  **kwargs_)
supermod.OrgInfoForeignAddType.subclass = OrgInfoForeignAddTypeSub
# end class OrgInfoForeignAddTypeSub


class AddFOTypeSub(supermod.AddFOType):
    def __init__(self, LocalClientCode=None, FullName=None, ShortName=None, address=None, **kwargs_):
        super(AddFOTypeSub, self).__init__(LocalClientCode, FullName, ShortName, address,  **kwargs_)
supermod.AddFOType.subclass = AddFOTypeSub
# end class AddFOTypeSub


class AddTSTypeSub(supermod.AddTSType):
    def __init__(self, LocalClientCode=None, FullName=None, ShortName=None, TSNUM=None, address=None, **kwargs_):
        super(AddTSTypeSub, self).__init__(LocalClientCode, FullName, ShortName, TSNUM, address,  **kwargs_)
supermod.AddTSType.subclass = AddTSTypeSub
# end class AddTSTypeSub


class ReplyHistoryTransferShopSub(supermod.ReplyHistoryTransferShop):
    def __init__(self, ReplyDate=None, monthReport=None, yearReport=None, AlcCode=None, History=None, **kwargs_):
        super(ReplyHistoryTransferShopSub, self).__init__(ReplyDate, monthReport, yearReport, AlcCode, History,  **kwargs_)
supermod.ReplyHistoryTransferShop.subclass = ReplyHistoryTransferShopSub
# end class ReplyHistoryTransferShopSub


class DocDataTypeSub(supermod.DocDataType):
    def __init__(self, DocType=None, DocId=None, OperDate=None, Quantity=None, RegForm2=None, **kwargs_):
        super(DocDataTypeSub, self).__init__(DocType, DocId, OperDate, Quantity, RegForm2,  **kwargs_)
supermod.DocDataType.subclass = DocDataTypeSub
# end class DocDataTypeSub


class ReplyWOChequeSub(supermod.ReplyWOCheque):
    def __init__(self, ReplyDate=None, monthReport=None, yearReport=None, AlcCode=None, WriteOffCh=None, ReturnCh=None, **kwargs_):
        super(ReplyWOChequeSub, self).__init__(ReplyDate, monthReport, yearReport, AlcCode, WriteOffCh, ReturnCh,  **kwargs_)
supermod.ReplyWOCheque.subclass = ReplyWOChequeSub
# end class ReplyWOChequeSub


class AscpNavSub(supermod.AscpNav):
    def __init__(self, Sensor=None, TimeUTC=None, Latitude=None, Longitude=None, CountSatellite=None, Accuracy=None, Course=None, Speed=None, DataLevelGauge=None, **kwargs_):
        super(AscpNavSub, self).__init__(Sensor, TimeUTC, Latitude, Longitude, CountSatellite, Accuracy, Course, Speed, DataLevelGauge,  **kwargs_)
supermod.AscpNav.subclass = AscpNavSub
# end class AscpNavSub


class DataType37Sub(supermod.DataType37):
    def __init__(self, Number=None, Readings=None, Temperature=None, Density=None, **kwargs_):
        super(DataType37Sub, self).__init__(Number, Readings, Temperature, Density,  **kwargs_)
supermod.DataType37.subclass = DataType37Sub
# end class DataType37Sub


class WayBillType_v3Sub(supermod.WayBillType_v3):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillType_v3Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillType_v3.subclass = WayBillType_v3Sub
# end class WayBillType_v3Sub


class PositionType38Sub(supermod.PositionType38):
    def __init__(self, Product=None, Pack_ID=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Price=None, Party=None, Identity=None, EXCISE_NUMBER=None, EXCISE_DATE=None, EXCISE_SUM=None, EXCISE_BS=None, EAN13=None, FARegId=None, InformF2=None, boxInfo=None, **kwargs_):
        super(PositionType38Sub, self).__init__(Product, Pack_ID, Quantity, alcPercent, alcPercentMin, alcPercentMax, Price, Party, Identity, EXCISE_NUMBER, EXCISE_DATE, EXCISE_SUM, EXCISE_BS, EAN13, FARegId, InformF2, boxInfo,  **kwargs_)
supermod.PositionType38.subclass = PositionType38Sub
# end class PositionType38Sub


class TransportType39Sub(supermod.TransportType39):
    def __init__(self, TRAN_TYPE=None, TRAN_COMPANY=None, TRAN_CAR=None, TRAN_TRAILER=None, TRAN_CUSTOMER=None, TRAN_DRIVER=None, TRAN_LOADPOINT=None, TRAN_UNLOADPOINT=None, TRAN_REDIRECT=None, TRAN_FORWARDER=None, **kwargs_):
        super(TransportType39Sub, self).__init__(TRAN_TYPE, TRAN_COMPANY, TRAN_CAR, TRAN_TRAILER, TRAN_CUSTOMER, TRAN_DRIVER, TRAN_LOADPOINT, TRAN_UNLOADPOINT, TRAN_REDIRECT, TRAN_FORWARDER,  **kwargs_)
supermod.TransportType39.subclass = TransportType39Sub
# end class TransportType39Sub


class ActWriteOffType_v3Sub(supermod.ActWriteOffType_v3):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActWriteOffType_v3Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActWriteOffType_v3.subclass = ActWriteOffType_v3Sub
# end class ActWriteOffType_v3Sub


class ActWriteOffPositionType42Sub(supermod.ActWriteOffPositionType42):
    def __init__(self, Identity=None, Quantity=None, SumSale=None, InformF1F2=None, MarkCodeInfo=None, **kwargs_):
        super(ActWriteOffPositionType42Sub, self).__init__(Identity, Quantity, SumSale, InformF1F2, MarkCodeInfo,  **kwargs_)
supermod.ActWriteOffPositionType42.subclass = ActWriteOffPositionType42Sub
# end class ActWriteOffPositionType42Sub


class InformF1F243Sub(supermod.InformF1F243):
    def __init__(self, InformF2=None, InformF1=None, **kwargs_):
        super(InformF1F243Sub, self).__init__(InformF2, InformF1,  **kwargs_)
supermod.InformF1F243.subclass = InformF1F243Sub
# end class InformF1F243Sub


class WayBillActType_v3Sub(supermod.WayBillActType_v3):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillActType_v3Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillActType_v3.subclass = WayBillActType_v3Sub
# end class WayBillActType_v3Sub


class PositionType44Sub(supermod.PositionType44):
    def __init__(self, Identity=None, InformF2RegId=None, RealQuantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, MarkInfo=None, **kwargs_):
        super(PositionType44Sub, self).__init__(Identity, InformF2RegId, RealQuantity, alcPercent, alcPercentMin, alcPercentMax, MarkInfo,  **kwargs_)
supermod.PositionType44.subclass = PositionType44Sub
# end class PositionType44Sub


class RepProducedType_v3Sub(supermod.RepProducedType_v3):
    def __init__(self, Identity=None, Header=None, Content=None, ContentResource=None, **kwargs_):
        super(RepProducedType_v3Sub, self).__init__(Identity, Header, Content, ContentResource,  **kwargs_)
supermod.RepProducedType_v3.subclass = RepProducedType_v3Sub
# end class RepProducedType_v3Sub


class PositionType46Sub(supermod.PositionType46):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType46Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType46.subclass = PositionType46Sub
# end class PositionType46Sub


class UsedResourceType47Sub(supermod.UsedResourceType47):
    def __init__(self, IdentityRes=None, Product=None, RegForm2=None, Quantity=None, **kwargs_):
        super(UsedResourceType47Sub, self).__init__(IdentityRes, Product, RegForm2, Quantity,  **kwargs_)
supermod.UsedResourceType47.subclass = UsedResourceType47Sub
# end class UsedResourceType47Sub


class RepImportedType_v3Sub(supermod.RepImportedType_v3):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RepImportedType_v3Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RepImportedType_v3.subclass = RepImportedType_v3Sub
# end class RepImportedType_v3Sub


class PositionType49Sub(supermod.PositionType49):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType49Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType49.subclass = PositionType49Sub
# end class PositionType49Sub


class ReplyRestBCodeSub(supermod.ReplyRestBCode):
    def __init__(self, RestsDate=None, Inform2RegId=None, MarkInfo=None, **kwargs_):
        super(ReplyRestBCodeSub, self).__init__(RestsDate, Inform2RegId, MarkInfo,  **kwargs_)
supermod.ReplyRestBCode.subclass = ReplyRestBCodeSub
# end class ReplyRestBCodeSub


class ActFixBarCodeSub(supermod.ActFixBarCode):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActFixBarCodeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActFixBarCode.subclass = ActFixBarCodeSub
# end class ActFixBarCodeSub


class ActFixBarCodePositionTypeSub(supermod.ActFixBarCodePositionType):
    def __init__(self, Identity=None, Inform2RegId=None, MarkInfo=None, **kwargs_):
        super(ActFixBarCodePositionTypeSub, self).__init__(Identity, Inform2RegId, MarkInfo,  **kwargs_)
supermod.ActFixBarCodePositionType.subclass = ActFixBarCodePositionTypeSub
# end class ActFixBarCodePositionTypeSub


class ActUnFixBarCodeSub(supermod.ActUnFixBarCode):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActUnFixBarCodeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActUnFixBarCode.subclass = ActUnFixBarCodeSub
# end class ActUnFixBarCodeSub


class ActUnFixBarCodePositionTypeSub(supermod.ActUnFixBarCodePositionType):
    def __init__(self, Identity=None, Inform2RegId=None, MarkInfo=None, **kwargs_):
        super(ActUnFixBarCodePositionTypeSub, self).__init__(Identity, Inform2RegId, MarkInfo,  **kwargs_)
supermod.ActUnFixBarCodePositionType.subclass = ActUnFixBarCodePositionTypeSub
# end class ActUnFixBarCodePositionTypeSub


class ReplyParentHistForm2Sub(supermod.ReplyParentHistForm2):
    def __init__(self, InformF2RegId=None, HistForm2Date=None, ParentHist=None, **kwargs_):
        super(ReplyParentHistForm2Sub, self).__init__(InformF2RegId, HistForm2Date, ParentHist,  **kwargs_)
supermod.ReplyParentHistForm2.subclass = ReplyParentHistForm2Sub
# end class ReplyParentHistForm2Sub


class stepBTypeSub(supermod.stepBType):
    def __init__(self, lev=None, Form2=None, parentForm2=None, Shipper=None, Consignee=None, WBRegId=None, amount=None, **kwargs_):
        super(stepBTypeSub, self).__init__(lev, Form2, parentForm2, Shipper, Consignee, WBRegId, amount,  **kwargs_)
supermod.stepBType.subclass = stepBTypeSub
# end class stepBTypeSub


class TTNHistoryF2RegSub(supermod.TTNHistoryF2Reg):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(TTNHistoryF2RegSub, self).__init__(Header, Content,  **kwargs_)
supermod.TTNHistoryF2Reg.subclass = TTNHistoryF2RegSub
# end class TTNHistoryF2RegSub


class InformParentF2TypeSub(supermod.InformParentF2Type):
    def __init__(self, Identity=None, HistF2=None, **kwargs_):
        super(InformParentF2TypeSub, self).__init__(Identity, HistF2,  **kwargs_)
supermod.InformParentF2Type.subclass = InformParentF2TypeSub
# end class InformParentF2TypeSub


class stepTypeSub(supermod.stepType):
    def __init__(self, lev=None, Form2=None, parentForm2=None, Shipper=None, Consignee=None, WBRegId=None, amount=None, **kwargs_):
        super(stepTypeSub, self).__init__(lev, Form2, parentForm2, Shipper, Consignee, WBRegId, amount,  **kwargs_)
supermod.stepType.subclass = stepTypeSub
# end class stepTypeSub


class CarrierNoticeSub(supermod.CarrierNotice):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(CarrierNoticeSub, self).__init__(Header, Content,  **kwargs_)
supermod.CarrierNotice.subclass = CarrierNoticeSub
# end class CarrierNoticeSub


class PositionType50Sub(supermod.PositionType50):
    def __init__(self, PosIdentity=None, Product=None, Quantity20=None, AlcPerc20=None, **kwargs_):
        super(PositionType50Sub, self).__init__(PosIdentity, Product, Quantity20, AlcPerc20,  **kwargs_)
supermod.PositionType50.subclass = PositionType50Sub
# end class PositionType50Sub


class CarrierNotice_v4Sub(supermod.CarrierNotice_v4):
    def __init__(self, Header=None, Content=None, **kwargs_):
        super(CarrierNotice_v4Sub, self).__init__(Header, Content,  **kwargs_)
supermod.CarrierNotice_v4.subclass = CarrierNotice_v4Sub
# end class CarrierNotice_v4Sub


class PositionType51Sub(supermod.PositionType51):
    def __init__(self, PosIdentity=None, Product=None, Quantity20=None, AlcPerc20=None, **kwargs_):
        super(PositionType51Sub, self).__init__(PosIdentity, Product, Quantity20, AlcPerc20,  **kwargs_)
supermod.PositionType51.subclass = PositionType51Sub
# end class PositionType51Sub


class ClientTransportTypeSub(supermod.ClientTransportType):
    def __init__(self, Car=None, Railway=None, **kwargs_):
        super(ClientTransportTypeSub, self).__init__(Car, Railway,  **kwargs_)
supermod.ClientTransportType.subclass = ClientTransportTypeSub
# end class ClientTransportTypeSub


class RailwayTypeSub(supermod.RailwayType):
    def __init__(self, RailwayModel=None, RailwayVid=None, RailwayNumber=None, **kwargs_):
        super(RailwayTypeSub, self).__init__(RailwayModel, RailwayVid, RailwayNumber,  **kwargs_)
supermod.RailwayType.subclass = RailwayTypeSub
# end class RailwayTypeSub


class ClaimIssueFSMType52Sub(supermod.ClaimIssueFSMType52):
    def __init__(self, Identity=None, Header=None, Content=None, CalculationDemand=None, **kwargs_):
        super(ClaimIssueFSMType52Sub, self).__init__(Identity, Header, Content, CalculationDemand,  **kwargs_)
supermod.ClaimIssueFSMType52.subclass = ClaimIssueFSMType52Sub
# end class ClaimIssueFSMType52Sub


class producedruSub(supermod.producedru):
    def __init__(self, TypeClaim=None, **kwargs_):
        super(producedruSub, self).__init__(TypeClaim,  **kwargs_)
supermod.producedru.subclass = producedruSub
# end class producedruSub


class producedtsSub(supermod.producedts):
    def __init__(self, TypeClaim=None, CONTRACTNUMBER=None, CONTRACTDATE=None, SHIPPER=None, **kwargs_):
        super(producedtsSub, self).__init__(TypeClaim, CONTRACTNUMBER, CONTRACTDATE, SHIPPER,  **kwargs_)
supermod.producedts.subclass = producedtsSub
# end class producedtsSub


class producedimpSub(supermod.producedimp):
    def __init__(self, TypeClaim=None, CONTRACTNUMBER=None, CONTRACTDATE=None, SHIPPER=None, **kwargs_):
        super(producedimpSub, self).__init__(TypeClaim, CONTRACTNUMBER, CONTRACTDATE, SHIPPER,  **kwargs_)
supermod.producedimp.subclass = producedimpSub
# end class producedimpSub


class ClaimIssueFSMComplTypeSub(supermod.ClaimIssueFSMComplType):
    def __init__(self, TypeClaim1=None, TypeClaim3=None, TypeClaim2=None, **kwargs_):
        super(ClaimIssueFSMComplTypeSub, self).__init__(TypeClaim1, TypeClaim3, TypeClaim2,  **kwargs_)
supermod.ClaimIssueFSMComplType.subclass = ClaimIssueFSMComplTypeSub
# end class ClaimIssueFSMComplTypeSub


class PositionClaimTypeSub(supermod.PositionClaimType):
    def __init__(self, VidAP171fz=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, QuantityDal=None, Capacity=None, Identity=None, SampleFSM=None, MarkType=None, Quantity=None, **kwargs_):
        super(PositionClaimTypeSub, self).__init__(VidAP171fz, alcPercent, alcPercentMin, alcPercentMax, QuantityDal, Capacity, Identity, SampleFSM, MarkType, Quantity,  **kwargs_)
supermod.PositionClaimType.subclass = PositionClaimTypeSub
# end class PositionClaimTypeSub


class CalculationDemandTypeSub(supermod.CalculationDemandType):
    def __init__(self, Spirit=None, WineMaterial=None, RawAged=None, MarkedAP=None, WinemakingAP=None, WinemakingAPSTP=None, **kwargs_):
        super(CalculationDemandTypeSub, self).__init__(Spirit, WineMaterial, RawAged, MarkedAP, WinemakingAP, WinemakingAPSTP,  **kwargs_)
supermod.CalculationDemandType.subclass = CalculationDemandTypeSub
# end class CalculationDemandTypeSub


class SpiritTypeSub(supermod.SpiritType):
    def __init__(self, Raw=None, VolumeAnhydrousRest=None, VolumeProducedRaw=None, VolumeOutRaw=None, VolumeReceivedRaw=None, VolumeUsedRaw=None, ClaimRaw=None, TotalRaw=None, **kwargs_):
        super(SpiritTypeSub, self).__init__(Raw, VolumeAnhydrousRest, VolumeProducedRaw, VolumeOutRaw, VolumeReceivedRaw, VolumeUsedRaw, ClaimRaw, TotalRaw,  **kwargs_)
supermod.SpiritType.subclass = SpiritTypeSub
# end class SpiritTypeSub


class WineMaterialTypeSub(supermod.WineMaterialType):
    def __init__(self, Raw=None, VolumeAnhydrousRest=None, VolumeProducedRaw=None, VolumeOutRaw=None, VolumeReceivedRaw=None, VolumeUsedRaw=None, VolumeEstimatedRest=None, TotalRaw=None, **kwargs_):
        super(WineMaterialTypeSub, self).__init__(Raw, VolumeAnhydrousRest, VolumeProducedRaw, VolumeOutRaw, VolumeReceivedRaw, VolumeUsedRaw, VolumeEstimatedRest, TotalRaw,  **kwargs_)
supermod.WineMaterialType.subclass = WineMaterialTypeSub
# end class WineMaterialTypeSub


class VolumeSpiritTypeSub(supermod.VolumeSpiritType):
    def __init__(self, Volume20C=None, VolumeAnhydrous=None, **kwargs_):
        super(VolumeSpiritTypeSub, self).__init__(Volume20C, VolumeAnhydrous,  **kwargs_)
supermod.VolumeSpiritType.subclass = VolumeSpiritTypeSub
# end class VolumeSpiritTypeSub


class VolumeReceivedRawTypeSub(supermod.VolumeReceivedRawType):
    def __init__(self, VolumeFromAgingRaw=None, VolumeBuyRaw=None, VolumeConversionRaw=None, **kwargs_):
        super(VolumeReceivedRawTypeSub, self).__init__(VolumeFromAgingRaw, VolumeBuyRaw, VolumeConversionRaw,  **kwargs_)
supermod.VolumeReceivedRawType.subclass = VolumeReceivedRawTypeSub
# end class VolumeReceivedRawTypeSub


class VolumeUsedRawTypeSub(supermod.VolumeUsedRawType):
    def __init__(self, VolumeToAgingRaw=None, VolumeToProducedRaw=None, **kwargs_):
        super(VolumeUsedRawTypeSub, self).__init__(VolumeToAgingRaw, VolumeToProducedRaw,  **kwargs_)
supermod.VolumeUsedRawType.subclass = VolumeUsedRawTypeSub
# end class VolumeUsedRawTypeSub


class ClaimRawTypeSub(supermod.ClaimRawType):
    def __init__(self, ClaimNumber=None, ClaimDate=None, SumAdvancePayment=None, VolumeAnhydrous=None, ClaimNumberFNS=None, ClaimDateFNS=None, VolumeNotUsed=None, **kwargs_):
        super(ClaimRawTypeSub, self).__init__(ClaimNumber, ClaimDate, SumAdvancePayment, VolumeAnhydrous, ClaimNumberFNS, ClaimDateFNS, VolumeNotUsed,  **kwargs_)
supermod.ClaimRawType.subclass = ClaimRawTypeSub
# end class ClaimRawTypeSub


class VolumeLocateAgainRawTypeSub(supermod.VolumeLocateAgainRawType):
    def __init__(self, TypeRawMaterial=None, VolumeSpirit=None, VolumeRestOld=None, VolumeTransferred=None, VolumeReturned=None, VolumeRest=None, **kwargs_):
        super(VolumeLocateAgainRawTypeSub, self).__init__(TypeRawMaterial, VolumeSpirit, VolumeRestOld, VolumeTransferred, VolumeReturned, VolumeRest,  **kwargs_)
supermod.VolumeLocateAgainRawType.subclass = VolumeLocateAgainRawTypeSub
# end class VolumeLocateAgainRawTypeSub


class RawAgedTypeSub(supermod.RawAgedType):
    def __init__(self, ExposureOneYear=None, ExposureThreeYear=None, ExposureFiveYear=None, ExposureSevenYear=None, **kwargs_):
        super(RawAgedTypeSub, self).__init__(ExposureOneYear, ExposureThreeYear, ExposureFiveYear, ExposureSevenYear,  **kwargs_)
supermod.RawAgedType.subclass = RawAgedTypeSub
# end class RawAgedTypeSub


class VolumeMarkedProductTypeSub(supermod.VolumeMarkedProductType):
    def __init__(self, SampleFSM=None, VidAP171fz=None, VolumeSpirit=None, VolumeMarkedAP=None, Capacity=None, AmountFSM=None, VolumeAnhydrousSpirit=None, **kwargs_):
        super(VolumeMarkedProductTypeSub, self).__init__(SampleFSM, VidAP171fz, VolumeSpirit, VolumeMarkedAP, Capacity, AmountFSM, VolumeAnhydrousSpirit,  **kwargs_)
supermod.VolumeMarkedProductType.subclass = VolumeMarkedProductTypeSub
# end class VolumeMarkedProductTypeSub


class MarkedAPTypeSub(supermod.MarkedAPType):
    def __init__(self, RestFSM=None, RequestFSM=None, TotalVolumeAnhydrousSpirit=None, TotalVolumeMarkedAP=None, **kwargs_):
        super(MarkedAPTypeSub, self).__init__(RestFSM, RequestFSM, TotalVolumeAnhydrousSpirit, TotalVolumeMarkedAP,  **kwargs_)
supermod.MarkedAPType.subclass = MarkedAPTypeSub
# end class MarkedAPTypeSub


class WinemakingAPTypeSub(supermod.WinemakingAPType):
    def __init__(self, Raw=None, VolumeGrape=None, VolumeGrapeGeographical=None, VolumeGrapeRegion=None, VolumeGrapeGrowing=None, TotalRaw=None, **kwargs_):
        super(WinemakingAPTypeSub, self).__init__(Raw, VolumeGrape, VolumeGrapeGeographical, VolumeGrapeRegion, VolumeGrapeGrowing, TotalRaw,  **kwargs_)
supermod.WinemakingAPType.subclass = WinemakingAPTypeSub
# end class WinemakingAPTypeSub


class WinemakingAPSTPTypeSub(supermod.WinemakingAPSTPType):
    def __init__(self, Raw=None, VolumeRest=None, VolumeGrapeCollect=None, VolumeGrapeUse=None, VolumeToAgingRaw=None, VolumeFromAgingRaw=None, VolumeUsedgRaw=None, TotalRaw=None, **kwargs_):
        super(WinemakingAPSTPTypeSub, self).__init__(Raw, VolumeRest, VolumeGrapeCollect, VolumeGrapeUse, VolumeToAgingRaw, VolumeFromAgingRaw, VolumeUsedgRaw, TotalRaw,  **kwargs_)
supermod.WinemakingAPSTPType.subclass = WinemakingAPSTPTypeSub
# end class WinemakingAPSTPTypeSub


class RequestManufacturerFSMTypeSub(supermod.RequestManufacturerFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RequestManufacturerFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RequestManufacturerFSMType.subclass = RequestManufacturerFSMTypeSub
# end class RequestManufacturerFSMTypeSub


class PositionReportTypeSub(supermod.PositionReportType):
    def __init__(self, Identity=None, VidAP171fz=None, MarkType=None, Quantity=None, **kwargs_):
        super(PositionReportTypeSub, self).__init__(Identity, VidAP171fz, MarkType, Quantity,  **kwargs_)
supermod.PositionReportType.subclass = PositionReportTypeSub
# end class PositionReportTypeSub


class TTNShipmentFSMTypeSub(supermod.TTNShipmentFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(TTNShipmentFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.TTNShipmentFSMType.subclass = TTNShipmentFSMTypeSub
# end class TTNShipmentFSMTypeSub


class PositionTTNFSMTypeSub(supermod.PositionTTNFSMType):
    def __init__(self, Identity=None, SampleFSM=None, MarkType=None, RollNumber=None, RangeNumberInRoll=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionTTNFSMTypeSub, self).__init__(Identity, SampleFSM, MarkType, RollNumber, RangeNumberInRoll, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionTTNFSMType.subclass = PositionTTNFSMTypeSub
# end class PositionTTNFSMTypeSub


class TTNIssueFSMTypeSub(supermod.TTNIssueFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(TTNIssueFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.TTNIssueFSMType.subclass = TTNIssueFSMTypeSub
# end class TTNIssueFSMTypeSub


class PositionTTNIssueFSMTypeSub(supermod.PositionTTNIssueFSMType):
    def __init__(self, Identity=None, SampleFSM=None, MarkType=None, RollNumber=None, RangeNumberInRoll=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionTTNIssueFSMTypeSub, self).__init__(Identity, SampleFSM, MarkType, RollNumber, RangeNumberInRoll, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionTTNIssueFSMType.subclass = PositionTTNIssueFSMTypeSub
# end class PositionTTNIssueFSMTypeSub


class RejectionNoticeFSMTypeSub(supermod.RejectionNoticeFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RejectionNoticeFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RejectionNoticeFSMType.subclass = RejectionNoticeFSMTypeSub
# end class RejectionNoticeFSMTypeSub


class PositionRejectionNoticeFSMTypeSub(supermod.PositionRejectionNoticeFSMType):
    def __init__(self, Identity=None, RejectionReasonCode=None, RejectionReason=None, **kwargs_):
        super(PositionRejectionNoticeFSMTypeSub, self).__init__(Identity, RejectionReasonCode, RejectionReason,  **kwargs_)
supermod.PositionRejectionNoticeFSMType.subclass = PositionRejectionNoticeFSMTypeSub
# end class PositionRejectionNoticeFSMTypeSub


class ReturnNoticeFSMTypeSub(supermod.ReturnNoticeFSMType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(ReturnNoticeFSMTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.ReturnNoticeFSMType.subclass = ReturnNoticeFSMTypeSub
# end class ReturnNoticeFSMTypeSub


class RecheckNotificationsFSMTypeSub(supermod.RecheckNotificationsFSMType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(RecheckNotificationsFSMTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.RecheckNotificationsFSMType.subclass = RecheckNotificationsFSMTypeSub
# end class RecheckNotificationsFSMTypeSub


class ReplyPlaceOfBusinessSub(supermod.ReplyPlaceOfBusiness):
    def __init__(self, Clients=None, **kwargs_):
        super(ReplyPlaceOfBusinessSub, self).__init__(Clients,  **kwargs_)
supermod.ReplyPlaceOfBusiness.subclass = ReplyPlaceOfBusinessSub
# end class ReplyPlaceOfBusinessSub


class QueryGenerationOpenKeyTypeSub(supermod.QueryGenerationOpenKeyType):
    def __init__(self, ClientId=None, CertificateRequest=None, **kwargs_):
        super(QueryGenerationOpenKeyTypeSub, self).__init__(ClientId, CertificateRequest,  **kwargs_)
supermod.QueryGenerationOpenKeyType.subclass = QueryGenerationOpenKeyTypeSub
# end class QueryGenerationOpenKeyTypeSub


class ReplyGenerationOpenKeyTypeSub(supermod.ReplyGenerationOpenKeyType):
    def __init__(self, ClientId=None, Certificate=None, **kwargs_):
        super(ReplyGenerationOpenKeyTypeSub, self).__init__(ClientId, Certificate,  **kwargs_)
supermod.ReplyGenerationOpenKeyType.subclass = ReplyGenerationOpenKeyTypeSub
# end class ReplyGenerationOpenKeyTypeSub


class InvoiceIssueAMTypeSub(supermod.InvoiceIssueAMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(InvoiceIssueAMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.InvoiceIssueAMType.subclass = InvoiceIssueAMTypeSub
# end class InvoiceIssueAMTypeSub


class PositionInvoiceIssueAMTypeSub(supermod.PositionInvoiceIssueAMType):
    def __init__(self, Identity=None, MarkType=None, MarkTypeCode=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionInvoiceIssueAMTypeSub, self).__init__(Identity, MarkType, MarkTypeCode, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionInvoiceIssueAMType.subclass = PositionInvoiceIssueAMTypeSub
# end class PositionInvoiceIssueAMTypeSub


class InvoiceExportFSMTypeSub(supermod.InvoiceExportFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(InvoiceExportFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.InvoiceExportFSMType.subclass = InvoiceExportFSMTypeSub
# end class InvoiceExportFSMTypeSub


class PositionInvoiceExportFSMTypeSub(supermod.PositionInvoiceExportFSMType):
    def __init__(self, Identity=None, MarkType=None, MarkTypeCode=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionInvoiceExportFSMTypeSub, self).__init__(Identity, MarkType, MarkTypeCode, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionInvoiceExportFSMType.subclass = PositionInvoiceExportFSMTypeSub
# end class PositionInvoiceExportFSMTypeSub


class InvoicePlannedImportTypeSub(supermod.InvoicePlannedImportType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(InvoicePlannedImportTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.InvoicePlannedImportType.subclass = InvoicePlannedImportTypeSub
# end class InvoicePlannedImportTypeSub


class PositionInvoicePlannedImportTypeSub(supermod.PositionInvoicePlannedImportType):
    def __init__(self, Identity=None, MarkType=None, MarkTypeCode=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionInvoicePlannedImportTypeSub, self).__init__(Identity, MarkType, MarkTypeCode, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionInvoicePlannedImportType.subclass = PositionInvoicePlannedImportTypeSub
# end class PositionInvoicePlannedImportTypeSub


class NotificationsBeginningTurnoverTypeSub(supermod.NotificationsBeginningTurnoverType):
    def __init__(self, Identity=None, Header=None, CompositionProducts=None, IdentifyingDocuments=None, Declaration=None, **kwargs_):
        super(NotificationsBeginningTurnoverTypeSub, self).__init__(Identity, Header, CompositionProducts, IdentifyingDocuments, Declaration,  **kwargs_)
supermod.NotificationsBeginningTurnoverType.subclass = NotificationsBeginningTurnoverTypeSub
# end class NotificationsBeginningTurnoverTypeSub


class PositionCompositionProductsTypeSub(supermod.PositionCompositionProductsType):
    def __init__(self, Identity=None, IngredientType=None, IngredientCode=None, IngredientName=None, **kwargs_):
        super(PositionCompositionProductsTypeSub, self).__init__(Identity, IngredientType, IngredientCode, IngredientName,  **kwargs_)
supermod.PositionCompositionProductsType.subclass = PositionCompositionProductsTypeSub
# end class PositionCompositionProductsTypeSub


class PositionIdentifyingDocumentsTypeSub(supermod.PositionIdentifyingDocumentsType):
    def __init__(self, Identity=None, DocumentVid=None, DocumentNumber=None, ElectronicView=None, **kwargs_):
        super(PositionIdentifyingDocumentsTypeSub, self).__init__(Identity, DocumentVid, DocumentNumber, ElectronicView,  **kwargs_)
supermod.PositionIdentifyingDocumentsType.subclass = PositionIdentifyingDocumentsTypeSub
# end class PositionIdentifyingDocumentsTypeSub


class PositionDeclarationTypeSub(supermod.PositionDeclarationType):
    def __init__(self, Identity=None, DeclarationtVid=None, DeclarationNumber=None, DateValidity=None, DateExpiration=None, **kwargs_):
        super(PositionDeclarationTypeSub, self).__init__(Identity, DeclarationtVid, DeclarationNumber, DateValidity, DateExpiration,  **kwargs_)
supermod.PositionDeclarationType.subclass = PositionDeclarationTypeSub
# end class PositionDeclarationTypeSub


class ChequeV3TypeSub(supermod.ChequeV3Type):
    def __init__(self, Identity=None, Header=None, HeaderTTN=None, Content=None, **kwargs_):
        super(ChequeV3TypeSub, self).__init__(Identity, Header, HeaderTTN, Content,  **kwargs_)
supermod.ChequeV3Type.subclass = ChequeV3TypeSub
# end class ChequeV3TypeSub


class HeaderSub(supermod.Header):
    def __init__(self, Date=None, Kassa=None, Shift=None, Number=None, Type=None, ConfirmOrder=None, **kwargs_):
        super(HeaderSub, self).__init__(Date, Kassa, Shift, Number, Type, ConfirmOrder,  **kwargs_)
supermod.Header.subclass = HeaderSub
# end class HeaderSub


class HeaderTTNSub(supermod.HeaderTTN):
    def __init__(self, Date=None, BillNumber=None, TTNNumber=None, Type=None, **kwargs_):
        super(HeaderTTNSub, self).__init__(Date, BillNumber, TTNNumber, Type,  **kwargs_)
supermod.HeaderTTN.subclass = HeaderTTNSub
# end class HeaderTTNSub


class BottleSub(supermod.Bottle):
    def __init__(self, Barcode=None, EAN=None, Price=None, **kwargs_):
        super(BottleSub, self).__init__(Barcode, EAN, Price,  **kwargs_)
supermod.Bottle.subclass = BottleSub
# end class BottleSub


class NomarkSub(supermod.Nomark):
    def __init__(self, PosIdentity=None, Product=None, Quantity=None, EAN=None, Price=None, **kwargs_):
        super(NomarkSub, self).__init__(PosIdentity, Product, Quantity, EAN, Price,  **kwargs_)
supermod.Nomark.subclass = NomarkSub
# end class NomarkSub


class RepProducedType_v4Sub(supermod.RepProducedType_v4):
    def __init__(self, Identity=None, Header=None, Content=None, ContentResource=None, **kwargs_):
        super(RepProducedType_v4Sub, self).__init__(Identity, Header, Content, ContentResource,  **kwargs_)
supermod.RepProducedType_v4.subclass = RepProducedType_v4Sub
# end class RepProducedType_v4Sub


class PositionType53Sub(supermod.PositionType53):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType53Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType53.subclass = PositionType53Sub
# end class PositionType53Sub


class UsedResourceType54Sub(supermod.UsedResourceType54):
    def __init__(self, IdentityRes=None, Product=None, RegForm2=None, Quantity=None, MarkInfo=None, **kwargs_):
        super(UsedResourceType54Sub, self).__init__(IdentityRes, Product, RegForm2, Quantity, MarkInfo,  **kwargs_)
supermod.UsedResourceType54.subclass = UsedResourceType54Sub
# end class UsedResourceType54Sub


class RepImportedType_v4Sub(supermod.RepImportedType_v4):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RepImportedType_v4Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RepImportedType_v4.subclass = RepImportedType_v4Sub
# end class RepImportedType_v4Sub


class PositionType56Sub(supermod.PositionType56):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, PlannedImport=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType56Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, PlannedImport, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType56.subclass = PositionType56Sub
# end class PositionType56Sub


class ReportDestructionAMFSMTypeSub(supermod.ReportDestructionAMFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ReportDestructionAMFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ReportDestructionAMFSMType.subclass = ReportDestructionAMFSMTypeSub
# end class ReportDestructionAMFSMTypeSub


class PositionAMFSMTypeSub(supermod.PositionAMFSMType):
    def __init__(self, Identity=None, CauseOfDestruction=None, SampleFSM=None, MarkType=None, RollNumber=None, RangeNumberInRoll=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionAMFSMTypeSub, self).__init__(Identity, CauseOfDestruction, SampleFSM, MarkType, RollNumber, RangeNumberInRoll, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionAMFSMType.subclass = PositionAMFSMTypeSub
# end class PositionAMFSMTypeSub


class RequestRepealIPISub(supermod.RequestRepealIPI):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, IPIRegId=None, **kwargs_):
        super(RequestRepealIPISub, self).__init__(ClientId, RequestNumber, RequestDate, IPIRegId,  **kwargs_)
supermod.RequestRepealIPI.subclass = RequestRepealIPISub
# end class RequestRepealIPISub


class RequestRepealEFSMSub(supermod.RequestRepealEFSM):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, EFSMRegId=None, **kwargs_):
        super(RequestRepealEFSMSub, self).__init__(ClientId, RequestNumber, RequestDate, EFSMRegId,  **kwargs_)
supermod.RequestRepealEFSM.subclass = RequestRepealEFSMSub
# end class RequestRepealEFSMSub


class RequestRepealIAMSub(supermod.RequestRepealIAM):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, IAMRegId=None, **kwargs_):
        super(RequestRepealIAMSub, self).__init__(ClientId, RequestNumber, RequestDate, IAMRegId,  **kwargs_)
supermod.RequestRepealIAM.subclass = RequestRepealIAMSub
# end class RequestRepealIAMSub


class TTNShipmentReturnFSMTypeSub(supermod.TTNShipmentReturnFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(TTNShipmentReturnFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.TTNShipmentReturnFSMType.subclass = TTNShipmentReturnFSMTypeSub
# end class TTNShipmentReturnFSMTypeSub


class PositionTTNFSMType57Sub(supermod.PositionTTNFSMType57):
    def __init__(self, Identity=None, SampleFSM=None, MarkType=None, RollNumber=None, RangeNumberInRoll=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionTTNFSMType57Sub, self).__init__(Identity, SampleFSM, MarkType, RollNumber, RangeNumberInRoll, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionTTNFSMType57.subclass = PositionTTNFSMType57Sub
# end class PositionTTNFSMType57Sub


class TTNIssueReturnFSMTypeSub(supermod.TTNIssueReturnFSMType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(TTNIssueReturnFSMTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.TTNIssueReturnFSMType.subclass = TTNIssueReturnFSMTypeSub
# end class TTNIssueReturnFSMTypeSub


class PositionTTNIssueReturnFSMTypeSub(supermod.PositionTTNIssueReturnFSMType):
    def __init__(self, Identity=None, SampleFSM=None, MarkType=None, RollNumber=None, RangeNumberInRoll=None, Rank=None, Start=None, Last=None, QuantityRange=None, **kwargs_):
        super(PositionTTNIssueReturnFSMTypeSub, self).__init__(Identity, SampleFSM, MarkType, RollNumber, RangeNumberInRoll, Rank, Start, Last, QuantityRange,  **kwargs_)
supermod.PositionTTNIssueReturnFSMType.subclass = PositionTTNIssueReturnFSMTypeSub
# end class PositionTTNIssueReturnFSMTypeSub


class ReferenceOfDeficienciesSub(supermod.ReferenceOfDeficiencies):
    def __init__(self, Header=None, **kwargs_):
        super(ReferenceOfDeficienciesSub, self).__init__(Header,  **kwargs_)
supermod.ReferenceOfDeficiencies.subclass = ReferenceOfDeficienciesSub
# end class ReferenceOfDeficienciesSub


class ManufacturingNoticeFSMSub(supermod.ManufacturingNoticeFSM):
    def __init__(self, Header=None, **kwargs_):
        super(ManufacturingNoticeFSMSub, self).__init__(Header,  **kwargs_)
supermod.ManufacturingNoticeFSM.subclass = ManufacturingNoticeFSMSub
# end class ManufacturingNoticeFSMSub


class WayBillType_v4Sub(supermod.WayBillType_v4):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(WayBillType_v4Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.WayBillType_v4.subclass = WayBillType_v4Sub
# end class WayBillType_v4Sub


class PositionType58Sub(supermod.PositionType58):
    def __init__(self, Product=None, Pack_ID=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Price=None, Party=None, Identity=None, EXCISE_NUMBER=None, EXCISE_DATE=None, EXCISE_SUM=None, EXCISE_BS=None, EAN13=None, FARegId=None, InformF2=None, boxInfo=None, **kwargs_):
        super(PositionType58Sub, self).__init__(Product, Pack_ID, Quantity, alcPercent, alcPercentMin, alcPercentMax, Price, Party, Identity, EXCISE_NUMBER, EXCISE_DATE, EXCISE_SUM, EXCISE_BS, EAN13, FARegId, InformF2, boxInfo,  **kwargs_)
supermod.PositionType58.subclass = PositionType58Sub
# end class PositionType58Sub


class TransportType59Sub(supermod.TransportType59):
    def __init__(self, ChangeOwnership=None, TRAN_TYPE=None, TRAN_COMPANY=None, TRANSPORT_TYPE=None, TRANSPORT_REGNUMBER=None, TRAN_TRAILER=None, TRAN_CUSTOMER=None, TRAN_DRIVER=None, TRAN_LOADPOINT=None, TRAN_UNLOADPOINT=None, TRAN_REDIRECT=None, TRAN_FORWARDER=None, **kwargs_):
        super(TransportType59Sub, self).__init__(ChangeOwnership, TRAN_TYPE, TRAN_COMPANY, TRANSPORT_TYPE, TRANSPORT_REGNUMBER, TRAN_TRAILER, TRAN_CUSTOMER, TRAN_DRIVER, TRAN_LOADPOINT, TRAN_UNLOADPOINT, TRAN_REDIRECT, TRAN_FORWARDER,  **kwargs_)
supermod.TransportType59.subclass = TransportType59Sub
# end class TransportType59Sub


class WayBillActType_v4Sub(supermod.WayBillActType_v4):
    def __init__(self, Identity=None, Header=None, Content=None, Transport=None, **kwargs_):
        super(WayBillActType_v4Sub, self).__init__(Identity, Header, Content, Transport,  **kwargs_)
supermod.WayBillActType_v4.subclass = WayBillActType_v4Sub
# end class WayBillActType_v4Sub


class PositionType62Sub(supermod.PositionType62):
    def __init__(self, Identity=None, InformF2RegId=None, RealQuantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, MarkInfo=None, **kwargs_):
        super(PositionType62Sub, self).__init__(Identity, InformF2RegId, RealQuantity, alcPercent, alcPercentMin, alcPercentMax, MarkInfo,  **kwargs_)
supermod.PositionType62.subclass = PositionType62Sub
# end class PositionType62Sub


class TransportActTypeSub(supermod.TransportActType):
    def __init__(self, ChangeOwnership=None, **kwargs_):
        super(TransportActTypeSub, self).__init__(ChangeOwnership,  **kwargs_)
supermod.TransportActType.subclass = TransportActTypeSub
# end class TransportActTypeSub


class RouteSub(supermod.Route):
    def __init__(self, NUMBER=None, Date=None, Ownership=None, WBRegId=None, ParentRoutes=None, TRAN_TYPE=None, TRAN_COMPANY=None, TRAN_CAR=None, TRAN_TRAILER=None, TRAN_CUSTOMER=None, TRAN_DRIVER=None, TRAN_LOADPOINT=None, TRAN_UNLOADPOINT=None, TRAN_REDIRECT=None, TRAN_FORWARDER=None, Quantity=None, **kwargs_):
        super(RouteSub, self).__init__(NUMBER, Date, Ownership, WBRegId, ParentRoutes, TRAN_TYPE, TRAN_COMPANY, TRAN_CAR, TRAN_TRAILER, TRAN_CUSTOMER, TRAN_DRIVER, TRAN_LOADPOINT, TRAN_UNLOADPOINT, TRAN_REDIRECT, TRAN_FORWARDER, Quantity,  **kwargs_)
supermod.Route.subclass = RouteSub
# end class RouteSub


class CancelRouteSub(supermod.CancelRoute):
    def __init__(self, Date=None, RouteId=None, **kwargs_):
        super(CancelRouteSub, self).__init__(Date, RouteId,  **kwargs_)
supermod.CancelRoute.subclass = CancelRouteSub
# end class CancelRouteSub


class DebtAbsenceTypeSub(supermod.DebtAbsenceType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(DebtAbsenceTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.DebtAbsenceType.subclass = DebtAbsenceTypeSub
# end class DebtAbsenceTypeSub


class RequestAdjustmentDataSub(supermod.RequestAdjustmentData):
    def __init__(self, ClientId=None, RequestNumber=None, RequestDate=None, ProveDocs=None, Content=None, **kwargs_):
        super(RequestAdjustmentDataSub, self).__init__(ClientId, RequestNumber, RequestDate, ProveDocs, Content,  **kwargs_)
supermod.RequestAdjustmentData.subclass = RequestAdjustmentDataSub
# end class RequestAdjustmentDataSub


class RequestAdjustmentPositionTypeSub(supermod.RequestAdjustmentPositionType):
    def __init__(self, TTN=None, TTNPos=None, ReportProduced=None, ReportImported=None, ActWO=None, ActWOPos=None, ActWOS=None, ActWOSPos=None, ActCO=None, ActTTN=None, Route=None, **kwargs_):
        super(RequestAdjustmentPositionTypeSub, self).__init__(TTN, TTNPos, ReportProduced, ReportImported, ActWO, ActWOPos, ActWOS, ActWOSPos, ActCO, ActTTN, Route,  **kwargs_)
supermod.RequestAdjustmentPositionType.subclass = RequestAdjustmentPositionTypeSub
# end class RequestAdjustmentPositionTypeSub


class TTNTypeSub(supermod.TTNType):
    def __init__(self, WBRegId=None, NUMBER=None, Date=None, ShippingDate=None, Type=None, Transport=None, **kwargs_):
        super(TTNTypeSub, self).__init__(WBRegId, NUMBER, Date, ShippingDate, Type, Transport,  **kwargs_)
supermod.TTNType.subclass = TTNTypeSub
# end class TTNTypeSub


class TTNPosTypeSub(supermod.TTNPosType):
    def __init__(self, WBRegId=None, Identity=None, Price=None, EXCISE_NUMBER=None, EXCISE_DATE=None, EXCISE_SUM=None, EXCISE_BS=None, **kwargs_):
        super(TTNPosTypeSub, self).__init__(WBRegId, Identity, Price, EXCISE_NUMBER, EXCISE_DATE, EXCISE_SUM, EXCISE_BS,  **kwargs_)
supermod.TTNPosType.subclass = TTNPosTypeSub
# end class TTNPosTypeSub


class ReportProducedTypeSub(supermod.ReportProducedType):
    def __init__(self, RegId=None, NUMBER=None, Date=None, ProducedDate=None, **kwargs_):
        super(ReportProducedTypeSub, self).__init__(RegId, NUMBER, Date, ProducedDate,  **kwargs_)
supermod.ReportProducedType.subclass = ReportProducedTypeSub
# end class ReportProducedTypeSub


class ReportImportedTypeSub(supermod.ReportImportedType):
    def __init__(self, RegId=None, NUMBER=None, Date=None, ImportedDate=None, GTDNUMBER=None, GTDDate=None, Country=None, supplierOwnerid=None, **kwargs_):
        super(ReportImportedTypeSub, self).__init__(RegId, NUMBER, Date, ImportedDate, GTDNUMBER, GTDDate, Country, supplierOwnerid,  **kwargs_)
supermod.ReportImportedType.subclass = ReportImportedTypeSub
# end class ReportImportedTypeSub


class ActWOTypeSub(supermod.ActWOType):
    def __init__(self, AWORegId=None, ActNumber=None, ActDate=None, TypeWriteOff=None, **kwargs_):
        super(ActWOTypeSub, self).__init__(AWORegId, ActNumber, ActDate, TypeWriteOff,  **kwargs_)
supermod.ActWOType.subclass = ActWOTypeSub
# end class ActWOTypeSub


class ActWOPosTypeSub(supermod.ActWOPosType):
    def __init__(self, AWORegId=None, Identity=None, SumSale=None, **kwargs_):
        super(ActWOPosTypeSub, self).__init__(AWORegId, Identity, SumSale,  **kwargs_)
supermod.ActWOPosType.subclass = ActWOPosTypeSub
# end class ActWOPosTypeSub


class ActWOSTypeSub(supermod.ActWOSType):
    def __init__(self, AWOSRegId=None, ActNumber=None, ActDate=None, TypeWriteOff=None, **kwargs_):
        super(ActWOSTypeSub, self).__init__(AWOSRegId, ActNumber, ActDate, TypeWriteOff,  **kwargs_)
supermod.ActWOSType.subclass = ActWOSTypeSub
# end class ActWOSTypeSub


class ActWOSPosTypeSub(supermod.ActWOSPosType):
    def __init__(self, AWOSRegId=None, Identity=None, SumSale=None, **kwargs_):
        super(ActWOSPosTypeSub, self).__init__(AWOSRegId, Identity, SumSale,  **kwargs_)
supermod.ActWOSPosType.subclass = ActWOSPosTypeSub
# end class ActWOSPosTypeSub


class ActCOTypeSub(supermod.ActCOType):
    def __init__(self, ACORegId=None, Number=None, ActDate=None, **kwargs_):
        super(ActCOTypeSub, self).__init__(ACORegId, Number, ActDate,  **kwargs_)
supermod.ActCOType.subclass = ActCOTypeSub
# end class ActCOTypeSub


class ActTTNTypeSub(supermod.ActTTNType):
    def __init__(self, WBRegId=None, ACTNUMBER=None, ActDate=None, **kwargs_):
        super(ActTTNTypeSub, self).__init__(WBRegId, ACTNUMBER, ActDate,  **kwargs_)
supermod.ActTTNType.subclass = ActTTNTypeSub
# end class ActTTNTypeSub


class RouteTypeSub(supermod.RouteType):
    def __init__(self, RegId=None, Date=None, TRAN_TYPE=None, TRAN_COMPANY=None, TRAN_CAR=None, TRAN_TRAILER=None, TRAN_CUSTOMER=None, TRAN_DRIVER=None, TRAN_LOADPOINT=None, TRAN_UNLOADPOINT=None, TRAN_REDIRECT=None, TRAN_FORWARDER=None, **kwargs_):
        super(RouteTypeSub, self).__init__(RegId, Date, TRAN_TYPE, TRAN_COMPANY, TRAN_CAR, TRAN_TRAILER, TRAN_CUSTOMER, TRAN_DRIVER, TRAN_LOADPOINT, TRAN_UNLOADPOINT, TRAN_REDIRECT, TRAN_FORWARDER,  **kwargs_)
supermod.RouteType.subclass = RouteTypeSub
# end class RouteTypeSub


class ActCancelOnlineOrderTypeSub(supermod.ActCancelOnlineOrderType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(ActCancelOnlineOrderTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.ActCancelOnlineOrderType.subclass = ActCancelOnlineOrderTypeSub
# end class ActCancelOnlineOrderTypeSub


class ActConfirmOnlineOrderTypeSub(supermod.ActConfirmOnlineOrderType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActConfirmOnlineOrderTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActConfirmOnlineOrderType.subclass = ActConfirmOnlineOrderTypeSub
# end class ActConfirmOnlineOrderTypeSub


class ActConfirmOnlineOrderPositionTypeSub(supermod.ActConfirmOnlineOrderPositionType):
    def __init__(self, Identity=None, Product=None, Quantity=None, SumSale=None, F2Detail=None, **kwargs_):
        super(ActConfirmOnlineOrderPositionTypeSub, self).__init__(Identity, Product, Quantity, SumSale, F2Detail,  **kwargs_)
supermod.ActConfirmOnlineOrderPositionType.subclass = ActConfirmOnlineOrderPositionTypeSub
# end class ActConfirmOnlineOrderPositionTypeSub


class F2DetailTypeSub(supermod.F2DetailType):
    def __init__(self, InformF2=None, QuantityF2=None, Price=None, **kwargs_):
        super(F2DetailTypeSub, self).__init__(InformF2, QuantityF2, Price,  **kwargs_)
supermod.F2DetailType.subclass = F2DetailTypeSub
# end class F2DetailTypeSub


class ActReceiptOnlineOrderTypeSub(supermod.ActReceiptOnlineOrderType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActReceiptOnlineOrderTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActReceiptOnlineOrderType.subclass = ActReceiptOnlineOrderTypeSub
# end class ActReceiptOnlineOrderTypeSub


class ActReceiptOnlineOrderPositionTypeSub(supermod.ActReceiptOnlineOrderPositionType):
    def __init__(self, Identity=None, Product=None, Quantity=None, SumSale=None, **kwargs_):
        super(ActReceiptOnlineOrderPositionTypeSub, self).__init__(Identity, Product, Quantity, SumSale,  **kwargs_)
supermod.ActReceiptOnlineOrderPositionType.subclass = ActReceiptOnlineOrderPositionTypeSub
# end class ActReceiptOnlineOrderPositionTypeSub


class RequestBalanceTransferSub(supermod.RequestBalanceTransfer):
    def __init__(self, Header=None, **kwargs_):
        super(RequestBalanceTransferSub, self).__init__(Header,  **kwargs_)
supermod.RequestBalanceTransfer.subclass = RequestBalanceTransferSub
# end class RequestBalanceTransferSub


class RequestManufacturerFSMforCheckTypeSub(supermod.RequestManufacturerFSMforCheckType):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RequestManufacturerFSMforCheckTypeSub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RequestManufacturerFSMforCheckType.subclass = RequestManufacturerFSMforCheckTypeSub
# end class RequestManufacturerFSMforCheckTypeSub


class PositionReportType67Sub(supermod.PositionReportType67):
    def __init__(self, Identity=None, VidAP171fz=None, MarkType=None, Quantity=None, **kwargs_):
        super(PositionReportType67Sub, self).__init__(Identity, VidAP171fz, MarkType, Quantity,  **kwargs_)
supermod.PositionReportType67.subclass = PositionReportType67Sub
# end class PositionReportType67Sub


class TicketRMCheckTypeSub(supermod.TicketRMCheckType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(TicketRMCheckTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.TicketRMCheckType.subclass = TicketRMCheckTypeSub
# end class TicketRMCheckTypeSub


class FrapClaimsTypeSub(supermod.FrapClaimsType):
    def __init__(self, NameDoc=None, Header=None, **kwargs_):
        super(FrapClaimsTypeSub, self).__init__(NameDoc, Header,  **kwargs_)
supermod.FrapClaimsType.subclass = FrapClaimsTypeSub
# end class FrapClaimsTypeSub


class PositionCompositionProductsType69Sub(supermod.PositionCompositionProductsType69):
    def __init__(self, Identity=None, CompulsoryRawMaterials=None, CompulsoryRawMaterialsDescr=None, OtherAP=None, OtherRawMaterials=None, **kwargs_):
        super(PositionCompositionProductsType69Sub, self).__init__(Identity, CompulsoryRawMaterials, CompulsoryRawMaterialsDescr, OtherAP, OtherRawMaterials,  **kwargs_)
supermod.PositionCompositionProductsType69.subclass = PositionCompositionProductsType69Sub
# end class PositionCompositionProductsType69Sub


class PositionAdditionalDocumentsTypeSub(supermod.PositionAdditionalDocumentsType):
    def __init__(self, Identity=None, AdditionalDoc=None, **kwargs_):
        super(PositionAdditionalDocumentsTypeSub, self).__init__(Identity, AdditionalDoc,  **kwargs_)
supermod.PositionAdditionalDocumentsType.subclass = PositionAdditionalDocumentsTypeSub
# end class PositionAdditionalDocumentsTypeSub


class PositionDeclarationType70Sub(supermod.PositionDeclarationType70):
    def __init__(self, Identity=None, DeclarCertif=None, **kwargs_):
        super(PositionDeclarationType70Sub, self).__init__(Identity, DeclarCertif,  **kwargs_)
supermod.PositionDeclarationType70.subclass = PositionDeclarationType70Sub
# end class PositionDeclarationType70Sub


class NameAPTypeSub(supermod.NameAPType):
    def __init__(self, FullName=None, TypeBeer=None, BeerProcessingMethod=None, **kwargs_):
        super(NameAPTypeSub, self).__init__(FullName, TypeBeer, BeerProcessingMethod,  **kwargs_)
supermod.NameAPType.subclass = NameAPTypeSub
# end class NameAPTypeSub


class CapacityTypeSub(supermod.CapacityType):
    def __init__(self, Capacity=None, DescriptionPackaging=None, ShelfLife=None, **kwargs_):
        super(CapacityTypeSub, self).__init__(Capacity, DescriptionPackaging, ShelfLife,  **kwargs_)
supermod.CapacityType.subclass = CapacityTypeSub
# end class CapacityTypeSub


class DescriptionPackagingTypeSub(supermod.DescriptionPackagingType):
    def __init__(self, PackageType=None, ContComposition=None, LabelFotoAP=None, **kwargs_):
        super(DescriptionPackagingTypeSub, self).__init__(PackageType, ContComposition, LabelFotoAP,  **kwargs_)
supermod.DescriptionPackagingType.subclass = DescriptionPackagingTypeSub
# end class DescriptionPackagingTypeSub


class TrademarkDetailsTypeSub(supermod.TrademarkDetailsType):
    def __init__(self, TrademarkName=None, StateRegistrationNumber=None, DateStateRegistration=None, NameCopyrightHolder=None, **kwargs_):
        super(TrademarkDetailsTypeSub, self).__init__(TrademarkName, StateRegistrationNumber, DateStateRegistration, NameCopyrightHolder,  **kwargs_)
supermod.TrademarkDetailsType.subclass = TrademarkDetailsTypeSub
# end class TrademarkDetailsTypeSub


class FrapClaimsCorTypeSub(supermod.FrapClaimsCorType):
    def __init__(self, NameDoc=None, Header=None, **kwargs_):
        super(FrapClaimsCorTypeSub, self).__init__(NameDoc, Header,  **kwargs_)
supermod.FrapClaimsCorType.subclass = FrapClaimsCorTypeSub
# end class FrapClaimsCorTypeSub


class PositionCompositionProductsType71Sub(supermod.PositionCompositionProductsType71):
    def __init__(self, Identity=None, CompulsoryRawMaterials=None, CompulsoryRawMaterialsDescr=None, OtherAP=None, OtherRawMaterials=None, **kwargs_):
        super(PositionCompositionProductsType71Sub, self).__init__(Identity, CompulsoryRawMaterials, CompulsoryRawMaterialsDescr, OtherAP, OtherRawMaterials,  **kwargs_)
supermod.PositionCompositionProductsType71.subclass = PositionCompositionProductsType71Sub
# end class PositionCompositionProductsType71Sub


class CapacityType72Sub(supermod.CapacityType72):
    def __init__(self, Capacity=None, DescriptionPackaging=None, ShelfLife=None, **kwargs_):
        super(CapacityType72Sub, self).__init__(Capacity, DescriptionPackaging, ShelfLife,  **kwargs_)
supermod.CapacityType72.subclass = CapacityType72Sub
# end class CapacityType72Sub


class DescriptionPackagingType73Sub(supermod.DescriptionPackagingType73):
    def __init__(self, PackageType=None, ContComposition=None, LabelFotoAP=None, **kwargs_):
        super(DescriptionPackagingType73Sub, self).__init__(PackageType, ContComposition, LabelFotoAP,  **kwargs_)
supermod.DescriptionPackagingType73.subclass = DescriptionPackagingType73Sub
# end class DescriptionPackagingType73Sub


class TrademarkDetailsType74Sub(supermod.TrademarkDetailsType74):
    def __init__(self, TrademarkName=None, StateRegistrationNumber=None, DateStateRegistration=None, NameCopyrightHolder=None, **kwargs_):
        super(TrademarkDetailsType74Sub, self).__init__(TrademarkName, StateRegistrationNumber, DateStateRegistration, NameCopyrightHolder,  **kwargs_)
supermod.TrademarkDetailsType74.subclass = TrademarkDetailsType74Sub
# end class TrademarkDetailsType74Sub


class PositionAdditionalDocumentsType75Sub(supermod.PositionAdditionalDocumentsType75):
    def __init__(self, Identity=None, AdditionalDoc=None, **kwargs_):
        super(PositionAdditionalDocumentsType75Sub, self).__init__(Identity, AdditionalDoc,  **kwargs_)
supermod.PositionAdditionalDocumentsType75.subclass = PositionAdditionalDocumentsType75Sub
# end class PositionAdditionalDocumentsType75Sub


class PositionDeclarationType76Sub(supermod.PositionDeclarationType76):
    def __init__(self, Identity=None, DeclarCertif=None, **kwargs_):
        super(PositionDeclarationType76Sub, self).__init__(Identity, DeclarCertif,  **kwargs_)
supermod.PositionDeclarationType76.subclass = PositionDeclarationType76Sub
# end class PositionDeclarationType76Sub


class ApplicationsTypeSub(supermod.ApplicationsType):
    def __init__(self, Application=None, **kwargs_):
        super(ApplicationsTypeSub, self).__init__(Application,  **kwargs_)
supermod.ApplicationsType.subclass = ApplicationsTypeSub
# end class ApplicationsTypeSub


class GovernmentFeeTypeSub(supermod.GovernmentFeeType):
    def __init__(self, KBK=None, Date=None, Number=None, Total=None, **kwargs_):
        super(GovernmentFeeTypeSub, self).__init__(KBK, Date, Number, Total,  **kwargs_)
supermod.GovernmentFeeType.subclass = GovernmentFeeTypeSub
# end class GovernmentFeeTypeSub


class DivisionTypeSub(supermod.DivisionType):
    def __init__(self, ObjectKPP=None, NameBank=None, Account=None, PhoneNumber=None, EmailAddress=None, ContractNumber=None, ContractDate=None, ObjectName=None, ObjectTime=None, ObjectType=None, BusinessAddress=None, ObjectAddress=None, ObjectNumber=None, ObjectCompanyType=None, ObjectCompanySize=None, ObjectSize=None, ObjectCoordinate=None, **kwargs_):
        super(DivisionTypeSub, self).__init__(ObjectKPP, NameBank, Account, PhoneNumber, EmailAddress, ContractNumber, ContractDate, ObjectName, ObjectTime, ObjectType, BusinessAddress, ObjectAddress, ObjectNumber, ObjectCompanyType, ObjectCompanySize, ObjectSize, ObjectCoordinate,  **kwargs_)
supermod.DivisionType.subclass = DivisionTypeSub
# end class DivisionTypeSub


class RepProducedType_v5Sub(supermod.RepProducedType_v5):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RepProducedType_v5Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RepProducedType_v5.subclass = RepProducedType_v5Sub
# end class RepProducedType_v5Sub


class PositionType77Sub(supermod.PositionType77):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, alcPercentMin=None, alcPercentMax=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, ContentResource=None, **kwargs_):
        super(PositionType77Sub, self).__init__(ProductCode, Quantity, alcPercent, alcPercentMin, alcPercentMax, Party, Identity, Comment1, Comment2, Comment3, MarkInfo, ContentResource,  **kwargs_)
supermod.PositionType77.subclass = PositionType77Sub
# end class PositionType77Sub


class UsedResourceType78Sub(supermod.UsedResourceType78):
    def __init__(self, IdentityRes=None, Product=None, RegForm2=None, Quantity=None, MarkInfo=None, **kwargs_):
        super(UsedResourceType78Sub, self).__init__(IdentityRes, Product, RegForm2, Quantity, MarkInfo,  **kwargs_)
supermod.UsedResourceType78.subclass = UsedResourceType78Sub
# end class UsedResourceType78Sub


class ReturnNotificationsFSMTypeSub(supermod.ReturnNotificationsFSMType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(ReturnNotificationsFSMTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.ReturnNotificationsFSMType.subclass = ReturnNotificationsFSMTypeSub
# end class ReturnNotificationsFSMTypeSub


class TTNInternalMoveFSMTypeSub(supermod.TTNInternalMoveFSMType):
    def __init__(self, Identity=None, Header=None, **kwargs_):
        super(TTNInternalMoveFSMTypeSub, self).__init__(Identity, Header,  **kwargs_)
supermod.TTNInternalMoveFSMType.subclass = TTNInternalMoveFSMTypeSub
# end class TTNInternalMoveFSMTypeSub


class ActWriteOffType_v4Sub(supermod.ActWriteOffType_v4):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(ActWriteOffType_v4Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.ActWriteOffType_v4.subclass = ActWriteOffType_v4Sub
# end class ActWriteOffType_v4Sub


class ActWriteOffPositionType80Sub(supermod.ActWriteOffPositionType80):
    def __init__(self, Identity=None, writeoffvolume=None, SumSale=None, InformF1F2=None, MarkCodeInfo=None, **kwargs_):
        super(ActWriteOffPositionType80Sub, self).__init__(Identity, writeoffvolume, SumSale, InformF1F2, MarkCodeInfo,  **kwargs_)
supermod.ActWriteOffPositionType80.subclass = ActWriteOffPositionType80Sub
# end class ActWriteOffPositionType80Sub


class InformF1F281Sub(supermod.InformF1F281):
    def __init__(self, InformF2=None, InformF1=None, **kwargs_):
        super(InformF1F281Sub, self).__init__(InformF2, InformF1,  **kwargs_)
supermod.InformF1F281.subclass = InformF1F281Sub
# end class InformF1F281Sub


class ChequeV4TypeSub(supermod.ChequeV4Type):
    def __init__(self, Identity=None, Header=None, HeaderTTN=None, Content=None, **kwargs_):
        super(ChequeV4TypeSub, self).__init__(Identity, Header, HeaderTTN, Content,  **kwargs_)
supermod.ChequeV4Type.subclass = ChequeV4TypeSub
# end class ChequeV4TypeSub


class Header82Sub(supermod.Header82):
    def __init__(self, Date=None, Kassa=None, Shift=None, Number=None, Type=None, ConfirmOrder=None, **kwargs_):
        super(Header82Sub, self).__init__(Date, Kassa, Shift, Number, Type, ConfirmOrder,  **kwargs_)
supermod.Header82.subclass = Header82Sub
# end class Header82Sub


class HeaderTTN83Sub(supermod.HeaderTTN83):
    def __init__(self, Date=None, BillNumber=None, TTNNumber=None, Type=None, **kwargs_):
        super(HeaderTTN83Sub, self).__init__(Date, BillNumber, TTNNumber, Type,  **kwargs_)
supermod.HeaderTTN83.subclass = HeaderTTN83Sub
# end class HeaderTTN83Sub


class Bottle84Sub(supermod.Bottle84):
    def __init__(self, Barcode=None, EAN=None, Price=None, **kwargs_):
        super(Bottle84Sub, self).__init__(Barcode, EAN, Price,  **kwargs_)
supermod.Bottle84.subclass = Bottle84Sub
# end class Bottle84Sub


class CateringSub(supermod.Catering):
    def __init__(self, Barcode=None, EAN=None, Price=None, Volume=None, **kwargs_):
        super(CateringSub, self).__init__(Barcode, EAN, Price, Volume,  **kwargs_)
supermod.Catering.subclass = CateringSub
# end class CateringSub


class Nomark85Sub(supermod.Nomark85):
    def __init__(self, PosIdentity=None, Product=None, Quantity=None, EAN=None, Price=None, **kwargs_):
        super(Nomark85Sub, self).__init__(PosIdentity, Product, Quantity, EAN, Price,  **kwargs_)
supermod.Nomark85.subclass = Nomark85Sub
# end class Nomark85Sub


class RepProducedType_v6Sub(supermod.RepProducedType_v6):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RepProducedType_v6Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RepProducedType_v6.subclass = RepProducedType_v6Sub
# end class RepProducedType_v6Sub


class PositionType88Sub(supermod.PositionType88):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, Party=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, ContentResource=None, **kwargs_):
        super(PositionType88Sub, self).__init__(ProductCode, Quantity, alcPercent, Party, Identity, Comment1, Comment2, Comment3, MarkInfo, ContentResource,  **kwargs_)
supermod.PositionType88.subclass = PositionType88Sub
# end class PositionType88Sub


class UsedResourceType89Sub(supermod.UsedResourceType89):
    def __init__(self, IDENTITYPRODUCT=None, Product=None, RegForm2=None, Quantity=None, MarkInfo=None, **kwargs_):
        super(UsedResourceType89Sub, self).__init__(IDENTITYPRODUCT, Product, RegForm2, Quantity, MarkInfo,  **kwargs_)
supermod.UsedResourceType89.subclass = UsedResourceType89Sub
# end class UsedResourceType89Sub


class GRAPERESOURCETypeSub(supermod.GRAPERESOURCEType):
    def __init__(self, IDENTITYGRAPERES=None, GRAPESORT=None, WEIGHT=None, DATEOFRECEIPT=None, VINEYARDNUMBER=None, GRAPESUPPLIER=None, **kwargs_):
        super(GRAPERESOURCETypeSub, self).__init__(IDENTITYGRAPERES, GRAPESORT, WEIGHT, DATEOFRECEIPT, VINEYARDNUMBER, GRAPESUPPLIER,  **kwargs_)
supermod.GRAPERESOURCEType.subclass = GRAPERESOURCETypeSub
# end class GRAPERESOURCETypeSub


class RepImportedType_v5Sub(supermod.RepImportedType_v5):
    def __init__(self, Identity=None, Header=None, Content=None, **kwargs_):
        super(RepImportedType_v5Sub, self).__init__(Identity, Header, Content,  **kwargs_)
supermod.RepImportedType_v5.subclass = RepImportedType_v5Sub
# end class RepImportedType_v5Sub


class PositionType91Sub(supermod.PositionType91):
    def __init__(self, ProductCode=None, Quantity=None, alcPercent=None, Party=None, PlannedImport=None, Identity=None, Comment1=None, Comment2=None, Comment3=None, MarkInfo=None, **kwargs_):
        super(PositionType91Sub, self).__init__(ProductCode, Quantity, alcPercent, Party, PlannedImport, Identity, Comment1, Comment2, Comment3, MarkInfo,  **kwargs_)
supermod.PositionType91.subclass = PositionType91Sub
# end class PositionType91Sub


class addresslistTypeSub(supermod.addresslistType):
    def __init__(self, address=None, **kwargs_):
        super(addresslistTypeSub, self).__init__(address,  **kwargs_)
supermod.addresslistType.subclass = addresslistTypeSub
# end class addresslistTypeSub


class RangesTypeSub(supermod.RangesType):
    def __init__(self, Range=None, **kwargs_):
        super(RangesTypeSub, self).__init__(Range,  **kwargs_)
supermod.RangesType.subclass = RangesTypeSub
# end class RangesTypeSub


class RangeTypeSub(supermod.RangeType):
    def __init__(self, Identity=None, Rank=None, Start=None, Last=None, **kwargs_):
        super(RangeTypeSub, self).__init__(Identity, Rank, Start, Last,  **kwargs_)
supermod.RangeType.subclass = RangeTypeSub
# end class RangeTypeSub


class HeaderTypeSub(supermod.HeaderType):
    def __init__(self, Type='WBInvoiceFromMe', UnitType=None, NUMBER=None, Date=None, ShippingDate=None, Transport=None, Shipper=None, Consignee=None, Supplier=None, Base=None, Note=None, **kwargs_):
        super(HeaderTypeSub, self).__init__(Type, UnitType, NUMBER, Date, ShippingDate, Transport, Shipper, Consignee, Supplier, Base, Note,  **kwargs_)
supermod.HeaderType.subclass = HeaderTypeSub
# end class HeaderTypeSub


class ContentTypeSub(supermod.ContentType):
    def __init__(self, Position=None, **kwargs_):
        super(ContentTypeSub, self).__init__(Position,  **kwargs_)
supermod.ContentType.subclass = ContentTypeSub
# end class ContentTypeSub


class HeaderType96Sub(supermod.HeaderType96):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType96Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType96.subclass = HeaderType96Sub
# end class HeaderType96Sub


class ContentType98Sub(supermod.ContentType98):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType98Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType98.subclass = ContentType98Sub
# end class ContentType98Sub


class HeaderType99Sub(supermod.HeaderType99):
    def __init__(self, IsConfirm=None, TicketNumber=None, TicketDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType99Sub, self).__init__(IsConfirm, TicketNumber, TicketDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType99.subclass = HeaderType99Sub
# end class HeaderType99Sub


class HeaderType101Sub(supermod.HeaderType101):
    def __init__(self, Number=None, DivisionName=None, InventoryBasis=None, InventoryBasisNumber=None, InventoryBasisDate=None, InventoryDateBegin=None, InventoryDateEnd=None, Note=None, **kwargs_):
        super(HeaderType101Sub, self).__init__(Number, DivisionName, InventoryBasis, InventoryBasisNumber, InventoryBasisDate, InventoryDateBegin, InventoryDateEnd, Note,  **kwargs_)
supermod.HeaderType101.subclass = HeaderType101Sub
# end class HeaderType101Sub


class ContentType103Sub(supermod.ContentType103):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType103Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType103.subclass = ContentType103Sub
# end class ContentType103Sub


class InformBType104Sub(supermod.InformBType104):
    def __init__(self, InformBItem=None, **kwargs_):
        super(InformBType104Sub, self).__init__(InformBItem,  **kwargs_)
supermod.InformBType104.subclass = InformBType104Sub
# end class InformBType104Sub


class HeaderType105Sub(supermod.HeaderType105):
    def __init__(self, Number=None, ActDate=None, Note=None, **kwargs_):
        super(HeaderType105Sub, self).__init__(Number, ActDate, Note,  **kwargs_)
supermod.HeaderType105.subclass = HeaderType105Sub
# end class HeaderType105Sub


class ContentType107Sub(supermod.ContentType107):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType107Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType107.subclass = ContentType107Sub
# end class ContentType107Sub


class InformABTypeSub(supermod.InformABType):
    def __init__(self, InformABKey=None, InformABReg=None, **kwargs_):
        super(InformABTypeSub, self).__init__(InformABKey, InformABReg,  **kwargs_)
supermod.InformABType.subclass = InformABTypeSub
# end class InformABTypeSub


class HeaderType108Sub(supermod.HeaderType108):
    def __init__(self, Identity=None, ActRegId=None, Number=None, **kwargs_):
        super(HeaderType108Sub, self).__init__(Identity, ActRegId, Number,  **kwargs_)
supermod.HeaderType108.subclass = HeaderType108Sub
# end class HeaderType108Sub


class ContentType109Sub(supermod.ContentType109):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType109Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType109.subclass = ContentType109Sub
# end class ContentType109Sub


class InformBType110Sub(supermod.InformBType110):
    def __init__(self, InformBItem=None, **kwargs_):
        super(InformBType110Sub, self).__init__(InformBItem,  **kwargs_)
supermod.InformBType110.subclass = InformBType110Sub
# end class InformBType110Sub


class ParametersTypeSub(supermod.ParametersType):
    def __init__(self, Parameter=None, **kwargs_):
        super(ParametersTypeSub, self).__init__(Parameter,  **kwargs_)
supermod.ParametersType.subclass = ParametersTypeSub
# end class ParametersTypeSub


class HeaderType111Sub(supermod.HeaderType111):
    def __init__(self, Identity=None, WBRegId=None, EGAISFixNumber=None, EGAISFixDate=None, WBNUMBER=None, WBDate=None, Shipper=None, Consignee=None, Supplier=None, **kwargs_):
        super(HeaderType111Sub, self).__init__(Identity, WBRegId, EGAISFixNumber, EGAISFixDate, WBNUMBER, WBDate, Shipper, Consignee, Supplier,  **kwargs_)
supermod.HeaderType111.subclass = HeaderType111Sub
# end class HeaderType111Sub


class ContentType112Sub(supermod.ContentType112):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType112Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType112.subclass = ContentType112Sub
# end class ContentType112Sub


class HeaderType113Sub(supermod.HeaderType113):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType113Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType113.subclass = HeaderType113Sub
# end class HeaderType113Sub


class ContentType115Sub(supermod.ContentType115):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType115Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType115.subclass = ContentType115Sub
# end class ContentType115Sub


class HeaderType116Sub(supermod.HeaderType116):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType116Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType116.subclass = HeaderType116Sub
# end class HeaderType116Sub


class ContentType118Sub(supermod.ContentType118):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType118Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType118.subclass = ContentType118Sub
# end class ContentType118Sub


class ContentResourceTypeSub(supermod.ContentResourceType):
    def __init__(self, Resource=None, **kwargs_):
        super(ContentResourceTypeSub, self).__init__(Resource,  **kwargs_)
supermod.ContentResourceType.subclass = ContentResourceTypeSub
# end class ContentResourceTypeSub


class addresslistType119Sub(supermod.addresslistType119):
    def __init__(self, address=None, **kwargs_):
        super(addresslistType119Sub, self).__init__(address,  **kwargs_)
supermod.addresslistType119.subclass = addresslistType119Sub
# end class addresslistType119Sub


class RangesType151Sub(supermod.RangesType151):
    def __init__(self, Range=None, **kwargs_):
        super(RangesType151Sub, self).__init__(Range,  **kwargs_)
supermod.RangesType151.subclass = RangesType151Sub
# end class RangesType151Sub


class RangeType152Sub(supermod.RangeType152):
    def __init__(self, Identity=None, Rank=None, Start=None, Last=None, **kwargs_):
        super(RangeType152Sub, self).__init__(Identity, Rank, Start, Last,  **kwargs_)
supermod.RangeType152.subclass = RangeType152Sub
# end class RangeType152Sub


class HeaderType183Sub(supermod.HeaderType183):
    def __init__(self, NUMBER=None, Date=None, ImportedDate=None, Importer=None, Supplier=None, GTDNUMBER=None, GTDDate=None, ContractNUMBER=None, ContractDate=None, Country=None, Note=None, **kwargs_):
        super(HeaderType183Sub, self).__init__(NUMBER, Date, ImportedDate, Importer, Supplier, GTDNUMBER, GTDDate, ContractNUMBER, ContractDate, Country, Note,  **kwargs_)
supermod.HeaderType183.subclass = HeaderType183Sub
# end class HeaderType183Sub


class ContentType186Sub(supermod.ContentType186):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType186Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType186.subclass = ContentType186Sub
# end class ContentType186Sub


class ProductsType190Sub(supermod.ProductsType190):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType190Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType190.subclass = ProductsType190Sub
# end class ProductsType190Sub


class ProductsType191Sub(supermod.ProductsType191):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType191Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType191.subclass = ProductsType191Sub
# end class ProductsType191Sub


class ClientsTypeSub(supermod.ClientsType):
    def __init__(self, Client=None, **kwargs_):
        super(ClientsTypeSub, self).__init__(Client,  **kwargs_)
supermod.ClientsType.subclass = ClientsTypeSub
# end class ClientsTypeSub


class ProductsType192Sub(supermod.ProductsType192):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType192Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType192.subclass = ProductsType192Sub
# end class ProductsType192Sub


class ProductsType193Sub(supermod.ProductsType193):
    def __init__(self, StockPosition=None, **kwargs_):
        super(ProductsType193Sub, self).__init__(StockPosition,  **kwargs_)
supermod.ProductsType193.subclass = ProductsType193Sub
# end class ProductsType193Sub


class HistoryBTypeSub(supermod.HistoryBType):
    def __init__(self, OperationB=None, **kwargs_):
        super(HistoryBTypeSub, self).__init__(OperationB,  **kwargs_)
supermod.HistoryBType.subclass = HistoryBTypeSub
# end class HistoryBTypeSub


class ProductsType194Sub(supermod.ProductsType194):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType194Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType194.subclass = ProductsType194Sub
# end class ProductsType194Sub


class ProductsType195Sub(supermod.ProductsType195):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType195Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType195.subclass = ProductsType195Sub
# end class ProductsType195Sub


class ClientsType196Sub(supermod.ClientsType196):
    def __init__(self, Client=None, **kwargs_):
        super(ClientsType196Sub, self).__init__(Client,  **kwargs_)
supermod.ClientsType196.subclass = ClientsType196Sub
# end class ClientsType196Sub


class ProductsType197Sub(supermod.ProductsType197):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType197Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType197.subclass = ProductsType197Sub
# end class ProductsType197Sub


class ProductsType198Sub(supermod.ProductsType198):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType198Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType198.subclass = ProductsType198Sub
# end class ProductsType198Sub


class ProductsType199Sub(supermod.ProductsType199):
    def __init__(self, StockPosition=None, **kwargs_):
        super(ProductsType199Sub, self).__init__(StockPosition,  **kwargs_)
supermod.ProductsType199.subclass = ProductsType199Sub
# end class ProductsType199Sub


class HistoryF2TypeSub(supermod.HistoryF2Type):
    def __init__(self, OperationB=None, **kwargs_):
        super(HistoryF2TypeSub, self).__init__(OperationB,  **kwargs_)
supermod.HistoryF2Type.subclass = HistoryF2TypeSub
# end class HistoryF2TypeSub


class HeaderType200Sub(supermod.HeaderType200):
    def __init__(self, Type='WBInvoiceFromMe', NUMBER=None, Date=None, ShippingDate=None, Transport=None, Shipper=None, Consignee=None, Base=None, Note=None, VarField1=None, VarField2=None, VarField3=None, **kwargs_):
        super(HeaderType200Sub, self).__init__(Type, NUMBER, Date, ShippingDate, Transport, Shipper, Consignee, Base, Note, VarField1, VarField2, VarField3,  **kwargs_)
supermod.HeaderType200.subclass = HeaderType200Sub
# end class HeaderType200Sub


class ContentType203Sub(supermod.ContentType203):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType203Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType203.subclass = ContentType203Sub
# end class ContentType203Sub


class HeaderType214Sub(supermod.HeaderType214):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType214Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType214.subclass = HeaderType214Sub
# end class HeaderType214Sub


class ContentType216Sub(supermod.ContentType216):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType216Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType216.subclass = ContentType216Sub
# end class ContentType216Sub


class HeaderType217Sub(supermod.HeaderType217):
    def __init__(self, Number=None, ActDate=None, TypeChargeOn=None, ActWriteOff=None, Note=None, **kwargs_):
        super(HeaderType217Sub, self).__init__(Number, ActDate, TypeChargeOn, ActWriteOff, Note,  **kwargs_)
supermod.HeaderType217.subclass = HeaderType217Sub
# end class HeaderType217Sub


class ContentType219Sub(supermod.ContentType219):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType219Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType219.subclass = ContentType219Sub
# end class ContentType219Sub


class InformF1F2TypeSub(supermod.InformF1F2Type):
    def __init__(self, InformF1F2Reg=None, **kwargs_):
        super(InformF1F2TypeSub, self).__init__(InformF1F2Reg,  **kwargs_)
supermod.InformF1F2Type.subclass = InformF1F2TypeSub
# end class InformF1F2TypeSub


class HeaderType220Sub(supermod.HeaderType220):
    def __init__(self, Identity=None, ActRegId=None, Number=None, **kwargs_):
        super(HeaderType220Sub, self).__init__(Identity, ActRegId, Number,  **kwargs_)
supermod.HeaderType220.subclass = HeaderType220Sub
# end class HeaderType220Sub


class ContentType221Sub(supermod.ContentType221):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType221Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType221.subclass = ContentType221Sub
# end class ContentType221Sub


class InformF2Type222Sub(supermod.InformF2Type222):
    def __init__(self, InformF2Item=None, **kwargs_):
        super(InformF2Type222Sub, self).__init__(InformF2Item,  **kwargs_)
supermod.InformF2Type222.subclass = InformF2Type222Sub
# end class InformF2Type222Sub


class HeaderType223Sub(supermod.HeaderType223):
    def __init__(self, Identity=None, WBRegId=None, EGAISFixNumber=None, EGAISFixDate=None, WBNUMBER=None, WBDate=None, Shipper=None, Consignee=None, **kwargs_):
        super(HeaderType223Sub, self).__init__(Identity, WBRegId, EGAISFixNumber, EGAISFixDate, WBNUMBER, WBDate, Shipper, Consignee,  **kwargs_)
supermod.HeaderType223.subclass = HeaderType223Sub
# end class HeaderType223Sub


class ContentType224Sub(supermod.ContentType224):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType224Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType224.subclass = ContentType224Sub
# end class ContentType224Sub


class HeaderType225Sub(supermod.HeaderType225):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType225Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType225.subclass = HeaderType225Sub
# end class HeaderType225Sub


class ContentType227Sub(supermod.ContentType227):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType227Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType227.subclass = ContentType227Sub
# end class ContentType227Sub


class HeaderType228Sub(supermod.HeaderType228):
    def __init__(self, TransferNumber=None, TransferDate=None, Note=None, **kwargs_):
        super(HeaderType228Sub, self).__init__(TransferNumber, TransferDate, Note,  **kwargs_)
supermod.HeaderType228.subclass = HeaderType228Sub
# end class HeaderType228Sub


class ContentType230Sub(supermod.ContentType230):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType230Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType230.subclass = ContentType230Sub
# end class ContentType230Sub


class HeaderType231Sub(supermod.HeaderType231):
    def __init__(self, TransferNumber=None, TransferDate=None, Note=None, **kwargs_):
        super(HeaderType231Sub, self).__init__(TransferNumber, TransferDate, Note,  **kwargs_)
supermod.HeaderType231.subclass = HeaderType231Sub
# end class HeaderType231Sub


class ContentType233Sub(supermod.ContentType233):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType233Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType233.subclass = ContentType233Sub
# end class ContentType233Sub


class HeaderType234Sub(supermod.HeaderType234):
    def __init__(self, Identity=None, RepRegId=None, Client=None, **kwargs_):
        super(HeaderType234Sub, self).__init__(Identity, RepRegId, Client,  **kwargs_)
supermod.HeaderType234.subclass = HeaderType234Sub
# end class HeaderType234Sub


class ContentType235Sub(supermod.ContentType235):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType235Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType235.subclass = ContentType235Sub
# end class ContentType235Sub


class ttnlistTypeSub(supermod.ttnlistType):
    def __init__(self, NoAnswer=None, **kwargs_):
        super(ttnlistTypeSub, self).__init__(NoAnswer,  **kwargs_)
supermod.ttnlistType.subclass = ttnlistTypeSub
# end class ttnlistTypeSub


class ProductsType236Sub(supermod.ProductsType236):
    def __init__(self, ShopPosition=None, **kwargs_):
        super(ProductsType236Sub, self).__init__(ShopPosition,  **kwargs_)
supermod.ProductsType236.subclass = ProductsType236Sub
# end class ProductsType236Sub


class SensorTypeSub(supermod.SensorType):
    def __init__(self, SensorNumber=None, PlaceId=None, SensorModel=None, **kwargs_):
        super(SensorTypeSub, self).__init__(SensorNumber, PlaceId, SensorModel,  **kwargs_)
supermod.SensorType.subclass = SensorTypeSub
# end class SensorTypeSub


class DataType237Sub(supermod.DataType237):
    def __init__(self, Position=None, **kwargs_):
        super(DataType237Sub, self).__init__(Position,  **kwargs_)
supermod.DataType237.subclass = DataType237Sub
# end class DataType237Sub


class SensorType238Sub(supermod.SensorType238):
    def __init__(self, SensorNumber=None, PlaceId=None, SensorModel=None, **kwargs_):
        super(SensorType238Sub, self).__init__(SensorNumber, PlaceId, SensorModel,  **kwargs_)
supermod.SensorType238.subclass = SensorType238Sub
# end class SensorType238Sub


class DataType239Sub(supermod.DataType239):
    def __init__(self, Position=None, **kwargs_):
        super(DataType239Sub, self).__init__(Position,  **kwargs_)
supermod.DataType239.subclass = DataType239Sub
# end class DataType239Sub


class HeaderType240Sub(supermod.HeaderType240):
    def __init__(self, Number=None, ActDate=None, TypeChargeOn=None, ActWriteOff=None, Note=None, **kwargs_):
        super(HeaderType240Sub, self).__init__(Number, ActDate, TypeChargeOn, ActWriteOff, Note,  **kwargs_)
supermod.HeaderType240.subclass = HeaderType240Sub
# end class HeaderType240Sub


class ContentType242Sub(supermod.ContentType242):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType242Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType242.subclass = ContentType242Sub
# end class ContentType242Sub


class HeaderType243Sub(supermod.HeaderType243):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType243Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType243.subclass = HeaderType243Sub
# end class HeaderType243Sub


class ContentType245Sub(supermod.ContentType245):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType245Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType245.subclass = ContentType245Sub
# end class ContentType245Sub


class MarksTypeSub(supermod.MarksType):
    def __init__(self, Mark=None, **kwargs_):
        super(MarksTypeSub, self).__init__(Mark,  **kwargs_)
supermod.MarksType.subclass = MarksTypeSub
# end class MarksTypeSub


class MarksType246Sub(supermod.MarksType246):
    def __init__(self, Mark=None, **kwargs_):
        super(MarksType246Sub, self).__init__(Mark,  **kwargs_)
supermod.MarksType246.subclass = MarksType246Sub
# end class MarksType246Sub


class HeaderType247Sub(supermod.HeaderType247):
    def __init__(self, IsConfirm=None, ConfirmNumber=None, ConfirmDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType247Sub, self).__init__(IsConfirm, ConfirmNumber, ConfirmDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType247.subclass = HeaderType247Sub
# end class HeaderType247Sub


class ProductsType249Sub(supermod.ProductsType249):
    def __init__(self, StockPosition=None, **kwargs_):
        super(ProductsType249Sub, self).__init__(StockPosition,  **kwargs_)
supermod.ProductsType249.subclass = ProductsType249Sub
# end class ProductsType249Sub


class ProductsType250Sub(supermod.ProductsType250):
    def __init__(self, ShopPosition=None, **kwargs_):
        super(ProductsType250Sub, self).__init__(ShopPosition,  **kwargs_)
supermod.ProductsType250.subclass = ProductsType250Sub
# end class ProductsType250Sub


class HistoryTypeSub(supermod.HistoryType):
    def __init__(self, DocData=None, **kwargs_):
        super(HistoryTypeSub, self).__init__(DocData,  **kwargs_)
supermod.HistoryType.subclass = HistoryTypeSub
# end class HistoryTypeSub


class SensorType259Sub(supermod.SensorType259):
    def __init__(self, IMEI=None, **kwargs_):
        super(SensorType259Sub, self).__init__(IMEI,  **kwargs_)
supermod.SensorType259.subclass = SensorType259Sub
# end class SensorType259Sub


class DataLevelGaugeTypeSub(supermod.DataLevelGaugeType):
    def __init__(self, LevelGauge=None, **kwargs_):
        super(DataLevelGaugeTypeSub, self).__init__(LevelGauge,  **kwargs_)
supermod.DataLevelGaugeType.subclass = DataLevelGaugeTypeSub
# end class DataLevelGaugeTypeSub


class HeaderType260Sub(supermod.HeaderType260):
    def __init__(self, Type='WBInvoiceFromMe', NUMBER=None, Date=None, ShippingDate=None, Transport=None, Shipper=None, Consignee=None, Base=None, Note=None, VarField1=None, VarField2=None, VarField3=None, **kwargs_):
        super(HeaderType260Sub, self).__init__(Type, NUMBER, Date, ShippingDate, Transport, Shipper, Consignee, Base, Note, VarField1, VarField2, VarField3,  **kwargs_)
supermod.HeaderType260.subclass = HeaderType260Sub
# end class HeaderType260Sub


class ContentType266Sub(supermod.ContentType266):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType266Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType266.subclass = ContentType266Sub
# end class ContentType266Sub


class boxInfoTypeSub(supermod.boxInfoType):
    def __init__(self, boxtree=None, **kwargs_):
        super(boxInfoTypeSub, self).__init__(boxtree,  **kwargs_)
supermod.boxInfoType.subclass = boxInfoTypeSub
# end class boxInfoTypeSub


class HeaderType277Sub(supermod.HeaderType277):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType277Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType277.subclass = HeaderType277Sub
# end class HeaderType277Sub


class ContentType279Sub(supermod.ContentType279):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType279Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType279.subclass = ContentType279Sub
# end class ContentType279Sub


class HeaderType280Sub(supermod.HeaderType280):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType280Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType280.subclass = HeaderType280Sub
# end class HeaderType280Sub


class ContentType282Sub(supermod.ContentType282):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType282Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType282.subclass = ContentType282Sub
# end class ContentType282Sub


class HeaderType283Sub(supermod.HeaderType283):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType283Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType283.subclass = HeaderType283Sub
# end class HeaderType283Sub


class ContentType285Sub(supermod.ContentType285):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType285Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType285.subclass = ContentType285Sub
# end class ContentType285Sub


class ContentResourceType286Sub(supermod.ContentResourceType286):
    def __init__(self, Resource=None, **kwargs_):
        super(ContentResourceType286Sub, self).__init__(Resource,  **kwargs_)
supermod.ContentResourceType286.subclass = ContentResourceType286Sub
# end class ContentResourceType286Sub


class HeaderType290Sub(supermod.HeaderType290):
    def __init__(self, NUMBER=None, Date=None, ImportedDate=None, Importer=None, Supplier=None, GTDNUMBER=None, GTDDate=None, ContractNUMBER=None, ContractDate=None, Country=None, Note=None, **kwargs_):
        super(HeaderType290Sub, self).__init__(NUMBER, Date, ImportedDate, Importer, Supplier, GTDNUMBER, GTDDate, ContractNUMBER, ContractDate, Country, Note,  **kwargs_)
supermod.HeaderType290.subclass = HeaderType290Sub
# end class HeaderType290Sub


class ContentType293Sub(supermod.ContentType293):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType293Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType293.subclass = ContentType293Sub
# end class ContentType293Sub


class HeaderType297Sub(supermod.HeaderType297):
    def __init__(self, Number=None, ActDate=None, Note=None, **kwargs_):
        super(HeaderType297Sub, self).__init__(Number, ActDate, Note,  **kwargs_)
supermod.HeaderType297.subclass = HeaderType297Sub
# end class HeaderType297Sub


class ContentType299Sub(supermod.ContentType299):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType299Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType299.subclass = ContentType299Sub
# end class ContentType299Sub


class HeaderType300Sub(supermod.HeaderType300):
    def __init__(self, Number=None, ActDate=None, Note=None, **kwargs_):
        super(HeaderType300Sub, self).__init__(Number, ActDate, Note,  **kwargs_)
supermod.HeaderType300.subclass = HeaderType300Sub
# end class HeaderType300Sub


class ContentType302Sub(supermod.ContentType302):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType302Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType302.subclass = ContentType302Sub
# end class ContentType302Sub


class ParentHistTypeSub(supermod.ParentHistType):
    def __init__(self, step=None, **kwargs_):
        super(ParentHistTypeSub, self).__init__(step,  **kwargs_)
supermod.ParentHistType.subclass = ParentHistTypeSub
# end class ParentHistTypeSub


class HeaderType303Sub(supermod.HeaderType303):
    def __init__(self, WBRegId=None, **kwargs_):
        super(HeaderType303Sub, self).__init__(WBRegId,  **kwargs_)
supermod.HeaderType303.subclass = HeaderType303Sub
# end class HeaderType303Sub


class ContentType304Sub(supermod.ContentType304):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType304Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType304.subclass = ContentType304Sub
# end class ContentType304Sub


class HistF2TypeSub(supermod.HistF2Type):
    def __init__(self, step=None, **kwargs_):
        super(HistF2TypeSub, self).__init__(step,  **kwargs_)
supermod.HistF2Type.subclass = HistF2TypeSub
# end class HistF2TypeSub


class HeaderType305Sub(supermod.HeaderType305):
    def __init__(self, ClientIdentity=None, Serial=None, Shipper=None, Consignee=None, Carrier=None, ClientTransport=None, ShipmentOutDate=None, ShipmentInDate=None, EGAISFixNumberTTN=None, NotifNumber=None, NotifDate=None, **kwargs_):
        super(HeaderType305Sub, self).__init__(ClientIdentity, Serial, Shipper, Consignee, Carrier, ClientTransport, ShipmentOutDate, ShipmentInDate, EGAISFixNumberTTN, NotifNumber, NotifDate,  **kwargs_)
supermod.HeaderType305.subclass = HeaderType305Sub
# end class HeaderType305Sub


class ContentType306Sub(supermod.ContentType306):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType306Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType306.subclass = ContentType306Sub
# end class ContentType306Sub


class HeaderType307Sub(supermod.HeaderType307):
    def __init__(self, ClientIdentity=None, Serial=None, Shipper=None, Consignee=None, Carrier=None, ClientTransport=None, ShipmentOutDate=None, ShipmentInDate=None, EGAISFixNumberTTN=None, NotifNumber=None, NotifDate=None, **kwargs_):
        super(HeaderType307Sub, self).__init__(ClientIdentity, Serial, Shipper, Consignee, Carrier, ClientTransport, ShipmentOutDate, ShipmentInDate, EGAISFixNumberTTN, NotifNumber, NotifDate,  **kwargs_)
supermod.HeaderType307.subclass = HeaderType307Sub
# end class HeaderType307Sub


class ContentType308Sub(supermod.ContentType308):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType308Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType308.subclass = ContentType308Sub
# end class ContentType308Sub


class HeaderType309Sub(supermod.HeaderType309):
    def __init__(self, NUMBER=None, Date=None, TerrOrganRAR=None, Declarer=None, Note=None, ReportUseAutoProcess=None, ParentClaimID=None, TypeClaimM=None, **kwargs_):
        super(HeaderType309Sub, self).__init__(NUMBER, Date, TerrOrganRAR, Declarer, Note, ReportUseAutoProcess, ParentClaimID, TypeClaimM,  **kwargs_)
supermod.HeaderType309.subclass = HeaderType309Sub
# end class HeaderType309Sub


class ContentType311Sub(supermod.ContentType311):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType311Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType311.subclass = ContentType311Sub
# end class ContentType311Sub


class HeaderType312Sub(supermod.HeaderType312):
    def __init__(self, NUMBER=None, Date=None, RequestFSM=None, Client=None, TerrOrganRAR=None, **kwargs_):
        super(HeaderType312Sub, self).__init__(NUMBER, Date, RequestFSM, Client, TerrOrganRAR,  **kwargs_)
supermod.HeaderType312.subclass = HeaderType312Sub
# end class HeaderType312Sub


class ContentType313Sub(supermod.ContentType313):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType313Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType313.subclass = ContentType313Sub
# end class ContentType313Sub


class HeaderType314Sub(supermod.HeaderType314):
    def __init__(self, NUMBER=None, Date=None, Sender=None, Consignee=None, RequestFSM=None, ManufacturerShortName=None, ActualShipmentDate=None, TotalQuantity=None, **kwargs_):
        super(HeaderType314Sub, self).__init__(NUMBER, Date, Sender, Consignee, RequestFSM, ManufacturerShortName, ActualShipmentDate, TotalQuantity,  **kwargs_)
supermod.HeaderType314.subclass = HeaderType314Sub
# end class HeaderType314Sub


class ContentType315Sub(supermod.ContentType315):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType315Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType315.subclass = ContentType315Sub
# end class ContentType315Sub


class HeaderType316Sub(supermod.HeaderType316):
    def __init__(self, NUMBER=None, Date=None, Sender=None, Consignee=None, RequestFSM=None, ManufacturerShortName=None, ActualShipmentDate=None, TotalQuantity=None, **kwargs_):
        super(HeaderType316Sub, self).__init__(NUMBER, Date, Sender, Consignee, RequestFSM, ManufacturerShortName, ActualShipmentDate, TotalQuantity,  **kwargs_)
supermod.HeaderType316.subclass = HeaderType316Sub
# end class HeaderType316Sub


class ContentType317Sub(supermod.ContentType317):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType317Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType317.subclass = ContentType317Sub
# end class ContentType317Sub


class HeaderType318Sub(supermod.HeaderType318):
    def __init__(self, NUMBER=None, Date=None, RequestFSM=None, Declarer=None, **kwargs_):
        super(HeaderType318Sub, self).__init__(NUMBER, Date, RequestFSM, Declarer,  **kwargs_)
supermod.HeaderType318.subclass = HeaderType318Sub
# end class HeaderType318Sub


class ContentType319Sub(supermod.ContentType319):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType319Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType319.subclass = ContentType319Sub
# end class ContentType319Sub


class HeaderType320Sub(supermod.HeaderType320):
    def __init__(self, NUMBER=None, Date=None, RequestNUMBER=None, RequestDate=None, RequestFSM=None, Declarer=None, ReasonReturn=None, **kwargs_):
        super(HeaderType320Sub, self).__init__(NUMBER, Date, RequestNUMBER, RequestDate, RequestFSM, Declarer, ReasonReturn,  **kwargs_)
supermod.HeaderType320.subclass = HeaderType320Sub
# end class HeaderType320Sub


class HeaderType321Sub(supermod.HeaderType321):
    def __init__(self, NUMBER=None, Date=None, RequestNUMBER=None, RequestDate=None, RequestFSM=None, Declarer=None, Comment=None, **kwargs_):
        super(HeaderType321Sub, self).__init__(NUMBER, Date, RequestNUMBER, RequestDate, RequestFSM, Declarer, Comment,  **kwargs_)
supermod.HeaderType321.subclass = HeaderType321Sub
# end class HeaderType321Sub


class ClientsType322Sub(supermod.ClientsType322):
    def __init__(self, Client=None, **kwargs_):
        super(ClientsType322Sub, self).__init__(Client,  **kwargs_)
supermod.ClientsType322.subclass = ClientsType322Sub
# end class ClientsType322Sub


class HeaderType323Sub(supermod.HeaderType323):
    def __init__(self, NUMBER=None, Date=None, Importer=None, CustomsDepartment=None, RequestAM=None, ActualShipmentDate=None, TotalQuantity=None, **kwargs_):
        super(HeaderType323Sub, self).__init__(NUMBER, Date, Importer, CustomsDepartment, RequestAM, ActualShipmentDate, TotalQuantity,  **kwargs_)
supermod.HeaderType323.subclass = HeaderType323Sub
# end class HeaderType323Sub


class ContentType324Sub(supermod.ContentType324):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType324Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType324.subclass = ContentType324Sub
# end class ContentType324Sub


class HeaderType325Sub(supermod.HeaderType325):
    def __init__(self, NUMBER=None, Date=None, Importer=None, TerrOrganRAR=None, RequestFSM=None, ActualShipmentDate=None, TotalQuantity=None, **kwargs_):
        super(HeaderType325Sub, self).__init__(NUMBER, Date, Importer, TerrOrganRAR, RequestFSM, ActualShipmentDate, TotalQuantity,  **kwargs_)
supermod.HeaderType325.subclass = HeaderType325Sub
# end class HeaderType325Sub


class ContentType326Sub(supermod.ContentType326):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType326Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType326.subclass = ContentType326Sub
# end class ContentType326Sub


class HeaderType327Sub(supermod.HeaderType327):
    def __init__(self, NUMBER=None, Date=None, Importer=None, CustomsDepartment=None, Product=None, TotalQuantity=None, TotalQuantityDal=None, **kwargs_):
        super(HeaderType327Sub, self).__init__(NUMBER, Date, Importer, CustomsDepartment, Product, TotalQuantity, TotalQuantityDal,  **kwargs_)
supermod.HeaderType327.subclass = HeaderType327Sub
# end class HeaderType327Sub


class ContentType328Sub(supermod.ContentType328):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType328Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType328.subclass = ContentType328Sub
# end class ContentType328Sub


class HeaderType329Sub(supermod.HeaderType329):
    def __init__(self, NUMBER=None, Date=None, LicenseRegNumber=None, Notifier=None, Producer=None, FullName=None, FullNameManufacturerLanguage=None, AlcVolumeMin=None, AlcVolumeMax=None, AlcVolume=None, UnitType=None, PackageType=None, Capacity=None, DistinctiveCharacteristics=None, ShelfLife=None, StorageTemperatureMin=None, StorageTemperatureMax=None, StorageHumidityMin=None, StorageHumidityMax=None, OtherStorageCharacteristics=None, CodAP231=None, CodOKPD2=None, CodTNVEDTS=None, VidAP171FZ=None, DateFirstDelivery=None, TrademarkDetails=None, Note=None, TermsTransportation=None, TermsSale=None, TermsDisposal=None, LabelFoto=None, **kwargs_):
        super(HeaderType329Sub, self).__init__(NUMBER, Date, LicenseRegNumber, Notifier, Producer, FullName, FullNameManufacturerLanguage, AlcVolumeMin, AlcVolumeMax, AlcVolume, UnitType, PackageType, Capacity, DistinctiveCharacteristics, ShelfLife, StorageTemperatureMin, StorageTemperatureMax, StorageHumidityMin, StorageHumidityMax, OtherStorageCharacteristics, CodAP231, CodOKPD2, CodTNVEDTS, VidAP171FZ, DateFirstDelivery, TrademarkDetails, Note, TermsTransportation, TermsSale, TermsDisposal, LabelFoto,  **kwargs_)
supermod.HeaderType329.subclass = HeaderType329Sub
# end class HeaderType329Sub


class CompositionProductsTypeSub(supermod.CompositionProductsType):
    def __init__(self, Position=None, **kwargs_):
        super(CompositionProductsTypeSub, self).__init__(Position,  **kwargs_)
supermod.CompositionProductsType.subclass = CompositionProductsTypeSub
# end class CompositionProductsTypeSub


class IdentifyingDocumentsTypeSub(supermod.IdentifyingDocumentsType):
    def __init__(self, Position=None, **kwargs_):
        super(IdentifyingDocumentsTypeSub, self).__init__(Position,  **kwargs_)
supermod.IdentifyingDocumentsType.subclass = IdentifyingDocumentsTypeSub
# end class IdentifyingDocumentsTypeSub


class DeclarationTypeSub(supermod.DeclarationType):
    def __init__(self, Position=None, **kwargs_):
        super(DeclarationTypeSub, self).__init__(Position,  **kwargs_)
supermod.DeclarationType.subclass = DeclarationTypeSub
# end class DeclarationTypeSub


class ContentType332Sub(supermod.ContentType332):
    def __init__(self, Bottle=None, Nomark=None, **kwargs_):
        super(ContentType332Sub, self).__init__(Bottle, Nomark,  **kwargs_)
supermod.ContentType332.subclass = ContentType332Sub
# end class ContentType332Sub


class HeaderType333Sub(supermod.HeaderType333):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType333Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType333.subclass = HeaderType333Sub
# end class HeaderType333Sub


class ContentType335Sub(supermod.ContentType335):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType335Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType335.subclass = ContentType335Sub
# end class ContentType335Sub


class ContentResourceType336Sub(supermod.ContentResourceType336):
    def __init__(self, Resource=None, **kwargs_):
        super(ContentResourceType336Sub, self).__init__(Resource,  **kwargs_)
supermod.ContentResourceType336.subclass = ContentResourceType336Sub
# end class ContentResourceType336Sub


class HeaderType340Sub(supermod.HeaderType340):
    def __init__(self, NUMBER=None, Date=None, ImportedDate=None, Importer=None, Supplier=None, GTDNUMBER=None, GTDDate=None, ContractNUMBER=None, ContractDate=None, Country=None, Note=None, IDInvoicePlannedImport=None, **kwargs_):
        super(HeaderType340Sub, self).__init__(NUMBER, Date, ImportedDate, Importer, Supplier, GTDNUMBER, GTDDate, ContractNUMBER, ContractDate, Country, Note, IDInvoicePlannedImport,  **kwargs_)
supermod.HeaderType340.subclass = HeaderType340Sub
# end class HeaderType340Sub


class ContentType343Sub(supermod.ContentType343):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType343Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType343.subclass = ContentType343Sub
# end class ContentType343Sub


class HeaderType347Sub(supermod.HeaderType347):
    def __init__(self, NUMBER=None, Date=None, Client=None, TotalQuantity=None, **kwargs_):
        super(HeaderType347Sub, self).__init__(NUMBER, Date, Client, TotalQuantity,  **kwargs_)
supermod.HeaderType347.subclass = HeaderType347Sub
# end class HeaderType347Sub


class ContentType348Sub(supermod.ContentType348):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType348Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType348.subclass = ContentType348Sub
# end class ContentType348Sub


class HeaderType349Sub(supermod.HeaderType349):
    def __init__(self, NUMBER=None, Date=None, Sender=None, Consignee=None, RequestFSM=None, ManufacturerShortName=None, ActualShipmentDate=None, TotalQuantity=None, **kwargs_):
        super(HeaderType349Sub, self).__init__(NUMBER, Date, Sender, Consignee, RequestFSM, ManufacturerShortName, ActualShipmentDate, TotalQuantity,  **kwargs_)
supermod.HeaderType349.subclass = HeaderType349Sub
# end class HeaderType349Sub


class ContentType350Sub(supermod.ContentType350):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType350Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType350.subclass = ContentType350Sub
# end class ContentType350Sub


class HeaderType351Sub(supermod.HeaderType351):
    def __init__(self, NUMBER=None, Date=None, Sender=None, Consignee=None, RequestFSM=None, ManufacturerShortName=None, ActualShipmentDate=None, TotalQuantity=None, **kwargs_):
        super(HeaderType351Sub, self).__init__(NUMBER, Date, Sender, Consignee, RequestFSM, ManufacturerShortName, ActualShipmentDate, TotalQuantity,  **kwargs_)
supermod.HeaderType351.subclass = HeaderType351Sub
# end class HeaderType351Sub


class ContentType352Sub(supermod.ContentType352):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType352Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType352.subclass = ContentType352Sub
# end class ContentType352Sub


class HeaderType353Sub(supermod.HeaderType353):
    def __init__(self, ReferenceDate=None, RequestFSM=None, NUMBERIssueFSM=None, DateIssueFSM=None, TerrOrganRAR=None, Declarer=None, Comments=None, SignReference=None, SignCertificate=None, **kwargs_):
        super(HeaderType353Sub, self).__init__(ReferenceDate, RequestFSM, NUMBERIssueFSM, DateIssueFSM, TerrOrganRAR, Declarer, Comments, SignReference, SignCertificate,  **kwargs_)
supermod.HeaderType353.subclass = HeaderType353Sub
# end class HeaderType353Sub


class HeaderType354Sub(supermod.HeaderType354):
    def __init__(self, NoticeNumber=None, NoticeDate=None, DecisionNumber=None, DecisionDate=None, RequestFSM=None, NUMBERIssueFSM=None, DateIssueFSM=None, TerrOrganRAR=None, Declarer=None, **kwargs_):
        super(HeaderType354Sub, self).__init__(NoticeNumber, NoticeDate, DecisionNumber, DecisionDate, RequestFSM, NUMBERIssueFSM, DateIssueFSM, TerrOrganRAR, Declarer,  **kwargs_)
supermod.HeaderType354.subclass = HeaderType354Sub
# end class HeaderType354Sub


class HeaderType355Sub(supermod.HeaderType355):
    def __init__(self, Type='WBInvoiceFromMe', NUMBER=None, Date=None, ShippingDate=None, Transport=None, Shipper=None, Consignee=None, Base=None, Note=None, VarField1=None, VarField2=None, VarField3=None, **kwargs_):
        super(HeaderType355Sub, self).__init__(Type, NUMBER, Date, ShippingDate, Transport, Shipper, Consignee, Base, Note, VarField1, VarField2, VarField3,  **kwargs_)
supermod.HeaderType355.subclass = HeaderType355Sub
# end class HeaderType355Sub


class ContentType361Sub(supermod.ContentType361):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType361Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType361.subclass = ContentType361Sub
# end class ContentType361Sub


class boxInfoType363Sub(supermod.boxInfoType363):
    def __init__(self, boxtree=None, **kwargs_):
        super(boxInfoType363Sub, self).__init__(boxtree,  **kwargs_)
supermod.boxInfoType363.subclass = boxInfoType363Sub
# end class boxInfoType363Sub


class HeaderType373Sub(supermod.HeaderType373):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType373Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType373.subclass = HeaderType373Sub
# end class HeaderType373Sub


class ContentType375Sub(supermod.ContentType375):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType375Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType375.subclass = ContentType375Sub
# end class ContentType375Sub


class ParentRoutesTypeSub(supermod.ParentRoutesType):
    def __init__(self, RouteId=None, **kwargs_):
        super(ParentRoutesTypeSub, self).__init__(RouteId,  **kwargs_)
supermod.ParentRoutesType.subclass = ParentRoutesTypeSub
# end class ParentRoutesTypeSub


class HeaderType377Sub(supermod.HeaderType377):
    def __init__(self, NUMBER=None, Date=None, Client=None, Issuer=None, DateDebtAbsence=None, ClaimIssueFSMNumber=None, ClaimIssueFSMDate=None, **kwargs_):
        super(HeaderType377Sub, self).__init__(NUMBER, Date, Client, Issuer, DateDebtAbsence, ClaimIssueFSMNumber, ClaimIssueFSMDate,  **kwargs_)
supermod.HeaderType377.subclass = HeaderType377Sub
# end class HeaderType377Sub


class HeaderType381Sub(supermod.HeaderType381):
    def __init__(self, Applicant=None, OnlineStoreId=None, DocID=None, CancelNumber=None, CancelDateTime=None, CauseCancel=None, **kwargs_):
        super(HeaderType381Sub, self).__init__(Applicant, OnlineStoreId, DocID, CancelNumber, CancelDateTime, CauseCancel,  **kwargs_)
supermod.HeaderType381.subclass = HeaderType381Sub
# end class HeaderType381Sub


class HeaderType382Sub(supermod.HeaderType382):
    def __init__(self, Applicant=None, OnlineStoreId=None, DocID=None, ConfirmNumber=None, ConfirmDateTime=None, Note=None, **kwargs_):
        super(HeaderType382Sub, self).__init__(Applicant, OnlineStoreId, DocID, ConfirmNumber, ConfirmDateTime, Note,  **kwargs_)
supermod.HeaderType382.subclass = HeaderType382Sub
# end class HeaderType382Sub


class ContentType385Sub(supermod.ContentType385):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType385Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType385.subclass = ContentType385Sub
# end class ContentType385Sub


class F2DetailType386Sub(supermod.F2DetailType386):
    def __init__(self, Form2=None, **kwargs_):
        super(F2DetailType386Sub, self).__init__(Form2,  **kwargs_)
supermod.F2DetailType386.subclass = F2DetailType386Sub
# end class F2DetailType386Sub


class HeaderType387Sub(supermod.HeaderType387):
    def __init__(self, Applicant=None, OnlineStoreId=None, OrderNumber=None, OrderDateTime=None, Note=None, **kwargs_):
        super(HeaderType387Sub, self).__init__(Applicant, OnlineStoreId, OrderNumber, OrderDateTime, Note,  **kwargs_)
supermod.HeaderType387.subclass = HeaderType387Sub
# end class HeaderType387Sub


class ContentType390Sub(supermod.ContentType390):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType390Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType390.subclass = ContentType390Sub
# end class ContentType390Sub


class HeaderType391Sub(supermod.HeaderType391):
    def __init__(self, RequestNumber=None, RequestDate=None, Sender=None, Recipient=None, **kwargs_):
        super(HeaderType391Sub, self).__init__(RequestNumber, RequestDate, Sender, Recipient,  **kwargs_)
supermod.HeaderType391.subclass = HeaderType391Sub
# end class HeaderType391Sub


class HeaderType392Sub(supermod.HeaderType392):
    def __init__(self, NUMBER=None, Date=None, RequestFSM=None, Client=None, TerrOrganRAR=None, **kwargs_):
        super(HeaderType392Sub, self).__init__(NUMBER, Date, RequestFSM, Client, TerrOrganRAR,  **kwargs_)
supermod.HeaderType392.subclass = HeaderType392Sub
# end class HeaderType392Sub


class ContentType393Sub(supermod.ContentType393):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType393Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType393.subclass = ContentType393Sub
# end class ContentType393Sub


class HeaderType394Sub(supermod.HeaderType394):
    def __init__(self, TicketDate=None, RequestFSM=None, CheckResult=None, Comments=None, **kwargs_):
        super(HeaderType394Sub, self).__init__(TicketDate, RequestFSM, CheckResult, Comments,  **kwargs_)
supermod.HeaderType394.subclass = HeaderType394Sub
# end class HeaderType394Sub


class HeaderType395Sub(supermod.HeaderType395):
    def __init__(self, DocNumber=None, DocDate=None, Notifier=None, TypeOrg=None, Producer=None, VidAP=None, NameAP=None, FullNameManufacturerLanguage=None, Brend=None, CountryOrigin=None, AlcVolume=None, CapacityList=None, MarketSupply=None, CompositionProducts=None, TechReglStandard=None, AdditionalDocuments=None, DistinctiveCharacteristics=None, SugarContWine=None, SugarContSparkWine=None, MinAge=None, StorageTemperature=None, StorageHumidity=None, OtherStorageCharacteristics=None, CodOKPD2=None, CodTNVED=None, DeclarationCertificate=None, DateFirstDelivery=None, TrademarkDetails=None, TermsTransportation=None, TermsSale=None, TermsDisposal=None, Note=None, **kwargs_):
        super(HeaderType395Sub, self).__init__(DocNumber, DocDate, Notifier, TypeOrg, Producer, VidAP, NameAP, FullNameManufacturerLanguage, Brend, CountryOrigin, AlcVolume, CapacityList, MarketSupply, CompositionProducts, TechReglStandard, AdditionalDocuments, DistinctiveCharacteristics, SugarContWine, SugarContSparkWine, MinAge, StorageTemperature, StorageHumidity, OtherStorageCharacteristics, CodOKPD2, CodTNVED, DeclarationCertificate, DateFirstDelivery, TrademarkDetails, TermsTransportation, TermsSale, TermsDisposal, Note,  **kwargs_)
supermod.HeaderType395.subclass = HeaderType395Sub
# end class HeaderType395Sub


class NotifierTypeSub(supermod.NotifierType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, UL=None, FL=None, **kwargs_):
        super(NotifierTypeSub, self).__init__(ClientRegId, FullName, ShortName, UL, FL,  **kwargs_)
supermod.NotifierType.subclass = NotifierTypeSub
# end class NotifierTypeSub


class ULType398Sub(supermod.ULType398):
    def __init__(self, INN=None, KPP=None, address=None, **kwargs_):
        super(ULType398Sub, self).__init__(INN, KPP, address,  **kwargs_)
supermod.ULType398.subclass = ULType398Sub
# end class ULType398Sub


class addressType401Sub(supermod.addressType401):
    def __init__(self, Country=None, RegionCode=None, Description=None, **kwargs_):
        super(addressType401Sub, self).__init__(Country, RegionCode, Description,  **kwargs_)
supermod.addressType401.subclass = addressType401Sub
# end class addressType401Sub


class FLType404Sub(supermod.FLType404):
    def __init__(self, FullName=None, INN=None, address=None, **kwargs_):
        super(FLType404Sub, self).__init__(FullName, INN, address,  **kwargs_)
supermod.FLType404.subclass = FLType404Sub
# end class FLType404Sub


class addressType407Sub(supermod.addressType407):
    def __init__(self, Country=None, RegionCode=None, Description=None, **kwargs_):
        super(addressType407Sub, self).__init__(Country, RegionCode, Description,  **kwargs_)
supermod.addressType407.subclass = addressType407Sub
# end class addressType407Sub


class ProducerTypeSub(supermod.ProducerType):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, UL=None, FL=None, FO=None, **kwargs_):
        super(ProducerTypeSub, self).__init__(ClientRegId, FullName, ShortName, UL, FL, FO,  **kwargs_)
supermod.ProducerType.subclass = ProducerTypeSub
# end class ProducerTypeSub


class ULType414Sub(supermod.ULType414):
    def __init__(self, INN=None, KPP=None, address=None, **kwargs_):
        super(ULType414Sub, self).__init__(INN, KPP, address,  **kwargs_)
supermod.ULType414.subclass = ULType414Sub
# end class ULType414Sub


class addressType417Sub(supermod.addressType417):
    def __init__(self, Country=None, RegionCode=None, Description=None, **kwargs_):
        super(addressType417Sub, self).__init__(Country, RegionCode, Description,  **kwargs_)
supermod.addressType417.subclass = addressType417Sub
# end class addressType417Sub


class FLType421Sub(supermod.FLType421):
    def __init__(self, FullName=None, INN=None, address=None, **kwargs_):
        super(FLType421Sub, self).__init__(FullName, INN, address,  **kwargs_)
supermod.FLType421.subclass = FLType421Sub
# end class FLType421Sub


class addressType424Sub(supermod.addressType424):
    def __init__(self, Country=None, RegionCode=None, Description=None, **kwargs_):
        super(addressType424Sub, self).__init__(Country, RegionCode, Description,  **kwargs_)
supermod.addressType424.subclass = addressType424Sub
# end class addressType424Sub


class FOType428Sub(supermod.FOType428):
    def __init__(self, address=None, **kwargs_):
        super(FOType428Sub, self).__init__(address,  **kwargs_)
supermod.FOType428.subclass = FOType428Sub
# end class FOType428Sub


class addressType429Sub(supermod.addressType429):
    def __init__(self, Country=None, Description=None, **kwargs_):
        super(addressType429Sub, self).__init__(Country, Description,  **kwargs_)
supermod.addressType429.subclass = addressType429Sub
# end class addressType429Sub


class AlcVolumeType433Sub(supermod.AlcVolumeType433):
    def __init__(self, AlcVolumeMin=None, AlcVolumeMax=None, **kwargs_):
        super(AlcVolumeType433Sub, self).__init__(AlcVolumeMin, AlcVolumeMax,  **kwargs_)
supermod.AlcVolumeType433.subclass = AlcVolumeType433Sub
# end class AlcVolumeType433Sub


class CapacityListTypeSub(supermod.CapacityListType):
    def __init__(self, CapacityDescr=None, **kwargs_):
        super(CapacityListTypeSub, self).__init__(CapacityDescr,  **kwargs_)
supermod.CapacityListType.subclass = CapacityListTypeSub
# end class CapacityListTypeSub


class CompositionProductsType437Sub(supermod.CompositionProductsType437):
    def __init__(self, Position=None, **kwargs_):
        super(CompositionProductsType437Sub, self).__init__(Position,  **kwargs_)
supermod.CompositionProductsType437.subclass = CompositionProductsType437Sub
# end class CompositionProductsType437Sub


class TechReglStandardTypeSub(supermod.TechReglStandardType):
    def __init__(self, TechRegl=None, TechStandard=None, **kwargs_):
        super(TechReglStandardTypeSub, self).__init__(TechRegl, TechStandard,  **kwargs_)
supermod.TechReglStandardType.subclass = TechReglStandardTypeSub
# end class TechReglStandardTypeSub


class TechReglTypeSub(supermod.TechReglType):
    def __init__(self, TechReglNumber=None, TechReglName=None, **kwargs_):
        super(TechReglTypeSub, self).__init__(TechReglNumber, TechReglName,  **kwargs_)
supermod.TechReglType.subclass = TechReglTypeSub
# end class TechReglTypeSub


class TechStandardTypeSub(supermod.TechStandardType):
    def __init__(self, StandardNumber=None, StandardName=None, **kwargs_):
        super(TechStandardTypeSub, self).__init__(StandardNumber, StandardName,  **kwargs_)
supermod.TechStandardType.subclass = TechStandardTypeSub
# end class TechStandardTypeSub


class AdditionalDocumentsType438Sub(supermod.AdditionalDocumentsType438):
    def __init__(self, Position=None, **kwargs_):
        super(AdditionalDocumentsType438Sub, self).__init__(Position,  **kwargs_)
supermod.AdditionalDocumentsType438.subclass = AdditionalDocumentsType438Sub
# end class AdditionalDocumentsType438Sub


class StorageTemperatureTypeSub(supermod.StorageTemperatureType):
    def __init__(self, StorageTemperatureMin=None, StorageTemperatureMax=None, **kwargs_):
        super(StorageTemperatureTypeSub, self).__init__(StorageTemperatureMin, StorageTemperatureMax,  **kwargs_)
supermod.StorageTemperatureType.subclass = StorageTemperatureTypeSub
# end class StorageTemperatureTypeSub


class StorageHumidityTypeSub(supermod.StorageHumidityType):
    def __init__(self, StorageHumidityMin=None, StorageHumidityMax=None, **kwargs_):
        super(StorageHumidityTypeSub, self).__init__(StorageHumidityMin, StorageHumidityMax,  **kwargs_)
supermod.StorageHumidityType.subclass = StorageHumidityTypeSub
# end class StorageHumidityTypeSub


class CodTNVEDTypeSub(supermod.CodTNVEDType):
    def __init__(self, CodTNVEDTS=None, **kwargs_):
        super(CodTNVEDTypeSub, self).__init__(CodTNVEDTS,  **kwargs_)
supermod.CodTNVEDType.subclass = CodTNVEDTypeSub
# end class CodTNVEDTypeSub


class DeclarationCertificateTypeSub(supermod.DeclarationCertificateType):
    def __init__(self, Position=None, **kwargs_):
        super(DeclarationCertificateTypeSub, self).__init__(Position,  **kwargs_)
supermod.DeclarationCertificateType.subclass = DeclarationCertificateTypeSub
# end class DeclarationCertificateTypeSub


class AdditionalDocTypeSub(supermod.AdditionalDocType):
    def __init__(self, TechnologicalInstruction=None, OrganizationStandard=None, InternationalStandardCountryOrigin=None, NationalStandardCountryOrigin=None, NationalRegulations=None, TechnicalDocumentation=None, RC=None, **kwargs_):
        super(AdditionalDocTypeSub, self).__init__(TechnologicalInstruction, OrganizationStandard, InternationalStandardCountryOrigin, NationalStandardCountryOrigin, NationalRegulations, TechnicalDocumentation, RC,  **kwargs_)
supermod.AdditionalDocType.subclass = AdditionalDocTypeSub
# end class AdditionalDocTypeSub


class TechnologicalInstructionTypeSub(supermod.TechnologicalInstructionType):
    def __init__(self, TINumber=None, TIDate=None, TIName=None, TIElectronicView=None, **kwargs_):
        super(TechnologicalInstructionTypeSub, self).__init__(TINumber, TIDate, TIName, TIElectronicView,  **kwargs_)
supermod.TechnologicalInstructionType.subclass = TechnologicalInstructionTypeSub
# end class TechnologicalInstructionTypeSub


class OrganizationStandardTypeSub(supermod.OrganizationStandardType):
    def __init__(self, OSNumber=None, OSDate=None, OSName=None, **kwargs_):
        super(OrganizationStandardTypeSub, self).__init__(OSNumber, OSDate, OSName,  **kwargs_)
supermod.OrganizationStandardType.subclass = OrganizationStandardTypeSub
# end class OrganizationStandardTypeSub


class InternationalStandardCountryOriginTypeSub(supermod.InternationalStandardCountryOriginType):
    def __init__(self, ISCONumber=None, ISCOName=None, **kwargs_):
        super(InternationalStandardCountryOriginTypeSub, self).__init__(ISCONumber, ISCOName,  **kwargs_)
supermod.InternationalStandardCountryOriginType.subclass = InternationalStandardCountryOriginTypeSub
# end class InternationalStandardCountryOriginTypeSub


class NationalStandardCountryOriginTypeSub(supermod.NationalStandardCountryOriginType):
    def __init__(self, NSCONumber=None, NSCOName=None, **kwargs_):
        super(NationalStandardCountryOriginTypeSub, self).__init__(NSCONumber, NSCOName,  **kwargs_)
supermod.NationalStandardCountryOriginType.subclass = NationalStandardCountryOriginTypeSub
# end class NationalStandardCountryOriginTypeSub


class NationalRegulationsTypeSub(supermod.NationalRegulationsType):
    def __init__(self, NRNumber=None, NRName=None, **kwargs_):
        super(NationalRegulationsTypeSub, self).__init__(NRNumber, NRName,  **kwargs_)
supermod.NationalRegulationsType.subclass = NationalRegulationsTypeSub
# end class NationalRegulationsTypeSub


class TechnicalDocumentationTypeSub(supermod.TechnicalDocumentationType):
    def __init__(self, TDNumber=None, TDDate=None, TDName=None, TDElectronicView=None, **kwargs_):
        super(TechnicalDocumentationTypeSub, self).__init__(TDNumber, TDDate, TDName, TDElectronicView,  **kwargs_)
supermod.TechnicalDocumentationType.subclass = TechnicalDocumentationTypeSub
# end class TechnicalDocumentationTypeSub


class RCTypeSub(supermod.RCType):
    def __init__(self, RCNumber=None, RCDate=None, RCName=None, **kwargs_):
        super(RCTypeSub, self).__init__(RCNumber, RCDate, RCName,  **kwargs_)
supermod.RCType.subclass = RCTypeSub
# end class RCTypeSub


class DeclarCertifTypeSub(supermod.DeclarCertifType):
    def __init__(self, Declaration=None, Certificate=None, **kwargs_):
        super(DeclarCertifTypeSub, self).__init__(Declaration, Certificate,  **kwargs_)
supermod.DeclarCertifType.subclass = DeclarCertifTypeSub
# end class DeclarCertifTypeSub


class DeclarationType443Sub(supermod.DeclarationType443):
    def __init__(self, DeclarationNumber=None, DateValidity=None, DateExpiration=None, **kwargs_):
        super(DeclarationType443Sub, self).__init__(DeclarationNumber, DateValidity, DateExpiration,  **kwargs_)
supermod.DeclarationType443.subclass = DeclarationType443Sub
# end class DeclarationType443Sub


class CertificateTypeSub(supermod.CertificateType):
    def __init__(self, CertificateNumber=None, DateValidity=None, DateExpiration=None, **kwargs_):
        super(CertificateTypeSub, self).__init__(CertificateNumber, DateValidity, DateExpiration,  **kwargs_)
supermod.CertificateType.subclass = CertificateTypeSub
# end class CertificateTypeSub


class LabelFotoAPTypeSub(supermod.LabelFotoAPType):
    def __init__(self, LabelFoto=None, CapacityDescrVal=None, **kwargs_):
        super(LabelFotoAPTypeSub, self).__init__(LabelFoto, CapacityDescrVal,  **kwargs_)
supermod.LabelFotoAPType.subclass = LabelFotoAPTypeSub
# end class LabelFotoAPTypeSub


class HeaderType447Sub(supermod.HeaderType447):
    def __init__(self, RegNumber=None, Producer=None, CapacityList=None, MarketSupply=None, CompositionProducts=None, TechReglStandard=None, AdditionalDocuments=None, DistinctiveCharacteristics=None, SugarContWine=None, SugarContSparkWine=None, MinAge=None, StorageTemperature=None, StorageHumidity=None, OtherStorageCharacteristics=None, DeclarationCertificate=None, TrademarkDetails=None, Note=None, TermsTransportation=None, TermsSale=None, TermsDisposal=None, **kwargs_):
        super(HeaderType447Sub, self).__init__(RegNumber, Producer, CapacityList, MarketSupply, CompositionProducts, TechReglStandard, AdditionalDocuments, DistinctiveCharacteristics, SugarContWine, SugarContSparkWine, MinAge, StorageTemperature, StorageHumidity, OtherStorageCharacteristics, DeclarationCertificate, TrademarkDetails, Note, TermsTransportation, TermsSale, TermsDisposal,  **kwargs_)
supermod.HeaderType447.subclass = HeaderType447Sub
# end class HeaderType447Sub


class ProducerType448Sub(supermod.ProducerType448):
    def __init__(self, ClientRegId=None, FullName=None, ShortName=None, UL=None, FL=None, FO=None, **kwargs_):
        super(ProducerType448Sub, self).__init__(ClientRegId, FullName, ShortName, UL, FL, FO,  **kwargs_)
supermod.ProducerType448.subclass = ProducerType448Sub
# end class ProducerType448Sub


class ULType452Sub(supermod.ULType452):
    def __init__(self, INN=None, KPP=None, address=None, **kwargs_):
        super(ULType452Sub, self).__init__(INN, KPP, address,  **kwargs_)
supermod.ULType452.subclass = ULType452Sub
# end class ULType452Sub


class addressType455Sub(supermod.addressType455):
    def __init__(self, Country=None, RegionCode=None, Description=None, **kwargs_):
        super(addressType455Sub, self).__init__(Country, RegionCode, Description,  **kwargs_)
supermod.addressType455.subclass = addressType455Sub
# end class addressType455Sub


class FLType459Sub(supermod.FLType459):
    def __init__(self, FullName=None, INN=None, address=None, **kwargs_):
        super(FLType459Sub, self).__init__(FullName, INN, address,  **kwargs_)
supermod.FLType459.subclass = FLType459Sub
# end class FLType459Sub


class addressType462Sub(supermod.addressType462):
    def __init__(self, Country=None, RegionCode=None, Description=None, **kwargs_):
        super(addressType462Sub, self).__init__(Country, RegionCode, Description,  **kwargs_)
supermod.addressType462.subclass = addressType462Sub
# end class addressType462Sub


class FOType466Sub(supermod.FOType466):
    def __init__(self, address=None, **kwargs_):
        super(FOType466Sub, self).__init__(address,  **kwargs_)
supermod.FOType466.subclass = FOType466Sub
# end class FOType466Sub


class addressType467Sub(supermod.addressType467):
    def __init__(self, Country=None, Description=None, **kwargs_):
        super(addressType467Sub, self).__init__(Country, Description,  **kwargs_)
supermod.addressType467.subclass = addressType467Sub
# end class addressType467Sub


class CapacityListType470Sub(supermod.CapacityListType470):
    def __init__(self, CapacityDescr=None, **kwargs_):
        super(CapacityListType470Sub, self).__init__(CapacityDescr,  **kwargs_)
supermod.CapacityListType470.subclass = CapacityListType470Sub
# end class CapacityListType470Sub


class CompositionProductsType472Sub(supermod.CompositionProductsType472):
    def __init__(self, Position=None, **kwargs_):
        super(CompositionProductsType472Sub, self).__init__(Position,  **kwargs_)
supermod.CompositionProductsType472.subclass = CompositionProductsType472Sub
# end class CompositionProductsType472Sub


class TechReglStandardType473Sub(supermod.TechReglStandardType473):
    def __init__(self, TechRegl=None, TechStandard=None, **kwargs_):
        super(TechReglStandardType473Sub, self).__init__(TechRegl, TechStandard,  **kwargs_)
supermod.TechReglStandardType473.subclass = TechReglStandardType473Sub
# end class TechReglStandardType473Sub


class TechReglType474Sub(supermod.TechReglType474):
    def __init__(self, TechReglNumber=None, TechReglName=None, **kwargs_):
        super(TechReglType474Sub, self).__init__(TechReglNumber, TechReglName,  **kwargs_)
supermod.TechReglType474.subclass = TechReglType474Sub
# end class TechReglType474Sub


class TechStandardType477Sub(supermod.TechStandardType477):
    def __init__(self, StandardNumber=None, StandardName=None, **kwargs_):
        super(TechStandardType477Sub, self).__init__(StandardNumber, StandardName,  **kwargs_)
supermod.TechStandardType477.subclass = TechStandardType477Sub
# end class TechStandardType477Sub


class AdditionalDocumentsType480Sub(supermod.AdditionalDocumentsType480):
    def __init__(self, Position=None, **kwargs_):
        super(AdditionalDocumentsType480Sub, self).__init__(Position,  **kwargs_)
supermod.AdditionalDocumentsType480.subclass = AdditionalDocumentsType480Sub
# end class AdditionalDocumentsType480Sub


class StorageTemperatureType485Sub(supermod.StorageTemperatureType485):
    def __init__(self, StorageTemperatureMin=None, StorageTemperatureMax=None, **kwargs_):
        super(StorageTemperatureType485Sub, self).__init__(StorageTemperatureMin, StorageTemperatureMax,  **kwargs_)
supermod.StorageTemperatureType485.subclass = StorageTemperatureType485Sub
# end class StorageTemperatureType485Sub


class StorageHumidityType486Sub(supermod.StorageHumidityType486):
    def __init__(self, StorageHumidityMin=None, StorageHumidityMax=None, **kwargs_):
        super(StorageHumidityType486Sub, self).__init__(StorageHumidityMin, StorageHumidityMax,  **kwargs_)
supermod.StorageHumidityType486.subclass = StorageHumidityType486Sub
# end class StorageHumidityType486Sub


class DeclarationCertificateType488Sub(supermod.DeclarationCertificateType488):
    def __init__(self, Position=None, **kwargs_):
        super(DeclarationCertificateType488Sub, self).__init__(Position,  **kwargs_)
supermod.DeclarationCertificateType488.subclass = DeclarationCertificateType488Sub
# end class DeclarationCertificateType488Sub


class LabelFotoAPType502Sub(supermod.LabelFotoAPType502):
    def __init__(self, LabelFoto=None, CapacityDescrVal=None, **kwargs_):
        super(LabelFotoAPType502Sub, self).__init__(LabelFoto, CapacityDescrVal,  **kwargs_)
supermod.LabelFotoAPType502.subclass = LabelFotoAPType502Sub
# end class LabelFotoAPType502Sub


class AdditionalDocType508Sub(supermod.AdditionalDocType508):
    def __init__(self, TechnologicalInstruction=None, OrganizationStandard=None, InternationalStandardCountryOrigin=None, NationalStandardCountryOrigin=None, NationalRegulations=None, TechnicalDocumentation=None, RC=None, **kwargs_):
        super(AdditionalDocType508Sub, self).__init__(TechnologicalInstruction, OrganizationStandard, InternationalStandardCountryOrigin, NationalStandardCountryOrigin, NationalRegulations, TechnicalDocumentation, RC,  **kwargs_)
supermod.AdditionalDocType508.subclass = AdditionalDocType508Sub
# end class AdditionalDocType508Sub


class TechnologicalInstructionType509Sub(supermod.TechnologicalInstructionType509):
    def __init__(self, TINumber=None, TIDate=None, TIName=None, TIElectronicView=None, **kwargs_):
        super(TechnologicalInstructionType509Sub, self).__init__(TINumber, TIDate, TIName, TIElectronicView,  **kwargs_)
supermod.TechnologicalInstructionType509.subclass = TechnologicalInstructionType509Sub
# end class TechnologicalInstructionType509Sub


class OrganizationStandardType512Sub(supermod.OrganizationStandardType512):
    def __init__(self, OSNumber=None, OSDate=None, OSName=None, **kwargs_):
        super(OrganizationStandardType512Sub, self).__init__(OSNumber, OSDate, OSName,  **kwargs_)
supermod.OrganizationStandardType512.subclass = OrganizationStandardType512Sub
# end class OrganizationStandardType512Sub


class InternationalStandardCountryOriginType515Sub(supermod.InternationalStandardCountryOriginType515):
    def __init__(self, ISCONumber=None, ISCOName=None, **kwargs_):
        super(InternationalStandardCountryOriginType515Sub, self).__init__(ISCONumber, ISCOName,  **kwargs_)
supermod.InternationalStandardCountryOriginType515.subclass = InternationalStandardCountryOriginType515Sub
# end class InternationalStandardCountryOriginType515Sub


class NationalStandardCountryOriginType518Sub(supermod.NationalStandardCountryOriginType518):
    def __init__(self, NSCONumber=None, NSCOName=None, **kwargs_):
        super(NationalStandardCountryOriginType518Sub, self).__init__(NSCONumber, NSCOName,  **kwargs_)
supermod.NationalStandardCountryOriginType518.subclass = NationalStandardCountryOriginType518Sub
# end class NationalStandardCountryOriginType518Sub


class NationalRegulationsType521Sub(supermod.NationalRegulationsType521):
    def __init__(self, NRNumber=None, NRName=None, **kwargs_):
        super(NationalRegulationsType521Sub, self).__init__(NRNumber, NRName,  **kwargs_)
supermod.NationalRegulationsType521.subclass = NationalRegulationsType521Sub
# end class NationalRegulationsType521Sub


class TechnicalDocumentationType524Sub(supermod.TechnicalDocumentationType524):
    def __init__(self, TDNumber=None, TDDate=None, TDName=None, TDElectronicView=None, **kwargs_):
        super(TechnicalDocumentationType524Sub, self).__init__(TDNumber, TDDate, TDName, TDElectronicView,  **kwargs_)
supermod.TechnicalDocumentationType524.subclass = TechnicalDocumentationType524Sub
# end class TechnicalDocumentationType524Sub


class RCType527Sub(supermod.RCType527):
    def __init__(self, RCNumber=None, RCDate=None, RCName=None, **kwargs_):
        super(RCType527Sub, self).__init__(RCNumber, RCDate, RCName,  **kwargs_)
supermod.RCType527.subclass = RCType527Sub
# end class RCType527Sub


class DeclarCertifType531Sub(supermod.DeclarCertifType531):
    def __init__(self, Declaration=None, Certificate=None, **kwargs_):
        super(DeclarCertifType531Sub, self).__init__(Declaration, Certificate,  **kwargs_)
supermod.DeclarCertifType531.subclass = DeclarCertifType531Sub
# end class DeclarCertifType531Sub


class DeclarationType532Sub(supermod.DeclarationType532):
    def __init__(self, DeclarationNumber=None, DateValidity=None, DateExpiration=None, **kwargs_):
        super(DeclarationType532Sub, self).__init__(DeclarationNumber, DateValidity, DateExpiration,  **kwargs_)
supermod.DeclarationType532.subclass = DeclarationType532Sub
# end class DeclarationType532Sub


class CertificateType534Sub(supermod.CertificateType534):
    def __init__(self, CertificateNumber=None, DateValidity=None, DateExpiration=None, **kwargs_):
        super(CertificateType534Sub, self).__init__(CertificateNumber, DateValidity, DateExpiration,  **kwargs_)
supermod.CertificateType534.subclass = CertificateType534Sub
# end class CertificateType534Sub


class ApplicationTypeSub(supermod.ApplicationType):
    def __init__(self, ApplicationType_member=None, ActivityType=None, NameOrg=None, INN=None, OGRN=None, KPP=None, LicenseNumber=None, LicenseDate=None, LicenseValidityTime=None, RegisteredAddress=None, GovernmentFeeList=None, DivisionList=None, **kwargs_):
        super(ApplicationTypeSub, self).__init__(ApplicationType_member, ActivityType, NameOrg, INN, OGRN, KPP, LicenseNumber, LicenseDate, LicenseValidityTime, RegisteredAddress, GovernmentFeeList, DivisionList,  **kwargs_)
supermod.ApplicationType.subclass = ApplicationTypeSub
# end class ApplicationTypeSub


class GovernmentFeeListTypeSub(supermod.GovernmentFeeListType):
    def __init__(self, GovernmentFee=None, **kwargs_):
        super(GovernmentFeeListTypeSub, self).__init__(GovernmentFee,  **kwargs_)
supermod.GovernmentFeeListType.subclass = GovernmentFeeListTypeSub
# end class GovernmentFeeListTypeSub


class DivisionListTypeSub(supermod.DivisionListType):
    def __init__(self, Division=None, **kwargs_):
        super(DivisionListTypeSub, self).__init__(Division,  **kwargs_)
supermod.DivisionListType.subclass = DivisionListTypeSub
# end class DivisionListTypeSub


class HeaderType536Sub(supermod.HeaderType536):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType536Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType536.subclass = HeaderType536Sub
# end class HeaderType536Sub


class ContentType538Sub(supermod.ContentType538):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType538Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType538.subclass = ContentType538Sub
# end class ContentType538Sub


class ContentResourceType542Sub(supermod.ContentResourceType542):
    def __init__(self, Resource=None, **kwargs_):
        super(ContentResourceType542Sub, self).__init__(Resource,  **kwargs_)
supermod.ContentResourceType542.subclass = ContentResourceType542Sub
# end class ContentResourceType542Sub


class HeaderType543Sub(supermod.HeaderType543):
    def __init__(self, NUMBER=None, Date=None, RequestNUMBER=None, RequestDate=None, RequestFSM=None, Declarer=None, Comment=None, **kwargs_):
        super(HeaderType543Sub, self).__init__(NUMBER, Date, RequestNUMBER, RequestDate, RequestFSM, Declarer, Comment,  **kwargs_)
supermod.HeaderType543.subclass = HeaderType543Sub
# end class HeaderType543Sub


class HeaderType544Sub(supermod.HeaderType544):
    def __init__(self, NUMBER=None, Date=None, Sender=None, Consignee=None, **kwargs_):
        super(HeaderType544Sub, self).__init__(NUMBER, Date, Sender, Consignee,  **kwargs_)
supermod.HeaderType544.subclass = HeaderType544Sub
# end class HeaderType544Sub


class HeaderType545Sub(supermod.HeaderType545):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType545Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType545.subclass = HeaderType545Sub
# end class HeaderType545Sub


class ContentType547Sub(supermod.ContentType547):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType547Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType547.subclass = ContentType547Sub
# end class ContentType547Sub


class writeoffvolumeTypeSub(supermod.writeoffvolumeType):
    def __init__(self, Quantity=None, volume=None, **kwargs_):
        super(writeoffvolumeTypeSub, self).__init__(Quantity, volume,  **kwargs_)
supermod.writeoffvolumeType.subclass = writeoffvolumeTypeSub
# end class writeoffvolumeTypeSub


class ContentType548Sub(supermod.ContentType548):
    def __init__(self, Bottle=None, Nomark=None, Catering=None, **kwargs_):
        super(ContentType548Sub, self).__init__(Bottle, Nomark, Catering,  **kwargs_)
supermod.ContentType548.subclass = ContentType548Sub
# end class ContentType548Sub


class HeaderType549Sub(supermod.HeaderType549):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType549Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType549.subclass = HeaderType549Sub
# end class HeaderType549Sub


class ContentType551Sub(supermod.ContentType551):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType551Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType551.subclass = ContentType551Sub
# end class ContentType551Sub


class ContentResourceType555Sub(supermod.ContentResourceType555):
    def __init__(self, Resource=None, GRAPERESOURCE=None, **kwargs_):
        super(ContentResourceType555Sub, self).__init__(Resource, GRAPERESOURCE,  **kwargs_)
supermod.ContentResourceType555.subclass = ContentResourceType555Sub
# end class ContentResourceType555Sub


class HeaderType556Sub(supermod.HeaderType556):
    def __init__(self, NUMBER=None, Date=None, ImportedDate=None, Importer=None, Supplier=None, GTDNUMBER=None, GTDDate=None, ContractNUMBER=None, ContractDate=None, Country=None, Note=None, IDInvoicePlannedImport=None, **kwargs_):
        super(HeaderType556Sub, self).__init__(NUMBER, Date, ImportedDate, Importer, Supplier, GTDNUMBER, GTDDate, ContractNUMBER, ContractDate, Country, Note, IDInvoicePlannedImport,  **kwargs_)
supermod.HeaderType556.subclass = HeaderType556Sub
# end class HeaderType556Sub


class ContentType559Sub(supermod.ContentType559):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType559Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType559.subclass = ContentType559Sub
# end class ContentType559Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Documents'
        rootClass = supermod.Documents
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"',
##             pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Documents'
        rootClass = supermod.Documents
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(content)
##         sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Documents'
        rootClass = supermod.Documents
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='xmlns:ns="http://fsrar.ru/WEGAIS/WB_DOC_SINGLE_01"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Documents'
        rootClass = supermod.Documents
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('#from ??? import *\n\n')
##         sys.stdout.write('import ??? as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
