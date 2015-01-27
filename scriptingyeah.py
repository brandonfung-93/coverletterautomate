# -*- coding: utf-8 -*-
import os
# os.system("cd /Users/chengpeng123/Dropbox/Resume And Cover Letter")
source_dir = "/Users/chengpeng123/Documents/coverletterautomate"
target_dir =  "/Users/chengpeng123/Dropbox/Resume\ and\ Cover\ letter/OlderCover"

cover_letter = "rawLetter.tex"
cv = "cv_4.tex"
os.system("cd " + source_dir)

listofJobs = [["NodeJs Web Engineering","blueRover"],
["Software Engineering","Skimble Inc"],
["Android Engineering","Luxe"],
["Software Engineering","Luxe"],
["DevOps Specialist","Enflick Inc"],
["Server Developer","Enflick Inc"]]

os.system('pdflatex ' + cv)
for j in listofJobs:
	file_src = j[0].replace(" ","")+j[1].replace(" ","")
	file1pdf = j[0].replace(" ","")+j[1].replace(" ","")+'1.pdf'
	file2pdf = j[0].replace(" ","")+j[1].replace(" ","")+'2.pdf'
	file1tex = j[0].replace(" ","")+j[1].replace(" ","")+'1.tex'
	file2tex = j[0].replace(" ","")+j[1].replace(" ","")+'2.tex'
	# First cover letter
	with open(file1tex, "wt") as fout:
		with open(cover_letter, "rt") as fin:
			for line in fin:
				if ("COMPANY" in line or "POSITION" in line):
					line = line.replace("COMPANY", j[1])
					line = line.replace("POSITION", j[0])
					fout.write(line)
				else:
					fout.write(line)
	os.system('pdflatex ' + file1tex)

	# Combine
	os.system("pdfjam " + file1pdf + " " + "cv_4.pdf" + ' --outfile ' +  file_src + ".pdf")
	os.system("rm " + file_src + "1.*")
	os.system("rm " + file_src + "2.*")

