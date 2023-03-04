# import selenium and other modules
import os
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import urllib.request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


def testing(arg_session,arg_startvideo,arg_endvideo):
    s=Service("/home/uslsz344/Desktop/chromedriver")
    driver=webdriver.Chrome(service=s)

    # 1190626/video/199998
    session=arg_session
    startvideo=arg_startvideo
    endvideo=arg_endvideo

    currentnumber=startvideo

    # for login
    try:
        driver.get("https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/video/"+str(currentnumber))
        
        driver.find_element(By.XPATH,'//*[@id="user_email"]').send_keys(email)
        driver.find_element(By.XPATH,'//*[@id="user_password"]').send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="new_user"]/div[5]/button').click()    
        print('Login Successful...!!')

    except Exception as e:
        print(e.__class__)
        print('Login Failed')

    #function for downloading pdf
    def download_file(download_url, filename):
        response = urllib.request.urlopen(download_url) 
        with open(filename+".pdf",'wb') as f:
            f.write(response.read())  


    #for cloning

    while currentnumber<=endvideo:
        if currentnumber>endvideo:
            break
        try:
            driver.get("https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/video/"
            +str(currentnumber))

            if(driver.current_url=="https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/video/"
            +str(currentnumber)):    

                print("cloning video page")  
                #for making directory according to name
                directory=driver.current_url[35:]
                parent_dir="/home/uslsz344/Desktop/practise/task_assigned"
                directorypath=parent_dir+directory
                empty_list=directorypath.split("/")
                lastelement=empty_list.pop()
                directorypath=("/".join(map(str,empty_list)))+"/"
                if(os.path.isdir(directorypath)==False):  #checking if directory already exists
                    os.makedirs(directorypath)
                    
                filename=directorypath+lastelement+".html"
                pageSource = driver.page_source

                #replacing old urls to new one
                for i in range(startvideo,endvideo+1):
                    pageSource=pageSource.replace("/"+str(i)+"&quot","/"+str(i)+".html"+"&quot")

                pageSource=pageSource.replace("&quot;/course_sessions/"+str(session)+"/","&quot;/paths/17/course_sessions/"+str(session)+"/")

                with open(filename,'w') as f:
                    f.write(pageSource)
            else:
                raise Exception("not video url")


        except:
            try:
                driver.get("https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/labs/"+str(currentnumber))
                # time.sleep(1)
                if(driver.current_url=="https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/labs/"+str(currentnumber)):
                    print("cloning lab page")
                    directory=driver.current_url[35:]
                    parent_dir="/home/uslsz344/Desktop/practise/task_assigned"
                    directorypath=parent_dir+directory
                    empty_list=directorypath.split("/")
                    lastelement=empty_list.pop()
                    directorypath=("/".join(map(str,empty_list)))+"/"
                    if(os.path.isdir(directorypath)==False):
                        os.makedirs(directorypath)
                    
                    filename=directorypath+lastelement+".html"
                    pageSource = driver.page_source
                    #replacing old urls to new one
                    for i in range(startvideo,endvideo+1):
                        pageSource=pageSource.replace("/"+str(i)+"&quot","/"+str(i)+".html"+"&quot")
                    # &quot;/course_sessions/1174581/
                    pageSource=pageSource.replace("&quot;/course_sessions/"+str(session)+"/","&quot;/paths/17/course_sessions/"+str(session)+"/")
                    with open(filename,'w') as f:
                        f.write(pageSource)
                else:
                    raise Exception("not labs page")        
            except:
                try:
                    driver.get("https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/quizzes/"+str(currentnumber))
                    # time.sleep(1)
                    if(driver.current_url=="https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/quizzes/"+str(currentnumber)):
                        print("cloning quiz page")
                        directory=driver.current_url[35:]
                        parent_dir="/home/uslsz344/Desktop/practise/task_assigned"
                        directorypath=parent_dir+directory
                        empty_list=directorypath.split("/")
                        lastelement=empty_list.pop()
                        directorypath=("/".join(map(str,empty_list)))+"/"
                        if(os.path.isdir(directorypath)==False):
                            os.makedirs(directorypath)
                        filename=directorypath+lastelement+".html"
                        pageSource = driver.page_source
                        #replacing old urls to new one
                        for i in range(startvideo,endvideo+1):
                            pageSource=pageSource.replace("/"+str(i)+"&quot","/"+str(i)+".html"+"&quot")
                        pageSource=pageSource.replace("&quot;/course_sessions/"+str(session)+"/","&quot;/paths/17/course_sessions/"+str(session)+"/")


                        with open(filename,'w') as f:
                            f.write(pageSource)
                    else:
                        raise Exception("not quiz page")
                except:
                    try:
                        driver.get("https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/documents/"+str(currentnumber))

                        if driver.current_url=="https://www.cloudskillsboost.google/course_sessions/"+str(session)+"/documents/"+str(currentnumber):
                            print("cloning document page")
                            directory=driver.current_url[35:]
                            #making document directory
                            parent_dir="/home/uslsz344/Desktop/practise/task_assigned"
                            directorypath=parent_dir+directory
                            empty_list=directorypath.split("/")
                            lastelement=empty_list.pop()
                            directorypath=("/".join(map(str,empty_list)))+"/"
                            if(os.path.isdir(directorypath)==False):

                                os.makedirs(directorypath)    
                            filename=directorypath+lastelement+".html"   
                            # print(filename)
                
                            #replacing old urls to new one
                            pageSource = driver.page_source

                            for i in range(startvideo,endvideo+1):
                                pageSource=pageSource.replace("/"+str(i)+"&quot","/"+str(i)+".html"+"&quot")
                            pageSource=pageSource.replace("&quot;/course_sessions/"+str(session)+"/","&quot;/paths/17/course_sessions/"+str(session)+"/")
                                
                            #changing pagesource pdf url
                            soup=BeautifulSoup(pageSource,'html.parser')
                            iframe=soup.find_all('iframe')[1]
                            pageSource=pageSource.replace(str(iframe),'<iframe class="document-iframe" src='+"\paths\\17\course_sessions\\"+str(session)+"\pdfs\\"+lastelement+".pdf"+'></iframe>')

                            with open(filename,'w') as f:
        
                                f.write(pageSource)
        
                            #making pdf directory

                            directorypath=parent_dir+"/course_sessions/"+str(session)+"/pdfs/"

                            if(os.path.isdir(directorypath)==False):
        
                                os.makedirs(directorypath)

                            filename=directorypath+lastelement
                            #downloading pdf from website

                            iframe_tag=driver.execute_script('return document.querySelector("#main-wrapper > ql-drawer-container > ql-drawer-content > iframe")')
                            pdf_link=iframe_tag.get_attribute("src")
                            download_file(pdf_link,filename)
                            
                        else:
                            raise Exception("not document page")

                    except Exception as e:
                        print(e.__class__)
                        print(e.__str__)
                        print(e)
                        print("some unexpected error occurred")    

            
        currentnumber+=1


    