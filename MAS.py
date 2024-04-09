import subprocess

class SystemInfo:
    
        def __init__(self):
            self.powershell_exe = "powershell.exe"
            self.total_score = 0
            self.perfect_score = 0

        def run_powershell_command(self, command):
            powershell_cmd = [self.powershell_exe, "-Command", command]
            result = subprocess.run(powershell_cmd, capture_output=True, text=True)
            return result.stdout.strip()

        def get_os_info(self):
            command = r"$os = Get-WmiObject -Class Win32_OperatingSystem; $version = $os.Version; $installDate = $os.ConvertToDateTime($os.InstallDate); $license = (Get-WmiObject -Query 'SELECT * FROM SoftwareLicensingService').OA3xOriginalProductKey; $version, $installDate, $license"
            os_info = self.run_powershell_command(command)
            return os_info


        def calculate_os_version_score(self):
            os_version = self.get_os_info()
            if os_version.startswith("10"):      
                score = 5
            elif os_version.startswith("8"):
                score = 3
            elif os_version.startswith("7") or os_version.startswith("XP"):
                score = 1
            else:
                score = 0

            self.total_score += score
            self.perfect_score += 5
            return score

        def check_last_update(self):
            command = r"$InstallDate = (Get-WmiObject -Class Win32_OperatingSystem).ConvertToDateTime((Get-WmiObject -Class Win32_OperatingSystem).InstallDate); $LastUpdate = Get-Hotfix | Where-Object { $_.InstalledOn } | Select-Object -First 1; if ($InstallDate -ne $LastUpdate.InstalledOn) { 'UPDATED' } else { 'NEVER UPDATED' }"
            last_update = self.run_powershell_command(command)
            return last_update
       
        def score_last_update(self):
            update = self.check_last_update()
            if update == "UPDATED":
                score = 3
            else:
                score = 0

            self.total_score += score
            self.perfect_score += 3
            return score

        def check_antivirus_info(self):
            command = r"$antivirus = Get-WmiObject -Namespace 'root\SecurityCenter2' -Class AntivirusProduct; if ($antivirus) { $name = $antivirus.DisplayName; $installedDate = $antivirus.InstallDate; $expirationDate = $antivirus.ExpireDate; $licensed = $antivirus.IsLicenseValid; $name, $installedDate, $expirationDate, $licensed } else { 'No antivirus software found on the system.' }"
            antivirus_info = self.run_powershell_command(command)
            return antivirus_info
       
        def score_antivirus(self):
            av_present = self.check_antivirus_info()
            if av_present.startswith("NO antivirus"):
                score = 0
            else:
                score =  5

            self.total_score += score
            self.perfect_score += 5
            return score

        def count_usb_devices(self):
            command = r"(Get-PnpDevice -Class USB -Status OK).Count"
            usb_count = self.run_powershell_command(command)
            usb_count = int(usb_count)
           
            return usb_count

        def calculate_usb_devices_score(self):
            usb_count = self.count_usb_devices()
            if int(usb_count) >= 6:
                score = 0
            elif int(usb_count) >= 3:
                score = 2
            else:
                score = 3

            self.total_score += score
            self.perfect_score += 3
            return score


        def count_user_accounts(self):
            command = r"$adminUsers = Get-LocalUser | Where-Object { $_.Enabled -eq $true -and $_.PrincipalSource -eq 'Local' -and $_.IsMemberOf -contains 'Administrators' }; $normalUsers = Get-LocalUser | Where-Object { $_.Enabled -eq $true -and $_.PrincipalSource -eq 'Local' -and $_.IsMemberOf -notcontains 'Administrators' }; $adminUserCount = $adminUsers.Count; $normalUserCount = $normalUsers.Count; $adminUserCount, $normalUserCount"
            user_counts = self.run_powershell_command(command)
            return user_counts
       
        def count_users(self):
            command = r"$users = Get-WmiObject -Class Win32_UserAccount | Where-Object { $_.LocalAccount -eq $True }; $users.Count"
            users_count = self.run_powershell_command(command)
            users_count = int(users_count)

            if users_count == 1:
                score = 5
            elif users_count > 1:
                score = 1
            else:
                return "ERROR"

            self.total_score += score
            self.perfect_score += 5
            return score



        def detect_file_modification(self):
            command = r"$fileModificationEvents = Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4663}; $fileModificationEventsCount = $fileModificationEvents.Count; $fileModificationEventsCount"
            file_modification_events_count = self.run_powershell_command(command)
            file_modification_events_count = int(file_modification_events_count)
            return file_modification_events_count

        def calculate_file_modification_score(self):
            file_modification_events_count = self.detect_file_modification()
            if file_modification_events_count > 0:
                score = 0
            else:
                score = 2

            self.total_score += score
            self.perfect_score += 2
            return score

        def count_lnk_files(self):
            command = r"(Get-ChildItem -Path C:\Users -Filter *.lnk -Recurse -File).Count"
            lnk_files_count = self.run_powershell_command(command)
            lnk_files_count = int(lnk_files_count)
            #print("NUMBER OF LNK FILES:")
            #print(lnk_files_count)
           
            if lnk_files_count > 20:
                score = 0
            elif lnk_files_count >= 10:
                score = 1
            elif lnk_files_count >= 5:
                score = 3
            elif lnk_files_count >= 0:
                score = 4
            else:
                return "NO FILE FOUND"
            self.total_score += score
            self.perfect_score += 4
            lnk_files_count = str(lnk_files_count)
            score = str(score)
            return "NUMBER OF LNK FILES: "+ lnk_files_count  + " SCORE FOR LNK FILES: "+score



        def count_pe_files(self):
            command = r"(Get-ChildItem -Path C:\Users -Filter *.exe -Recurse -File).Count"
            pe_files_count = self.run_powershell_command(command)
            pe_files_count = int(pe_files_count)

            if pe_files_count > 1000:
                score = 0
            elif pe_files_count >= 500:
                score = 1
            elif pe_files_count > 0:
                score = 3
            else:
                return "NO FILE FOUND"

            self.total_score += score
            self.perfect_score += 3
            pe_files_count = str(pe_files_count)
            score = str(score)
            return "NUMBER OF PE FILES: "+ pe_files_count  + " SCORE FOR PE FILES: "+score



        def count_dll_files(self):
            command = r"(Get-ChildItem -Path C:\Users -Filter *.dll -Recurse -File).Count"
            dll_files_count = self.run_powershell_command(command)
            dll_files_count = int(dll_files_count)

            if dll_files_count > 500:
                score = 1
            elif dll_files_count > 0:
                score = 2
            else:
                return "NO FILE FOUND"

            self.total_score += score
            self.perfect_score += 2
            dll_files_count = str(dll_files_count)
            score = str(score)
            return "NUMBER OF DLL FILES: "+ dll_files_count  + " SCORE FOR DLL FILES: "+score


        def count_hidden_files(self):
            command = r"Get-ChildItem -Path '*' -Recurse -File -Attributes Hidden"
            hidden_files_count = self.run_powershell_command(command)
            return hidden_files_count

        def count_access_privilege_attempts(self):
            command = r"$accessPrivilegeAttempts = Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625}; $accessPrivilegeAttemptsCount = $accessPrivilegeAttempts.Count; $accessPrivilegeAttemptsCount"
            access_privilege_attempts_count = self.run_powershell_command(command)
            access_privilege_attempts_count = int(access_privilege_attempts_count)
            return access_privilege_attempts_count

        def calculate_access_privilege_attempts_score(self):
            access_privilege_attempts_count = self.count_access_privilege_attempts()
            if access_privilege_attempts_count >= 1:
                score = 0
            elif access_privilege_attempts_count == 0:
                score = 3
            else:
                return "ERROR"

            self.total_score += score
            self.perfect_score += 3
            return score


        def trace_root_files(self):
            command = r"Get-WmiObject Win32_Process | Where-Object {$_.ExecutablePath -like 'C:\*'} | ForEach-Object { $_.Name + ' : ' + (Split-Path -Path $_.ExecutablePath -Parent) }"
            root_files = self.run_powershell_command(command)
            return root_files

        def count_failed_attempts_while_admin(self):
            command = r"$failedAttempts = Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625}; $failedAttemptsCount = $failedAttempts.Count; $failedAttemptsCount"
            failed_attempts_count = self.run_powershell_command(command)
            failed_attempts_count = int(failed_attempts_count)
            return failed_attempts_count

        def calculate_failed_attempts_score(self):
            failed_attempts_count = self.count_failed_attempts_while_admin()
            if failed_attempts_count > 4:
                score = 0
            elif failed_attempts_count > 1:
                score = 3
            elif failed_attempts_count == 0:
                score = 4
            else:
                return "ERROR"

            self.total_score += score
            self.perfect_score += 4
            return score

        def count_tcp_connections(self):
            command = r"$tcpConnections = Get-NetTCPConnection; $tcpConnectionCount = $tcpConnections.Count; $tcpConnectionCount, $tcpConnections"
            tcp_info = self.run_powershell_command(command)
            return tcp_info

        def startup_programs(self):
            command = r"Get-CimInstance -Query 'SELECT * FROM Win32_StartupCommand'"
            startup_programs = self.run_powershell_command(command)
            return startup_programs
       
        def count_startup_programs(self):
            command = r"(Get-CimInstance -Query 'SELECT * FROM Win32_StartupCommand').Count"
            startup_programs_count = self.run_powershell_command(command)
            startup_programs_count = int(startup_programs_count)
            if startup_programs_count > 15:
                score = 1
            elif startup_programs_count > 5:
                score = 3
            elif startup_programs_count > 2:
                score = 4
            elif startup_programs_count == 2:
                score = 5
            else:
                return "ERROR"

            self.total_score += score
            self.perfect_score += 5
            score = str(score)
            return "NUMBER OF STARTUP PROGRAMS: " + str(startup_programs_count) + "\nSCORE FOR STARTUP PROGRAMS: " + score

        def list_network_services_and_ports(self):
            command = r"$maliciousPorts = @(21, 22, 23, 25, 80, 110, 135, 137, 138, 139, 410, 445); $runningPorts = (Get-NetTCPConnection | Select-Object -ExpandProperty LocalPort); $maliciousRunningPorts = $runningPorts | Where-Object { $maliciousPorts -contains $_ }; if ($maliciousRunningPorts) { $maliciousRunningPorts | Group-Object | ForEach-Object { 'Potentially malicious port ' + $_.Name + ' is running. Count: ' + $_.Count } } else { 'No potentially malicious ports are running.' }"
            network_services_ports = self.run_powershell_command(command)
            return network_services_ports
       
        def count_malicious_ports(self):
            command = r"$maliciousPorts = @(21, 22, 23, 25, 80, 110, 135, 137, 138, 139, 410, 445); $runningPorts = (Get-NetTCPConnection | Select-Object -ExpandProperty LocalPort); $maliciousRunningPorts = $runningPorts | Where-Object { $maliciousPorts -contains $_ }; $maliciousRunningPortsCount = $maliciousRunningPorts.Count; $maliciousRunningPortsCount"
            malicious_ports_count = self.run_powershell_command(command)
            malicious_ports_count = int(malicious_ports_count)
            return malicious_ports_count

        def calculate_malicious_ports_score(self):
            malicious_ports_count = self.count_malicious_ports()
            if malicious_ports_count >= 4:
                score = 0
            elif malicious_ports_count >= 1:
                score = 2
            else:
                return "ERROR"
            self.total_score += score
            self.perfect_score += 2
            return score



# Usage example:
system_info = SystemInfo()

#DISPLAYS OS INFO
print("OS Info:")
print(system_info.get_os_info())
print("\n")

#DISPLAYS OS VERSION SCORE
score = system_info.calculate_os_version_score()
print("OS VERSION SCORE: ")
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DISPLAYS WHETEHR WINDOWS IS UPDATED OR NOT
print("Last Windows Update:")
print(system_info.check_last_update())
print("\n")

#DISPLAYS SCORE FOR WINDOWS UPDATE
print("Windows update score")
print(system_info.score_last_update())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DISPLAYS ANTIVIRUS INFO
print("Antivirus Info:")
print(system_info.check_antivirus_info())
print("\n")

#DISPLAYS SCORE FOR ANTIVIRUS
print("ANTIVIRUS SCORE: ")
print(system_info.score_antivirus())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#NUMBER OF USB DEVICES
print("Number of USB devices:")
print(system_info.count_usb_devices())
print("\n")

#SCORE FOR USB DEVICES
print("SCORE FOR USB DEVICES: ")
score = system_info.calculate_usb_devices_score()
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#NUMBER OF ADMIN AND NORMAL USERS
print("Number of Admin and Normal User Accounts:")
print(system_info.count_user_accounts())
print("respectively")
print("\n")

#SCORE FOR USERS
print("Score for users:")
score = system_info.count_users()
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#FILE MODIFICATION EVENTS
print("File Modification Events:")
file_modification_events_count = system_info.detect_file_modification()
print(file_modification_events_count)
print("\n")

#SCORE FOR FILE MODIFICATION EVENTS
print("Score for File Modification Events:")
score = system_info.calculate_file_modification_score()
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#LNK FILES
print(system_info.count_lnk_files())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#PE FILES
print(system_info.count_pe_files())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DLL FILES
print(system_info.count_dll_files())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DISPLAYS NUMBER OF HIDDEN FILES
print("Number of hidden files:")
print(system_info.count_hidden_files())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DISPLAYS ACCESS PRIVELAGE ATTEMPTS
print("Access Privilege Attempts:")
access_privilege_attempts_count = system_info.count_access_privilege_attempts()
print(access_privilege_attempts_count)
print("\n")

#SCORE FOR ACCESS PRIVELAGE ATTEMPTS
print("Score for Access Privilege Attempts:")
score = system_info.calculate_access_privilege_attempts_score()
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#FAILED ATTEMPTS WHILE ADMIN COUNT
print("Failed Attempts while Admin:")
failed_attempts_count = system_info.count_failed_attempts_while_admin()
print(failed_attempts_count)
print("\n")

#SCORE FOR FAILED ATTEMPT
print("Score for Failed Attempts:")
score = system_info.calculate_failed_attempts_score()
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DISPLAY STARTUP PROGRAMS
print("Startup Programs:")
print(system_info.startup_programs())
print("\n")

#COUNT STARTUP PROGRAMS
print(system_info.count_startup_programs())
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

#DISPLAY MALICIOUS PORTS
print("List of Network Services and Ports:")
print(system_info.list_network_services_and_ports())
print("\n")

#COUNT MALICIOUS PORTS
print("Number of Malicious Ports:")
malicious_ports_count = system_info.count_malicious_ports()
print(malicious_ports_count)
print("\n")

#SCORE FOR MALICIOUS PORTS
print("Score for Malicious Ports:")
score = system_info.calculate_malicious_ports_score()
print(score)
print("\n")

print("-------------------------------------------------------------------------------------------------------------------")

total_score = system_info.total_score
perfect_score = system_info.perfect_score
#total_score = str(total_score)
#perfect_score = str(perfect_score)

print("YOUR DEVICE SCORED(in percentage): " ,(total_score/perfect_score)*100)


print("-------------------------------------------------------------------------------------------------------------------")