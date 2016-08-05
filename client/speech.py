#!/usr/bin/python

import sys
import pyttsx


if __name__ == '__main__':
	engine = pyttsx.init()
	str=44.5
	para="Lesson plans, activities and ideas for kindergarten classrooms, including math problem-solving ... I believe so strongly in teaching math through problem solving."
	engine.setProperty("rate",100)
	engine.say(str)
	engine.say(para)
	engine.runAndWait()

