import os
# os.system("cd /Users/chengpeng123/Dropbox/Resume And Cover Letter")
source_dir = "/Users/chengpeng123/Documents/coverletterautomate"
target_dir =  "/Users/chengpeng123/Dropbox/Resume\ and\ Cover\ letter/OlderCover"

cover_letter = "rawLetter.tex"
cv = "cv_4.tex"
os.system("cd " + source_dir)

listofJobs = []

with open('shortlistdata') as f:
    content = f.readlines()
    count = 5
    temp = []

    for line in content:
    	line = line.strip()
    	line = line.replace('/', " or ")
    	
	    # Check if we are at a new row, get the next 4 data
        if ("00" in line and len(line) == 8):
		    count = 0
		
		# Grab data for the next field cells
        if (count < 3):
			count = count + 1
			if ("00" not in line):
				temp.append(line)
        elif temp:
			listofJobs.append(temp)
			temp = []

# Compiles the Resume first
os.system('pdflatex ' + cv)
for j in listofJobs:
	file_src = j[0].replace(" ","")+j[1].replace(" ","")
	file1pdf = j[0].replace(" ","")+j[1].replace(" ","")+'1.pdf'
	file1tex = j[0].replace(" ","")+j[1].replace(" ","")+'1.tex'
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
	# Combine
	os.system("pdfjam " + file1pdf + " " + "cv_4.pdf" + ' --outfile ' +  file_src + ".pdf")
	os.system("rm " + file_src + "1.*")
	os.system("rm " + file_src + "2.*")


