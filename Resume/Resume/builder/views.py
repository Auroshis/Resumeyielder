from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import View
 
#importing get_template from loader
#from django.template.loader import get_template
 
#import render_to_pdf from util.py 
#from .utils import render_to_pdf 

def index(request):
    return render(request, 'index.html')

def frontpage(request):
    return render(request,'frontpage.html')



def resumepage(request):
    full_name = request.GET.get('Full Name', 'default')
    DOB = request.GET.get('DOB', 'default')
    Contact = request.GET.get('Contact', 'default')
    Email = request.GET.get('Email', 'default')
    SocialMedia = request.GET.get('SocialMedia', 'default')
    objective = request.GET.get('objective', 'default')
    PI_head = request.GET.get('PI_head', 'default')
    projectname = request.GET.get('projectname', 'default')
    duration_start = request.GET.get('duration_start', 'default')
    duration_end = request.GET.get('duration_end', 'default')
    project_detail1 = request.GET.get('project_detail1', 'default')
    project_detail2 = request.GET.get('project_detail2', 'default')
    PI_head2 = request.GET.get('PI_head2', 'default')
    projectname2 = request.GET.get('projectname2', 'default')
    duration_start2 = request.GET.get('duration_start2', 'default')
    duration_end2 = request.GET.get('duration_end2', 'default')
    project_detail3 = request.GET.get('project_detail3', 'default')
    project_detail4 = request.GET.get('project_detail4', 'default')
    graduation = request.GET.get('graduation', 'default')
    cgpa = request.GET.get('cgpa', 'default')
    HigherSecondary = request.GET.get('HigherSecondary', 'default')
    percentage_marks = request.GET.get('percentage_marks', 'default')
    skill1 = request.GET.get('skill1', 'default')
    skill2 = request.GET.get('skill2', 'default')
    skill3 = request.GET.get('skill3', 'default')
    award1 = request.GET.get('Award1', 'default')
    prize_position = request.GET.get('prize_position', 'default')
    prize_year = request.GET.get('prize_year', 'default')
    option = request.GET.get('option', 'default')
    language1 = request.GET.get('language1','default')
    language2 = request.GET.get('language2','default')
    stream = request.GET.get('stream', 'default')
    branch = request.GET.get('branch', 'default')
    params = {
        'full_name': full_name,
        'DOB': DOB,
        'Contact': Contact,
        'Email': Email,
        'SocialMedia': SocialMedia,
        'objective': objective,
        'PI_head' : PI_head,
        'projectname': projectname,
        'duration_start':  duration_start,
        'duration_end':duration_end,
        'project_detail1':project_detail1,
        'project_detail2':project_detail2,
        'PI_head2': PI_head2,
        'projectname2': projectname2,
        'duration_start2': duration_start2,
        'duration_end2':duration_end2,
        'project_detail3':project_detail3,
        'project_detail4':project_detail4,
        'graduation':  graduation,
        'cgpa': cgpa,
        'HigherSecondary':HigherSecondary,
        'percentage_marks': percentage_marks,
        'skill1':skill1,
        'skill2':skill2,
        'skill3':skill3,
        'award1':award1,
        'prize_position': prize_position,
        'prize_year':prize_year,
        'language1': language1,
        'language2': language2,
        'stream': stream,
        'branch': branch,
    }
    if(option == '1'):
        return render(request, 'resumepage.html', params)
    elif(option == '2'):
        return render(request, 'resumepage1.html', params) 
    elif(option == '3'):
        return render(request, 'resumepage2.html', params)     
    else:
        return HttpResponse("wrong choice!Go back")
'''
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
                full_name = request.GET.get('Full Name', 'default')
                DOB = request.GET.get('DOB', 'default')
                Contact = request.GET.get('Contact', 'default')
                Email = request.GET.get('Email', 'default')
                SocialMedia = request.GET.get('SocialMedia', 'default')
                objective = request.GET.get('objective', 'default')
                PI_head = request.GET.get('PI_head', 'default')
                projectname = request.GET.get('projectname', 'default')
                duration_start = request.GET.get('duration_start', 'default')
                duration_end = request.GET.get('duration_end', 'default')
                project_detail1 = request.GET.get('project_detail1', 'default')
                project_detail2 = request.GET.get('project_detail2', 'default')
                PI_head2 = request.GET.get('PI_head2', 'default')
                projectname2 = request.GET.get('projectname2', 'default')
                duration_start2 = request.GET.get('duration_start2', 'default')
                duration_end2 = request.GET.get('duration_end2', 'default')
                project_detail3 = request.GET.get('project_detail3', 'default')
                project_detail4 = request.GET.get('project_detail4', 'default')
                graduation = request.GET.get('graduation', 'default')
                cgpa = request.GET.get('cgpa', 'default')
                HigherSecondary = request.GET.get('HigherSecondary', 'default')
                percentage_marks = request.GET.get('percentage_marks', 'default')
                skill1 = request.GET.get('skill1', 'default')
                skill2 = request.GET.get('skill2', 'default')
                skill3 = request.GET.get('skill3', 'default')
                award1 = request.GET.get('Award1', 'default')
                prize_position = request.GET.get('prize_position', 'default')
                prize_year = request.GET.get('prize_year', 'default')
                language1 = request.GET.get('language1','default')
                language2 = request.GET.get('language2','default')
                params = {
                    'full_name': 'auro',
                    'DOB': DOB,
                    'Contact': Contact,
                    'Email': Email,
                    'SocialMedia': SocialMedia,
                    'objective': objective,
                    'PI_head' : PI_head,
                    'projectname': projectname,
                    'duration_start':  duration_start,
                    'duration_end':duration_end,
                    'project_detail1':project_detail1,
                    'project_detail2':project_detail2,
                    'PI_head2': PI_head2,
                    'projectname2': projectname2,
                    'duration_start2': duration_start2,
                    'duration_end2':duration_end2,
                    'project_detail3':project_detail3,
                    'project_detail4':project_detail4,
                    'graduation':  graduation,
                    'cgpa': cgpa,
                    'HigherSecondary':HigherSecondary,
                    'percentage_marks': percentage_marks,
                    'skill1':skill1,
                    'skill2':skill2,
                    'skill3':skill3,
                    'award1':award1,
                    'prize_position': prize_position,
                    'prize_year':prize_year,
                    'language1': language1,
                    'language2': language2,
                }
                #getting the template
                pdf = render_to_pdf('resumepage1_1.html', params)
                
                #rendering the template
                return HttpResponse(pdf, content_type='application/pdf')
                '''