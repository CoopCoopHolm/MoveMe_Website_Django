from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Moving, JunkRemoval, Consignment

# Create your views here.


def index(request):
    return render(request, 'home.html')


def consent(request):
    return render(request, 'consent.html')


def moving(request):
    return render(request, 'moving.html')


def junk_removal(request):
    return render(request, 'junk_removal.html')


def consignment(request):
    return render(request, 'consignment.html')


def quoteMoving(request):
    errors = Moving.objects.moving_validator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/moving')
        moving_quote = Moving.objects.create(
            name=request.POST['inputName'],
            email=request.POST['inputEmail'],
            phone=request.POST['inputPhone'],
            currentAddress=request.POST['inputCurrentAddress'],
            movingAddress=request.POST['inputMovingAddress'],
            moveDateTime=request.POST['inputMoveDate'],
            itemImages=request.FILES['inputImages'],
            message=request.POST['inputMessage'],
        )
        return redirect(f'/moving/review/{moving_quote.id}')
    return redirect('/moving')


def quoteJunk_removal(request):
    errors = JunkRemoval.objects.junk_removal_validator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/junk_removal')
        junk_removal_quote = JunkRemoval.objects.create(
            name=request.POST['inputName'],
            email=request.POST['inputEmail'],
            phone=request.POST['inputPhone'],
            itemAddress=request.POST['inputItemAddress'],
            moveDateTime=request.POST['inputMoveDate'],
            itemImages=request.FILES['inputImages'],
            message=request.POST['inputMessage'],
        )
        return redirect(f'/junk_removal/review/{junk_removal_quote.id}')
    return redirect('/junk_removal')


def quoteConsignment(request):
    errors = Consignment.objects.consignment_validator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/consignment')
        consignment_quote = Consignment.objects.create(
            name=request.POST['inputName'],
            email=request.POST['inputEmail'],
            phone=request.POST['inputPhone'],
            itemAddress=request.POST['inputItemAddress'],
            moveDateTime=request.POST['inputMoveDate'],
            itemImages=request.FILES['inputImages'],
            message=request.POST['inputMessage'],
        )
        return redirect(f'/consignment/review/{consignment_quote.id}')
    return redirect('/consignment')


def movingQuoteReview(request, quote_id):
    movingQuote = Moving.objects.get(id=quote_id)
    context = {
        'movingReview':  movingQuote
    }
    return render(request, 'moving_quoteReview.html', context)


def junk_removalQuoteReview(request, quote_id):
    junk_removalQuote = JunkRemoval.objects.get(id=quote_id)
    context = {
        'junk_removalReview':  junk_removalQuote
    }
    return render(request, 'junk_removal_quoteReview.html', context)


def consignmentQuoteReview(request, quote_id):
    consignmentQuote = Consignment.objects.get(id=quote_id)
    context = {
        'consignmentReview':  consignmentQuote
    }
    return render(request, 'consignment_quoteReview.html', context)
