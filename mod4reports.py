#!/usr/bin/env python3

"""Script for Creating Report."""
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  
  info1 = Paragraph(a1, styles["BodyText"])
  info2 = Paragraph(a2, styles["BodyText"])
  info3 = Paragraph(a3, styles["BodyText"])
  info4 = Paragraph(a4, styles["BodyText"])
  info5 = Paragraph(a5, styles["BodyText"])
  info6 = Paragraph(a6, styles["BodyText"])
  info7 = Paragraph(a7, styles["BodyText"])
  info8 = Paragraph(a8, styles["BodyText"])
  info9 = Paragraph(a9, styles["BodyText"])
  info10 = Paragraph(a10, styles["BodyText"])
  info11 = Paragraph(a11, styles["BodyText"])
  info12 = Paragraph(a12, styles["BodyText"])
  info13 = Paragraph(a13, styles["BodyText"])
  info14 = Paragraph(a14, styles["BodyText"])
  info15 = Paragraph(a15, styles["BodyText"])
  info16 = Paragraph(a16, styles["BodyText"])
  info17 = Paragraph(a17, styles["BodyText"])
  info18 = Paragraph(a18, styles["BodyText"])
  info19 = Paragraph(a19, styles["BodyText"])
  info20 = Paragraph(a20, styles["BodyText"])
  
  empty_line = Spacer(1,20)
  
  report.build([report_title, empty_line,info1,info2, empty_line,info3,info4, empty_line,info5,info6, empty_line,info7,info8, empty_line,info9,info10,empty_line,info11,info12, empty_line,info13,info14, empty_line,info15,info16, empty_line,info17,info18, empty_line,info19,info20])
