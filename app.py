import paramiko

def infoConnect():
  global ip, port0, user, passwrd
  ip = ""
  port0 = 
  user = ""
  passwrd = ""
  #return False
infoConnect()

def connect():
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(ip, port0, user, passwrd)
  def command():
    inputCommandPy = str(input("rentre une commande : "))
    if inputCommandPy == "-c --p 8080":
      stdin, stdout, stderr = client.exec_command("sudo ufw delete allow 8080", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        print(f"sortie : \n{stdout.readlines()}")
    elif inputCommandPy == "-c --p 25565":
      stdin, stdout, stderr = client.exec_command("sudo ufw delete allow 25565", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        print(f"sortie : \n{stdout.readlines()}")
    elif inputCommandPy == "-c --p 5657":
      stdin, stdout, stderr = client.exec_command("sudo ufw delete allow 5657", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
         print(f"sortie : \n{stdout.readlines()}")
    else:
      print("aucune commande exécuter pour suprimer des port")
    if inputCommandPy == "-o --p 8080":
      stdin, stdout, stderr = client.exec_command("sudo ufw allow 8080", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        print(f"sortie : \n{stdout.readlines()}")
    elif inputCommandPy == "-o --p 25565":
      stdin, stdout, stderr = client.exec_command("sudo ufw allow 25565", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        print(f"sortie : \n{stdout.readlines()}")
    elif inputCommandPy == "-o --p 5657":
      stdin, stdout, stderr = client.exec_command("sudo ufw allow 5657", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
         print(f"sortie : \n{stdout.readlines()}")
    else:
      print("aucune commande exécuter pour ajouter des port")
    if inputCommandPy == "-p --s":
      stdin, stdout, stderr = client.exec_command("sudo ufw status verbose", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        output = stdout.readlines()
        print("\n".join(output))
    else:
      print("aucune commande exécuter pour voir le status")
    if inputCommandPy == "-p --e":
      stdin, stdout, stderr = client.exec_command("sudo ufw --force enable", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        print(f"sortie : \n{stdout.readlines()}")
    elif inputCommandPy == "-p --d":
      stdin, stdout, stderr = client.exec_command("sudo ufw disable", get_pty=True)
      stdin.write(passwrd+"\n")
      stdin.flush()
      if stderr.channel.recv_exit_status() != 0:
        print(f"erreur : {stderr.readlines()}")
      else:
        print(f"sortie : \n{stdout.readlines()}")
    else:
      print("aucune commande exécuter pour activer/désactiver les ports")
  command()
  client.close()
connect()
while True:
    inputCommandPy = str(input("voulez-vous refaire une commande[y/n] : "))
    if inputCommandPy == "y":
      connect()
    else:
      print("Finish")
      break

