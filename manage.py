from common import model
import argparse 
import os

parser = argparse.ArgumentParser(description='ui-autotest manage')

parser.add_argument('-p', dest='page_name',nargs = 1,help = 'create a page object') 
parser.add_argument('-t', dest='test_name',nargs = 1,help = 'create a test file')
parser.add_argument('-run', dest='testsuite',nargs = '*',help = 'run a testsuite')


args = parser.parse_args() 

path = os.path.dirname(__file__)

def creat_page(page_name):
    file_name = os.path.join(path+'/page',page_name+'.py')
    with open(file_name,'w',encoding='utf-8') as f :
        f.write(model.PAGE_MODEL%{"page_name":page_name.capitalize()})

def creat_test(test_name):
    file_name = os.path.join(path+'/test','test_%s.py'%test_name)
    with open(file_name,'w',encoding='utf-8') as f :
        f.write(model.TEST_MODEL%{"test_name":test_name.capitalize()})


def run(testsuites):
    pass


if args.page_name:
    creat_page(args.page_name[0])

if args.test_name:
    creat_test(args.test_name[0])

if args.testsuite:
    run(args.testsuite)