import xml.etree.ElementTree as ET
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

file_name = args.filename
tree = ET.parse(file_name)
# tree.write(file_name + '.bak', encoding='utf-8', xml_declaration=True)
root = tree.getroot()

def traverse(node, depth=0):
    indent = depth * "  "
    for subnode in node:
        traverse(subnode, depth=depth+1)

def build_imgdir(node):
    imgdir = {}
    for subnode in node:
        imgdir[subnode.attrib["name"]] = subnode.attrib["value"]
    return imgdir

for life_node in root:
    if life_node.attrib["name"] != "life": continue
    # print("", node.tag, node.attrib)
    highest_idx = 0
    nodes_to_copy = []
    for imgdir_node in life_node:
        info = {}
        idx = int(imgdir_node.attrib["name"])
        if idx > highest_idx:
            highest_idx = idx

        do_copy = False

        for subnode in imgdir_node:
            if subnode.attrib["name"] == "limitedname" and subnode.attrib["value"] == "anniversary2022":
                subnode.attrib["value"] = "anniversary2"
                do_copy = True
            
        if do_copy:
            nodes_to_copy.append(copy.deepcopy(imgdir_node))

    idx = highest_idx + 1
    for node_to_copy in nodes_to_copy:
        new_node = ET.Element("imgdir", { "name": str(idx) })
        for subnode_to_copy in node_to_copy:
            if subnode_to_copy.attrib["name"] == "id" and subnode_to_copy.attrib["value"] == "9400017":
                subnode_to_copy.attrib["value"] = "9400015"
            elif subnode_to_copy.attrib["name"] == "limitedname" and subnode_to_copy.attrib["value"] == "anniversary2":
                subnode_to_copy.attrib["value"] = "anniversary1"
            new_node.append(subnode_to_copy)
        idx += 1
        life_node.append(new_node)

tree.write(file_name, encoding='utf-8', xml_declaration=True)
