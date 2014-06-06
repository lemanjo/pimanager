import os
import json
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from logtailer.models import LogFile, Filter
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings

HISTORY_LINES = getattr(settings, 'LOGTAILER_HISTORY_LINES', 0)

def read_logs(request):
    context = {
    }

    return render_to_response('log_reader.html',
                              context, 
                              RequestContext(request, {}),)


def get_history(f, lines=HISTORY_LINES):
    BUFSIZ = 1024
    f.seek(0, os.SEEK_END)
    bytes = f.tell()
    size = lines
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if (bytes - BUFSIZ > 0):
            # Seek back one whole BUFSIZ
            f.seek(block*BUFSIZ, 2)
            # read BUFFER
            data.append(f.read(BUFSIZ))
        else:
            # file too small, start from beginning
            f.seek(0,0)
            # only read what was not read
            data.append(f.read(bytes))
        linesFound = data[-1].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return ''.join(data).splitlines(True)[-lines:]

def get_log_lines(request,file_id, history=False):
    try:
        file_record = LogFile.objects.get(id=file_id)
    except LogFile.DoesNotExist:
        return HttpResponse(json.dumps([_('error_logfile_notexist')]),
                            mimetype = 'text/html')
    content = []
    file = open(file_record.path, 'r')

    if history:
        content = get_history(file)
        content = [line.replace('\n','<br/>') for line in content]
    else:
        last_position = request.session.get('file_position_%s' % file_id)

        file.seek(0, os.SEEK_END)
        if last_position and last_position<=file.tell():
            file.seek(last_position)

        for line in file:
            content.append('%s' % line.replace('\n','<br/>'))

    request.session['file_position_%s' % file_id] = file.tell()
    file.close()
    return HttpResponse(json.dumps(content), mimetype = 'application/json')

def add_log(request):
    context = {
        "logfiles": LogFile.objects.all()
    }

    if request.POST:
        if "filename" in request.POST:
            filename = request.POST.get('filename')
            filepath = request.POST.get('filepath')

            logfile = LogFile()
            logfile.name = filename
            logfile.path = filepath
            logfile.save()

        elif "delete_id" in request.POST:
            pass


    return render_to_response('add_log.html',
                              context, 
                              RequestContext(request, {}),)

def add_filter(request):
    context = {
        "filters": Filter.objects.all()
    }

    if request.POST:
        if "filtername" in request.POST:
            filtername = request.POST.get('filtername')
            filterregex = request.POST.get('filterregex')

            filt = Filter()
            filt.name = filtername
            filt.regex = filterregex
            filt.save()

        elif "delete_id" in request.POST:
            pass


    return render_to_response('add_filter.html',
                              context, 
                              RequestContext(request, {}),)

def log_select(request):
    
    context = {
        "logfiles": LogFile.objects.all()
    }

    if request.POST:
        if u"logfile" in request.POST:
            logfile_id = request.POST.get(u"logfile")

            context["logfile_id"] = logfile_id
            context["filters"] = Filter.objects.all()

            return render_to_response('log_reader.html', context, RequestContext(request, {}),)

    return render_to_response('log_select.html', context, RequestContext(request, {}),)