import os
os.system("cd /Users/BrandonFung")
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
os.system("cd /Users/BrandonFung/Desktop/thingsof")
for j in listofJobs:
	with open(j[0].replace(" ","")+j[1].replace(" ","")+'.tex', "wt") as fout:
		with open("rawLetter.tex", "rt") as fin:
			for line in fin:
				if ("COMPANY" in line):
					fout.write(line.replace("COMPANY", j[1]))
				elif ("POSITION" in line):
					fout.write(line.replace("POSITION", j[0]))
				else:
					fout.write(line)
	os.system("cd /Users/BrandonFung/Desktop/thingsof/ohyeah")
	os.system('pdflatex /Users/BrandonFung/Desktop/thingsof/'+j[0].replace(" ","")+j[1].replace(" ","")+'.tex')
