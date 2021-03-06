# -*- coding: utf-8 -*-
# @Author: Jay Patel
# @Email: jsp0053@auburn.edu
# @Date:   2020-06-27 07:50:42
# @Last Modified by:   Jay Patel
<<<<<<< HEAD
# @Last Modified time: 2020-06-27 11:02:39
=======
# @Last Modified time: 2020-06-27 09:23:26
>>>>>>> 6c4a83fe5b95b7fc265361e1bd88df8aa356e36e

import os
from magical_function import wordsToInteger
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/<words>')
def hello_name(words):
	response = "Requested query is: " + str(words) 
	return response + "<br> Words to Integer output: " + str(wordsToInteger(words)) + "! 🙂"

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8080)