from common import model
from common import HTMLTestReportCN
import argparse 
import os,time
import unittest

parser = argparse.ArgumentParser(description='ui-autotest manage')

parser.add_argument('-p', dest='page_name',nargs = 1,help = 'create a page object') 
parser.add_argument('-t', dest='test_name',nargs = 1,help = 'create a test file')
parser.add_argument('-run', dest='testsuite',nargs = '?',help = 'run testsuite (default to run all testsuite in .test)',const=1)



args = parser.parse_args() 

path = os.path.dirname(__file__)
filePath = path + '/report/'+time.strftime("%Y-%m-%d", time.localtime())


def creat_page(page_name):
    file_name = os.path.join(path+'/page',page_name+'.py')
    with open(file_name,'w',encoding='utf-8') as f :
        f.write(model.PAGE_MODEL%{"page_name":page_name.capitalize()})

def creat_test(test_name):
    file_name = os.path.join(path+'/test','test_%s.py'%test_name)
    with open(file_name,'w',encoding='utf-8') as f :
        f.write(model.TEST_MODEL%{"test_name":test_name.capitalize()})


def run_all():
    discover= unittest.defaultTestLoader.discover(path+'/test',pattern="test*.py",top_level_dir=None)
    print(discover)
    fp = open(filePath+'_alltest.html','wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        #description='',
        tester="fengf233"
        )
    runner.run(discover)

def run_one(testsuite):
    discover= unittest.defaultTestLoader.discover(path+'/test',pattern=testsuite+'*',top_level_dir=None)
    fp = open(filePath+'_%s.html'%testsuite,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        #description='',
        tester="fengf233"
        )
    runner.run(discover)

if args.page_name:
    creat_page(args.page_name[0])

if args.test_name:
    creat_test(args.test_name[0])


if args.testsuite:
    if args.testsuite == 1:
        run_all()
    else:
        run_one(args.testsuite)