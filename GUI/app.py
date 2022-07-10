from datetime import datetime
import paramiko
import json
from tkinter import *
import webbrowser
import os

PATH = "GUI/sessions/"
F_LIST = os.listdir(PATH)
sessionsNamesList = [
  "",
]
for f in F_LIST:
    if f.endswith(".json"):
        sessionsNamesList.append(f.removesuffix(".json"))

window = Tk()
window.title("Command Linux Server")

class ClientCommand():
  def __init__(self, ip = None, port0 = None, user = None, passwrd = None, output = None):
    self.ip = ip
    self.port0 = port0
    self.user = user
    self.passwrd = passwrd
    self.output = output

  def connect(self):
    self.connected = False
    if self.connected:
      buttonConnect.config(bg="green")
    else:
      buttonConnect.config(bg="red")
    self.client = paramiko.SSHClient()
    self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    self.client.connect(self.ip, self.port0, self.user, self.passwrd)
    self.connected = True
    if self.connected:
      buttonConnect.config(bg="green")
    else:
      buttonConnect.config(bg="red")

  def initVarAndConnect(self, ip, port0, user, passwrd):
    self.ip = ip
    self.port0 = port0
    self.user = user
    self.passwrd = passwrd
    self.connect()

  def saveSessions(self, ip, port0, user):
    self.ip = ip
    self.port0 = port0
    self.user = user
    sessionsDict = {
      "username": self.user,
      "ip": self.ip,
      "port": self.port0
    }
    with open('GUI/sessions/'+self.user+"_["+self.ip+"].json", 'w') as usernameIpAndPortSave:
      json.dump(sessionsDict, usernameIpAndPortSave)

  def loadSessions(self, nameOfSession):
    self.nameOfSession = nameOfSession
    openSession = open("GUI/sessions/"+self.nameOfSession+".json", 'r')
    sessionContent = openSession.read()
    loadJson = json.loads(sessionContent)

    #load and put in userContent
    userLoadContent = loadJson['username']
    userContent.set(userLoadContent)

    #load and put in ipContent
    ipLoadContent = loadJson['ip']
    ipContent.set(ipLoadContent)

    #load and put in portContent  
    portLoadContent = loadJson['port']
    portContent.set(portLoadContent)

  def customDeletePorts(self, deletePort):
    self.deletePort = deletePort
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw delete allow " + self.deletePort, get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)
  
  def customAddPorts(self, addPort):
    self.addPort = addPort
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw allow " + self.addPort, get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)
    
  def deletePort8080(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw delete allow 8080", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def deletePort25565(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw delete allow 25565", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def deletePort5657(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw delete allow 5657", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def allowPort8080(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw allow 8080", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def allowPort25565(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw allow 25565", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def allowPort5657(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw allow 5657", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole()
    
  def statusVerbosePort(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw status verbose", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def statusNumberedPort(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw status numbered", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def enableFireWall(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw --force enable", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def disableFireWall(self):
    stdin, self.stdout, self.stderr = self.client.exec_command("sudo ufw disable", get_pty=True)
    stdin.write(self.passwrd+"\n")
    stdin.flush()
    self.outputConsole(self.stdout)

  def outputConsole(self, output):
    date = "GUI/log/"+ str(datetime.now().date())+".txt"
    time = "\noutput["+str(datetime.now().time())+"] :"
    self.output = output
    if self.stderr.channel.recv_exit_status() != 0:
      self.output = self.stdout.readlines()
      labelConsole.config(text="\n".join(self.output))
      fichierError = open(date, "a")
      fichierError.write(time + "\n".join(self.output))
      fichierError.close()
    else:
      self.output = self.stdout.readlines()
      labelConsole.config(text="\n".join(self.output))
      fichieroutput = open(date, "a")
      fichieroutput.write(time + "\n".join(self.output))
      fichieroutput.close()

clientCommand = ClientCommand()

#delete port of the fireWall
buttonDeletePort8080 = Button(window, text="DeletePort8080", command=clientCommand.deletePort8080)
buttonDeletePort8080.grid(row=0, column=1, padx=20,pady=15)
buttonDeletePort25565 = Button(window, text="DeletePort25565", command=clientCommand.deletePort25565)
buttonDeletePort25565.grid(row=1, column=1, padx=20, pady=15)
buttonDeletePort5657 = Button(window, text="DeletePort5657", command=clientCommand.deletePort5657)
buttonDeletePort5657.grid(row=2, column=1, padx=20, pady=15)

#add port of the fireWall
buttonAllowPort8080 = Button(window, text="AllowPort8080", command=clientCommand.allowPort8080)
buttonAllowPort8080.grid(row=0, column=2, padx=20,pady=15)
buttonAllowPort25565 = Button(window, text="AllowPort25565", command=clientCommand.allowPort25565)
buttonAllowPort25565.grid(row=1, column=2, padx=20,pady=15)
buttonAllowPort5657 = Button(window, text="AllowPort5657", command=clientCommand.allowPort5657)
buttonAllowPort5657.grid(row=2, column=2, padx=20,pady=15)

#enable/disable fireWall
buttonDisableFireWall = Button(window, text="DisableFireWall", command=clientCommand.disableFireWall)
buttonDisableFireWall.grid(row=3, column=2, padx=20,pady=15)
buttonEnableFireWall = Button(window, text="EnableFireWall", command=clientCommand.enableFireWall)
buttonEnableFireWall.grid(row=3, column=1, padx=20,pady=15)

#look status of fireWall
buttonStatusVerbosePort = Button(window, text="StatusVerbosePort", command=clientCommand.statusVerbosePort)
buttonStatusVerbosePort.grid(row=4, column=1, padx=20, pady=15)
buttonStatusVerbosePort = Button(window, text="StatusNumberedPort", command=clientCommand.statusNumberedPort)
buttonStatusVerbosePort.grid(row=4, column=2, padx=20, pady=15)

#add/delete custom port
buttonDeleteCustomPort = Button(window, text="DeleteCustomPort", command= lambda: clientCommand.customDeletePorts(customPortContent.get()))
buttonDeleteCustomPort.grid(row=5, column=1, padx=20, pady=15)
buttonAllowCustomPort = Button(window, text="AllowCustomPort", command= lambda: clientCommand.customAddPorts(customPortContent.get()))
buttonAllowCustomPort.grid(row=5, column=2, padx=20, pady=15)

entryCustomPort = Entry(window, width=7, bg='#a2a2a6')
entryCustomPort.grid(row=5, column=3)

customPortContent = StringVar()
customPortContent.set("0")
entryCustomPort["textvariable"] = customPortContent

#add informations
entryIp = Entry(window, width=15, bg='#a2a2a6')
entryIp.grid(row=0, column=3, padx=20, pady=20)

ipContent = StringVar()
ipContent.set("ip...")
entryIp["textvariable"] = ipContent

entryPort = Entry(window, width=15, bg='#a2a2a6')
entryPort.grid(row=0, column=4, padx=20, pady=20)

portContent = StringVar()
portContent.set("port...")
entryPort["textvariable"] = portContent

entryUser = Entry(window, width=15, bg='#a2a2a6')
entryUser.grid(row=1, column=3, padx=20, pady=20)

userContent = StringVar()
userContent.set("username...")
entryUser["textvariable"] = userContent

entryPasswrd = Entry(window, width=15, bg='#a2a2a6')
entryPasswrd.grid(row=1, column=4, padx=20, pady=20)

passwrdContent = StringVar()
passwrdContent.set("passorwd...")
entryPasswrd["textvariable"] = passwrdContent

#Save informations and connect
buttonConnect = Button(window, text="Connect", command= lambda: clientCommand.initVarAndConnect(ipContent.get(), portContent.get(), userContent.get(), passwrdContent.get()))
buttonConnect.grid(row=2, column=3, padx=20, pady=15)

#load information
buttonLoadSession = Button(window, text="Load", command= lambda: clientCommand.loadSessions(sessionsNamesContent.get()))
buttonLoadSession.grid(row=2, column=4, padx=20, pady=15)

#save informations in files.json
buttonSaveSession = Button(window, text="Save", command= lambda: clientCommand.saveSessions(ipContent.get(), portContent.get(), userContent.get()))
buttonSaveSession.grid(row=3, column=4, padx=20, pady=15)

#TopLevel new window console
topLevelConsole = Toplevel(window)
topLevelConsole.title = "Python Console Linux"
topLevelConsole.geometry("800x800")
topLevelConsole.minsize(800,800)

frameMainConsole = Frame(topLevelConsole)
frameMainConsole.pack(fill=BOTH, expand=1)

canvasConsole = Canvas(frameMainConsole)
canvasConsole.pack(side=LEFT, fill=BOTH, expand=1)

#scroll bar
scrollbarConsole = Scrollbar(frameMainConsole, orient=VERTICAL, command=canvasConsole.yview)
scrollbarConsole.pack(side=RIGHT, fill=Y)

canvasConsole.configure(yscrollcommand=scrollbarConsole.set)
canvasConsole.bind('<Configure>', lambda e: canvasConsole.configure(scrollregion = canvasConsole.bbox("all")))

frameSecondConsole = Frame(canvasConsole)

canvasConsole.create_window((0,0), window=frameSecondConsole, anchor="nw")

#in the TopLevel
labelConsole = Message(frameSecondConsole, text="Console output")
labelConsole.pack(fill="both", side="right" and "top")

#Menu déroulant
sessionsNamesContent = StringVar(window)
sessionsNamesContent.set(sessionsNamesList[0])

optionMenuSessionsNames = OptionMenu(window, sessionsNamesContent, *sessionsNamesList)
optionMenuSessionsNames.config(width=20)
optionMenuSessionsNames.grid(row=3, column=3, padx=20, pady=15)

#Menu
mainMenu = Menu(window)

#First menu
menu1 = Menu(window, tearoff=0)
menu1.add_command(label="My Github", command=lambda: webbrowser.open("https://github.com/Titi0603"))
menu1.add_command(label="My Modpacks Minecraft", command=lambda: webbrowser.open("https://www.curseforge.com/members/titi0603/projects"))
menu1.add_command(label="Diavo", command=lambda: webbrowser.open("https://www.youtube.com/channel/UCgVFOK24H2TZOv2AqGZgJIw/featured"))
menu1.add_separator()
menu1.add_command(label="Quitter", command=quit)
mainMenu.add_cascade(label="Menu", menu=menu1)

window.config(menu=mainMenu)

window.geometry("640x340")
window.mainloop()