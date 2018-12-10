import pdfx
import os
import sys
from os import walk
import csv
import git

# [filter(lambda item: "docker" in item or "github" in item or "pdf" in item, link_list) for link_list in l]


def main():
    #path = "/mnt/c/Users/Fjona/Desktop/2018-2019/UROP/icse/2018/pdfs/ICSE2018-7hDWfdAOTaSxSTuYmZ7C9S/73vOGjBkf23NHodSgD3DR2/"
    path = "/mnt/c/Users/Fjona/Desktop/2018-2019/UROP/icse/2018/pdfs/ICSE2018-7hDWfdAOTaSxSTuYmZ7C9S/"
    #path = "/mnt/c/Users/Fjona/Desktop/2018-2019/UROP"
    #https://weakdh.org/imperfect-forward-secrecy.pdf"
#    papers = ["1OWvuIr0ODMO3SiUdEDKEV.pdf"]  
#    links = extractURLsFromPDFs(path, papers)
    list_of_pdfs = getRecursiveFilenames(path, '.pdf')
    #print(list_of_pdfs)
    pdf_links = extractURLsFromPDFs(list_of_pdfs)
    writeLinksCSV("paper_links.csv", pdf_links)
    
def extractURLsFromPDFs(papers):
    links_in_papers = {}
    i = 1
    for paper in papers:
        sys.stderr.write(str(i) + " extracted: " + paper + "\n")
        i+= 1
        try: 
            pdf = pdfx.PDFx(paper)
            set_of_urls = pdf.get_references()
            list_of_urls = []
            for e in set_of_urls:
                list_of_urls.append(e.ref)
            links_in_papers[paper] = list_of_urls
        except UnicodeDecodeError:
            sys.stderr.write("This file has a UnicodeDecodeError!")
    return links_in_papers
    
def writeLinksCSV(filename, pdfLinks):
#    download_dir = filename #where you want the file to be downloaded to 

    csv = open(filename, "w") 
    #"w" indicates that you're writing strings to the file
    #columnTitleRow = "name, email\n"
    #csv.write(filename)
    i=1
    for paper, links in pdfLinks.items():
        row = paper + "," + ",".join(links) + ",\n"
        try: 
            csv.write(row)
            sys.stderr.write(str(i) + " written: " + paper + "\n")
            i+= 1
        except:
            sys.stderr.write("This file has a UnicodeDecodeError!")
    csv.close()
    

# Sample call: getRecurisiveFilenames(path, ".pdf")
# Return: List of PDF files with complete path
def getRecursiveFilenames(path, suffix):
    pdf_files = []
    for (dirpath, dirnames, files) in walk(path):
        for name in files:
            if name.lower().endswith(suffix):
                pdf_files.append(os.path.join(dirpath, name))
    return pdf_files
    
def get_GitHub_links(links):
    """Gets the github links with username and repo"""
    general_links = [filter(lambda item: "docker" in item or "github" in item or "pdf" in item, link_list) for link_list in links]
    gh_links = [filter(lambda item: "http://github.com/" in item, link) for link in general_links]
    return gh_links

def get_paper_titles(links):
    
    
def attempt_build()

#    metadata = pdf.get_metadata()   
#    references_list = 
#    references_dict = pdf.get_references_as_dict()

def build_docker(links):
    for link in links:
        repo = git.Repo.clone_from(link,os.path.join(rw_dir,'repo'),branch="master")
        docker_paths = repo.get_paths('Dockerfile')
        for dockerfile in docker_paths:
            os.chdir(dockerfile)
            stdout,st


    
main()
