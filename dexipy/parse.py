"""The module ``dexipy.parse`` implements parsing and reading of ``.dxi`` files.

The only functions interesting for public use are :py:func:`dexipy.parse.read_dexi` and
:py:func:`dexipy.parse.read_dexi_from_string`; both are aliased in the module
:py:mod:`dexipy.dexi`.

For more information, please refer to
:py:func:`dexipy.dexi.read_dexi` and :py:func:`dexipy.dexi.read_dexi_from_string` .
"""

from typing import Any, List, Dict, Sequence, Optional
import xml.etree.ElementTree as ET
import dexipy.utils as utl
from dexipy.types import BoundAssoc, DexiOrder, DexiQuality, DexiValue
from dexipy.dexi import DexiModel, DexiAttribute
from dexipy.dexi import DexiScale, DexiContinuousScale, DexiDiscreteScale
from dexipy.dexi import DexiFunction, DexiTabularFunction, DexiDiscretizeFunction

def dexi_bool(x: str) -> bool:
    try:
        return x.upper() in ("TRUE", "T", "1")
    except AttributeError:
        return False

def dexi_vector(x: str) -> List[float]:
    flts = [float(s) for s in x.split(";")]
    return [int(flt) if flt.is_integer() else flt for flt in flts]

def dexi_value(x: Optional[str], add: int = 0) -> DexiValue:
    if x is None:
        return None
    else:
        x = x.lower()
        if x == "":
            return None
        elif x == "*":
            return "*"
        elif x.startswith("undef"):
            return None
        elif x.startswith("{") and x.endswith("}"):
            valset: Sequence[int] = [int(val) + add for val in dexi_vector(x[1:-1])]
            return set(valset)
        elif x.startswith("<") and x.endswith(">"):
            return dexi_vector(x[1:-1])
        else:
            lh = x.split(":")
            if len(lh) == 1:
                return int(lh[0]) + add
            else:
                l = int(lh[0]) + add
                h = int(lh[1]) + add
                return set(range(l, h + 1))

def dexi_option_value(x: Optional[str]) -> DexiValue:
    if x is None:
        return None
    else:
        x = x.lower()
        if x in ("", "*"):
            return "*"
        elif x.startswith("undef"):
            return None
        else:
            vals = utl.rule_values(x)
            return vals[0] if len(vals) == 1 else set(vals)

def parse_dexi_continuous_scale(scl_xml: ET.Element, order: DexiOrder = DexiOrder.ascending) -> DexiContinuousScale:
    low_point = float(scl_xml.findtext("LOW", default = "-inf"))
    high_point = float(scl_xml.findtext("HIGH", default = "+inf"))
    return DexiContinuousScale(order = order, lpoint = low_point, hpoint = high_point)

def parse_dexi_discrete_scale(scl_xml: List[ET.Element], order: DexiOrder = DexiOrder.ascending) -> DexiDiscreteScale:
    values: List[str] = []
    descrs: List[str] = []
    quals: List[DexiQuality] = []
    for val_xml in scl_xml:
        values.append(val_xml.findtext("NAME", default = ""))
        descrs.append(val_xml.findtext("DESCRIPTION", default = ""))
        qual = val_xml.findtext("GROUP", default = "NONE").upper()
        quality = DexiQuality.good if qual == "GOOD" else DexiQuality.bad if qual == "BAD" else DexiQuality.none
        quals.append(quality)
    return DexiDiscreteScale(order = order, values = values, descriptions = descrs, quality = quals)

def parse_dexi_scale(att_xml: ET.Element) -> Optional[DexiScale]:
    scl_xml = att_xml.find("SCALE")
    if scl_xml is None:
        return None
    order_text: str = scl_xml.findtext("ORDER", default = "ASC").upper()
    order: DexiOrder = DexiOrder.descending if order_text == "DESC" else DexiOrder.none if order_text == "NONE" else DexiOrder.ascending
    xml = scl_xml.find("CONTINUOUS")
    if xml is not None:
        return parse_dexi_continuous_scale(xml, order)
    xmls = scl_xml.findall("SCALEVALUE")
    if xmls is not None and len(xmls) > 0:
        return parse_dexi_discrete_scale(xmls, order)
    return None

def parse_dexi_tabular_funct_def(att_xml: ET.Element) -> Optional[Dict[str, Any]]:
    fnc_xml = att_xml.find("FUNCTION")
    if fnc_xml is not None:
        low = fnc_xml.findtext("LOW", default = "")
        high = fnc_xml.findtext("HIGH", default = low)
        return {"low": low, "high": high}
    tab_xml = att_xml.find("TABLE")
    if tab_xml is not None:
        values: List[DexiValue] = []
        rul_xml = tab_xml.findall("RULE")
        for val_xml in rul_xml:
            val = dexi_value(val_xml.text)
            values.append(val)
        return {"values": values}
    return None

def parse_dexi_discretize_funct_def(att_xml: ET.Element) -> Optional[Dict[str, Any]]:
    fnc_xml = att_xml.find("DISCRETIZE")
    if fnc_xml is None or len(fnc_xml) == 0:
        return None
    values_xml = fnc_xml.findall("VALUE")
    values: List[DexiValue] = []
    for val_xml in values_xml:
        val = dexi_value(val_xml.text)
        values.append(val)
    bounds_xml = fnc_xml.findall("BOUND")
    bounds: List[float] = []
    assoc: List[BoundAssoc] = []
    for bnd_xml in bounds_xml:
        bnd = float(str(bnd_xml.text))
        attrib = bnd_xml.attrib
        asc_text = attrib["Associate"] if "Associate" in attrib else "down"
        asc = BoundAssoc.up if asc_text.upper() == "UP" else BoundAssoc.down
        bounds.append(bnd)
        assoc.append(asc)
    values = utl.pad_list(values, len(bounds) + 1, None)
    return {"values": values, "bounds": bounds, "assoc": assoc}

def parse_dexi_alternative_names(att_xml: ET.Element) -> List[str]:
    names: List[str] = []
    for el in att_xml:
        if el.tag == "OPTION":
            txt = el.text
            names.append("" if txt is None else txt)
        elif el.tag == "ALTERNATIVE":
            txt = el.findtext("NAME", default = "")
            names.append("" if txt is None else txt)
    return names

def parse_dexi_alternative_values(att_xml: ET.Element) -> List[DexiValue]:
    values = []
    for el in att_xml:
        if el.tag == "OPTION":
            values.append(dexi_option_value(el.text))
        elif el.tag == "ALTERNATIVE":
            values.append(dexi_value(el.text))
    return values

def parse_dexi_attributes(xml: ET.Element, def_name: str = "", alt_values: bool = True) -> DexiAttribute:
    name = xml.findtext("NAME", default = def_name)
    description = xml.findtext("DESCRIPTION", default = "")


    scale: Optional[DexiScale] = parse_dexi_scale(xml)
    tab_funct_def = parse_dexi_tabular_funct_def(xml)
    disc_funct_def = parse_dexi_discretize_funct_def(xml)

    inp_xmls = xml.findall("ATTRIBUTE")
    inp_list: List[DexiAttribute] =  []
    for inp_xml in inp_xmls:
        inp = parse_dexi_attributes(inp_xml)
        inp_list.append(inp)
    att = DexiAttribute(name, description, inputs = inp_list, scale = scale)

    # parents
    for inp in att.inputs:
        inp.parent = att

    # function
    funct: Optional[DexiFunction] = None
    if scale is not None:
        if tab_funct_def is not None and isinstance(scale, DexiDiscreteScale):
            if "values" in tab_funct_def:
                funct = DexiTabularFunction(att, values = tab_funct_def["values"])
            else:
                funct = DexiTabularFunction(att, low = tab_funct_def["low"], high = tab_funct_def["high"])
        elif disc_funct_def is not None and isinstance(scale, DexiDiscreteScale):
            funct = DexiDiscretizeFunction(att, values = disc_funct_def["values"], bounds = disc_funct_def["bounds"], assoc = disc_funct_def["assoc"])
    att.funct = funct

    # _alternatives
    if alt_values:
        att._alternatives = parse_dexi_alternative_values(xml)
    else:
        att._alternatives = parse_dexi_alternative_names(xml)

    return att

def parse_dexi(xml: ET.Element) -> DexiModel:
    name = xml.findtext("NAME", default = "")
    if name == "":
        name = "DEXi Model"
    description = xml.findtext("DESCRIPTION", default = "")
    linking = dexi_bool(xml.findtext("./SETTINGS/LINKING", default = ""))
    root = parse_dexi_attributes(xml, def_name = "root", alt_values = False)
    return DexiModel(name, description, root, linking)

def read_dexi(filename: str) -> DexiModel:
    tree = ET.parse(filename)
    root = tree.getroot()
    if root.tag != "DEXi":
        raise ValueError(f'File "{filename}" does not contain a DEXi model')
    return parse_dexi(root)

def read_dexi_from_string(xml: str) -> DexiModel:
    root = ET.fromstring(xml)
    if root.tag != "DEXi":
        raise ValueError("XML argument does not contain a DEXi model")
    return parse_dexi(root)
