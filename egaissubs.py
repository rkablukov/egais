#!/usr/bin/env python

#
# Generated Wed Mar 11 12:21:36 2020 by generateDS.py version 2.35.15.
# Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'egais.py')
#   ('-s', 'egaissubs.py')
#   ('--use-old-simpletype-validators', '')
#   ('--external-encoding', 'utf-8')
#   ('--silence', '')
#
# Command line arguments:
#   .\xsd\WB_DOC_SINGLE_01.xsd
#
# Command line:
#   C:\Users\roof\.virtualenvs\egais-djViaaeL\Scripts\generateDS.py -o "egais.py" -s "egaissubs.py" --use-old-simpletype-validators --external-encoding="utf-8" --silence .\xsd\WB_DOC_SINGLE_01.xsd
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
    def __init__(self, WayBill=None, Ticket=None, WayBillAct=None, ConfirmTicket=None, TTNInformBReg=None, ActInventory=None, ActChargeOn=None, ActInventoryInformBReg=None, QueryAP=None, QuerySSP=None, QuerySP=None, QueryClients=None, QueryClientVersion=None, QueryRests=None, QueryFormBHistory=None, QueryResendDoc=None, QueryFormA=None, QueryFormB=None, ActWriteOff=None, RepProducedProduct=None, RepImportedProduct=None, ReplySSP=None, ReplySpirit=None, ReplyClient=None, ReplyAP=None, ReplyRests=None, ReplyFormA=None, ReplyFormB=None, ReplyHistFormB=None, ReplyClientVersion=None, QueryRejectRepProduced=None, QueryRejectRepImported=None, ReplySSP_v2=None, ReplySpirit_v2=None, ReplyClient_v2=None, ReplyAP_v2=None, ReplyRests_v2=None, ReplyForm1=None, ReplyForm2=None, ReplyHistForm2=None, WayBill_v2=None, WayBillAct_v2=None, ActChargeOn_v2=None, ActInventoryInformF2Reg=None, TTNInformF2Reg=None, QueryAP_v2=None, QuerySSP_v2=None, QuerySP_v2=None, QueryClients_v2=None, QueryRests_v2=None, QueryFormF1=None, QueryFormF2=None, ActWriteOff_v2=None, TransferFromShop=None, TransferToShop=None, QueryForm2History=None, RepInformF1Reg=None, ReplyNoAnswerTTN=None, QueryNATTN=None, QueryRestsShop_v2=None, ReplyRestsShop_v2=None, Asiiu=None, AsiiuTime=None, ActChargeOnShop_v2=None, ActWriteOffShop_v2=None, InfoVersionTTN=None, QueryBarcode=None, ReplyBarcode=None, RequestRepealWB=None, ConfirmRepealWB=None, RequestRepealACO=None, RequestRepealAWO=None, QueryRests_Mini=None, QueryRestsShop_Mini=None, ReplyRests_Mini=None, ReplyRestsShop_Mini=None, RequestAddFProducer=None, RequestAddProducts=None, QueryHistoryRestShop=None, QueryWriteOffCheque=None, ReplyHistoryShop=None, ReplyWriteOffCheque=None, AscpNav=None, AsiiuSign=None, AsiiuTimeSign=None, WayBill_v3=None, ActWriteOff_v3=None, WayBillAct_v3=None, RepProducedProduct_v3=None, RepImportedProduct_v3=None, QueryRestBCode=None, ReplyRestBCode=None, ActFixBarCode=None, ActUnFixBarCode=None, QueryParentHistForm2=None, ReplyParentHistForm2=None, TTNHistoryF2Reg=None, CarrierNotice=None, **kwargs_):
        super(DocBodySub, self).__init__(WayBill, Ticket, WayBillAct, ConfirmTicket, TTNInformBReg, ActInventory, ActChargeOn, ActInventoryInformBReg, QueryAP, QuerySSP, QuerySP, QueryClients, QueryClientVersion, QueryRests, QueryFormBHistory, QueryResendDoc, QueryFormA, QueryFormB, ActWriteOff, RepProducedProduct, RepImportedProduct, ReplySSP, ReplySpirit, ReplyClient, ReplyAP, ReplyRests, ReplyFormA, ReplyFormB, ReplyHistFormB, ReplyClientVersion, QueryRejectRepProduced, QueryRejectRepImported, ReplySSP_v2, ReplySpirit_v2, ReplyClient_v2, ReplyAP_v2, ReplyRests_v2, ReplyForm1, ReplyForm2, ReplyHistForm2, WayBill_v2, WayBillAct_v2, ActChargeOn_v2, ActInventoryInformF2Reg, TTNInformF2Reg, QueryAP_v2, QuerySSP_v2, QuerySP_v2, QueryClients_v2, QueryRests_v2, QueryFormF1, QueryFormF2, ActWriteOff_v2, TransferFromShop, TransferToShop, QueryForm2History, RepInformF1Reg, ReplyNoAnswerTTN, QueryNATTN, QueryRestsShop_v2, ReplyRestsShop_v2, Asiiu, AsiiuTime, ActChargeOnShop_v2, ActWriteOffShop_v2, InfoVersionTTN, QueryBarcode, ReplyBarcode, RequestRepealWB, ConfirmRepealWB, RequestRepealACO, RequestRepealAWO, QueryRests_Mini, QueryRestsShop_Mini, ReplyRests_Mini, ReplyRestsShop_Mini, RequestAddFProducer, RequestAddProducts, QueryHistoryRestShop, QueryWriteOffCheque, ReplyHistoryShop, ReplyWriteOffCheque, AscpNav, AsiiuSign, AsiiuTimeSign, WayBill_v3, ActWriteOff_v3, WayBillAct_v3, RepProducedProduct_v3, RepImportedProduct_v3, QueryRestBCode, ReplyRestBCode, ActFixBarCode, ActUnFixBarCode, QueryParentHistForm2, ReplyParentHistForm2, TTNHistoryF2Reg, CarrierNotice,  **kwargs_)
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
    def __init__(self, amc=None, **kwargs_):
        super(AMCforDocTypeSub, self).__init__(amc,  **kwargs_)
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
    def __init__(self, UL=None, FL=None, **kwargs_):
        super(OrgInfoRus_v2Sub, self).__init__(UL, FL,  **kwargs_)
supermod.OrgInfoRus_v2.subclass = OrgInfoRus_v2Sub
# end class OrgInfoRus_v2Sub


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
    def __init__(self, Product=None, StartDate=None, EndDate=None, VbsStart=None, VbsEnd=None, AStart=None, AEnd=None, PercentAlc=None, BottleCountStart=None, BottleCountEnd=None, Temperature=None, Mode=None, **kwargs_):
        super(DataTypeSub, self).__init__(Product, StartDate, EndDate, VbsStart, VbsEnd, AStart, AEnd, PercentAlc, BottleCountStart, BottleCountEnd, Temperature, Mode,  **kwargs_)
supermod.DataType.subclass = DataTypeSub
# end class DataTypeSub


class AsiiuTimeSub(supermod.AsiiuTime):
    def __init__(self, Sensor=None, Producer=None, Data=None, **kwargs_):
        super(AsiiuTimeSub, self).__init__(Sensor, Producer, Data,  **kwargs_)
supermod.AsiiuTime.subclass = AsiiuTimeSub
# end class AsiiuTimeSub


class DataType32Sub(supermod.DataType32):
    def __init__(self, Product=None, ControlDate=None, VbsControl=None, AControl=None, PercentAlc=None, BottleCountControl=None, Temperature=None, Mode=None, **kwargs_):
        super(DataType32Sub, self).__init__(Product, ControlDate, VbsControl, AControl, PercentAlc, BottleCountControl, Temperature, Mode,  **kwargs_)
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
    def __init__(self, Producer=None, Type=None, VidCode=None, CountryCode=None, FullName=None, ShortName=None, Unpacked_Flag=None, Capacity=None, PERCENT_ALC=None, PERCENT_ALC_min=None, PERCENT_ALC_max=None, FRAPID=None, **kwargs_):
        super(RequestAddSSPPositionTypeSub, self).__init__(Producer, Type, VidCode, CountryCode, FullName, ShortName, Unpacked_Flag, Capacity, PERCENT_ALC, PERCENT_ALC_min, PERCENT_ALC_max, FRAPID,  **kwargs_)
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
    def __init__(self, ProductCode=None, Quantity20=None, AlcPerc20=None, PosIdentity=None, **kwargs_):
        super(PositionType50Sub, self).__init__(ProductCode, Quantity20, AlcPerc20, PosIdentity,  **kwargs_)
supermod.PositionType50.subclass = PositionType50Sub
# end class PositionType50Sub


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


class HeaderType55Sub(supermod.HeaderType55):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType55Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType55.subclass = HeaderType55Sub
# end class HeaderType55Sub


class ContentType57Sub(supermod.ContentType57):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType57Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType57.subclass = ContentType57Sub
# end class ContentType57Sub


class HeaderType58Sub(supermod.HeaderType58):
    def __init__(self, IsConfirm=None, TicketNumber=None, TicketDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType58Sub, self).__init__(IsConfirm, TicketNumber, TicketDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType58.subclass = HeaderType58Sub
# end class HeaderType58Sub


class HeaderType60Sub(supermod.HeaderType60):
    def __init__(self, Number=None, DivisionName=None, InventoryBasis=None, InventoryBasisNumber=None, InventoryBasisDate=None, InventoryDateBegin=None, InventoryDateEnd=None, Note=None, **kwargs_):
        super(HeaderType60Sub, self).__init__(Number, DivisionName, InventoryBasis, InventoryBasisNumber, InventoryBasisDate, InventoryDateBegin, InventoryDateEnd, Note,  **kwargs_)
supermod.HeaderType60.subclass = HeaderType60Sub
# end class HeaderType60Sub


class ContentType62Sub(supermod.ContentType62):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType62Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType62.subclass = ContentType62Sub
# end class ContentType62Sub


class InformBType63Sub(supermod.InformBType63):
    def __init__(self, InformBItem=None, **kwargs_):
        super(InformBType63Sub, self).__init__(InformBItem,  **kwargs_)
supermod.InformBType63.subclass = InformBType63Sub
# end class InformBType63Sub


class HeaderType64Sub(supermod.HeaderType64):
    def __init__(self, Number=None, ActDate=None, Note=None, **kwargs_):
        super(HeaderType64Sub, self).__init__(Number, ActDate, Note,  **kwargs_)
supermod.HeaderType64.subclass = HeaderType64Sub
# end class HeaderType64Sub


class ContentType66Sub(supermod.ContentType66):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType66Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType66.subclass = ContentType66Sub
# end class ContentType66Sub


class InformABTypeSub(supermod.InformABType):
    def __init__(self, InformABKey=None, InformABReg=None, **kwargs_):
        super(InformABTypeSub, self).__init__(InformABKey, InformABReg,  **kwargs_)
supermod.InformABType.subclass = InformABTypeSub
# end class InformABTypeSub


class HeaderType67Sub(supermod.HeaderType67):
    def __init__(self, Identity=None, ActRegId=None, Number=None, **kwargs_):
        super(HeaderType67Sub, self).__init__(Identity, ActRegId, Number,  **kwargs_)
supermod.HeaderType67.subclass = HeaderType67Sub
# end class HeaderType67Sub


class ContentType68Sub(supermod.ContentType68):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType68Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType68.subclass = ContentType68Sub
# end class ContentType68Sub


class InformBType69Sub(supermod.InformBType69):
    def __init__(self, InformBItem=None, **kwargs_):
        super(InformBType69Sub, self).__init__(InformBItem,  **kwargs_)
supermod.InformBType69.subclass = InformBType69Sub
# end class InformBType69Sub


class ParametersTypeSub(supermod.ParametersType):
    def __init__(self, Parameter=None, **kwargs_):
        super(ParametersTypeSub, self).__init__(Parameter,  **kwargs_)
supermod.ParametersType.subclass = ParametersTypeSub
# end class ParametersTypeSub


class HeaderType70Sub(supermod.HeaderType70):
    def __init__(self, Identity=None, WBRegId=None, EGAISFixNumber=None, EGAISFixDate=None, WBNUMBER=None, WBDate=None, Shipper=None, Consignee=None, Supplier=None, **kwargs_):
        super(HeaderType70Sub, self).__init__(Identity, WBRegId, EGAISFixNumber, EGAISFixDate, WBNUMBER, WBDate, Shipper, Consignee, Supplier,  **kwargs_)
supermod.HeaderType70.subclass = HeaderType70Sub
# end class HeaderType70Sub


class ContentType71Sub(supermod.ContentType71):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType71Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType71.subclass = ContentType71Sub
# end class ContentType71Sub


class HeaderType72Sub(supermod.HeaderType72):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType72Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType72.subclass = HeaderType72Sub
# end class HeaderType72Sub


class ContentType74Sub(supermod.ContentType74):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType74Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType74.subclass = ContentType74Sub
# end class ContentType74Sub


class HeaderType75Sub(supermod.HeaderType75):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType75Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType75.subclass = HeaderType75Sub
# end class HeaderType75Sub


class ContentType77Sub(supermod.ContentType77):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType77Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType77.subclass = ContentType77Sub
# end class ContentType77Sub


class ContentResourceTypeSub(supermod.ContentResourceType):
    def __init__(self, Resource=None, **kwargs_):
        super(ContentResourceTypeSub, self).__init__(Resource,  **kwargs_)
supermod.ContentResourceType.subclass = ContentResourceTypeSub
# end class ContentResourceTypeSub


class addresslistType78Sub(supermod.addresslistType78):
    def __init__(self, address=None, **kwargs_):
        super(addresslistType78Sub, self).__init__(address,  **kwargs_)
supermod.addresslistType78.subclass = addresslistType78Sub
# end class addresslistType78Sub


class RangesType104Sub(supermod.RangesType104):
    def __init__(self, Range=None, **kwargs_):
        super(RangesType104Sub, self).__init__(Range,  **kwargs_)
supermod.RangesType104.subclass = RangesType104Sub
# end class RangesType104Sub


class RangeType105Sub(supermod.RangeType105):
    def __init__(self, Identity=None, Rank=None, Start=None, Last=None, **kwargs_):
        super(RangeType105Sub, self).__init__(Identity, Rank, Start, Last,  **kwargs_)
supermod.RangeType105.subclass = RangeType105Sub
# end class RangeType105Sub


class HeaderType131Sub(supermod.HeaderType131):
    def __init__(self, NUMBER=None, Date=None, ImportedDate=None, Importer=None, Supplier=None, GTDNUMBER=None, GTDDate=None, ContractNUMBER=None, ContractDate=None, Country=None, Note=None, **kwargs_):
        super(HeaderType131Sub, self).__init__(NUMBER, Date, ImportedDate, Importer, Supplier, GTDNUMBER, GTDDate, ContractNUMBER, ContractDate, Country, Note,  **kwargs_)
supermod.HeaderType131.subclass = HeaderType131Sub
# end class HeaderType131Sub


class ContentType134Sub(supermod.ContentType134):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType134Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType134.subclass = ContentType134Sub
# end class ContentType134Sub


class ProductsType138Sub(supermod.ProductsType138):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType138Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType138.subclass = ProductsType138Sub
# end class ProductsType138Sub


class ProductsType139Sub(supermod.ProductsType139):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType139Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType139.subclass = ProductsType139Sub
# end class ProductsType139Sub


class ClientsTypeSub(supermod.ClientsType):
    def __init__(self, Client=None, **kwargs_):
        super(ClientsTypeSub, self).__init__(Client,  **kwargs_)
supermod.ClientsType.subclass = ClientsTypeSub
# end class ClientsTypeSub


class ProductsType140Sub(supermod.ProductsType140):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType140Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType140.subclass = ProductsType140Sub
# end class ProductsType140Sub


class ProductsType141Sub(supermod.ProductsType141):
    def __init__(self, StockPosition=None, **kwargs_):
        super(ProductsType141Sub, self).__init__(StockPosition,  **kwargs_)
supermod.ProductsType141.subclass = ProductsType141Sub
# end class ProductsType141Sub


class HistoryBTypeSub(supermod.HistoryBType):
    def __init__(self, OperationB=None, **kwargs_):
        super(HistoryBTypeSub, self).__init__(OperationB,  **kwargs_)
supermod.HistoryBType.subclass = HistoryBTypeSub
# end class HistoryBTypeSub


class ProductsType142Sub(supermod.ProductsType142):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType142Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType142.subclass = ProductsType142Sub
# end class ProductsType142Sub


class ProductsType143Sub(supermod.ProductsType143):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType143Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType143.subclass = ProductsType143Sub
# end class ProductsType143Sub


class ClientsType144Sub(supermod.ClientsType144):
    def __init__(self, Client=None, **kwargs_):
        super(ClientsType144Sub, self).__init__(Client,  **kwargs_)
supermod.ClientsType144.subclass = ClientsType144Sub
# end class ClientsType144Sub


class ProductsType145Sub(supermod.ProductsType145):
    def __init__(self, Product=None, **kwargs_):
        super(ProductsType145Sub, self).__init__(Product,  **kwargs_)
supermod.ProductsType145.subclass = ProductsType145Sub
# end class ProductsType145Sub


class ProductsType146Sub(supermod.ProductsType146):
    def __init__(self, StockPosition=None, **kwargs_):
        super(ProductsType146Sub, self).__init__(StockPosition,  **kwargs_)
supermod.ProductsType146.subclass = ProductsType146Sub
# end class ProductsType146Sub


class HistoryF2TypeSub(supermod.HistoryF2Type):
    def __init__(self, OperationB=None, **kwargs_):
        super(HistoryF2TypeSub, self).__init__(OperationB,  **kwargs_)
supermod.HistoryF2Type.subclass = HistoryF2TypeSub
# end class HistoryF2TypeSub


class HeaderType147Sub(supermod.HeaderType147):
    def __init__(self, Type='WBInvoiceFromMe', NUMBER=None, Date=None, ShippingDate=None, Transport=None, Shipper=None, Consignee=None, Base=None, Note=None, VarField1=None, VarField2=None, VarField3=None, **kwargs_):
        super(HeaderType147Sub, self).__init__(Type, NUMBER, Date, ShippingDate, Transport, Shipper, Consignee, Base, Note, VarField1, VarField2, VarField3,  **kwargs_)
supermod.HeaderType147.subclass = HeaderType147Sub
# end class HeaderType147Sub


class ContentType150Sub(supermod.ContentType150):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType150Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType150.subclass = ContentType150Sub
# end class ContentType150Sub


class HeaderType161Sub(supermod.HeaderType161):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType161Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType161.subclass = HeaderType161Sub
# end class HeaderType161Sub


class ContentType163Sub(supermod.ContentType163):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType163Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType163.subclass = ContentType163Sub
# end class ContentType163Sub


class HeaderType164Sub(supermod.HeaderType164):
    def __init__(self, Number=None, ActDate=None, TypeChargeOn=None, ActWriteOff=None, Note=None, **kwargs_):
        super(HeaderType164Sub, self).__init__(Number, ActDate, TypeChargeOn, ActWriteOff, Note,  **kwargs_)
supermod.HeaderType164.subclass = HeaderType164Sub
# end class HeaderType164Sub


class ContentType166Sub(supermod.ContentType166):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType166Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType166.subclass = ContentType166Sub
# end class ContentType166Sub


class InformF1F2TypeSub(supermod.InformF1F2Type):
    def __init__(self, InformF1F2Reg=None, **kwargs_):
        super(InformF1F2TypeSub, self).__init__(InformF1F2Reg,  **kwargs_)
supermod.InformF1F2Type.subclass = InformF1F2TypeSub
# end class InformF1F2TypeSub


class HeaderType167Sub(supermod.HeaderType167):
    def __init__(self, Identity=None, ActRegId=None, Number=None, **kwargs_):
        super(HeaderType167Sub, self).__init__(Identity, ActRegId, Number,  **kwargs_)
supermod.HeaderType167.subclass = HeaderType167Sub
# end class HeaderType167Sub


class ContentType168Sub(supermod.ContentType168):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType168Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType168.subclass = ContentType168Sub
# end class ContentType168Sub


class InformF2Type169Sub(supermod.InformF2Type169):
    def __init__(self, InformF2Item=None, **kwargs_):
        super(InformF2Type169Sub, self).__init__(InformF2Item,  **kwargs_)
supermod.InformF2Type169.subclass = InformF2Type169Sub
# end class InformF2Type169Sub


class HeaderType170Sub(supermod.HeaderType170):
    def __init__(self, Identity=None, WBRegId=None, EGAISFixNumber=None, EGAISFixDate=None, WBNUMBER=None, WBDate=None, Shipper=None, Consignee=None, **kwargs_):
        super(HeaderType170Sub, self).__init__(Identity, WBRegId, EGAISFixNumber, EGAISFixDate, WBNUMBER, WBDate, Shipper, Consignee,  **kwargs_)
supermod.HeaderType170.subclass = HeaderType170Sub
# end class HeaderType170Sub


class ContentType171Sub(supermod.ContentType171):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType171Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType171.subclass = ContentType171Sub
# end class ContentType171Sub


class HeaderType172Sub(supermod.HeaderType172):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType172Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType172.subclass = HeaderType172Sub
# end class HeaderType172Sub


class ContentType174Sub(supermod.ContentType174):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType174Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType174.subclass = ContentType174Sub
# end class ContentType174Sub


class HeaderType175Sub(supermod.HeaderType175):
    def __init__(self, TransferNumber=None, TransferDate=None, Note=None, **kwargs_):
        super(HeaderType175Sub, self).__init__(TransferNumber, TransferDate, Note,  **kwargs_)
supermod.HeaderType175.subclass = HeaderType175Sub
# end class HeaderType175Sub


class ContentType177Sub(supermod.ContentType177):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType177Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType177.subclass = ContentType177Sub
# end class ContentType177Sub


class HeaderType178Sub(supermod.HeaderType178):
    def __init__(self, TransferNumber=None, TransferDate=None, Note=None, **kwargs_):
        super(HeaderType178Sub, self).__init__(TransferNumber, TransferDate, Note,  **kwargs_)
supermod.HeaderType178.subclass = HeaderType178Sub
# end class HeaderType178Sub


class ContentType180Sub(supermod.ContentType180):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType180Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType180.subclass = ContentType180Sub
# end class ContentType180Sub


class HeaderType181Sub(supermod.HeaderType181):
    def __init__(self, Identity=None, RepRegId=None, Client=None, **kwargs_):
        super(HeaderType181Sub, self).__init__(Identity, RepRegId, Client,  **kwargs_)
supermod.HeaderType181.subclass = HeaderType181Sub
# end class HeaderType181Sub


class ContentType182Sub(supermod.ContentType182):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType182Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType182.subclass = ContentType182Sub
# end class ContentType182Sub


class ttnlistTypeSub(supermod.ttnlistType):
    def __init__(self, NoAnswer=None, **kwargs_):
        super(ttnlistTypeSub, self).__init__(NoAnswer,  **kwargs_)
supermod.ttnlistType.subclass = ttnlistTypeSub
# end class ttnlistTypeSub


class ProductsType183Sub(supermod.ProductsType183):
    def __init__(self, ShopPosition=None, **kwargs_):
        super(ProductsType183Sub, self).__init__(ShopPosition,  **kwargs_)
supermod.ProductsType183.subclass = ProductsType183Sub
# end class ProductsType183Sub


class SensorTypeSub(supermod.SensorType):
    def __init__(self, SensorNumber=None, PlaceId=None, SensorModel=None, **kwargs_):
        super(SensorTypeSub, self).__init__(SensorNumber, PlaceId, SensorModel,  **kwargs_)
supermod.SensorType.subclass = SensorTypeSub
# end class SensorTypeSub


class DataType184Sub(supermod.DataType184):
    def __init__(self, Position=None, **kwargs_):
        super(DataType184Sub, self).__init__(Position,  **kwargs_)
supermod.DataType184.subclass = DataType184Sub
# end class DataType184Sub


class SensorType185Sub(supermod.SensorType185):
    def __init__(self, SensorNumber=None, PlaceId=None, SensorModel=None, **kwargs_):
        super(SensorType185Sub, self).__init__(SensorNumber, PlaceId, SensorModel,  **kwargs_)
supermod.SensorType185.subclass = SensorType185Sub
# end class SensorType185Sub


class DataType186Sub(supermod.DataType186):
    def __init__(self, Position=None, **kwargs_):
        super(DataType186Sub, self).__init__(Position,  **kwargs_)
supermod.DataType186.subclass = DataType186Sub
# end class DataType186Sub


class HeaderType187Sub(supermod.HeaderType187):
    def __init__(self, Number=None, ActDate=None, TypeChargeOn=None, ActWriteOff=None, Note=None, **kwargs_):
        super(HeaderType187Sub, self).__init__(Number, ActDate, TypeChargeOn, ActWriteOff, Note,  **kwargs_)
supermod.HeaderType187.subclass = HeaderType187Sub
# end class HeaderType187Sub


class ContentType189Sub(supermod.ContentType189):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType189Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType189.subclass = ContentType189Sub
# end class ContentType189Sub


class HeaderType190Sub(supermod.HeaderType190):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType190Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType190.subclass = HeaderType190Sub
# end class HeaderType190Sub


class ContentType192Sub(supermod.ContentType192):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType192Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType192.subclass = ContentType192Sub
# end class ContentType192Sub


class MarksTypeSub(supermod.MarksType):
    def __init__(self, Mark=None, **kwargs_):
        super(MarksTypeSub, self).__init__(Mark,  **kwargs_)
supermod.MarksType.subclass = MarksTypeSub
# end class MarksTypeSub


class MarksType193Sub(supermod.MarksType193):
    def __init__(self, Mark=None, **kwargs_):
        super(MarksType193Sub, self).__init__(Mark,  **kwargs_)
supermod.MarksType193.subclass = MarksType193Sub
# end class MarksType193Sub


class HeaderType194Sub(supermod.HeaderType194):
    def __init__(self, IsConfirm=None, ConfirmNumber=None, ConfirmDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType194Sub, self).__init__(IsConfirm, ConfirmNumber, ConfirmDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType194.subclass = HeaderType194Sub
# end class HeaderType194Sub


class ProductsType196Sub(supermod.ProductsType196):
    def __init__(self, StockPosition=None, **kwargs_):
        super(ProductsType196Sub, self).__init__(StockPosition,  **kwargs_)
supermod.ProductsType196.subclass = ProductsType196Sub
# end class ProductsType196Sub


class ProductsType197Sub(supermod.ProductsType197):
    def __init__(self, ShopPosition=None, **kwargs_):
        super(ProductsType197Sub, self).__init__(ShopPosition,  **kwargs_)
supermod.ProductsType197.subclass = ProductsType197Sub
# end class ProductsType197Sub


class HistoryTypeSub(supermod.HistoryType):
    def __init__(self, DocData=None, **kwargs_):
        super(HistoryTypeSub, self).__init__(DocData,  **kwargs_)
supermod.HistoryType.subclass = HistoryTypeSub
# end class HistoryTypeSub


class SensorType206Sub(supermod.SensorType206):
    def __init__(self, IMEI=None, **kwargs_):
        super(SensorType206Sub, self).__init__(IMEI,  **kwargs_)
supermod.SensorType206.subclass = SensorType206Sub
# end class SensorType206Sub


class DataLevelGaugeTypeSub(supermod.DataLevelGaugeType):
    def __init__(self, LevelGauge=None, **kwargs_):
        super(DataLevelGaugeTypeSub, self).__init__(LevelGauge,  **kwargs_)
supermod.DataLevelGaugeType.subclass = DataLevelGaugeTypeSub
# end class DataLevelGaugeTypeSub


class HeaderType207Sub(supermod.HeaderType207):
    def __init__(self, Type='WBInvoiceFromMe', NUMBER=None, Date=None, ShippingDate=None, Transport=None, Shipper=None, Consignee=None, Base=None, Note=None, VarField1=None, VarField2=None, VarField3=None, **kwargs_):
        super(HeaderType207Sub, self).__init__(Type, NUMBER, Date, ShippingDate, Transport, Shipper, Consignee, Base, Note, VarField1, VarField2, VarField3,  **kwargs_)
supermod.HeaderType207.subclass = HeaderType207Sub
# end class HeaderType207Sub


class ContentType213Sub(supermod.ContentType213):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType213Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType213.subclass = ContentType213Sub
# end class ContentType213Sub


class boxInfoTypeSub(supermod.boxInfoType):
    def __init__(self, boxtree=None, **kwargs_):
        super(boxInfoTypeSub, self).__init__(boxtree,  **kwargs_)
supermod.boxInfoType.subclass = boxInfoTypeSub
# end class boxInfoTypeSub


class HeaderType224Sub(supermod.HeaderType224):
    def __init__(self, ActNumber=None, ActDate=None, TypeWriteOff=None, Note=None, **kwargs_):
        super(HeaderType224Sub, self).__init__(ActNumber, ActDate, TypeWriteOff, Note,  **kwargs_)
supermod.HeaderType224.subclass = HeaderType224Sub
# end class HeaderType224Sub


class ContentType226Sub(supermod.ContentType226):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType226Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType226.subclass = ContentType226Sub
# end class ContentType226Sub


class HeaderType227Sub(supermod.HeaderType227):
    def __init__(self, IsAccept=None, ACTNUMBER=None, ActDate=None, WBRegId=None, Note=None, **kwargs_):
        super(HeaderType227Sub, self).__init__(IsAccept, ACTNUMBER, ActDate, WBRegId, Note,  **kwargs_)
supermod.HeaderType227.subclass = HeaderType227Sub
# end class HeaderType227Sub


class ContentType229Sub(supermod.ContentType229):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType229Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType229.subclass = ContentType229Sub
# end class ContentType229Sub


class HeaderType230Sub(supermod.HeaderType230):
    def __init__(self, Type='OperProduction', NUMBER=None, Date=None, ProducedDate=None, Producer=None, Note=None, **kwargs_):
        super(HeaderType230Sub, self).__init__(Type, NUMBER, Date, ProducedDate, Producer, Note,  **kwargs_)
supermod.HeaderType230.subclass = HeaderType230Sub
# end class HeaderType230Sub


class ContentType232Sub(supermod.ContentType232):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType232Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType232.subclass = ContentType232Sub
# end class ContentType232Sub


class ContentResourceType233Sub(supermod.ContentResourceType233):
    def __init__(self, Resource=None, **kwargs_):
        super(ContentResourceType233Sub, self).__init__(Resource,  **kwargs_)
supermod.ContentResourceType233.subclass = ContentResourceType233Sub
# end class ContentResourceType233Sub


class HeaderType237Sub(supermod.HeaderType237):
    def __init__(self, NUMBER=None, Date=None, ImportedDate=None, Importer=None, Supplier=None, GTDNUMBER=None, GTDDate=None, ContractNUMBER=None, ContractDate=None, Country=None, Note=None, **kwargs_):
        super(HeaderType237Sub, self).__init__(NUMBER, Date, ImportedDate, Importer, Supplier, GTDNUMBER, GTDDate, ContractNUMBER, ContractDate, Country, Note,  **kwargs_)
supermod.HeaderType237.subclass = HeaderType237Sub
# end class HeaderType237Sub


class ContentType240Sub(supermod.ContentType240):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType240Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType240.subclass = ContentType240Sub
# end class ContentType240Sub


class HeaderType244Sub(supermod.HeaderType244):
    def __init__(self, Number=None, ActDate=None, Note=None, **kwargs_):
        super(HeaderType244Sub, self).__init__(Number, ActDate, Note,  **kwargs_)
supermod.HeaderType244.subclass = HeaderType244Sub
# end class HeaderType244Sub


class ContentType246Sub(supermod.ContentType246):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType246Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType246.subclass = ContentType246Sub
# end class ContentType246Sub


class HeaderType247Sub(supermod.HeaderType247):
    def __init__(self, Number=None, ActDate=None, Note=None, **kwargs_):
        super(HeaderType247Sub, self).__init__(Number, ActDate, Note,  **kwargs_)
supermod.HeaderType247.subclass = HeaderType247Sub
# end class HeaderType247Sub


class ContentType249Sub(supermod.ContentType249):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType249Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType249.subclass = ContentType249Sub
# end class ContentType249Sub


class ParentHistTypeSub(supermod.ParentHistType):
    def __init__(self, step=None, **kwargs_):
        super(ParentHistTypeSub, self).__init__(step,  **kwargs_)
supermod.ParentHistType.subclass = ParentHistTypeSub
# end class ParentHistTypeSub


class HeaderType250Sub(supermod.HeaderType250):
    def __init__(self, WBRegId=None, **kwargs_):
        super(HeaderType250Sub, self).__init__(WBRegId,  **kwargs_)
supermod.HeaderType250.subclass = HeaderType250Sub
# end class HeaderType250Sub


class ContentType251Sub(supermod.ContentType251):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType251Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType251.subclass = ContentType251Sub
# end class ContentType251Sub


class HistF2TypeSub(supermod.HistF2Type):
    def __init__(self, step=None, **kwargs_):
        super(HistF2TypeSub, self).__init__(step,  **kwargs_)
supermod.HistF2Type.subclass = HistF2TypeSub
# end class HistF2TypeSub


class HeaderType252Sub(supermod.HeaderType252):
    def __init__(self, ClientIdentity=None, Serial=None, Shipper=None, Consignee=None, Carrier=None, ClientTransport=None, ShipmentOutDate=None, ShipmentInDate=None, EGAISFixNumberTTN=None, NotifNumber=None, NotifDate=None, NotifSupplierId=None, NotifCustomerId=None, **kwargs_):
        super(HeaderType252Sub, self).__init__(ClientIdentity, Serial, Shipper, Consignee, Carrier, ClientTransport, ShipmentOutDate, ShipmentInDate, EGAISFixNumberTTN, NotifNumber, NotifDate, NotifSupplierId, NotifCustomerId,  **kwargs_)
supermod.HeaderType252.subclass = HeaderType252Sub
# end class HeaderType252Sub


class ContentType253Sub(supermod.ContentType253):
    def __init__(self, Position=None, **kwargs_):
        super(ContentType253Sub, self).__init__(Position,  **kwargs_)
supermod.ContentType253.subclass = ContentType253Sub
# end class ContentType253Sub


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
