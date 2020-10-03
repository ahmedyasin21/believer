from django.shortcuts import render, get_object_or_404
# from .models import Quiz,Solution,Week
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Questions
# class WeekListView(ListView):
#     model = Week
#     context_object_name = 'week_list'  
#     template_name = "quiz/week_list.html"

#     def get_queryset(self):
#         return Week.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')



# class QuizListView(ListView):
#     model = Quiz
#     template_name = "quiz/quiz_list.html"
#     context_object_name = 'quiz_list'  

#     def get_queryset(self,*args, **kwargs):
#         week = get_object_or_404(Week, weekend=self.kwargs.get('weekend'))
#         return Quiz.objects.filter(week=week).order_by('-create_date')









ques1=10

# Create your views here.
@login_required
def home(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,
        'quiz/home.html',
        {'choices':choices})

@login_required
def questions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    global ques1
    ques1 = Questions.objects.filter(catagory__exact = choice).count()
    # print('this is',ques1)
    return render(request,
        'quiz/questions.html',
        {'ques':ques})
        
@login_required
def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # q_totle= Questions.objects.count()
        # print('this is all ',q_totle)

        # print(ans)
        print(score)
        if score > 0 :
            eff = (score/total)*100
        else :
            eff = 0
        # q = Questions.objects.filter(catagory__exact = choice).count()
        # print('this is',q)
        print('this is',ques1)
     

    return render(request,
        'quiz/result.html',
        {'score':score,
        'eff':eff,
        'total':total,
        'q_total': ques1})
      
         
# Create your views here.
