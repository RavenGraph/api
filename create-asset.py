#!/usr/bin/env python3

# simple example of asset creation using ravencoinlib

import ravencoin
from neo4j import GraphDatabase
from py2neo import Graph
from ravencoin.assets import CMainAsset, InvalidAssetName
from ravencoin.rpc import RavenProxy
from ravencoin.core import b2lx

graph = Graph()
tx = graph.begin()

ravencoin.SelectParams("testnet")

rvn = RavenProxy() # will use local daemon, must be running with the rpc server enabled

asset_name = "BTC" # your asset name
qty = 21000000 # quantity to issue

try:
    asset_name = CMainAsset("VALID_ASSET")
except InvalidAssetName:
    print("Invalid asset name")

for name in ["BTC"]:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
alice, bob, carol = [result.one for result in tx.commit()]

# wallet must be unlocked or this will fail

r = rvn.issue(asset_name, qty)

print("Created asset {}, txid: {}".format(asset_name,b2lx(r)))