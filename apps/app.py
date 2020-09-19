from flask import Flask, render_template
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

