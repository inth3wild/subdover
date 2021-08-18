# from src.fingerprints import * 
import requests
import argparse
import sys
import os
import subprocess
import dns.resolver
import threading
import numpy as np
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


f1 = [
        "Acquia", #Service
        "Vulnerable", #Status
        ["acquia-test.co"], #CNAME
        "The site you are looking for could not be found."  #Fingerprint
	]

f2 = [
        "ActiveCampaign",
        "Vulnerable",
        ["activehosted.com"],  
        "alt=\"LIGHTTPD - fly light.\""
	]
    
f3 = [
        "AfterShip",
        "Vulnerable",
        ["aftership.com"],  
        "Oops.</h2><p class=\"text-muted text-tight\">The page you're looking for doesn't exist."
	]
    
f4 = [
        "AgileCRM",
        "Vulnerable",
        ["cname.agilecrm.com", "agilecrm.com"],
        "Sorry, this page is no longer available."
	]    

f5 = [
        "Aha",
        "Vulnerable",
        ["ideas.aha.io"],  
        "There is no portal here ... sending you back to Aha!"
	]
    
f6 = [
        "Airee.ru",
        "Vulnerable",
        ["cdn.airee.com", "airee.com"],
        "Ошибка 402. Сервис Айри.рф не оплачен"
        # "Сайт xyz.xyz.ru. , на который вы заходите, не оплатил сервис Айри.рф. Доступ к сайту временно невозможен."
	] 

f7 = [
        "Anima",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        # "Missing Website"
        "If this is your website and you've just created it, try refreshing in a minute"
        # A record : 35.164.217.247
	]     

f8 = [
        "Apigee",
        "Vulnerable",
        ["-portal.apigee.net"],  
        ""  #NoResponse_HenceNoFingerprint
	]   

f9 = [
        "AWS/S3",
        "Vulnerable",
        ["amazonaws"],  
        "The specified bucket does not exist"
	]      
    
f10 = [
        "Bigcartel",
        "Vulnerable",
        ["bigcartel.com"],
        "<h1>Oops! We could&#8217;t find that page.</h1>"
    ]

f11 = [
        "Bitbucket",
        "Vulnerable",
        ["bitbucket.io"],
        "Repository not found" 
	] 

f12 = [
        "Brightcove",
        "Vulnerable",
        ["bcvp0rtal.com", "brightcovegallery.com", "gallery.video"],
        "<p class=\"bc-gallery-error-code\">Error Code: 404</p>",
	]      

f13 = [
        "Canny.io",
        "Vulnerable",
        ["cname.canny.io"],
        # "Company Not Found"
        "There is no such company. Did you enter the right URL?"
	] 

f14 = [
        "CampaignMonitor",
        "Vulnerable",
        ["createsend.com", "name.createsend.com"], 
        "Double check the URL or <a href=\"mailto:help@createsend.com"
	]
    
f15 = [
        "Cargo",
        "Vulnerable",
        ["cargocollective.com"], 
        "If you're moving your domain away from Cargo you must make this configuration through your registrar's DNS control panel."
	]

f16 = [
        "CargoCollective",
        "Vulnerable",
        ["subdomain.cargocollective.com"], 
        "404 Not Found"
	]

f17 = [
        "Cloudfront",
        "Edge case ",
        ["cloudfront.net"],
        "Bad Request: ERROR: The request could not be satisfied"
	]    

f18 = [
        "Desk",
        "Not vulnerable",
        ["desk.com"],
        "Please try again or try Desk.com free for 14 days."
	]
    
f19 = [
        "ElasticBeanstalk_AWS_service",
        "Vulnerable",
        ["elasticbeanstalk.com"],
        "" #No Fingerprint Available
    ]     

f20 = [
        "Fastly",
        "Edge case ",
        ["fastly.net"],
        "Fastly error: unknown domain."
	]

f21 = [
        "Feedpress",
        "Vulnerable",
        ["redirect.feedpress.me"],
        "The feed has not been found."
	]
    
f22 = [
        "Freshdesk",
        "Vulnerable",  #NotSure
        ["freshdesk.com"],
        "May be this is still fresh!"
	] 

f23 = [
        "Frontify",
        "Vulnerable",
        ["frontify.com"],
        "404 - Page Not Found</h1>"
	]     

f24 = [
        "GetResponse",
        "Vulnerable",
        [".gr8.com"],
        "With GetResponse Landing Pages, lead generation has never been easier"
	]

f25 = [
        "Ghost",
        "Vulnerable",
        ["ghost.io"],
        "The thing you were looking for is no longer here, or never was"
	]

f26 = [
        "Github",
        "Vulnerable",
        ["github.io"],
        "There isn't a GitHub Pages site here."
	]

f27 = [
        "Help Juice",
        "Vulnerable",
        ["helpjuice.com"],
        "We could not find what you're looking for"
	]

f28 = [
        "Helprace",
        "Vulnerable",
        ["helprace.com"],
        # "Alias not configured!"
        "Admin of this Helprace account needs to set up domain alias"
    ] 

f29 = [
        "Help Scout",
        "Vulnerable",
        ["helpscoutdocs.com"],
        "No settings were found for this company"
	]

f30 = [
        "Heroku",
        "Edge case ",
        ["herokuapp"],
        "No such app"
	]
    
f31 = [
        "Hubspot",
        "Vulnerable",   ##Not Sure
        ["sites.hubspot.net"],
        "Domain Not found"
	]      

f32 = [
        "Instapage",
        "Vulnerable",
        ["pageserve.co", "secure.pageserve.co", "https://instapage.com/"],
        "You've Discovered A Missing Link. Our Apologies!"
	]
    
f33 = [
        "InterCom",
        "Vulnerable",
        ["custom.intercom.help"],
        "<h1 class=\"headline\"Uh oh. That page doesn't exist.</h1>"
	]    

f34 = [
        "JetBrains",
        "Vulnerable",
        ["myjetbrains.com"],
        "is not a registered InCloud YouTrack"
	]

f35 = [
        "Kajabi",
        "Vulnerable",
        ["endpoint.mykajabi.com"],
        "<h1>The page you were looking for doesn't exist.</h1>"
	]

f36 = [
        "Landingi",
        "Vulnerable",
        ["cname.landingi.com"],
        # A Record : 174.129.25.170
        # "<h1>It looks like you’re lost...</h1>"
        "<p>The page you are looking for is not found.</p>"
    ] 

f37 = [
        "LaunchRock",
        "Vulnerable",
        ["launchrock.com"],
        "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us."
	]   
""" 
LaunchRock
----------
A Record :
        54.243.190.28
        54.243.190.39
        54.243.190.47
        54.243.190.54
"""

f38 = [
        "LeadPages.com",
        "Vulnerable",
        ["custom-proxy.leadpages.net", "leadpages.net"],
        "Double check that you have the right web address and give it another go!</p>"
	] 
    
f39 = [
        "Mashery",
        "Edge Case ",
        ["mashery.com"],
        "Unrecognized domain"
	]    

f40 = [
        "MicrosoftAzure",
        "Vulnerable",  
        ["cloudapp.net", "cloudapp.azure.com", "azurewebsites.net", "blob.core.windows.net", "cloudapp.azure.com", "azure-api.net", "azurehdinsight.net", "azureedge.net", "azurecontainer.io", "database.windows.net", "azuredatalakestore.net", "search.windows.net", "azurecr.io", "redis.cache.windows.net", "azurehdinsight.net", "servicebus.windows.net", "visualstudio.com"],
        "404 Web Site not found"     
	]
    
f41 = [
        "Ngrok",
        "Vulnerable",
        ["ngrok.io"],
        "ngrok.io not found"
	]           

f42 = [
        "Pantheon",
        "Vulnerable",
        ["pantheonsite.io"],
        "The gods are wise, but do not know of the site which you seek."
	]
    
f43 = [
        "Pingdom",
        "Vulnerable",
        ["stats.pingdom.com"],
        "This public report page has not been activated by the user"
	]

f44 = [
        "Proposify",
        "Vulnerable",
        ["proposify.biz"],
        "If you need immediate assistance, please contact <a href=\"mailto:support@proposify.biz"
	]

f45 = [
        "Readme.io",
        "Vulnerable",
        ["readme.io"],
        "Project doesnt exist... yet!"
	] 

f46 = [
        "ReadTheDocs.org",
        "Vulnerable",
        ["readthedocs.io"],
        "is unknown to Read the Docs"
	]    

f47 = [
        "Shopify",
        "Edge Case ",
        ["myshopify.com"],
        "Sorry, this shop is currently unavailable"
	]

f48 = [
        "SimpleBooklet",
        "Vulnerable",
        ["simplebooklet.com"],
        "We can't find this <a href=\"https://simplebooklet.com"
	]
    
f49 = [
        "Smartling",
        "Vulnerable",
        ["smartling.com"],
        "Domain is not configured"
	]

f50 = [
        "Smugmug",
        "Vulnerable",
        ["domains.smugmug.com"],
        ""  #NotAvailable
	]      

f51 = [
        "StatusPage",
        "Vulnerable",
        ["statuspage.io"],
        "You are being <a href=\"https://www.statuspage.io\">redirected"
	]

f52 = [
        "Strikingly",
        "Vulnerable",
        [".s.strikinglydns.com"],
        "But if you're looking to build your own website,"
	]

f53 = [
        "Surge.sh",
        "Vulnerable",
        ["surge.sh"],
        "project not found"
	]    

f54 = [
        "Surveygizmo",
        "Vulnerable",
        ["privatedomain.sgizmo.com", "privatedomain.surveygizmo.eu", "privatedomain.sgizmoca.com"],
        "data-html-name"
	] 

f55 = [
        "Tave",
        "Vulnerable",
        ["clientaccess.tave.com"],
        "<h1>Error 404: Page Not Found</h1>"
	]
    
f56 = [
        "Teamwork",
        "Vulnerable",
        ["teamwork.com"],
        "Oops - We didn't find your site."
	]

f57 = [
        "Thinkific",
        "Vulnerable",
        ["thinkific.com"],
        "You may have mistyped the address or the page may have moved."
	]

f58 = [
        "Tictail",
        "Vulnerable",
        ["domains.tictail.com"],
        "to target URL: <a href=\"https://tictail.com", "Start selling on Tictail."
	]

f59 = [
        "Tilda",
        "Edge Case ",
        ["tilda.ws"],
        "Please renew your subscription"
	]

f60 = [
        "Tumblr",
        "Vulnerable",
        ["domains.tumblr.com"],
        "Whatever you were looking for doesn't currently exist at this address"
	]    

f61 = [
        "Uberflip",
        "Vulnerable",
        ["read.uberflip.com", "uberflip.com"],
        "Non-hub domain, The URL you've accessed does not provide a hub. Please check the URL and try again."
	] 

f62 = [
        "Unbounce",
        "Edge Case ",
        ["unbouncepages.com"],
        "The requested URL was not found on this server"
	]

f63 = [
        "UptimeRobot",
        "Vulnerable",
        ["stats.uptimerobot.com"],
        "This public status page <b>does not seem to exist</b>."
	]

f64 = [
        "UserVoice",
        "Vulnerable",
        ["uservoice.com"],
        "This UserVoice subdomain is currently available"
	]

f65 = [
        "Vend",
        "Vulnerable",
        ["vendecommerce.com"],
        "Looks like you've traveled too far into cyberspace"
	]
    
f66 = [
        "WebFlow",
        "Vulnerable",
        ["proxy.webflow.com", "proxy-ssl.webflow.com"],
        "<p class=\"description\">The page you are looking for doesn't exist or has been moved.</p>"
	]

f67 = [
        "WishPond",
        "Vulnerable",
        ["wishpond.com"],
        "https://www.wishpond.com/404?campaign=true"
	]
    
f68 = [
        "Worksites.net",
        "Vulnerable",
        ["NOT_AVAILABLE"],
        "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist."
        ## A Record IP ==> 69.164.223.206
	]       
    

f69 = [
        "Wordpress",
        "Vulnerable",
        ["wordpress.com"],
        "Do you want to register "
	]    

f70 = [
        "Zendesk",
        "Not Vulnerable",
        ["zendesk.com"],
        "Help Center Closed"
	]
 
f71 =  [
        "Appery.io",
        "Vulnerable",
        [""],  #404 Cname
        "<p>This page will be updated automatically when your app is published.</p>",
        # Pointing to 107.20.248.61
    ]
 
f72 = [
        "Vercel.com",
        "Vulnerable",
        [""], #404 Cname
        "The deployment could not be found on Vercel."
    ]
   
f73 = [
        "Datocms.com",
        "Vulnerable",
        [""], #404 Cname
        "<!doctype html><html><head><meta charset=\"utf-8\"><title>Loading...</title>",
    ]    
"""
Kinsta
Edge Case
[""]
""
# Here is the response from kinsta for orphan CNAME.
# 404 Not Found
# Content-Length=[33604]
# Server = kinsta-nginx

"""    

fingerprints_list = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70,f71,f72,f73]



if os.name in ('ce', 'nt', 'dos'):
    AttackerSystem = "Windows"
elif 'posix' in os.name:
    AttackerSystem = "Linux"


def get_arguments():
    parser = argparse.ArgumentParser(description=f'{RED}SubDover v1.4')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
    parser.add_argument("-t", "--thread", dest="thread", help="Number of Threads to Used. Default=10", default=10)
    parser.add_argument("-o", "--output", dest="output", help="Save Result in TXT file")
    parser.add_argument("--update", dest="check_and_update", help="Check & Update Subdover", action='store_true')
    parser.add_argument("-s", "--fingerprints", dest="show_fingerprint", help="Show Available Fingerprints & Exit", action='store_true')   
    
    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("-d", "--domain", dest="domain", help="Target Wildcard Domain [For AutoSubdomainEnumeration], ex:- google.com")
    required_arguments.add_argument("-l", "--list", dest="subdomain_list", help="Target Subdomain List, ex:- google_subdomain.txt")
    return parser.parse_args()


def check_and_update():            
    try:
        ongoing_version = requests.get("https://raw.githubusercontent.com/PushpenderIndia/subdover/master/version.txt")
    except Exception:
        print(f"{WHITE}[{RED}ERR{WHITE}] No Internet Connection")
        sys.exit()
        
    ongoing_version = ongoing_version.text.strip()
    
    with open("/opt/subdover/"+"version.txt", "r") as f:
        currentVersion = f.read()
        if currentVersion != ongoing_version:
            print(f"{YELLOW}[*] Installing Subdover v{ongoing_version}")
            subprocess.run("git pull origin master", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"{GREEN}[+] Updated to latest version: v{ongoing_version}..")
            
            with open("/opt/subdover/"+"version.txt", "w") as f:
                f.write(ongoing_version)
            sys.exit()
        else:
            print(f"{GREEN}[+] Subdover is already Up-to-Date: v{ongoing_version}..")
            sys.exit()

def readTargetFromFile(filepath):
    """
    Returns: List of Subdomain
    """
    subdomain_list = []
    
    with open(filepath, "r") as f:
        for subdomain in f.readlines():
            if subdomain != "": 
                subdomain_list.append(subdomain.strip())  

    return subdomain_list
    
def split_list(list_name, total_part_num):
    """
    Takes Python List and Split it into desired no. of sublist
    """
    final_list = []
    split = np.array_split(list_name, total_part_num)
    for array in split:
        final_list.append(list(array))		
    return final_list    
    
def enumSubdomain(domain):
    if AttackerSystem == "Windows":
        print("[*] Finding Subdomain Using findomain ...") 
        subprocess.run(f"\"{findomain_path}\" --output --target {domain}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        print(f"[*] Adding Appropriate Web Protocal to Subdomains using httpx ...")
        subprocess.run(f"type {domain}.txt | \"{httpx_path}\" -threads 100 -o {domain}-httpx.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        print("[*] Finding Subdomain Using findomain ...") 
        subprocess.run(f"findomain --output --target {domain}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        print(f"[*] Adding Appropriate Web Protocal to Subdomains using httpx ...")
        subprocess.run(f"cat {domain}.txt | httpx -threads 100 -o {domain}-httpx.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
     
    print(f"[*] Saving Subdomains in TXT file ...")
    os.remove(f"{domain}.txt")
    os.rename(f"{domain}-httpx.txt", f"{domain}.txt")
    print(f"[+] Done")  
    
def enumCNAME(domain):
    cname = ""

    domain_without_protocal = domain.replace("http://", "")
    domain_without_protocal = domain_without_protocal.replace("https://", "")
    
    try:
        result = dns.resolver.resolve(domain_without_protocal, 'CNAME')
        for cnameeval in result:
            cname = cnameeval.target.to_text()
    except Exception:
        pass
        
    return cname
    
def confirm_vulnerable(domain, service_cname_list):
    confirm = False

    enumeratedCNAME = enumCNAME(domain)
    if enumeratedCNAME == "":  # Because URL such as https://githublol.github.io (which doesn't exist) will have CNAME==""
        confirm = "NotSure"
    
    else:
        for service_cname in service_cname_list:
            if service_cname in enumeratedCNAME:
                confirm = True
                
    return confirm, enumeratedCNAME          

def testTarget(url):
    not_success = True

    try:
        response = requests.get(url, headers=headers, timeout=(3,5), verify=False)
        targetResponse = response.text
    except Exception:
        targetResponse = "ConnectionError_SubDover"
        
    for fingerprint in fingerprints_list:
        error = fingerprint[3]
        
        if targetResponse == "ConnectionError_SubDover":
            print(f"{RED}[!] ConnectionError : {WHITE}{url}")
            not_success = False
            break
        
        elif error.lower() in targetResponse.lower():
            if error.lower() == "":
                pass
                
            else:
                service_cname_list = fingerprint[2]
                confirm, enumeratedCNAME = confirm_vulnerable(url, service_cname_list)
                if confirm == True:            
                    print(f"{GREEN}[+] {fingerprint[1]} ===> : {WHITE}[{RED}Service{WHITE}: {fingerprint[0]}] {WHITE}[{RED}CNAME{WHITE}: {enumeratedCNAME}] : {GREEN}{url}{WHITE}")
                    not_success = False
                    if arguments.output:
                        with open(arguments.output, "a") as f:
                            f.write(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: {enumeratedCNAME}] : {url}\n")
                    break
                    
                elif confirm == "NotSure" and fingerprint[0] not in ["CargoCollective", "Akamai"]: 
                    #CargoCollective & Akamai fingerprints can leads to False +ve 
                    #If script is unable to confirm detection using CNAME, then we will ignore that detection
                    
                    print(f"{GREEN}[+] {fingerprint[1]} ===> : {WHITE}[{RED}Service{WHITE}: {fingerprint[0]}] {WHITE}[{RED}CNAME{WHITE}: 404, UnableToVerify-CouldBeFalsePositive] : {GREEN}{url}{WHITE}")
                    not_success = False
                    if arguments.output:
                        with open(arguments.output, "a") as f:
                            f.write(f"[+] {fingerprint[1]} ===> : [Service: {fingerprint[0]}] [CNAME: 404, UnableToVerify-CouldBeFalsePositive] : {url}\n")
                    break                    
         
    if not_success:
        print(f"{WHITE}[-] Not Vulnerable  : {GREEN}{url}{WHITE}")        

def start_scanning(subdomain_list):
    for subdomain in subdomain_list:
        testTarget(subdomain)     

if __name__ == '__main__':
    print("Starting Subover")
    arguments = get_arguments() 
    
    KillThread = False

    try:
        if arguments.check_and_update:
            if AttackerSystem == "Windows":
                try:
                    git_path = subprocess.check_output("where git", shell=True)
                    check_and_update()
                except Exception:
                    print(f"{WHITE}[{RED}ERR{WHITE}] GIT is NOT Installed on Your System! You can't use AutoUpdater .") 
                    sys.exit()
            else:
                try:
                    git_path = subprocess.check_output("which git", shell=True)
                    check_and_update()
                except Exception:
                    print(f"{WHITE}[{RED}ERR{WHITE}] GIT is NOT Installed on Your System! You can't use AutoUpdater .")              
                    sys.exit()
        if arguments.show_fingerprint:
            print("+------------------------+")
            print("| Available Fingerprints |")
            print("+------------------------+")
            number = 1
            for fingerprint in fingerprints_list:
                print(f"{number}. {fingerprint[0]}")
                number += 1            
            
        if arguments.subdomain_list:
            print("==================================================================")
            print(f"[*] Adding Appropriate Web Protocol to Subdomains using httpx ...")
            if "\\" in arguments.subdomain_list:
                filename = arguments.subdomain_list.split("\\")[-1]
                
            elif "\\\\" in arguments.subdomain_list:
                filename = arguments.subdomain_list.split("\\\\")[-1]
                
            elif "/" in arguments.subdomain_list:
                filename = arguments.subdomain_list.split("/")[-1] 
                
            else:
                filename = arguments.subdomain_list
                
            outputFileName = arguments.subdomain_list.replace(filename, filename.replace(" ", "_")) + "_httpx.txt"    
            
            if AttackerSystem == "Windows":
                subprocess.run(f"type \"{arguments.subdomain_list}\" | \"{httpx_path}\" -threads 100 -o \"" + outputFileName + "\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            else:
                subprocess.run(f"cat \"{arguments.subdomain_list}\" >> \"" + outputFileName + "\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

            
            print(f"[+] Done !")
            print("==================================================================\n")        
            subdomain_list = readTargetFromFile(outputFileName)
            
            final_subdomain_list = split_list(subdomain_list, int(arguments.thread))

            print("==================================================")
            print(f"[>>] Total Threads                : {arguments.thread}")
            print(f"[>>] Total Targets Loaded         : {len(subdomain_list)}")
            print(f"[>>] Total Fingerprints Available : {len(fingerprints_list)}")
            print("[>>] Scanning Targets for Subdomain Takeover")
            print("==================================================")
                        
            for thread_num in range(int(arguments.thread)):   
                t1 = threading.Thread(target=start_scanning, args=(final_subdomain_list[thread_num],)) 
                t1.start()
                
        elif arguments.domain:
            print("========================================================")
            print(f"[>>] Enumerating Subdomains for : {arguments.domain}")
            print("========================================================")
            enumSubdomain(arguments.domain)          
            
            subdomain_list = readTargetFromFile(f"{arguments.domain}.txt")
            
            final_subdomain_list = split_list(subdomain_list, int(arguments.thread))
            print("\n=============================================")
            print(f"[>>] Total Threads                : {arguments.thread}")
            print(f"[>>] Total Targets Loaded         : {len(subdomain_list)}")
            print(f"[>>] Total Fingerprints Available : {len(fingerprints_list)}")
            print("[>>] Scanning Targets for Subdomain Takeover")
            print("=============================================")
            
            for thread_num in range(int(arguments.thread)):
                t1 = threading.Thread(target=start_scanning, args=(final_subdomain_list[thread_num],)) 
                t1.start()           
        
        else:
            url = input("\n[?] Enter URL: ")
            testTarget(url)
    except KeyboardInterrupt:
        sys.exit()