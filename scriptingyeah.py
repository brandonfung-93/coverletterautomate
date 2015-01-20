import os
# os.system("cd /Users/chengpeng123/Dropbox/Resume And Cover Letter")
source_dir = "/Users/chengpeng123/Documents/coverletterautomate"
target_dir =  "/Users/chengpeng123/Dropbox/Resume\ and\ Cover\ letter/OlderCover"

cover_letter = "rawLetter.tex"
cv = "cv_4.tex"
os.system("cd " + source_dir)

listofJobs = [["3D Visualization Engineering-Tools Developer","2G Robotics Inc"],
["NET Engineering","2pointb"],
["Data Scientist","AdRoll"],
["Python Engineering","AdRoll"],
["Front-end Engineering","AdRoll"],
["Software Engineering","Air Computing Inc"],
["Video Processing","Apple Inc"],
["Engineering Intern","Atomic Labs"], 
["Software Engineering Intern","BandPage"],
["Software Developer","Bazaarvoice"],
["Test Automation Developer","Bazaarvoice"],
["Software Engineering - Intern","Careerify Corporation"],
["Software Engineering","Connected Lab Inc"],
["Biotech Software Developer","Cyclica Inc"],
["Software Engineering","Databricks"],
["Software Intern","Datera Inc"],
["Backend or Frontend Web Developer","ElationEMR"],
["Software Engineering","Esper Technologies Inc."],
["Production Engineering Co-op","Facebook"],
["Data Scientist","Facebook"],
["Software Engineering","FiveStars Loyalty Inc"],
["Software Engineering Intern","Google"],
["Software Engineering Student","Instart Logic Inc"],
["Software Engineering","Kanjoya Inc"],
["Software Engineering","LinkedIn Corporation"],
["Software Developer","Netskope"],
["Research Intern","New York University"],
["Pebble Software QA Tester","Pebble Technology"],
["Software Engineering","Quizlet LLC"],
["Frontend Engineering","Reflektion"],
["Backend Engineering","Reflektion"],
["Front End Software Engineering","Rubrik"],
["Back End Software Engineering","Rubrik"],
["Reporting and Analytics Engineering","Scopely"],
["Software Developer","Shoebox"],
["Imaging Research","Sunnybrook Health Sciences Centre"],
["Backend Engineering","Symphony Commerce"],
["Software Engineering","The Orange Chef Co"],
["Research and Technical Analyst","University of Toronto, Department of Medical Imaging"],
["Software Engineering","UpNest"],
["Software Engineering Intern","Wealthfront Inc"],
["Data Engineering","WhiteHat Security"],
["Software Engineering","Yahoo Inc."],
["Software Engineering","Zanbato Group LLC"],
["Software Engineering","ZenPayroll Inc"],
["Data Scientist and Developer","dataESP"],
["Analytics and Big Data Developer","nModal Solutions Inc."]]

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
				if ("COMPANY" in line):
					fout.write(line.replace("COMPANY", j[1]))
				elif ("POSITION" in line):
					fout.write(line.replace("POSITION", j[0]))
				else:
					fout.write(line)
	os.system('pdflatex ' + file1tex)
	# Second Resume
	with open(file2tex, "wt") as fout:
		with open(cv, "rt") as fin:
			for line in fin:
				fout.write(line)
	os.system('pdflatex ' + file2tex)

	# Combine
	os.system("pdfjam " + file1pdf + " " + file2pdf + ' --outfile ' +  file_src + ".pdf")
	os.system("rm " + file_src + "1.*")
	os.system("rm " + file_src + "2.*")

