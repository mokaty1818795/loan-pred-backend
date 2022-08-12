import pickle
import numpy as np
from flask import Flask, render_template, json, jsonify, request
import flask
import os
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


