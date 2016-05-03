import os
import subprocess
import zipfile
import fnmatch
import shutil
os.chdir("./feedback/")

frmt = open("../format.mks", "r")
frmttex = open("format.tex", "w")



frmttex.write("\\section{General formatting}\n")
frmttex.write("\\begin{enumerate}\n")

if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}The pages are of size 8 1/2 x 11 inches, with 1-inch margins.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}The pages are of size 8 1/2 x 11 inches, with 1-inch margins.\n")
	
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}The text is in 12-point Times New Roman font, with 1.5 spacing.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}The text is in 12-point Times New Roman font, with 1.5 spacing.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Sections and subsection headings are numbered (e.g., 2.1, 2.2, ...), and are in decreasing-sized fonts (e.g., 16-pt section headings, 14-pt subsection headings, 12-pt sub subsection headings).\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Sections and subsection headings are numbered (e.g., 2.1, 2.2, ...), and are in decreasing-sized fonts (e.g., 16-pt section headings, 14-pt subsection headings, 12-pt sub subsection headings).\n")	
	
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Appendices restart the section numbering, using capital letters as section labels and Arabic numerals as subsection labels (i.e., A.1, A.2, ); appendix headers are in decreasing-sized fonts.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Appendices restart the section numbering, using capital letters as section labels and Arabic numerals as subsection labels (i.e., A.1, A.2, ); appendix headers are in decreasing-sized fonts.\n")
	
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}If a section is divided into subsections, it has at least two subsections. Similarly for subsections divided into sub subsections, and so on.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}If a section is divided into subsections, it has at least two subsections. Similarly for subsections divided into sub subsections, and so on.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}The front matter, Conclusions, Recommendations, Glossary, Acknowledgements, and References sections are not divided into subsections.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}The front matter, Conclusions, Recommendations, Glossary, Acknowledgements, and References sections are not divided into subsections.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Each figure has a number and a caption below the figure.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Each figure has a number and a caption below the figure.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Each table has a number and a title above the table.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Each table has a number and a title above the table.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Figure and table numbering restarts at the beginning of each appendix, using a combination of the appendix label and figure/table number within the appendix (e.g., A-1, A-2).\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Figure and table numbering restarts at the beginning of each appendix, using a combination of the appendix label and figure/table number within the appendix (e.g., A-1, A-2).\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Each figure and table is cited (referred to by number) in the report text, either on the same page as the figure/table or on the preceding page.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Each figure and table is cited (referred to by number) in the report text, either on the same page as the figure/table or on the preceding page.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Figures and tables are legible.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Figures and tables are legible.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Paragraphs are indented, with one space between paragraphs.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Paragraphs are indented, with one space between paragraphs.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Front-matter pages are numbered using lower-case roman numerals, with the title page as page 1. Page numbers do not appear on either the title page or the letter of submittal.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Front-matter pages are numbered using lower-case roman numerals, with the title page as page 1. Page numbers do not appear on either the title page or the letter of submittal.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Page numbering restarts at the main body of the report: pages in the main body and back matter, including appendices, are numbered using Arabic numerals, with the first page of the Introduction as page one. Alternatively, page numbering could restart with each appendix where page numbers are prefixed with appendix letters (e.g. A-1, A-2)\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Page numbering restarts at the main body of the report: pages in the main body and back matter, including appendices, are numbered using Arabic numerals, with the first page of the Introduction as page one. Alternatively, page numbering could restart with each appendix where page numbers are prefixed with appendix letters (e.g. A-1, A-2)\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Page numbers are centred at the bottom of the page.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Page numbers are centred at the bottom of the page.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}Paper sections are correctly ordered.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}Paper sections are correctly ordered.\n")
		
if frmt.readline().strip()== "t":
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\checkmark$}\\hspace{2 mm}The length of the report's main body is 10-20 pages.\n")
else:
	frmttex.write("\\item \\makebox[0pt][l]{$\\square$}\\raisebox{.15ex}{$\\times$}\\hspace{2 mm}The length of the report's main body is 10-20 pages.\n")
frmttex.write("\\end{enumerate}\n")
	
frmt.close()
frmttex.close()
	
eval =  open("../eval.mks",'r')

for line in eval:
	toks = line.split(':')
	if toks[0].strip() == "grm" :
		efile = open("./evaluations/grammar.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "chs" :
		efile = open("./evaluations/cohesion.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "str" :
		efile = open("./evaluations/structure.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "bkg" :
		efile = open("./evaluations/background.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "pst" :
		efile = open("./evaluations/clarity.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "sig" :
		efile = open("./evaluations/significance.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "eda" :
		efile = open("./evaluations/description.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "cns" :
		efile = open("./evaluations/constraints.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "crt" :
		efile = open("./evaluations/criterias.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "alt" :
		efile = open("./evaluations/alternatives_offer.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "exp" :
		efile = open("./evaluations/alternatives_exploration.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "cnx" :
		efile = open("./evaluations/alternatives_context.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "asm" :
		efile = open("./evaluations/assumptions.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "frn" :
		efile = open("./evaluations/fairness.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "crb" :
		efile = open("./evaluations/evaluation_criteria.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "snd" :
		efile = open("./evaluations/soundness.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "hns" :
		efile = open("./evaluations/observation.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "trf" :
		efile = open("./evaluations/tradeoff.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "fin" :
		efile = open("./evaluations/final.txt",'w')
		efile.write(str(toks[1]))
		efile.close()
	elif toks[0].strip() == "cmt" :
		efile = open("./evaluations/comments.txt",'w')
		efile.write(str(toks[1]))
		efile.close()

eval.close()

subprocess.call(["pdflatex", "feedback.tex"])

for file in os.listdir("./../"):
    if fnmatch.fnmatch(file, "(commented)*"):
        filename = file

shutil.copy("../" + filename, ".")

arch = zipfile.ZipFile("../evaluation.zip", 'w')
arch.write("feedback.pdf")
arch.write(filename)
arch.close();

os.remove(filename)
os.remove("feedback.pdf")
os.remove("feedback.log")
os.remove("feedback.aux")
