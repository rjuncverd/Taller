# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "rjuncverd"
__date__ = "$07-ene-2016 14:52:16$"

import os

from conexion import bd
from fpdf import FPDF

def imprimir(fac,mat,dni):
    pdf = FPDF()
    pdf.add_page()
    header(pdf,fac,mat,dni)
    pdf.output('prueba2.pdf','F')
    os.system('/usr/bin/evince prueba2.pdf')

def header(pdf,fac,mat,dni):
    pdf.set_font('Arial','B',12)
    pdf.cell(60,10,'TALLERAUTO',0,1,'C')
    pdf.set_font('Arial','',10)
    pdf.cell(60,10,'Calle Senra, 12 Marin (Pontevedra)',0,1,'L')
    pdf.cell(60,10,'36911 Tlfo: 986 882 211 - 656 565 918',0,1,'L')
    pdf.image('car.png',170,10,25,25,'png','')
    pdf.line(5,40,200,40)